"""Bilingual geography learning data. Regional grouping and capitals follow IBGE Educa."""

REGIONS = {
    "N": {
        "pt": "Norte", "fr": "Nord", "color": "#4d9b83", "icon": "🌿",
        "description_pt": "Sete estados. A Amazônia e uma extensa rede de rios marcam grande parte da paisagem, mas a região reúne muitos ambientes e modos de vida.",
        "description_fr": "Sept États. L’Amazonie et un vaste réseau de fleuves marquent une grande partie du paysage, mais la région réunit des milieux et des modes de vie variés.",
    },
    "NE": {
        "pt": "Nordeste", "fr": "Nord-Est", "color": "#edb56d", "icon": "☀️",
        "description_pt": "Nove estados. O litoral, a Zona da Mata, o Agreste e o Sertão mostram como as paisagens e as chuvas variam dentro da mesma região.",
        "description_fr": "Neuf États. Le littoral, la Zona da Mata, l’Agreste et le Sertão montrent combien les paysages et les pluies varient au sein d’une même région.",
    },
    "CO": {
        "pt": "Centro-Oeste", "fr": "Centre-Ouest", "color": "#d3bf68", "icon": "🌾",
        "description_pt": "Três estados e o Distrito Federal. O Cerrado, o Pantanal e as nascentes de importantes rios ajudam a compreender a diversidade da região.",
        "description_fr": "Trois États et le District fédéral. Le Cerrado, le Pantanal et les sources de grands cours d’eau illustrent la diversité de la région.",
    },
    "SE": {
        "pt": "Sudeste", "fr": "Sud-Est", "color": "#cc8290", "icon": "⛰️",
        "description_pt": "Quatro estados. Serras, planaltos, áreas urbanas e litoral formam um mosaico de paisagens e atividades.",
        "description_fr": "Quatre États. Montagnes, plateaux, villes et littoral composent une mosaïque de paysages et d’activités.",
    },
    "S": {
        "pt": "Sul", "fr": "Sud", "color": "#8d9fd1", "icon": "🌊",
        "description_pt": "Três estados. Planaltos, campos, mata atlântica e litoral aparecem em diferentes partes da região.",
        "description_fr": "Trois États. Plateaux, prairies, forêt atlantique et littoral apparaissent dans différentes parties de la région.",
    },
}

# sigla, nome, capital, região
STATE_ROWS = [
    ("AC", "Acre", "Rio Branco", "N"), ("AP", "Amapá", "Macapá", "N"),
    ("AM", "Amazonas", "Manaus", "N"), ("PA", "Pará", "Belém", "N"),
    ("RO", "Rondônia", "Porto Velho", "N"), ("RR", "Roraima", "Boa Vista", "N"),
    ("TO", "Tocantins", "Palmas", "N"),
    ("AL", "Alagoas", "Maceió", "NE"), ("BA", "Bahia", "Salvador", "NE"),
    ("CE", "Ceará", "Fortaleza", "NE"), ("MA", "Maranhão", "São Luís", "NE"),
    ("PB", "Paraíba", "João Pessoa", "NE"), ("PE", "Pernambuco", "Recife", "NE"),
    ("PI", "Piauí", "Teresina", "NE"), ("RN", "Rio Grande do Norte", "Natal", "NE"),
    ("SE", "Sergipe", "Aracaju", "NE"),
    ("DF", "Distrito Federal", "Brasília", "CO"), ("GO", "Goiás", "Goiânia", "CO"),
    ("MT", "Mato Grosso", "Cuiabá", "CO"), ("MS", "Mato Grosso do Sul", "Campo Grande", "CO"),
    ("ES", "Espírito Santo", "Vitória", "SE"), ("MG", "Minas Gerais", "Belo Horizonte", "SE"),
    ("RJ", "Rio de Janeiro", "Rio de Janeiro", "SE"), ("SP", "São Paulo", "São Paulo", "SE"),
    ("PR", "Paraná", "Curitiba", "S"), ("RS", "Rio Grande do Sul", "Porto Alegre", "S"),
    ("SC", "Santa Catarina", "Florianópolis", "S"),
]

STATES = [
    {"sigla": sigla, "nome": nome, "capital": capital, "regiao": regiao}
    for sigla, nome, capital, regiao in STATE_ROWS
]

VIDEOS = [
    {
        "slug": "regioes", "icon": "🧭", "duration": "15 s",
        "title_pt": "Cinco regiões, muitos Brasis", "title_fr": "Cinq régions, plusieurs Brésils",
        "summary_pt": "Veja como os 26 estados e o Distrito Federal se agrupam em cinco grandes regiões.",
        "summary_fr": "Découvrez comment les 26 États et le District fédéral forment cinq grandes régions.",
        "transcript_pt": "O Brasil tem cinco grandes regiões: Norte, Nordeste, Centro-Oeste, Sudeste e Sul. Elas agrupam 26 estados e o Distrito Federal. Cada região reúne paisagens e histórias diferentes.",
        "transcript_fr": "Le Brésil compte cinq grandes régions : Nord, Nord-Est, Centre-Ouest, Sud-Est et Sud. Elles regroupent 26 États et le District fédéral. Chaque région réunit des paysages et des histoires variés.",
    },
    {
        "slug": "relevo", "icon": "⛰️", "duration": "15 s",
        "title_pt": "O relevo tem formas", "title_fr": "Les formes du relief",
        "summary_pt": "Uma animação para distinguir planalto, planície e depressão.",
        "summary_fr": "Une animation pour distinguer plateau, plaine et dépression.",
        "transcript_pt": "O relevo é a forma da superfície da Terra. Planaltos são áreas elevadas; planícies são superfícies de deposição de sedimentos; depressões ficam mais baixas que as áreas ao redor. O Brasil reúne todas essas formas.",
        "transcript_fr": "Le relief est la forme de la surface terrestre. Les plateaux sont des zones élevées ; les plaines résultent du dépôt de sédiments ; les dépressions sont plus basses que les zones voisines. Le Brésil réunit toutes ces formes.",
    },
    {
        "slug": "rios", "icon": "💧", "duration": "15 s",
        "title_pt": "Para onde vai a chuva?", "title_fr": "Où va la pluie ?",
        "summary_pt": "Siga uma gota de chuva da serra ao rio e descubra a ideia de bacia hidrográfica.",
        "summary_fr": "Suivez une goutte de pluie jusqu’au fleuve pour comprendre le bassin versant.",
        "transcript_pt": "A chuva cai sobre o relevo. A água escorre por córregos e rios até um ponto de saída. A área drenada por essa rede é uma bacia hidrográfica. As partes altas ajudam a separar uma bacia da outra.",
        "transcript_fr": "La pluie tombe sur le relief. L’eau s’écoule par les ruisseaux et les rivières vers un même point de sortie. La zone drainée par ce réseau est un bassin versant. Les hauteurs contribuent à séparer les bassins.",
    },
]
