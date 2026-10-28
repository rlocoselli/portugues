# -*- coding: utf-8 -*-
"""Aplicação Flask do site "Aprender Português".

Site bilíngue (português/francês) para aprender português com textos sobre
o Brasil. Os textos ficam em data/textos.py (sem banco de dados).
"""
import os
import re
import glob
import hashlib
import mimetypes

from flask import Flask, render_template, request, redirect, url_for, session, abort, send_file, Response

from data.textos import TEXTOS, CATEGORIAS, NIVEIS
from data.enriquecimento import enrich_texts
from data.poesias import POESIAS
from data.geografia import REGIONS, STATES, VIDEOS

enrich_texts(TEXTOS)

app = Flask(__name__)
mimetypes.add_type("image/webp", ".webp")
app.secret_key = os.environ.get("SECRET_KEY", "aprender-portugues-brasil-2024")
AUDIO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio_cache")

# Cores do banner (capa) por categoria — mantendo a paleta brasileira.
CAPA_TEMAS = {
    "natureza": ("#009739", "#003d1c"),
    "historia": ("#012169", "#0a3d91"),
    "geografia": ("#0e7490", "#065f46"),
    "cultura": ("#f59e0b", "#b45309"),
    "ciencia": ("#0f766e", "#164e63"),
}

# Textos da interface do usuário (i18n).
UI = {
    "pt": {
        "site_title": "Fala Brasil",
        "tagline": "Aprenda português com quem é do Brasil",
        "creator_role": "Professor de português e desenvolvedor de software",
        "nav_home": "Início",
        "nav_about": "Sobre",
        "nav_poetry": "Poesias",
        "nav_geography": "Geografia",
        "geo_title": "Explore a geografia do Brasil",
        "geo_intro": "Viaje pelas cinco regiões, descubra os estados no mapa e aprenda como relevo e rios ajudam a contar a história de cada paisagem.",
        "geo_map_title": "Um mapa para explorar",
        "geo_map_intro": "Selecione uma região ou toque em um estado. Você também pode usar a lista abaixo do mapa.",
        "geo_map_label": "Mapa interativo dos estados brasileiros",
        "geo_all_regions": "Todas as regiões",
        "geo_state": "Estado / unidade da Federação",
        "geo_capital": "Capital",
        "geo_region": "Região",
        "geo_select_state": "Escolha um estado",
        "geo_region_hint": "Selecione uma região para conhecer seus estados.",
        "geo_videos_title": "Geografia em movimento",
        "geo_videos_intro": "Três vídeos curtos, com desenhos e texto em português na tela, para aprender brincando. Os vídeos não têm áudio; leia a transcrição abaixo de cada um.",
        "geo_transcript": "Ler transcrição",
        "geo_game_title": "Desafio: encontre o estado",
        "geo_game_intro": "Leia a pista e encontre a unidade da Federação no mapa ou na lista. Tente acertar cinco rodadas!",
        "geo_game_start": "Começar desafio",
        "geo_game_next": "Próxima rodada",
        "geo_game_restart": "Jogar novamente",
        "geo_game_find": "Encontre",
        "geo_game_capital": "Qual unidade da Federação tem a capital",
        "geo_game_round": "Rodada",
        "geo_game_correct": "Boa! Você encontrou",
        "geo_game_wrong": "Quase! Você escolheu",
        "geo_game_answer": "A resposta era",
        "geo_game_score": "Pontuação",
        "geo_game_done": "Desafio concluído!",
        "geo_source": "Divisão regional e capitais: IBGE Educa. Contornos simplificados para fins educativos.",
        "geo_read_more": "Continue com os textos de geografia",
        "poetry_title": "Poesias brasileiras",
        "poetry_subtitle": "Poemas originais em português, inspirados nas paisagens, nos encontros e nos muitos Brasis do cotidiano.",
        "poetry_read": "Ler poema",
        "poetry_back": "Voltar às poesias",
        "poetry_portuguese": "Poema em português",
        "poetry_french": "Tradução em francês",
        "poetry_translation_action": "Abrir tradução",
        "poetry_original_note": "Poema original do Fala Brasil",
        "poetry_intro_note": "Leia os versos em voz alta e descubra a tradução quando quiser.",
        "hero_title": "Seu próximo destino: o português do Brasil",
        "hero_subtitle": "Viaje por histórias, paisagens e sabores brasileiros. Leia no seu ritmo, escute a pronúncia e descubra cada texto também em francês.",
        "hero_action": "Começar a explorar",
        "how_title": "Um jeito simples de aprender",
        "how_read": "Leia com calma",
        "how_read_body": "Comece pelo português e toque em uma frase para ouvir a pronúncia.",
        "how_discover": "Descubra palavras",
        "how_discover_body": "Abra a tradução quando precisar e pratique o vocabulário em voz alta.",
        "how_practice": "Teste e continue",
        "how_practice_body": "Responda ao quiz e acompanhe as leituras concluídas neste navegador.",
        "video_title": "Uma viagem pelo Brasil em imagens",
        "video_body": "Um pequeno convite visual para começar a explorar as histórias.",
        "progress_label": "leituras concluídas",
        "mark_complete": "Marcar como concluída",
        "marked_complete": "Leitura concluída ✓",
        "reading_time": "min de leitura",
        "search_placeholder": "Buscar por título ou palavra...",
        "all_categories": "Todas as categorias",
        "all_levels": "Todos os níveis",
        "filter": "Filtrar",
        "texts_count": "textos",
        "read": "Ler o texto",
        "listen": "Ouvir o texto",
        "stop": "Parar",
        "category": "Categoria",
        "level": "Nível",
        "portuguese": "Português",
        "french": "Francês",
        "vocabulary": "Vocabulário",
        "vocab_hint": "Clique na palavra para ouvir a pronúncia.",
        "quiz_title": "Teste o que você aprendeu",
        "quiz_intro": "Responda às perguntas de compreensão e vocabulário. Você pode tentar novamente.",
        "quiz_check": "Ver resultado",
        "quiz_retry": "Tentar novamente",
        "quiz_correct": "Correto!",
        "quiz_wrong": "Ainda não. Confira a resposta certa abaixo.",
        "quiz_score": "Você acertou",
        "quiz_of": "de",
        "quiz_questions": "perguntas",
        "quiz_pick": "Escolha uma resposta em cada pergunta.",
        "quiz_missing": "Responda a todas as perguntas antes de conferir.",
        "explore_label": "Um olhar mais de perto",
        "language_tip": "Leia primeiro em português. Depois, abra a tradução para conferir novas palavras e ideias.",
        "listen_hint": "Use o player para ouvir o texto completo. Clique em qualquer frase para ouvi-la separadamente.",
        "back": "Voltar",
        "no_results": "Nenhum texto encontrado.",
        "footer_note": "Textos sobre o Brasil com áudio (texto para fala).",
        "about_title": "Sobre este site",
        "about_intro": "Este site reúne textos sobre o Brasil — natureza, história, geografia, cultura e ciência — para ajudar você a aprender português. Cada texto está disponível em português e em francês, com áudio (texto para fala), vocabulário e quiz. A seção Geografia também oferece um mapa interativo e vídeos curtos com transcrições bilíngues. O áudio dos textos é gerado no servidor e pode demorar um pouco na primeira reprodução.",
        "about_how_title": "Como adicionar novos textos",
        "about_how_intro": "Os textos ficam em um único arquivo, sem banco de dados. Para adicionar um novo texto, abra o arquivo data/textos.py e copie um dos blocos existentes, preenchendo os seguintes campos:",
    },
    "fr": {
        "site_title": "Fala Brasil",
        "tagline": "Apprenez le portugais avec un Brésilien",
        "creator_role": "Professeur de portugais et développeur de logiciels",
        "nav_home": "Accueil",
        "nav_about": "À propos",
        "nav_poetry": "Poèmes",
        "nav_geography": "Géographie",
        "geo_title": "Explorez la géographie du Brésil",
        "geo_intro": "Parcourez les cinq régions, découvrez les États sur la carte et voyez comment le relief et les fleuves façonnent les paysages.",
        "geo_map_title": "Une carte à explorer",
        "geo_map_intro": "Choisissez une région ou touchez un État. La liste sous la carte est également disponible.",
        "geo_map_label": "Carte interactive des États brésiliens",
        "geo_all_regions": "Toutes les régions",
        "geo_state": "État / unité de la Fédération",
        "geo_capital": "Capitale",
        "geo_region": "Région",
        "geo_select_state": "Choisissez un État",
        "geo_region_hint": "Choisissez une région pour découvrir ses États.",
        "geo_videos_title": "La géographie en mouvement",
        "geo_videos_intro": "Trois courtes vidéos avec des dessins et du texte en portugais à l’écran pour apprendre en s’amusant. Elles sont sans son ; la transcription française figure sous chacune.",
        "geo_transcript": "Lire la transcription",
        "geo_game_title": "Défi : trouvez l’État",
        "geo_game_intro": "Lisez l’indice et trouvez l’unité de la Fédération sur la carte ou dans la liste. Essayez cinq manches !",
        "geo_game_start": "Commencer le défi",
        "geo_game_next": "Manche suivante",
        "geo_game_restart": "Rejouer",
        "geo_game_find": "Trouvez",
        "geo_game_capital": "Quelle unité de la Fédération a pour capitale",
        "geo_game_round": "Manche",
        "geo_game_correct": "Bravo ! Vous avez trouvé",
        "geo_game_wrong": "Presque ! Vous avez choisi",
        "geo_game_answer": "La bonne réponse était",
        "geo_game_score": "Score",
        "geo_game_done": "Défi terminé !",
        "geo_source": "Régions et capitales : IBGE Educa. Contours simplifiés à des fins pédagogiques.",
        "geo_read_more": "Poursuivez avec les textes de géographie",
        "poetry_title": "Poésie brésilienne",
        "poetry_subtitle": "Des poèmes originaux en portugais, inspirés par les paysages, les rencontres et les multiples Brésils du quotidien.",
        "poetry_read": "Lire le poème",
        "poetry_back": "Retour aux poèmes",
        "poetry_portuguese": "Poème en portugais",
        "poetry_french": "Traduction française",
        "poetry_translation_action": "Afficher la traduction",
        "poetry_original_note": "Poème original de Fala Brasil",
        "poetry_intro_note": "Lisez les vers à voix haute et ouvrez la traduction quand vous le souhaitez.",
        "hero_title": "Prochaine destination : le portugais du Brésil",
        "hero_subtitle": "Partez à la découverte des histoires, paysages et saveurs du Brésil. Lisez à votre rythme, écoutez la prononciation et retrouvez chaque texte en français.",
        "hero_action": "Commencer à explorer",
        "how_title": "Une façon simple d’apprendre",
        "how_read": "Lisez à votre rythme",
        "how_read_body": "Commencez en portugais et touchez une phrase pour entendre la prononciation.",
        "how_discover": "Découvrez des mots",
        "how_discover_body": "Ouvrez la traduction au besoin et prononcez les mots à voix haute.",
        "how_practice": "Testez et continuez",
        "how_practice_body": "Répondez au quiz et suivez vos lectures terminées sur cet appareil.",
        "video_title": "Un voyage au Brésil en images",
        "video_body": "Une courte invitation visuelle à découvrir les histoires.",
        "progress_label": "lectures terminées",
        "mark_complete": "Marquer comme terminé",
        "marked_complete": "Lecture terminée ✓",
        "reading_time": "min de lecture",
        "search_placeholder": "Rechercher un titre ou un mot...",
        "all_categories": "Toutes les catégories",
        "all_levels": "Tous les niveaux",
        "filter": "Filtrer",
        "texts_count": "textes",
        "read": "Lire le texte",
        "listen": "Écouter le texte",
        "stop": "Arrêter",
        "category": "Catégorie",
        "level": "Niveau",
        "portuguese": "Portugais",
        "french": "Français",
        "vocabulary": "Vocabulaire",
        "vocab_hint": "Cliquez sur le mot pour entendre la prononciation.",
        "quiz_title": "Vérifiez ce que vous avez appris",
        "quiz_intro": "Répondez aux questions de compréhension et de vocabulaire. Vous pouvez réessayer.",
        "quiz_check": "Voir le résultat",
        "quiz_retry": "Réessayer",
        "quiz_correct": "Bonne réponse !",
        "quiz_wrong": "Pas encore. Consultez la bonne réponse ci-dessous.",
        "quiz_score": "Vous avez trouvé",
        "quiz_of": "sur",
        "quiz_questions": "questions",
        "quiz_pick": "Choisissez une réponse pour chaque question.",
        "quiz_missing": "Répondez à toutes les questions avant de vérifier.",
        "explore_label": "Pour aller plus loin",
        "language_tip": "Lisez d’abord en portugais. Ouvrez ensuite la traduction pour vérifier les nouveaux mots et les idées.",
        "listen_hint": "Utilisez le lecteur pour écouter tout le texte. Cliquez sur une phrase pour l'écouter séparément.",
        "back": "Retour",
        "no_results": "Aucun texte trouvé.",
        "footer_note": "Textes sur le Brésil avec audio (synthèse vocale).",
        "about_title": "À propos de ce site",
        "about_intro": "Ce site rassemble des textes sur le Brésil — nature, histoire, géographie, culture et science — pour vous aider à apprendre le portugais. Chaque texte est disponible en portugais et en français, avec audio (synthèse vocale), vocabulaire et quiz. La section Géographie propose également une carte interactive et de courtes vidéos avec transcriptions bilingues. L’audio des textes est généré sur le serveur et peut prendre un moment lors de la première écoute.",
        "about_how_title": "Comment ajouter de nouveaux textes",
        "about_how_intro": "Les textes se trouvent dans un seul fichier, sans base de données. Pour ajouter un nouveau texte, ouvrez le fichier data/textos.py et copiez l'un des blocs existants, en remplissant les champs suivants :",
    },
}

def cat_label(slug, lang):
    for c in CATEGORIAS:
        if c["slug"] == slug:
            return c[lang]
    return slug


def nivel_label(slug, lang):
    for n in NIVEIS:
        if n["slug"] == slug:
            return n[lang]
    return slug


def get_texto(slug):
    for t in TEXTOS:
        if t["slug"] == slug:
            return t
    return None


def split_sentences(text):
    partes = re.findall(r"[^.!?…]+[.!?…]+[\"'»]?", text)
    if not partes:
        return [text.strip()]
    return [p.strip() for p in partes]


def _capa_svg(c1, c2, emoji):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="450" '
        'viewBox="0 0 800 450" role="img">'
        '<defs>'
        f'<linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/>'
        '</linearGradient>'
        '<radialGradient id="halo" cx="0.5" cy="0.5" r="0.5">'
        '<stop offset="0" stop-color="#ffffff" stop-opacity="0.35"/>'
        '<stop offset="1" stop-color="#ffffff" stop-opacity="0"/>'
        '</radialGradient>'
        '</defs>'
        '<rect width="800" height="450" fill="url(#g)"/>'
        '<circle cx="760" cy="60" r="210" fill="url(#halo)"/>'
        '<circle cx="170" cy="420" r="160" fill="#ffffff" opacity="0.06"/>'
        '<circle cx="640" cy="110" r="120" fill="#ffffff" opacity="0.05"/>'
        '<circle cx="700" cy="360" r="40" fill="#ffdf00" opacity="0.45"/>'
        '<circle cx="120" cy="90" r="24" fill="#ffdf00" opacity="0.55"/>'
        '<rect x="0" y="0" width="800" height="12" fill="#ffdf00"/>'
        f'<text x="400" y="235" font-size="190" text-anchor="middle" '
        f'dominant-baseline="central">{emoji}</text>'
        '</svg>'
    )


def _serve_audio(key, text):
    os.makedirs(AUDIO_DIR, exist_ok=True)
    path = os.path.join(AUDIO_DIR, key + ".mp3")
    if not os.path.exists(path):
        try:
            from gtts import gTTS
            gTTS(text=text, lang="pt-br", slow=False).save(path)
        except Exception:
            abort(503)
    return send_file(path, mimetype="audio/mpeg", conditional=True)


@app.context_processor
def inject_globals():
    lang = session.get("lang", "pt")
    return dict(
        lang=lang,
        ui=UI[lang],
        CATEGORIAS=CATEGORIAS,
        NIVEIS=NIVEIS,
        get_cat=lambda slug: cat_label(slug, lang),
        get_nivel=lambda slug: nivel_label(slug, lang),
    )


@app.route("/")
def index():
    cat = request.args.get("categoria", "")
    niv = request.args.get("nivel", "")
    busca_raw = request.args.get("busca", "")
    busca = busca_raw.strip().lower()

    textos = TEXTOS
    if cat:
        textos = [t for t in textos if t["categoria"] == cat]
    if niv:
        textos = [t for t in textos if t["nivel"] == niv]
    if busca:
        textos = [
            t
            for t in textos
            if busca in t["titulo_pt"].lower()
            or busca in t["titulo_fr"].lower()
            or busca in t["texto_pt"].lower()
        ]

    return render_template(
        "index.html", textos=textos, cat=cat, niv=niv, busca=busca_raw
    )


@app.route("/texto/<slug>")
def texto(slug):
    t = get_texto(slug)
    if not t:
        abort(404)
    return render_template(
        "texto.html", texto=t, sentences=split_sentences(t["texto_pt"])
    )


@app.route("/audio/<slug>.mp3")
def audio_full(slug):
    t = get_texto(slug)
    if not t:
        abort(404)
    version = hashlib.sha256(t["texto_pt"].encode("utf-8")).hexdigest()[:10]
    return _serve_audio(f"{slug}-{version}", t["texto_pt"])


@app.route("/audio/<slug>/frase/<int:i>.mp3")
def audio_sentence(slug, i):
    t = get_texto(slug)
    if not t:
        abort(404)
    frases = split_sentences(t["texto_pt"])
    if i < 0 or i >= len(frases):
        abort(404)
    version = hashlib.sha256(frases[i].encode("utf-8")).hexdigest()[:10]
    return _serve_audio(f"{slug}-frase-{i}-{version}", frases[i])


@app.route("/audio/<slug>/palavra/<int:i>.mp3")
def audio_word(slug, i):
    t = get_texto(slug)
    if not t:
        abort(404)
    vocab = t.get("vocabulario", [])
    if i < 0 or i >= len(vocab):
        abort(404)
    return _serve_audio(f"{slug}-palavra-{i}", vocab[i]["pt"])


@app.route("/capa/<slug>.svg")
def capa(slug):
    t = get_texto(slug)
    if not t:
        abort(404)
    c1, c2 = CAPA_TEMAS.get(t["categoria"], ("#009739", "#003d1c"))
    emoji = t.get("emoji", "🇧🇷")
    return Response(_capa_svg(c1, c2, emoji), mimetype="image/svg+xml")


@app.route("/foto-rodrigo")
def foto_rodrigo():
    """Serve a foto do Rodrigo (aceita .jpg/.jpeg/.png/.webp/.gif).

    Se a foto ainda não existir em static/img/rodrigo.*, usa o avatar padrão.
    """
    img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "img")
    mimes = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
             "webp": "image/webp", "gif": "image/gif"}
    for ext, mime in mimes.items():
        candidatos = glob.glob(os.path.join(img_dir, "rodrigo." + ext))
        if candidatos:
            return send_file(candidatos[0], mimetype=mime)
    return redirect(url_for("static", filename="img/avatar.svg"))


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/geografia")
def geografia():
    return render_template("geografia.html", regions=REGIONS, states=STATES, videos=VIDEOS)


@app.route("/poesias")
def poesias():
    return render_template("poesias.html", poesias=POESIAS)


@app.route("/poesia/<slug>")
def poesia(slug):
    item = next((p for p in POESIAS if p["slug"] == slug), None)
    if item is None:
        abort(404)
    return render_template("poesia.html", poesia=item)


@app.route("/lang/<l>")
def set_lang(l):
    if l in ("pt", "fr"):
        session["lang"] = l
    return redirect(request.referrer or url_for("index"))


@app.errorhandler(404)
def not_found(_e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
