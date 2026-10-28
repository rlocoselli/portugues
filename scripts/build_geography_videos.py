"""Render three short, captioned geography explainers as local MP4 files.

Requires Pillow, CairoSVG, and ffmpeg. The lessons are intentionally silent;
the web page supplies a bilingual transcript for each video.
"""
import io
import re
import subprocess
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "static/video"
OUT.mkdir(parents=True, exist_ok=True)
WIDTH, HEIGHT, FPS, SECONDS = 960, 540, 12, 15
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
title_font = ImageFont.truetype(BOLD, 39)
headline_font = ImageFont.truetype(BOLD, 32)
long_headline_font = ImageFont.truetype(BOLD, 26)
body_font = ImageFont.truetype(FONT, 22)
small_font = ImageFont.truetype(BOLD, 17)


def wrap(draw, message, font, limit):
    lines, line = [], ""
    for word in message.split():
        candidate = f"{line} {word}".strip()
        if line and draw.textlength(candidate, font=font) > limit:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines


def base(title, section, elapsed):
    image = Image.new("RGB", (WIDTH, HEIGHT), "#123b40")
    d = ImageDraw.Draw(image)
    d.rounded_rectangle((22, 20, 938, 520), 30, fill="#f7f6ed")
    d.text((47, 39), "FALA BRASIL  /  GEOGRAFIA", font=small_font, fill="#28705a")
    d.text((46, 72), title, font=title_font, fill="#123b40")
    d.rounded_rectangle((45, 474, 915, 482), 4, fill="#d8e4d9")
    d.rounded_rectangle((45, 474, 45 + 870 * elapsed / SECONDS, 482), 4, fill="#28705a")
    d.text((46, 492), section, font=small_font, fill="#566e70")
    d.text((860, 492), "15 s", font=small_font, fill="#566e70")
    return image


svg_source = (ROOT / "templates/_mapa_brasil.html").read_text(encoding="utf-8")
maps = {}
for region in ("N", "NE", "CO", "SE", "S"):
    def recolor(match):
        tag = match.group(0)
        if f'data-region="{region}"' not in tag:
            return re.sub(r'fill="#[0-9a-fA-F]{6}"', 'fill="#cbd9d1"', tag)
        return tag
    selected_svg = re.sub(r'<path\b[^>]+>', recolor, svg_source).replace("{{ ui.geo_map_label }}", "Mapa do Brasil")
    png = cairosvg.svg2png(bytestring=selected_svg.encode(), output_width=345, output_height=345)
    maps[region] = Image.open(io.BytesIO(png)).convert("RGBA")


def regions_frame(elapsed):
    stages = [
        ("N", "Norte", "7 estados", "A Amazônia e muitos rios fazem parte desta região."),
        ("NE", "Nordeste", "9 estados", "Do litoral ao Sertão, as paisagens mudam bastante."),
        ("CO", "Centro-Oeste", "3 estados + DF", "Cerrado, Pantanal e Brasília estão aqui."),
        ("SE", "Sudeste", "4 estados", "Serras, cidades e litoral convivem lado a lado."),
        ("S", "Sul", "3 estados", "Campos, planaltos e litoral compõem a região."),
    ]
    step = min(int(elapsed / 3), 4)
    region, name, count, fact = stages[step]
    image = base("Cinco regiões, muitos Brasis", f"REGIÃO {step + 1} DE 5", elapsed)
    image.paste(maps[region], (58, 118), maps[region])
    d = ImageDraw.Draw(image)
    d.rounded_rectangle((467, 149, 896, 440), 24, fill="#e5f0e7")
    d.text((495, 181), name, font=headline_font, fill="#123b40")
    d.text((495, 230), count, font=body_font, fill="#28705a")
    for i, line in enumerate(wrap(d, fact, body_font, 365)):
        d.text((495, 282 + i * 36), line, font=body_font, fill="#344b4e")
    d.text((495, 393), "Toque no mapa para explorar!", font=small_font, fill="#28705a")
    return image


def relief_frame(elapsed):
    stages = [
        ("Planalto", "Área mais elevada, com trechos relativamente planos.", [(68, 406), (145, 350), (178, 284), (391, 284), (469, 397)]),
        ("Planície", "Área plana formada pela deposição de sedimentos.", [(68, 406), (176, 373), (263, 370), (368, 374), (469, 397)]),
        ("Depressão", "Área mais baixa que os terrenos ao redor.", [(68, 333), (158, 333), (226, 396), (330, 396), (402, 333), (469, 333)]),
    ]
    step = min(int(elapsed / 5), 2)
    name, fact, points = stages[step]
    image = base("O relevo tem formas", f"FORMA {step + 1} DE 3", elapsed)
    d = ImageDraw.Draw(image)
    d.rounded_rectangle((47, 144, 476, 447), 25, fill="#dff0e8")
    d.ellipse((101, 182, 181, 262), fill="#f6cf70")
    d.polygon(points + [(469, 430), (68, 430)], fill="#a7c57d")
    d.line(points, fill="#4a8066", width=5, joint="curve")
    d.line((68, 430, 469, 430), fill="#77958a", width=2)
    d.text((70, 161), "↑ ALTITUDE", font=small_font, fill="#28705a")
    d.rounded_rectangle((500, 162, 902, 426), 25, fill="#fff")
    d.text((531, 198), name, font=headline_font, fill="#123b40")
    for i, line in enumerate(wrap(d, fact, body_font, 340)):
        d.text((531, 263 + i * 36), line, font=body_font, fill="#344b4e")
    d.text((531, 375), "Observe a altura do terreno!", font=small_font, fill="#28705a")
    return image


def rivers_frame(elapsed):
    stages = [
        ("1. Chuva", "A água cai sobre as partes altas do relevo."),
        ("2. Córregos e rios", "A água escorre e os cursos d’água se encontram."),
        ("3. Bacia hidrográfica", "Toda a área drenada leva a um ponto de saída."),
    ]
    step = min(int(elapsed / 5), 2)
    name, fact = stages[step]
    image = base("Para onde vai a chuva?", f"PASSO {step + 1} DE 3", elapsed)
    d = ImageDraw.Draw(image)
    d.rounded_rectangle((47, 144, 476, 447), 25, fill="#dff0ed")
    d.polygon([(68, 394), (166, 268), (242, 355), (317, 240), (464, 397), (464, 429), (68, 429)], fill="#8ebd91")
    d.line([(180, 312), (230, 360), (314, 388), (408, 401), (468, 409)], fill="#247cb0", width=12, joint="curve")
    d.line([(320, 275), (323, 316), (310, 352), (314, 388)], fill="#247cb0", width=7, joint="curve")
    d.ellipse((124, 188, 222, 229), fill="#fff")
    d.ellipse((161, 177, 244, 231), fill="#fff")
    d.ellipse((205, 192, 265, 231), fill="#fff")
    if step >= 1:
        for i in range(5):
            x = 193 + i * 24
            y = 245 + ((elapsed * 28 + i * 17) % 62)
            d.ellipse((x, y, x + 7, y + 13), fill="#247cb0")
    if step == 2:
        d.arc((106, 231, 440, 425), 192, 352, fill="#d39646", width=5)
        d.arc((123, 218, 449, 420), 12, 166, fill="#d39646", width=5)
    d.rounded_rectangle((500, 162, 902, 426), 25, fill="#fff")
    d.text((531, 198), name, font=long_headline_font, fill="#123b40")
    for i, line in enumerate(wrap(d, fact, body_font, 340)):
        d.text((531, 263 + i * 36), line, font=body_font, fill="#344b4e")
    d.text((531, 375), "Siga a gota azul!", font=small_font, fill="#28705a")
    return image


for slug, renderer in (("regioes", regions_frame), ("relevo", relief_frame), ("rios", rivers_frame)):
    target = OUT / f"{slug}.mp4"
    renderer(0).save(OUT / f"{slug}.webp", "WEBP", quality=86)
    command = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
               "-s", f"{WIDTH}x{HEIGHT}", "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264",
               "-preset", "veryfast", "-crf", "24", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(target)]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    try:
        for frame in range(FPS * SECONDS):
            process.stdin.write(renderer(frame / FPS).tobytes())
    finally:
        process.stdin.close()
    if process.wait() != 0:
        raise RuntimeError(f"ffmpeg failed for {slug}")
    print(f"{target.relative_to(ROOT)}: {target.stat().st_size:,} bytes")
