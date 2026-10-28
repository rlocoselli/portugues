"""Build the offline, keyboard-accessible Brazil map from the bundled GeoJSON."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
geo = json.loads((ROOT / "data/estados.geojson").read_text(encoding="utf-8"))
from data.geografia import REGIONS, STATES  # noqa: E402

state_by_code = {state["sigla"]: state for state in STATES}
assert len(geo["features"]) == len(state_by_code) == 27


def polygons(feature):
    geometry = feature["geometry"]
    if geometry["type"] == "Polygon":
        return [geometry["coordinates"]]
    return geometry["coordinates"]


points = [point for feature in geo["features"] for polygon in polygons(feature)
          for ring in polygon for point in ring]
min_x, max_x = min(p[0] for p in points), max(p[0] for p in points)
min_y, max_y = min(p[1] for p in points), max(p[1] for p in points)
scale = min(680 / (max_x - min_x), 680 / (max_y - min_y))
offset_x = (760 - (max_x - min_x) * scale) / 2
offset_y = (760 - (max_y - min_y) * scale) / 2


def project(point):
    return (offset_x + (point[0] - min_x) * scale,
            offset_y + (max_y - point[1]) * scale)


lines = [
    '<svg class="brazil-map" viewBox="0 0 760 760" xmlns="http://www.w3.org/2000/svg" '
    'role="group" aria-label="{{ ui.geo_map_label }}">',
    '<rect width="760" height="760" rx="28" class="map-ocean" fill="#e9f5f3"/>',
]
for feature in geo["features"]:
    code = feature["properties"]["sigla"]
    state = state_by_code[code]
    segments = []
    for polygon in polygons(feature):
        for ring in polygon:
            coords = [project(point) for point in ring]
            segments.append("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in coords) + " Z")
    path = " ".join(segments)
    lines.append(
        f'<path id="geo-{code}" class="map-state" data-state="{code}" '
        f'data-region="{state["regiao"]}" tabindex="0" role="button" '
        f'aria-label="{state["nome"]}" aria-pressed="false" '
        f'fill="{REGIONS[state["regiao"]]["color"]}" stroke="#fff" stroke-width="1.2" d="{path}">'
        f'<title>{state["nome"]}</title></path>'
    )
lines.append('</svg>')
(ROOT / "templates/_mapa_brasil.html").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Built 27 state paths from {len(points)} coordinates")
