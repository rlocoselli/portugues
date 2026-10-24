# -*- coding: utf-8 -*-
"""
Textos sobre o Brasil para o site "Fala Brasil".

COMO ADICIONAR UM NOVO TEXTO (sem banco de dados):
1) Abra este arquivo (data/textos.py).
2) Copie um dos blocos de dicionário abaixo e cole antes do último "]" da lista TEXTOS.
3) Preencha os campos:
   - slug: identificador único (somente letras minúsculas e hífens).
   - categoria: "natureza", "historia", "geografia", "cultura" ou "ciencia".
   - nivel: "iniciante", "intermediario" ou "avancado".
   - emoji: um emoji que representa o tema (usado na imagem de capa).
   - titulo_pt / titulo_fr: título em português e em francês.
   - texto_pt / texto_fr: o texto em português e a tradução em francês.
   - vocabulario: lista de {"pt": ..., "fr": ...} com palavras-chave.
4) Reinicie o servidor Flask. O áudio e a imagem são gerados automaticamente.
"""

CATEGORIAS = [
    {"slug": "natureza", "pt": "Natureza", "fr": "Nature"},
    {"slug": "historia", "pt": "História", "fr": "Histoire"},
    {"slug": "geografia", "pt": "Geografia", "fr": "Géographie"},
    {"slug": "cultura", "pt": "Cultura", "fr": "Culture"},
    {"slug": "ciencia", "pt": "Ciência", "fr": "Science"},
]

NIVEIS = [
    {"slug": "iniciante", "pt": "Iniciante", "fr": "Débutant"},
    {"slug": "intermediario", "pt": "Intermediário", "fr": "Intermédiaire"},
    {"slug": "avancado", "pt": "Avançado", "fr": "Avancé"},
]

TEXTOS = [
    {
        "slug": "floresta-amazonica",
        "categoria": "natureza",
        "nivel": "iniciante",
        "emoji": "🌳",
        "titulo_pt": "A Floresta Amazônica",
        "titulo_fr": "La forêt amazonienne",
        "texto_pt": (
            'A Floresta Amazônica é a maior floresta tropical do mundo. Ela cobre "\n            "cerca de 5,5 milhões de quilômetros quadrados e se estende por nove "\n            "países da América do Sul, sendo que a maior parte, aproximadamente 60%, "\n            "fica no Brasil. A floresta é atravessada pelo rio Amazonas e por "\n            "milhares de afluentes, formando a maior bacia hidrográfica do planeta. "\n            "A Amazônia abriga uma biodiversidade impressionante: estima-se que "\n            "existam milhões de espécies de plantas, animais e insetos, muitas ainda "\n            "desconhecidas pela ciência. A floresta é frequentemente chamada de "\n            "\'pulmão do mundo\', embora o mais correto seja dizer que ela recicla o "\n            "próprio oxigênio e tem papel fundamental na regulação do clima. Milhares "\n            "de comunidades indígenas e ribeirinhas vivem na região há séculos. "\n            "Infelizmente, o desmatamento e as queimadas ameaçam esse patrimônio, o "\n            "que preocupa cientistas e governos de todo o mundo. Para quem visita a "\n            "região, a floresta também aparece nos sons: ao amanhecer, aves e insetos "\n            "anunciam o dia antes de o sol atravessar as copas. Muitas comunidades usam "\n            "os rios como caminhos entre casas, escolas e mercados, e conhecem o ritmo "\n            "das cheias como parte da rotina. Proteger a Amazônia significa cuidar dos "\n            "animais e das plantas, respeitar os povos que vivem ali e apoiar formas de "\n            "produzir alimentos sem destruir a floresta. Para quem visita a região, a floresta também aparece nos sons: ao amanhecer, aves e insetos anunciam o dia antes de o sol atravessar as copas. Muitas comunidades usam os rios como caminhos entre casas, escolas e mercados, e conhecem o ritmo das cheias como parte da rotina. Proteger a Amazônia significa cuidar dos animais e das plantas, respeitar os povos que vivem ali e apoiar formas de produzir alimentos sem destruir a floresta.'
        ),
        "texto_fr": (
            'La forêt amazonienne est la plus grande forêt tropicale du monde. Elle "\n            "couvre environ 5,5 millions de kilomètres carrés et s\'étend sur neuf "\n            "pays d\'Amérique du Sud, dont la plus grande partie, environ 60 %, se "\n            "trouve au Brésil. La forêt est traversée par le fleuve Amazone et par "\n            "des milliers d\'affluents, formant le plus grand bassin hydrographique de "\n            "la planète. L\'Amazonie abrite une biodiversité impressionnante : on "\n            "estime qu\'il existe des millions d\'espèces de plantes, d\'animaux et "\n            "d\'insectes, dont beaucoup sont encore inconnues de la science. La forêt "\n            "est souvent appelée le « poumon du monde », même s\'il est plus exact de "\n            "dire qu\'elle recycle son propre oxygène et joue un rôle fondamental dans "\n            "la régulation du climat. Des milliers de communautés indigènes et "\n            "riveraines vivent dans la région depuis des siècles. Malheureusement, la "\n            "déforestation et les incendies menacent ce patrimoine, ce qui inquiète "\n            "les scientifiques et les gouvernements du monde entier. Pour les visiteurs, "\n            "la forêt se révèle aussi par ses sons : à l\'aube, les oiseaux et les insectes "\n            "annoncent le jour avant même que le soleil traverse les cimes. De nombreuses "\n            "communautés utilisent les rivières comme des chemins entre les maisons, les "\n            "écoles et les marchés, et connaissent le rythme des crues. Protéger l\'Amazonie, "\n            "c\'est prendre soin des animaux et des plantes, respecter les peuples qui y "\n            "vivent et soutenir des façons de produire sans détruire la forêt. Pour les visiteurs, la forêt se révèle aussi par ses sons : à l\'aube, les oiseaux et les insectes annoncent le jour avant même que le soleil traverse les cimes. De nombreuses communautés utilisent les rivières comme des chemins entre les maisons, les écoles et les marchés, et connaissent le rythme des crues. Protéger l\'Amazonie, c\'est prendre soin des animaux et des plantes, respecter les peuples qui y vivent et soutenir des façons de produire sans détruire la forêt.'      ),
                "quiz": [
            {
                "pergunta_pt": 'Por que a Amazônia é importante para o clima?',
                "pergunta_fr": 'Pourquoi l’Amazonie est-elle importante pour le climat ?',
                "opcoes_pt": ['Porque ajuda a regular o clima.', 'Porque produz todo o oxigênio do planeta.', 'Porque impede todas as chuvas.'],
                "opcoes_fr": ['Parce qu’elle contribue à réguler le climat.', 'Parce qu’elle produit tout l’oxygène de la planète.', 'Parce qu’elle empêche toutes les pluies.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'Como muitas comunidades se deslocam pela região?',
                "pergunta_fr": 'Comment de nombreuses communautés se déplacent-elles dans la région ?',
                "opcoes_pt": ['Por metrô.', 'Por teleférico.', 'Pelos rios.'],
                "opcoes_fr": ['En métro.', 'En téléphérique.', 'Par les rivières.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'O que ajuda a proteger a floresta?',
                "pergunta_fr": 'Qu’est-ce qui aide à protéger la forêt ?',
                "opcoes_pt": ['Aumentar as queimadas.', 'Produzir sem destruí-la.', 'Abrir estradas em toda parte.'],
                "opcoes_fr": ['Multiplier les incendies.', 'Produire sans la détruire.', 'Construire des routes partout.'],
                "resposta": 1,
            },
        ],
"vocabulario": [
            {"pt": "floresta", "fr": "forêt"},
            {"pt": "bacia", "fr": "bassin"},
            {"pt": "desmatamento", "fr": "déforestation"},
            {"pt": "clima", "fr": "climat"},
        ],
    },
    {
        "slug": "rio-amazonas",
        "categoria": "geografia",
        "nivel": "iniciante",
        "emoji": "🌊",
        "titulo_pt": "O Rio Amazonas",
        "titulo_fr": "Le fleuve Amazone",
        "texto_pt": (
            'O rio Amazonas é o maior rio do mundo em volume de água. Ele nasce nos "\n            "Andes peruanos e atravessa o Brasil até desaguar no oceano Atlântico, "\n            "percorrendo cerca de 7 mil quilômetros. Sua descarga é tão grande que "\n            "representa cerca de 20% de toda a água doce que chega aos oceanos. Durante "\n            "a estação das chuvas, a largura do rio pode ultrapassar 10 quilômetros em "\n            "alguns pontos, e na foz chega a dezenas de quilômetros. A bacia amazônica "\n            "sustenta uma vida aquática riquíssima, com milhares de espécies de "\n            "peixes, incluindo o pirarucu, um dos maiores peixes de água doce do "\n            "mundo, e o boto-cor-de-rosa, um golfinho que vive apenas em rios. O "\n            "encontro das águas escuras do rio Negro com as águas barrentas do rio "\n            "Solimões, perto de Manaus, é um fenômeno famoso: os dois correm lado a "\n            "lado sem se misturar por vários quilômetros. O rio Amazonas é essencial "\n            "para o transporte, a economia e a vida de milhões de pessoas na região Norte. "\n            "Em muitas cidades e comunidades, barcos funcionam como ônibus e levam moradores, "\n            "alimentos e mercadorias entre lugares que não têm estradas. As cheias anuais "\n            "fertilizam áreas próximas e mudam a paisagem: árvores que parecem estar em terra "\n            "firme podem ficar cercadas de água. Pescadores observam a correnteza e conhecem "\n            "os períodos em que cada espécie aparece. O rio não é apenas uma grande via "\n            "natural; é parte do calendário, do trabalho e da memória das populações amazônicas. Em muitas cidades e comunidades, barcos funcionam como ônibus e levam moradores, alimentos e mercadorias entre lugares que não têm estradas. As cheias anuais fertilizam áreas próximas e mudam a paisagem: árvores que parecem estar em terra firme podem ficar cercadas de água. Pescadores observam a correnteza e conhecem os períodos em que cada espécie aparece. O rio não é apenas uma grande via natural; é parte do calendário, do trabalho e da memória das populações amazônicas.'   ),
        "texto_fr": (
            'Le fleuve Amazone est le plus grand fleuve du monde en volume d\'eau. Il "\n            "naît dans les Andes péruviennes et traverse le Brésil jusqu\'à se jeter "\n            "dans l\'océan Atlantique, parcourant environ 7 000 kilomètres. Son débit "\n            "est si grand qu\'il représente environ 20 % de toute l\'eau douce qui "\n            "arrive dans les océans. Pendant la saison des pluies, la largeur du "\n            "fleuve peut dépasser 10 kilomètres à certains endroits, et à son "\n            "embouchure elle atteint des dizaines de kilomètres. Le bassin amazonien "\n            "abrite une vie aquatique très riche, avec des milliers d\'espèces de "\n            "poissons, dont le pirarucu, l\'un des plus grands poissons d\'eau douce du "\n            "monde, et le boto (dauphin rose), un dauphin qui ne vit que dans les "\n            "rivières. La rencontre des eaux sombres du rio Negro avec les eaux "\n            "boueuses du rio Solimões, près de Manaus, est un phénomène célèbre : les "\n            "deux coulent côte à côte sans se mélanger pendant plusieurs kilomètres. "\n            "Le fleuve Amazone est essentiel au transport, à l\'économie et à la vie de "\n            "millions de personnes dans la région Nord. Dans de nombreuses villes et "\n            "communautés, les bateaux font office de bus et transportent habitants, aliments "\n            "et marchandises entre des lieux sans routes. Les crues annuelles fertilisent les "\n            "zones voisines et transforment le paysage : des arbres qui semblent pousser sur "\n            "la terre ferme peuvent se retrouver entourés d\'eau. Les pêcheurs observent le "\n            "courant et connaissent les périodes où chaque espèce apparaît. Le fleuve n\'est "\n            "pas seulement une voie naturelle ; il fait partie du calendrier, du travail et "\n            "de la mémoire des populations amazoniennes. Dans de nombreuses villes et communautés, les bateaux font office de bus et transportent habitants, aliments et marchandises entre des lieux sans routes. Les crues annuelles fertilisent les zones voisines et transforment le paysage : des arbres qui semblent pousser sur la terre ferme peuvent se retrouver entourés d\'eau. Les pêcheurs observent le courant et connaissent les périodes où chaque espèce apparaît. Le fleuve n\'est pas seulement une voie naturelle ; il fait partie du calendrier, du travail et de la mémoire des populations amazoniennes.'        ),
                "quiz": [
            {
                "pergunta_pt": 'Em que oceano o Amazonas deságua?',
                "pergunta_fr": 'Dans quel océan l’Amazone se jette-t-il ?',
                "opcoes_pt": ['Pacífico.', 'Índico.', 'Atlântico.'],
                "opcoes_fr": ['Le Pacifique.', 'L’Indien.', 'L’Atlantique.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'O que os barcos fazem em muitas comunidades?',
                "pergunta_fr": 'Quel rôle jouent les bateaux dans de nombreuses communautés ?',
                "opcoes_pt": ['Produzem energia solar.', 'Servem como transporte.', 'Substituem as escolas.'],
                "opcoes_fr": ['Ils produisent de l’énergie solaire.', 'Ils servent de moyen de transport.', 'Ils remplacent les écoles.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'Como o rio influencia a vida local?',
                "pergunta_fr": 'Comment le fleuve influence-t-il la vie locale ?',
                "opcoes_pt": ['Faz parte do trabalho e do calendário.', 'Não afeta a rotina.', 'Só serve para o turismo.'],
                "opcoes_fr": ['Il fait partie du travail et du calendrier.', 'Il n’influence pas le quotidien.', 'Il sert uniquement au tourisme.'],
                "resposta": 0,
            },
        ],
"vocabulario": [
            {"pt": "nascer", "fr": "naître"},
            {"pt": "largura", "fr": "largeur"},
            {"pt": "foz", "fr": "embouchure"},
            {"pt": "peixe", "fr": "poisson"},
        ],
    },
    {
        "slug": "pantanal",
        "categoria": "natureza",
        "nivel": "intermediario",
        "emoji": "🐆",
        "titulo_pt": "O Pantanal",
        "titulo_fr": "Le Pantanal",
        "texto_pt": (
            'O Pantanal é a maior planície alagável do planeta, com cerca de 150 mil "\n            "quilômetros quadrados. Ele fica principalmente nos estados de Mato Grosso "\n            "e Mato Grosso do Sul, no centro-oeste do Brasil, mas também se estende "\n            "pela Bolívia e pelo Paraguai. Durante a estação das chuvas, os rios "\n            "transbordam e grande parte da região fica submersa; na seca, a água recua "\n            "e concentra os animais nas áreas úmidas que restam. Esse ciclo torna o "\n            "Pantanal um dos melhores lugares do mundo para observar animais "\n            "selvagens. Ali vivem a onça-pintada, o maior felino das Américas, além da "\n            "arara-azul, do tuiuiú (símbolo do Pantanal), da ariranha, do "\n            "jacaré-do-pantanal e de centenas de espécies de aves. A pesca esportiva e "\n            "o ecoturismo movimentam a economia local. Em 2000, o Pantanal foi "\n            "declarado Patrimônio Natural da Humanidade pela UNESCO, reconhecendo sua "\n            "importância ecológica única. A rotina acompanha o movimento da água. Nas cheias, barcos substituem caminhos e canoas chegam a áreas isoladas; na seca, surgem praias de rio e estradas de terra. Guias locais ajudam visitantes a observar animais sem se aproximar demais, especialmente as onças, que precisam de espaço. O turismo responsável pode gerar renda para as comunidades, desde que respeite os períodos de reprodução da fauna e mantenha o lixo longe dos rios.'      ),
        "texto_fr": (
            'Le Pantanal est la plus grande plaine inondable de la planète, avec "\n            "environ 150 000 kilomètres carrés. Il se situe principalement dans les "\n            "États du Mato Grosso et du Mato Grosso do Sul, au centre-ouest du "\n            "Brésil, mais il s\'étend aussi sur la Bolivie et le Paraguay. Pendant la "\n            "saison des pluies, les rivières débordent et une grande partie de la "\n            "région se retrouve sous l\'eau ; à la saison sèche, l\'eau se retire et "\n            "concentre les animaux dans les zones humides restantes. Ce cycle fait du "\n            "Pantanal l\'un des meilleurs endroits du monde pour observer les animaux "\n            "sauvages. On y trouve le jaguar, le plus grand félin des Amériques, ainsi "\n            "que l\'ara bleu, le jabiru (symbole du Pantanal), la loutre géante, le "\n            "caïman et des centaines d\'espèces d\'oiseaux. La pêche sportive et "\n            "l\'écotourisme font vivre l\'économie locale. En 2000, le Pantanal a été "\n            "déclaré patrimoine naturel de l\'humanité par l\'UNESCO, en reconnaissance "\n            "de son importance écologique unique. La vie quotidienne suit le mouvement de l\'eau. Pendant les crues, les bateaux remplacent les chemins et les canoës atteignent des zones isolées ; à la saison sèche, des plages fluviales et des pistes apparaissent. Les guides locaux aident les visiteurs à observer les animaux sans trop s\'approcher, surtout les jaguars, qui ont besoin d\'espace. Un tourisme responsable peut apporter des revenus aux communautés, à condition de respecter les périodes de reproduction de la faune et de garder les déchets loin des rivières.'        ),
                "quiz": [
            {
                "pergunta_pt": 'O que acontece na estação das chuvas?',
                "pergunta_fr": 'Que se passe-t-il pendant la saison des pluies ?',
                "opcoes_pt": ['Os rios secam.', 'Os rios transbordam.', 'A região fica coberta de neve.'],
                "opcoes_fr": ['Les rivières s’assèchent.', 'Les rivières débordent.', 'La région se couvre de neige.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'Qual animal é citado como símbolo do Pantanal?',
                "pergunta_fr": 'Quel animal est cité comme symbole du Pantanal ?',
                "opcoes_pt": ['O tuiuiú.', 'O pinguim.', 'O urso-polar.'],
                "opcoes_fr": ['Le jabiru.', 'Le pingouin.', 'L’ours polaire.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'Como o turismo pode ajudar a região?',
                "pergunta_fr": 'Comment le tourisme peut-il aider la région ?',
                "opcoes_pt": ['Afastando as comunidades.', 'Alimentando os animais selvagens.', 'Gerando renda com respeito à natureza.'],
                "opcoes_fr": ['En éloignant les communautés.', 'En nourrissant les animaux sauvages.', 'En apportant des revenus dans le respect de la nature.'],
                "resposta": 2,
            },
        ],
"vocabulario": [
            {"pt": "planície", "fr": "plaine"},
            {"pt": "alagável", "fr": "inondable"},
            {"pt": "onça-pintada", "fr": "jaguar"},
            {"pt": "observar", "fr": "observer"},
        ],
    },
    {
        "slug": "mata-atlantica",
        "categoria": "natureza",
        "nivel": "intermediario",
        "emoji": "🌿",
        "titulo_pt": "A Mata Atlântica",
        "titulo_fr": "La forêt atlantique",
        "texto_pt": (
            'A Mata Atlântica é a floresta que acompanha grande parte do litoral "\n            "brasileiro. No passado, ela cobria cerca de 1,3 milhão de quilômetros "\n            "quadrados, do Rio Grande do Norte ao Rio Grande do Sul. Hoje, "\n            "infelizmente, restam apenas cerca de 12% da vegetação original, o que a "\n            "torna um dos biomas mais ameaçados do planeta. A maior parte das grandes "\n            "cidades do Brasil, como São Paulo e Rio de Janeiro, foi construída sobre "\n            "áreas que já foram floresta. Apesar da redução, a Mata Atlântica continua "\n            "sendo uma das regiões com maior biodiversidade do mundo, com milhares de "\n            "espécies de plantas e animais, muitos deles encontrados em nenhum outro "\n            "lugar. É o caso do mico-leão-dourado, um pequeno primata que virou "\n            "símbolo da conservação. A preservação da Mata Atlântica é fundamental não "\n            "só para a natureza, mas também para garantir água e qualidade de vida "\n            "para milhões de brasileiros. A floresta ajuda a proteger encostas e nascentes, reduzindo a erosão e mantendo a água mais limpa. Corredores verdes permitem que animais se desloquem entre fragmentos de mata em busca de alimento e parceiros. Projetos de restauração plantam espécies nativas e conectam áreas preservadas, enquanto reservas urbanas oferecem espaços de lazer e contato com a natureza. A recuperação leva tempo, mas cada trecho protegido fortalece a paisagem onde vive grande parte da população.'        ),
        "texto_fr": (
            'La forêt atlantique (Mata Atlântica) est la forêt qui longe une grande "\n            "partie du littoral brésilien. Autrefois, elle couvrait environ 1,3 "\n            "million de kilomètres carrés, du Rio Grande do Norte au Rio Grande do "\n            "Sul. Aujourd\'hui, malheureusement, il ne reste qu\'environ 12 % de la "\n            "végétation d\'origine, ce qui en fait l\'un des biomes les plus menacés de "\n            "la planète. La plupart des grandes villes du Brésil, comme São Paulo et "\n            "Rio de Janeiro, ont été construites sur des zones qui étaient autrefois "\n            "couvertes de forêt. Malgré cette réduction, la forêt atlantique reste "\n            "l\'une des régions à la plus grande biodiversité du monde, avec des "\n            "milliers d\'espèces de plantes et d\'animaux, dont beaucoup ne se trouvent "\n            "nulle part ailleurs. C\'est le cas du tamarin-lion doré, un petit primate "\n            "devenu un symbole de la conservation. La préservation de la forêt "\n            "atlantique est essentielle non seulement pour la nature, mais aussi pour "\n            "garantir l\'eau et la qualité de vie de millions de Brésiliens. La forêt protège les pentes et les sources, limite l\'érosion et garde l\'eau plus propre. Des corridors verts permettent aux animaux de passer entre les fragments de forêt pour trouver de la nourriture et des partenaires. Des projets de restauration plantent des espèces locales et relient les zones préservées, tandis que des réserves urbaines offrent des lieux de promenade et de contact avec la nature. La restauration prend du temps, mais chaque espace protégé renforce le paysage où vit une grande partie de la population.'       ),
                "quiz": [
            {
                "pergunta_pt": 'Onde fica a Mata Atlântica?',
                "pergunta_fr": 'Où se trouve la forêt atlantique ?',
                "opcoes_pt": ['Ao longo de grande parte do litoral brasileiro.', 'No centro do deserto.', 'Somente no sul da Argentina.'],
                "opcoes_fr": ['Le long d’une grande partie du littoral brésilien.', 'Au centre du désert.', 'Uniquement dans le sud de l’Argentine.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'O que corredores verdes permitem?',
                "pergunta_fr": 'Que permettent les corridors verts ?',
                "opcoes_pt": ['A construção de fábricas.', 'A interrupção dos rios.', 'A circulação de animais entre áreas.'],
                "opcoes_fr": ['La construction d’usines.', 'L’interruption des rivières.', 'Le déplacement des animaux entre les zones.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'Por que a floresta também importa às cidades?',
                "pergunta_fr": 'Pourquoi cette forêt compte-t-elle aussi pour les villes ?',
                "opcoes_pt": ['Substitui o transporte público.', 'Ajuda a proteger água e encostas.', 'Aumenta o trânsito.'],
                "opcoes_fr": ['Elle remplace les transports publics.', 'Elle aide à protéger l’eau et les pentes.', 'Elle augmente la circulation.'],
                "resposta": 1,
            },
        ],
"vocabulario": [
            {"pt": "litoral", "fr": "littoral"},
            {"pt": "cobrir", "fr": "couvrir"},
            {"pt": "espécie", "fr": "espèce"},
            {"pt": "ameaçado", "fr": "menacé"},
        ],
    },
    {
        "slug": "cerrado",
        "categoria": "natureza",
        "nivel": "intermediario",
        "emoji": "🌾",
        "titulo_pt": "O Cerrado",
        "titulo_fr": "Le Cerrado",
        "texto_pt": (
            'O Cerrado é o segundo maior bioma do Brasil, atrás apenas da Amazônia, "\n            "ocupando cerca de 2 milhões de quilômetros quadrados, principalmente na "\n            "região central do país. É uma savana tropical com árvores baixas e "\n            "tortuosas, arbustos e gramíneas, adaptada a um clima com uma estação seca "\n            "bem marcada. Muitas pessoas o chamam de \'savana mais rica do mundo\' por "\n            "causa de sua biodiversidade. O Cerrado é conhecido como o \'berço das "\n            "águas\' porque abriga as nascentes de grandes rios brasileiros, como o São "\n            "Francisco, o Tocantins e afluentes do Paraná. Sua fauna inclui o "\n            "lobo-guará, o tamanduá-bandeira, o tatu-canastra e o gato-maracajá. "\n            "Infelizmente, grande parte do Cerrado já foi transformada em áreas de "\n            "soja, milho e pastagem, o que ameaça suas águas e seus animais. A "\n            "conservação desse bioma é considerada estratégica para o abastecimento de "\n            "água do país. As árvores de troncos retorcidos parecem frágeis, mas muitas têm raízes profundas e casca grossa, adaptações que ajudam a enfrentar a seca e as queimadas naturais. O fogo se torna destrutivo quando acontece com frequência ou é provocado para abrir novas áreas. No início das chuvas, o Cerrado muda rapidamente: flores aparecem, a vegetação fica verde e os animais encontram água e alimento. Pesquisadores e comunidades locais trabalham para proteger nascentes e produzir sem eliminar a savana.'       ),
        "texto_fr": (
            'Le Cerrado est le deuxième plus grand biome du Brésil, juste après "\n            "l\'Amazonie, occupant environ 2 millions de kilomètres carrés, "\n            "principalement dans la région centrale du pays. C\'est une savane "\n            "tropicale composée d\'arbres bas et tordus, d\'arbustes et d\'herbes, "\n            "adaptée à un climat marqué par une saison sèche bien définie. Beaucoup "\n            "l\'appellent la « savane la plus riche du monde » en raison de sa "\n            "biodiversité. Le Cerrado est surnommé le « berceau des eaux » car il "\n            "abrite les sources de grands fleuves brésiliens, comme le São Francisco, "\n            "le Tocantins et des affluents du Paraná. Sa faune comprend le loup à "\n            "crinière, le tamanoir, le tatou géant et l\'ocelot. Malheureusement, une "\n            "grande partie du Cerrado a déjà été transformée en champs de soja, de "\n            "maïs et en pâturages, ce qui menace ses eaux et ses animaux. La "\n            "conservation de ce biome est considérée comme stratégique pour "\n            "l\'approvisionnement en eau du pays. Les arbres aux troncs tordus semblent fragiles, mais beaucoup ont des racines profondes et une écorce épaisse qui les aident à résister à la sécheresse et aux incendies naturels. Le feu devient destructeur lorsqu\'il revient souvent ou qu\'il est provoqué pour ouvrir de nouvelles terres. Au début des pluies, le Cerrado change vite : les fleurs apparaissent, la végétation verdit et les animaux trouvent de l\'eau et de la nourriture. Des chercheurs et des communautés locales protègent les sources et cherchent à produire sans faire disparaître la savane.'
        ),
                "quiz": [
            {
                "pergunta_pt": 'Por que o Cerrado é chamado de “berço das águas”?',
                "pergunta_fr": 'Pourquoi le Cerrado est-il surnommé « berceau des eaux » ?',
                "opcoes_pt": ['Recebe água de geleiras.', 'Abriga nascentes de grandes rios.', 'Tem o maior oceano do Brasil.'],
                "opcoes_fr": ['Il reçoit l’eau des glaciers.', 'Il abrite les sources de grands fleuves.', 'Il possède le plus grand océan du Brésil.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'Como muitas árvores do Cerrado enfrentam a seca?',
                "pergunta_fr": 'Comment de nombreux arbres du Cerrado résistent-ils à la sécheresse ?',
                "opcoes_pt": ['Com raízes profundas e casca grossa.', 'Com folhas de gelo.', 'Vivendo debaixo d’água.'],
                "opcoes_fr": ['Grâce à leurs racines profondes et à leur écorce épaisse.', 'Grâce à des feuilles de glace.', 'En vivant sous l’eau.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'Quando o fogo se torna especialmente destrutivo?',
                "pergunta_fr": 'Quand le feu devient-il particulièrement destructeur ?',
                "opcoes_pt": ['Quando cai uma chuva leve.', 'Quando as flores aparecem.', 'Quando ocorre com frequência ou é provocado.'],
                "opcoes_fr": ['Lorsqu’une pluie légère tombe.', 'Lorsque les fleurs apparaissent.', 'Lorsqu’il revient souvent ou qu’il est provoqué.'],
                "resposta": 2,
            },
        ],
"vocabulario": [
            {"pt": "bioma", "fr": "biome"},
            {"pt": "savana", "fr": "savane"},
            {"pt": "nascente", "fr": "source"},
            {"pt": "lobo-guará", "fr": "loup à crinière"},
        ],
    },
    {
        "slug": "caatinga",
        "categoria": "natureza",
        "nivel": "avancado",
        "emoji": "🌵",
        "titulo_pt": "A Caatinga",
        "titulo_fr": "La Caatinga",
        "texto_pt": (
            'A Caatinga é o único bioma exclusivamente brasileiro e ocupa quase todo o "\n            "sertão do Nordeste. Seu nome vem da língua tupi e significa \'mata "\n            "branca\', por causa da aparência esbranquiçada da vegetação na longa "\n            "estação seca, quando a maioria das árvores perde as folhas. O clima é "\n            "semiárido, com chuvas irregulares e longos períodos de seca, o que moldou "\n            "uma vegetação única. As plantas da Caatinga, como o mandacaru, o "\n            "xique-xique e a carnaúba, desenvolveram estratégias para sobreviver com "\n            "pouca água, como espinhos e raízes profundas. A fauna também é especial: "\n            "o tatu-bola, a arara-azul-de-lear e o preá são alguns exemplos. Apesar da "\n            "aparência seca, o bioma é rico em vida e é a casa de milhões de "\n            "nordestinos, que adaptaram sua cultura, sua música e sua culinária ao "\n            "ritmo das chuvas. A Caatinga é um símbolo da resistência e da identidade "\n            "do povo do sertão. Quando a chuva chega, o solo seco absorve a água e a paisagem pode florescer em poucos dias. Essa mudança influencia festas, plantios e deslocamentos: famílias acompanham a previsão do tempo e guardam água para os meses mais difíceis. Cisternas e sistemas comunitários de captação ajudam a atravessar os períodos sem chuva. Conhecer a Caatinga é reconhecer que a vida no semiárido não se resume à seca; é também uma cultura de conhecimento, adaptação e criatividade.'        ),
        "texto_fr": (
            'La Caatinga est le seul biome exclusivement brésilien et elle occupe "\n            "presque tout le sertão du Nordeste. Son nom vient de la langue tupi et "\n            "signifie « forêt blanche », à cause de l\'apparence blanchâtre de la "\n            "végétation pendant la longue saison sèche, quand la plupart des arbres "\n            "perdent leurs feuilles. Le climat est semi-aride, avec des pluies "\n            "irrégulières et de longues périodes de sécheresse, ce qui a façonné une "\n            "végétation unique. Les plantes de la Caatinga, comme le mandacaru, le "\n            "xique-xique et le carnauba, ont développé des stratégies pour survivre "\n            "avec peu d\'eau, comme des épines et des racines profondes. La faune est "\n            "elle aussi spéciale : le tatou à trois bandes, l\'ara de Lear et le cobaye "\n            "en sont quelques exemples. Malgré son apparence sèche, le biome est riche "\n            "en vie et il est la maison de millions de Nordestins, qui ont adapté leur "\n            "culture, leur musique et leur cuisine au rythme des pluies. La Caatinga "\n            "est un symbole de la résistance et de l\'identité du peuple du sertão. Lorsque la pluie arrive, le sol sec absorbe l\'eau et le paysage peut fleurir en quelques jours. Ce changement influence les fêtes, les cultures et les déplacements : les familles suivent la météo et gardent de l\'eau pour les mois difficiles. Des citernes et des systèmes communautaires de collecte aident à traverser les périodes sans pluie. Découvrir la Caatinga, c\'est comprendre que la vie dans le semi-aride ne se résume pas à la sécheresse : c\'est aussi une culture de savoir, d\'adaptation et de créativité.'      ),
                "quiz": [
            {
                "pergunta_pt": 'O que significa o nome Caatinga?',
                "pergunta_fr": 'Que signifie le nom Caatinga ?',
                "opcoes_pt": ['Mata branca.', 'Rio profundo.', 'Terra gelada.'],
                "opcoes_fr": ['Forêt blanche.', 'Fleuve profond.', 'Terre glacée.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'Como a população guarda água para os períodos secos?',
                "pergunta_fr": 'Comment la population conserve-t-elle l’eau pendant les périodes sèches ?',
                "opcoes_pt": ['Com neve.', 'Com canais marítimos.', 'Com cisternas e captação comunitária.'],
                "opcoes_fr": ['Avec de la neige.', 'Avec des canaux maritimes.', 'Grâce à des citernes et à la collecte communautaire.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'A vida na Caatinga é descrita como...',
                "pergunta_fr": 'Comment la vie dans la Caatinga est-elle décrite ?',
                "opcoes_pt": ['Uma vida sem mudanças.', 'Uma cultura de adaptação e criatividade.', 'Uma região sem cultura.'],
                "opcoes_fr": ['Une vie sans changements.', 'Une culture d’adaptation et de créativité.', 'Une région sans culture.'],
                "resposta": 1,
            },
        ],
"vocabulario": [
            {"pt": "seca", "fr": "sécheresse"},
            {"pt": "chuva", "fr": "pluie"},
            {"pt": "semiárido", "fr": "semi-aride"},
            {"pt": "sertão", "fr": "sertão"},
        ],
    },
    {
        "slug": "cataratas-do-iguacu",
        "categoria": "natureza",
        "nivel": "iniciante",
        "emoji": "💦",
        "titulo_pt": "As Cataratas do Iguaçu",
        "titulo_fr": "Les chutes d'Iguaçu",
        "texto_pt": (
            'As Cataratas do Iguaçu são um dos espetáculos naturais mais "\n            "impressionantes do mundo. Elas ficam no rio Iguaçu, na fronteira entre o "\n            "Brasil e a Argentina, dentro do Parque Nacional do Iguaçu, no estado do "\n            "Paraná. Ao todo, são cerca de 275 quedas d\'água que se estendem por quase "\n            "3 quilômetros, cercadas por mata preservada. A queda mais famosa é a "\n            "Garganta do Diabo, um canyon em forma de U com cerca de 80 metros de "\n            "altura, onde a água despenca com força impressionante, levantando uma "\n            "nuvem de névoa. Passarelas levam os visitantes até bem perto das quedas. "\n            "A região abriga animais como o quati e a jaguatirica. Em 1986, as "\n            "cataratas foram declaradas Patrimônio Natural da Humanidade pela UNESCO, "\n            "e em 2011 foram eleitas uma das Sete Maravilhas da Natureza. É um dos "\n            "destinos mais visitados do Brasil. O volume das quedas muda conforme a quantidade de chuva, por isso a paisagem pode ser diferente em cada visita. Em dias de sol, gotas formam arco-íris perto das passarelas; depois de uma chuva forte, o barulho e a névoa ficam ainda mais intensos. Do lado brasileiro, o caminho oferece uma vista ampla do conjunto; do lado argentino, trilhas passam perto de várias quedas. A floresta ao redor também merece atenção: borboletas, aves e quatis aparecem com frequência, e é importante não alimentar os animais.'
        ),
        "texto_fr": (
            'Les chutes d\'Iguaçu sont l\'un des spectacles naturels les plus "\n            "impressionnants du monde. Elles se trouvent sur le rio Iguaçu, à la "\n            "frontière entre le Brésil et l\'Argentine, dans le parc national d\'Iguaçu, "\n            "dans l\'État du Paraná. Au total, il y a environ 275 chutes d\'eau qui "\n            "s\'étendent sur près de 3 kilomètres, entourées de forêt préservée. La "\n            "chute la plus célèbre est la Garganta do Diabo (gorge du Diable), un "\n            "canyon en forme de U haut d\'environ 80 mètres, où l\'eau plonge avec une "\n            "force impressionnante, soulevant un nuage de brume. Des passerelles "\n            "emmènent les visiteurs tout près des chutes. La région abrite des animaux "\n            "comme le coati et l\'ocelot. En 1986, les chutes ont été déclarées "\n            "patrimoine naturel de l\'humanité par l\'UNESCO, et en 2011 elles ont été "\n            "élues l\'une des sept merveilles de la nature. C\'est l\'une des "\n            "destinations les plus visitées du Brésil. Le volume des chutes varie selon la quantité de pluie ; le paysage peut donc être différent à chaque visite. Par temps ensoleillé, des gouttes forment des arcs-en-ciel près des passerelles ; après de fortes pluies, le bruit et la brume deviennent plus intenses. Du côté brésilien, le parcours offre une vue d\'ensemble ; du côté argentin, des sentiers passent près de plusieurs chutes. La forêt mérite aussi qu\'on s\'y attarde : papillons, oiseaux et coatis sont fréquents, et il est important de ne pas nourrir les animaux.'       ),
                "quiz": [
            {
                "pergunta_pt": 'Quantas quedas formam as Cataratas do Iguaçu, aproximadamente?',
                "pergunta_fr": 'Combien de chutes composent approximativement les chutes d’Iguaçu ?',
                "opcoes_pt": ['25.', '2.750.', '275.'],
                "opcoes_fr": ['25.', '2 750.', '275.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'O que pode aparecer perto das passarelas em dias de sol?',
                "pergunta_fr": 'Que peut-on voir près des passerelles par temps ensoleillé ?',
                "opcoes_pt": ['Dunas de areia.', 'Arco-íris.', 'Auroras boreais.'],
                "opcoes_fr": ['Des dunes de sable.', 'Des arcs-en-ciel.', 'Des aurores boréales.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'Qual atitude é recomendada ao encontrar animais?',
                "pergunta_fr": 'Quelle attitude est recommandée lorsqu’on rencontre des animaux ?',
                "opcoes_pt": ['Não alimentá-los.', 'Cham chamar para perto.', 'Levá-los para casa.'],
                "opcoes_fr": ['Ne pas les nourrir.', 'Les appeler pour les rapprocher.', 'Les ramener chez soi.'],
                "resposta": 0,
            },
        ],
"vocabulario": [
            {"pt": "queda d'água", "fr": "chute d'eau"},
            {"pt": "fronteira", "fr": "frontière"},
            {"pt": "altura", "fr": "hauteur"},
            {"pt": "névoa", "fr": "brume"},
        ],
    },
    {
        "slug": "lencois-maranhenses",
        "categoria": "geografia",
        "nivel": "intermediario",
        "emoji": "🏜️",
        "titulo_pt": "Os Lençóis Maranhenses",
        "titulo_fr": "Les Lençóis Maranhenses",
        "texto_pt": (
            'Os Lençóis Maranhenses são um parque nacional no estado do Maranhão, no "\n            "Nordeste do Brasil, famoso por uma paisagem que parece de outro planeta. "\n            "São imensas dunas de areia branca que se movem com o vento, entre as "\n            "quais se formam milhares de lagoas de água doce, azuis e verdes, de uma "\n            "beleza impressionante. Apesar de parecer um deserto, a região recebe "\n            "bastante chuva entre janeiro e junho, e é justamente essa água da chuva, "\n            "acumulada sobre uma camada de rocha impermeável, que forma as lagoas "\n            "temporárias. A melhor época para visitar é logo após as chuvas, quando as "\n            "lagoas estão cheias. O parque tem cerca de 155 mil hectares e abriga "\n            "comunidades de pescadores que vivem em oásis. Os Lençóis Maranhenses são "\n            "considerados um dos lugares mais bonitos e singulares do Brasil. As lagoas aparecem porque a água da chuva fica retida entre as dunas, sobre uma camada de rocha que impede a infiltração rápida. Por isso, a melhor época para ver as piscinas cheias costuma ser depois da estação chuvosa; ao longo dos meses secos, algumas diminuem ou desaparecem. O vento redesenha as dunas continuamente, então a paisagem nunca é exatamente igual. Pequenas comunidades vivem da pesca, do artesanato e do turismo, e os passeios com guias locais ajudam a conhecer o parque sem abrir novas trilhas sobre a vegetação delicada.'
        ),
        "texto_fr": (
            'Les Lençóis Maranhenses sont un parc national dans l\'État du Maranhão, "\n            "dans le Nordeste du Brésil, célèbre pour un paysage qui semble venir "\n            "d\'une autre planète. Ce sont d\'immenses dunes de sable blanc qui se "\n            "déplacent avec le vent, entre lesquelles se forment des milliers de "\n            "lagunes d\'eau douce, bleues et vertes, d\'une beauté impressionnante. Bien "\n            "que le paysage ressemble à un désert, la région reçoit beaucoup de pluie "\n            "entre janvier et juin, et c\'est justement cette eau de pluie, accumulée "\n            "sur une couche de roche imperméable, qui forme les lagunes temporaires. "\n            "La meilleure période pour visiter est juste après les pluies, quand les "\n            "lagunes sont pleines. Le parc compte environ 155 000 hectares et abrite "\n            "des communautés de pêcheurs qui vivent dans des oasis. Les Lençóis "\n            "Maranhenses sont considérés comme l\'un des endroits les plus beaux et les "\n            "plus singuliers du Brésil. Les lagunes se forment parce que l\'eau de pluie reste entre les dunes, au-dessus d\'une couche rocheuse qui ralentit son infiltration. La meilleure période pour voir les bassins remplis se situe donc souvent après la saison des pluies ; pendant les mois secs, certains diminuent ou disparaissent. Le vent redessine sans cesse les dunes, et le paysage n\'est jamais tout à fait le même. De petites communautés vivent de la pêche, de l\'artisanat et du tourisme. Les excursions avec des guides locaux permettent de découvrir le parc sans ouvrir de nouveaux sentiers dans la végétation fragile.'        ),
                "quiz": [
            {
                "pergunta_pt": 'Como se formam as lagoas entre as dunas?',
                "pergunta_fr": 'Comment se forment les lagunes entre les dunes ?',
                "opcoes_pt": ['A chuva fica retida entre as dunas.', 'A água vem de vulcões.', 'O mar cobre o parque todo dia.'],
                "opcoes_fr": ['L’eau de pluie reste entre les dunes.', 'L’eau vient des volcans.', 'La mer recouvre le parc chaque jour.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'O que o vento faz com as dunas?',
                "pergunta_fr": 'Que fait le vent aux dunes ?',
                "opcoes_pt": ['Transforma-as em florestas.', 'Faz desaparecer o parque.', 'Redesenha continuamente a paisagem.'],
                "opcoes_fr": ['Il les transforme en forêts.', 'Il fait disparaître le parc.', 'Il redessine constamment le paysage.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'Quem pode ajudar a conhecer o parque com cuidado?',
                "pergunta_fr": 'Qui peut aider à découvrir le parc avec soin ?',
                "opcoes_pt": ['Somente pescadores estrangeiros.', 'Guias locais.', 'Pilotos de corrida.'],
                "opcoes_fr": ['Uniquement des pêcheurs étrangers.', 'Les guides locaux.', 'Les pilotes de course.'],
                "resposta": 1,
            },
        ],
"vocabulario": [
            {"pt": "dunas", "fr": "dunes"},
            {"pt": "areia", "fr": "sable"},
            {"pt": "lagoa", "fr": "lagune"},
            {"pt": "deserto", "fr": "désert"},
        ],
    },
    {
        "slug": "descobrimento-do-brasil",
        "categoria": "historia",
        "nivel": "iniciante",
        "emoji": "⛵",
        "titulo_pt": "O Descobrimento do Brasil",
        "titulo_fr": "La découverte du Brésil",
        "texto_pt": (
            'O Brasil foi descoberto pelos portugueses em 22 de abril de 1500, quando "\n            "a esquadra comandada por Pedro Álvares Cabral chegou ao litoral do atual "\n            "estado da Bahia, na região de Porto Seguro. A frota tinha partido de "\n            "Lisboa com destino às Índias e acabou alcançando terras que, segundo o "\n            "Tratado de Tordesilhas, pertenciam a Portugal. Antes da chegada dos "\n            "europeus, o território já era habitado havia milhares de anos por milhões "\n            "de indígenas de centenas de povos diferentes, com suas próprias línguas e "\n            "culturas. A primeira missa em terra foi celebrada em 26 de abril de 1500. "\n            "O novo território foi inicialmente chamado de Ilha de Vera Cruz e, "\n            "depois, Terra de Santa Cruz. O nome \'Brasil\' surgiu mais tarde, por causa "\n            "do pau-brasil, uma árvore muito valorizada. A chegada dos portugueses deu "\n            "início à colonização e fez do português a língua do país. A chegada não aconteceu em uma terra vazia: milhões de pessoas indígenas já viviam em diferentes regiões, com línguas, conhecimentos e formas próprias de organização. Nos primeiros anos, os portugueses estabeleceram feitorias no litoral e exploraram o pau-brasil com trabalho indígena, muitas vezes por meio de trocas forçadas. Depois vieram a ocupação permanente, a produção de açúcar e a escravização de africanos. Por isso, hoje muitos historiadores preferem falar em chegada dos portugueses, lembrando que o território já tinha seus povos e sua história.'  ),
        "texto_fr": (
            'Le Brésil a été découvert par les Portugais le 22 avril 1500, lorsque "\n            "l\'escadre commandée par Pedro Álvares Cabral est arrivée sur la côte de "\n            "l\'actuel État de Bahia, dans la région de Porto Seguro. La flotte était "\n            "partie de Lisbonne en direction des Indes et a fini par atteindre des "\n            "terres qui, selon le traité de Tordesillas, appartenaient au Portugal. "\n            "Avant l\'arrivée des Européens, le territoire était habité depuis des "\n            "milliers d\'années par des millions d\'indigènes appartenant à des "\n            "centaines de peuples différents, avec leurs propres langues et cultures. "\n            "La première messe sur terre a été célébrée le 26 avril 1500. Le nouveau "\n            "territoire a d\'abord été appelé Ilha de Vera Cruz, puis Terra de Santa "\n            "Cruz. Le nom « Brésil » est apparu plus tard, à cause du pau-brasil (bois "\n            "de Brésil), un arbre très prisé. L\'arrivée des Portugais a marqué le "\n            "début de la colonisation et a fait du portugais la langue du pays. L\'arrivée ne se fit pas sur une terre vide : des millions d\'Autochtones vivaient déjà dans différentes régions, avec leurs langues, leurs savoirs et leurs propres formes d\'organisation. Au début, les Portugais établirent des comptoirs sur la côte et exploitèrent le pau-brasil grâce au travail des Autochtones, souvent au moyen d\'échanges forcés. Vinrent ensuite l\'occupation permanente, la production de sucre et l\'asservissement d\'Africains. C\'est pourquoi de nombreux historiens préfèrent aujourd\'hui parler de l\'arrivée des Portugais, en rappelant que le territoire avait déjà ses peuples et son histoire.'        ),
                "quiz": [
            {
                "pergunta_pt": 'Quem já vivia no território antes da chegada portuguesa?',
                "pergunta_fr": 'Qui vivait déjà sur le territoire avant l’arrivée des Portugais ?',
                "opcoes_pt": ['Ninguém.', 'Somente comerciantes europeus.', 'Povos indígenas.'],
                "opcoes_fr": ['Personne.', 'Uniquement des commerçants européens.', 'Des peuples autochtones.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'Para que era explorado o pau-brasil?',
                "pergunta_fr": 'Pourquoi le pau-brasil était-il exploité ?',
                "opcoes_pt": ['Para produzir café.', 'Sua madeira e tinta valiosas.', 'Para fabricar barcos de aço.'],
                "opcoes_fr": ['Pour produire du café.', 'Pour son bois et sa teinture précieux.', 'Pour fabriquer des bateaux en acier.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'Por que alguns historiadores preferem “chegada dos portugueses”?',
                "pergunta_fr": 'Pourquoi certains historiens préfèrent-ils parler de « l’arrivée des Portugais » ?',
                "opcoes_pt": ['Porque o território já tinha povos e história.', 'Porque os portugueses não chegaram.', 'Porque o Brasil ainda não tinha rios.'],
                "opcoes_fr": ['Parce que le territoire avait déjà des peuples et une histoire.', 'Parce que les Portugais ne sont pas arrivés.', 'Parce que le Brésil n’avait pas encore de rivières.'],
                "resposta": 0,
            },
        ],
"vocabulario": [
            {"pt": "descobrir", "fr": "découvrir"},
            {"pt": "esquadra", "fr": "escadre"},
            {"pt": "litoral", "fr": "littoral"},
            {"pt": "missa", "fr": "messe"},
        ],
    },
    {
        "slug": "independencia-do-brasil",
        "categoria": "historia",
        "nivel": "iniciante",
        "emoji": "🇧🇷",
        "titulo_pt": "A Independência do Brasil",
        "titulo_fr": "L'indépendance du Brésil",
        "texto_pt": (
            'A independência do Brasil foi proclamada em 7 de setembro de 1822. Dom "\n            "Pedro I, filho do rei Dom João VI de Portugal, estava às margens do "\n            "riacho do Ipiranga, em São Paulo, quando recebeu cartas de Portugal "\n            "exigindo seu retorno. Segundo a tradição, ele então desembainhou a espada "\n            "e gritou: \'Independência ou Morte!\'. Esse episódio ficou conhecido como o "\n            "Grito do Ipiranga. Com a independência, o Brasil deixou de ser colônia de "\n            "Portugal e se tornou um império independente, com Dom Pedro I como "\n            "primeiro imperador. O processo foi relativamente pacífico em comparação "\n            "com outros países da América, embora tenha havido resistências em algumas "\n            "províncias. O dia 7 de setembro é feriado nacional no Brasil e é "\n            "celebrado com desfiles cívicos e militares em todo o país, sendo uma das "\n            "datas mais importantes da história brasileira. A separação de Portugal, porém, não transformou imediatamente a vida de todos: a escravidão continuou e a maior parte da população não participou das decisões políticas. Nos anos seguintes, diferentes províncias resistiram ao novo governo, e conflitos armados mostraram que a unidade do país ainda precisava ser negociada. O Brasil tornou-se uma monarquia independente, governada por Dom Pedro I, e só em 1889 passou a ser uma república. A data de 7 de setembro é celebrada como um marco, mas a construção da independência foi um processo mais longo.'        ),
        "texto_fr": (
            'L\'indépendance du Brésil a été proclamée le 7 septembre 1822. Dom Pedro "\n            "Ier, fils du roi Dom João VI de Portugal, se trouvait au bord du ruisseau "\n            "Ipiranga, à São Paulo, lorsqu\'il a reçu des lettres du Portugal exigeant "\n            "son retour. Selon la tradition, il a alors dégainé son épée et crié : "\n            "« Independência ou Morte ! » (l\'indépendance ou la mort). Cet épisode est "\n            "connu sous le nom de « Cri d\'Ipiranga ». Avec l\'indépendance, le Brésil a "\n            "cessé d\'être une colonie du Portugal et il est devenu un empire "\n            "indépendant, avec Dom Pedro Ier comme premier empereur. Le processus a "\n            "été relativement pacifique par rapport à d\'autres pays d\'Amérique, même "\n            "s\'il y a eu des résistances dans certaines provinces. Le 7 septembre est "\n            "un jour férié national au Brésil et il est célébré avec des défilés "\n            "civiques et militaires dans tout le pays, étant l\'une des dates les plus "\n            "importantes de l\'histoire brésilienne. La séparation d\'avec le Portugal ne transforma pourtant pas immédiatement la vie de tous : l\'esclavage continua et la majeure partie de la population ne participa pas aux décisions politiques. Dans les années suivantes, plusieurs provinces résistèrent au nouveau gouvernement et des conflits armés montrèrent que l\'unité du pays restait à construire. Le Brésil devint une monarchie indépendante dirigée par Dom Pedro Ier et ne devint une république qu\'en 1889. Le 7 septembre est célébré comme une date clé, mais la construction de l\'indépendance fut un processus plus long.'        ),
                "quiz": [
            {
                "pergunta_pt": 'Em que ano ocorreu a independência do Brasil?',
                "pergunta_fr": 'En quelle année l’indépendance du Brésil a-t-elle eu lieu ?',
                "opcoes_pt": ['1500.', '1889.', '1822.'],
                "opcoes_fr": ['1500.', '1889.', '1822.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'A escravidão terminou imediatamente com a independência?',
                "pergunta_fr": 'L’esclavage a-t-il pris fin immédiatement avec l’indépendance ?',
                "opcoes_pt": ['Não existia escravidão.', 'Não.', 'Sim.'],
                "opcoes_fr": ['L’esclavage n’existait pas.', 'Non.', 'Oui.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'Quando o Brasil se tornou uma república?',
                "pergunta_fr": 'Quand le Brésil est-il devenu une république ?',
                "opcoes_pt": ['Em 1889.', 'Em 1822.', 'Em 1960.'],
                "opcoes_fr": ['En 1889.', 'En 1822.', 'En 1960.'],
                "resposta": 0,
            },
        ],
"vocabulario": [
            {"pt": "proclamar", "fr": "proclamer"},
            {"pt": "colônia", "fr": "colonie"},
            {"pt": "império", "fr": "empire"},
            {"pt": "feriado", "fr": "jour férié"},
        ],
    },
    {
        "slug": "tiradentes",
        "categoria": "historia",
        "nivel": "avancado",
        "emoji": "⚖️",
        "titulo_pt": "Tiradentes e a Inconfidência Mineira",
        "titulo_fr": "Tiradentes et la Conjuration Mineira",
        "texto_pt": (
            'A Inconfidência Mineira foi um movimento do final do século XVIII que "\n            "queria a independência do Brasil e aconteceu na capitania de Minas "\n            "Gerais. O movimento reunia intelectuais, militares e religiosos "\n            "inspirados pelas ideias do Iluminismo e pela independência dos Estados "\n            "Unidos. Entre seus líderes estava Joaquim José da Silva Xavier, conhecido "\n            "como Tiradentes, pois havia trabalhado como dentista (\'tira-dentes\'). O "\n            "plano era aproveitar o momento em que Portugal cobraria uma dívida de "\n            "impostos para iniciar a rebelião, mas o movimento foi traído e descoberto "\n            "antes de começar. Os envolvidos foram presos e Tiradentes, que assumiu a "\n            "responsabilidade, foi condenado à morte. Ele foi enforcado e esquartejado "\n            "em 21 de abril de 1792, no Rio de Janeiro, como exemplo para a população. "\n            "Hoje, Tiradentes é considerado herói nacional e mártir da independência, "\n            "e o dia 21 de abril é feriado no Brasil. O movimento não chegou a começar: antes que os planos fossem colocados em prática, autoridades descobriram a conspiração e prenderam seus participantes em 1789. Tiradentes foi o único condenado à morte; os outros receberam penas de prisão ou foram enviados para fora do Brasil. Durante muito tempo, ele foi apresentado como símbolo de uma luta nacional pela independência, embora os conspiradores tivessem objetivos variados e nem todos defendessem o fim da escravidão. Estudar a Inconfidência ajuda a entender tanto as ideias políticas da época quanto os limites sociais daquele projeto.'        ),
        "texto_fr": (
            'L\'Inconfidência Mineira (Conjuration Mineira) était un mouvement de la "\n            "fin du XVIIIe siècle qui voulait l\'indépendance du Brésil et qui a eu "\n            "lieu dans la capitainerie du Minas Gerais. Le mouvement réunissait des "\n            "intellectuels, des militaires et des religieux inspirés par les idées des "\n            "Lumières et par l\'indépendance des États-Unis. Parmi ses dirigeants se "\n            "trouvait Joaquim José da Silva Xavier, connu sous le nom de Tiradentes, "\n            "car il avait travaillé comme dentiste (« arracheur de dents »). Le plan "\n            "était de profiter du moment où le Portugal réclamerait une dette d\'impôts "\n            "pour lancer la rébellion, mais le mouvement a été trahi et découvert avant "\n            "de commencer. Les participants ont été arrêtés et Tiradentes, qui a "\n            "assumé la responsabilité, a été condamné à mort. Il a été pendu et "\n            "écartelé le 21 avril 1792 à Rio de Janeiro, pour servir d\'exemple à la "\n            "population. Aujourd\'hui, Tiradentes est considéré comme un héros national "\n            "et un martyr de l\'indépendance, et le 21 avril est un jour férié au "\n            "Brésil. Le mouvement ne passa jamais à l\'action : avant la mise en œuvre des plans, les autorités découvrirent la conspiration et arrêtèrent ses participants en 1789. Tiradentes fut le seul condamné à mort ; les autres furent emprisonnés ou envoyés hors du Brésil. Il fut longtemps présenté comme le symbole d\'une lutte nationale pour l\'indépendance, même si les conspirateurs avaient des objectifs variés et que tous ne défendaient pas l\'abolition de l\'esclavage. Étudier l\'Inconfidência permet de comprendre les idées politiques de l\'époque ainsi que les limites sociales de ce projet.'        ),
                "quiz": [
            {
                "pergunta_pt": 'Qual era o objetivo principal da Inconfidência Mineira?',
                "pergunta_fr": 'Quel était l’objectif principal de l’Inconfidência Mineira ?',
                "opcoes_pt": ['Proclamar a república francesa.', 'Buscar autonomia em relação a Portugal.', 'Criar uma nova rota marítima.'],
                "opcoes_fr": ['Proclamer la république française.', 'Chercher l’autonomie par rapport au Portugal.', 'Créer une nouvelle route maritime.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'Quando a conspiração foi descoberta?',
                "pergunta_fr": 'Quand la conspiration a-t-elle été découverte ?',
                "opcoes_pt": ['Em 1789.', 'Em 1500.', 'Em 1889.'],
                "opcoes_fr": ['En 1789.', 'En 1500.', 'En 1889.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'Por que a história de Tiradentes é complexa?',
                "pergunta_fr": 'Pourquoi l’histoire de Tiradentes est-elle complexe ?',
                "opcoes_pt": ['Todos defendiam exatamente as mesmas ideias.', 'O movimento ocorreu depois da república.', 'Os participantes tinham objetivos variados.'],
                "opcoes_fr": ['Tous défendaient exactement les mêmes idées.', 'Le mouvement eut lieu après la république.', 'Les participants avaient des objectifs variés.'],
                "resposta": 2,
            },
        ],
"vocabulario": [
            {"pt": "movimento", "fr": "mouvement"},
            {"pt": "independência", "fr": "indépendance"},
            {"pt": "condenado", "fr": "condamné"},
            {"pt": "herói", "fr": "héros"},
        ],
    },
    {
        "slug": "abolicao-da-escravatura",
        "categoria": "historia",
        "nivel": "avancado",
        "emoji": "🕊️",
        "titulo_pt": "A Abolição da Escravatura",
        "titulo_fr": "L'abolition de l'esclavage",
        "texto_pt": (
            'A escravidão no Brasil durou mais de trezentos anos. Milhões de "\n            "africanos foram trazidos à força, em condições desumanas, para trabalhar "\n            "em fazendas de cana-de-açúcar, de café e nas minas. A abolição foi um "\n            "processo gradual, resultado de muita luta de abolicionistas, de "\n            "intelectuais como Joaquim Nabuco e da resistência dos próprios "\n            "escravizados. Em 1850, a Lei Eusébio de Queirós proibiu o tráfico de "\n            "escravos. Em 1871, a Lei do Ventre Livre declarou livres os filhos de "\n            "escravizadas nascidos a partir daquela data. Em 1885, a Lei dos "\n            "Sexagenários libertou os escravizados com mais de sessenta anos. "\n            "Finalmente, em 13 de maio de 1888, a princesa Isabel assinou a Lei Áurea, "\n            "que aboliu a escravidão. O Brasil foi o último país das Américas a "\n            "abolir a escravidão, e as consequências desse período, como o racismo e a "\n            "desigualdade, ainda são sentidas hoje. A liberdade legal não veio acompanhada de terra, moradia, educação ou reparação para quem havia sido escravizado. Muitas pessoas libertas continuaram trabalhando em condições precárias, enquanto leis e práticas sociais limitaram seu acesso a oportunidades. Essa ausência de políticas de inclusão contribuiu para desigualdades que atravessam gerações. Ao mesmo tempo, comunidades negras preservaram tradições, criaram associações e lideraram movimentos por direitos. Conhecer a abolição significa lembrar a ação dessas pessoas e observar como a luta por igualdade continua no presente.'        ),
        "texto_fr": (
            'L\'esclavage au Brésil a duré plus de trois cents ans. Des millions "\n            "d\'Africains ont été amenés de force, dans des conditions inhumaines, pour "\n            "travailler dans les plantations de canne à sucre, de café et dans les "\n            "mines. L\'abolition a été un processus graduel, fruit d\'une longue lutte "\n            "menée par les abolitionnistes, par des intellectuels comme Joaquim Nabuco "\n            "et par la résistance des esclaves eux-mêmes. En 1850, la loi Eusébio de "\n            "Queirós a interdit la traite des esclaves. En 1871, la loi du Ventre "\n            "Libre a déclaré libres les enfants des esclaves nés à partir de cette "\n            "date. En 1885, la loi des Sexagénaires a libéré les esclaves de plus de "\n            "soixante ans. Finalement, le 13 mai 1888, la princesse Isabel a signé la "\n            "Lei Áurea (loi d\'or), qui a aboli l\'esclavage. Le Brésil a été le dernier "\n            "pays des Amériques à abolir l\'esclavage, et les conséquences de cette "\n            "période, comme le racisme et l\'inégalité, se font encore sentir "\n            "aujourd\'hui. La liberté juridique ne s\'accompagna ni de terres, ni de logement, ni d\'éducation, ni de réparations pour les personnes réduites en esclavage. Beaucoup continuèrent à travailler dans des conditions précaires, tandis que des lois et des pratiques sociales limitaient leur accès aux opportunités. L\'absence de politiques d\'inclusion contribua à des inégalités qui se transmettent entre générations. Dans le même temps, les communautés noires préservèrent leurs traditions, créèrent des associations et menèrent des mouvements pour leurs droits. Comprendre l\'abolition, c\'est se souvenir de leur action et constater que la lutte pour l\'égalité continue aujourd\'hui.'
        ),
                "quiz": [
            {
                "pergunta_pt": 'Em que ano a escravidão foi abolida no Brasil?',
                "pergunta_fr": 'En quelle année l’esclavage a-t-il été aboli au Brésil ?',
                "opcoes_pt": ['1822.', '1930.', '1888.'],
                "opcoes_fr": ['1822.', '1930.', '1888.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'O que faltou após a liberdade legal?',
                "pergunta_fr": 'Qu’est-ce qui a manqué après la liberté juridique ?',
                "opcoes_pt": ['O fim da cultura negra.', 'Acesso à terra, moradia, educação e reparação.', 'Novas leis de escravidão.'],
                "opcoes_fr": ['La fin de la culture noire.', 'L’accès à la terre, au logement, à l’éducation et aux réparations.', 'De nouvelles lois esclavagistes.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'O que comunidades negras fizeram após a abolição?',
                "pergunta_fr": 'Qu’ont fait les communautés noires après l’abolition ?',
                "opcoes_pt": ['Preservaram tradições e lutaram por direitos.', 'Deixaram de participar da sociedade.', 'Abandonaram suas associações.'],
                "opcoes_fr": ['Elles ont préservé leurs traditions et lutté pour leurs droits.', 'Elles ont cessé de participer à la société.', 'Elles ont abandonné leurs associations.'],
                "resposta": 0,
            },
        ],
"vocabulario": [
            {"pt": "escravidão", "fr": "esclavage"},
            {"pt": "tráfico", "fr": "traite"},
            {"pt": "abolir", "fr": "abolir"},
            {"pt": "lei", "fr": "loi"},
        ],
    },
    {
        "slug": "proclamacao-da-republica",
        "categoria": "historia",
        "nivel": "intermediario",
        "emoji": "🏛️",
        "titulo_pt": "A Proclamação da República",
        "titulo_fr": "La proclamation de la République",
        "texto_pt": (
            'A República do Brasil foi proclamada em 15 de novembro de 1889, pondo fim "\n            "ao Império. O marechal Deodoro da Fonseca liderou um movimento militar "\n            "que depôs o imperador Dom Pedro II, que governava o país havia quase "\n            "cinquenta anos. A família imperial foi obrigada a partir para o exílio na "\n            "Europa. Com a proclamação, o Brasil adotou o sistema republicano "\n            "presidencialista, e Deodoro da Fonseca tornou-se o primeiro presidente. A "\n            "mudança foi influenciada pelo desgaste da monarquia, pelo apoio de "\n            "fazendeiros e de parte do Exército, e pelas ideias republicanas que "\n            "circulavam desde o século XIX. O dia 15 de novembro é feriado nacional. A "\n            "Proclamação da República marcou o início de uma nova fase política, que "\n            "transformou profundamente a organização do país. A mudança de regime foi conduzida por militares e apoiada por grupos de proprietários e políticos, mas a população em geral teve pouca participação. O marechal Deodoro da Fonseca tornou-se o primeiro presidente, inicialmente em um governo provisório. A república trouxe novas instituições e uma constituição, mas o direito ao voto continuou restrito e as mulheres não podiam votar. Nas décadas seguintes, disputas entre elites regionais influenciaram a política nacional. A proclamação encerrou a monarquia, mas não resolveu de imediato os debates sobre cidadania e representação.'      ),
        "texto_fr": (
            'La République du Brésil a été proclamée le 15 novembre 1889, mettant fin "\n            "à l\'Empire. Le maréchal Deodoro da Fonseca a dirigé un mouvement "\n            "militaire qui a déposé l\'empereur Dom Pedro II, qui gouvernait le pays "\n            "depuis près de cinquante ans. La famille impériale a été obligée de "\n            "partir en exil en Europe. Avec la proclamation, le Brésil a adopté le "\n            "système républicain présidentiel, et Deodoro da Fonseca est devenu le "\n            "premier président. Ce changement a été influencé par l\'usure de la "\n            "monarchie, par le soutien des grands propriétaires terriens et d\'une "\n            "partie de l\'armée, et par les idées républicaines qui circulaient depuis "\n            "le XIXe siècle. Le 15 novembre est un jour férié national. La "\n            "proclamation de la République a marqué le début d\'une nouvelle phase "\n            "politique, qui a profondément transformé l\'organisation du pays. Le changement de régime fut mené par des militaires et soutenu par des propriétaires et des responsables politiques, mais la population participa peu. Le maréchal Deodoro da Fonseca devint le premier président, d\'abord à la tête d\'un gouvernement provisoire. La république apporta de nouvelles institutions et une constitution, mais le droit de vote resta limité et les femmes ne pouvaient pas voter. Dans les décennies suivantes, les rivalités entre élites régionales influencèrent la politique nationale. La proclamation mit fin à la monarchie sans résoudre immédiatement les débats sur la citoyenneté et la représentation.'       ),
                "quiz": [
            {
                "pergunta_pt": 'Quando a república foi proclamada?',
                "pergunta_fr": 'Quand la république a-t-elle été proclamée ?',
                "opcoes_pt": ['1960.', '1889.', '1822.'],
                "opcoes_fr": ['1960.', '1889.', '1822.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'Quem foi o primeiro presidente?',
                "pergunta_fr": 'Qui fut le premier président ?',
                "opcoes_pt": ['Deodoro da Fonseca.', 'Dom Pedro II.', 'Juscelino Kubitschek.'],
                "opcoes_fr": ['Deodoro da Fonseca.', 'Dom Pedro II.', 'Juscelino Kubitschek.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'Toda a população podia votar na época?',
                "pergunta_fr": 'Toute la population pouvait-elle voter à l’époque ?',
                "opcoes_pt": ['Sim, sem restrições.', 'Somente crianças votavam.', 'Não, o voto era restrito.'],
                "opcoes_fr": ['Oui, sans restriction.', 'Seuls les enfants votaient.', 'Non, le droit de vote était limité.'],
                "resposta": 2,
            },
        ],
"vocabulario": [
            {"pt": "proclamar", "fr": "proclamer"},
            {"pt": "depor", "fr": "déposer"},
            {"pt": "monarquia", "fr": "monarchie"},
            {"pt": "república", "fr": "république"},
        ],
    },
    {
        "slug": "construcao-de-brasilia",
        "categoria": "historia",
        "nivel": "intermediario",
        "emoji": "✈️",
        "titulo_pt": "A Construção de Brasília",
        "titulo_fr": "La construction de Brasília",
        "texto_pt": (
            'Brasília é a capital do Brasil desde 21 de abril de 1960. A cidade foi "\n            "construída em tempo recorde, em cerca de três anos e meio, durante o "\n            "governo do presidente Juscelino Kubitschek, que prometera \'cinquenta anos "\n            "de progresso em cinco\'. O plano urbanístico foi criado por Lúcio Costa e "\n            "os edifícios foram projetados pelo arquiteto Oscar Niemeyer. Brasília foi "\n            "erguida no Planalto Central, no interior do país, com o objetivo de "\n            "desenvolver a região e transferir a capital do Rio de Janeiro. Vista de "\n            "cima, a cidade lembra o formato de um avião, com o \'Plano Piloto\' "\n            "dividido em áreas para morar, trabalhar e circular. Monumentos como o "\n            "Congresso Nacional, a Catedral e o Palácio da Alvorada são marcos da "\n            "arquitetura moderna. Em 1987, Brasília foi declarada Patrimônio Cultural "\n            "da Humanidade pela UNESCO, sendo a única cidade moderna do mundo com esse "\n            "título. A construção começou em 1956 e mobilizou milhares de trabalhadores, muitos deles vindos do Nordeste e chamados de candangos. Eles ergueram edifícios e estradas em um ritmo acelerado, em condições difíceis e longe de suas famílias. O plano urbano foi desenhado por Lúcio Costa, e Oscar Niemeyer projetou edifícios públicos de formas curvas e marcantes. Inaugurada em 21 de abril de 1960, Brasília passou a abrigar os poderes do governo federal. Seu desenho é famoso, mas a vida na cidade também depende das regiões administrativas que cresceram ao redor do centro planejado.'        ),
        "texto_fr": (
            'Brasília est la capitale du Brésil depuis le 21 avril 1960. La ville a "\n            "été construite en un temps record, en environ trois ans et demi, pendant "\n            "le gouvernement du président Juscelino Kubitschek, qui avait promis "\n            "« cinquante ans de progrès en cinq ans ». Le plan urbain a été créé par "\n            "Lúcio Costa et les bâtiments ont été conçus par l\'architecte Oscar "\n            "Niemeyer. Brasília a été érigée sur le plateau central, à l\'intérieur du "\n            "pays, dans le but de développer la région et de transférer la capitale "\n            "depuis Rio de Janeiro. Vue d\'en haut, la ville ressemble à la forme d\'un "\n            "avion, avec le « Plan pilote » divisé en zones pour habiter, travailler "\n            "et circuler. Des monuments comme le Congrès national, la cathédrale et le "\n            "palais de l\'Alvorada sont des repères de l\'architecture moderne. En 1987, "\n            "Brasília a été déclarée patrimoine culturel de l\'humanité par l\'UNESCO, "\n            "étant la seule ville moderne du monde à porter ce titre. La construction commença en 1956 et mobilisa des milliers de travailleurs, dont beaucoup venaient du Nordeste et étaient appelés candangos. Ils bâtirent les édifices et les routes à un rythme rapide, dans des conditions difficiles et loin de leurs familles. Le plan urbain fut conçu par Lúcio Costa, et Oscar Niemeyer dessina des bâtiments publics aux formes courbes et remarquables. Inaugurée le 21 avril 1960, Brasília accueillit les pouvoirs du gouvernement fédéral. Son architecture est célèbre, mais la vie de la ville dépend aussi des quartiers administratifs qui se sont développés autour du centre planifié.'       ),
                "quiz": [
            {
                "pergunta_pt": 'Quem eram os candangos?',
                "pergunta_fr": 'Qui étaient les candangos ?',
                "opcoes_pt": ['Trabalhadores que construíram Brasília.', 'Arquitetos franceses.', 'Pilotos que inauguraram o aeroporto.'],
                "opcoes_fr": ['Les travailleurs qui construisirent Brasília.', 'Des architectes français.', 'Les pilotes qui inaugurèrent l’aéroport.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'Quem projetou os edifícios públicos famosos?',
                "pergunta_fr": 'Qui a conçu les célèbres bâtiments publics ?',
                "opcoes_pt": ['Charles Miller.', 'Tom Jobim.', 'Oscar Niemeyer.'],
                "opcoes_fr": ['Charles Miller.', 'Tom Jobim.', 'Oscar Niemeyer.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'Em que ano Brasília foi inaugurada?',
                "pergunta_fr": 'En quelle année Brasília a-t-elle été inaugurée ?',
                "opcoes_pt": ['1950.', '1960.', '1889.'],
                "opcoes_fr": ['1950.', '1960.', '1889.'],
                "resposta": 1,
            },
        ],
"vocabulario": [
            {"pt": "capital", "fr": "capitale"},
            {"pt": "construir", "fr": "construire"},
            {"pt": "arquitetura", "fr": "architecture"},
            {"pt": "interior", "fr": "intérieur"},
        ],
    },
    {
        "slug": "rio-de-janeiro",
        "categoria": "geografia",
        "nivel": "iniciante",
        "emoji": "🏖️",
        "titulo_pt": "O Rio de Janeiro",
        "titulo_fr": "Rio de Janeiro",
        "texto_pt": (
            'O Rio de Janeiro é uma das cidades mais famosas e bonitas do mundo. Foi a "\n            "capital do Brasil de 1763 até 1960. A cidade é conhecida por suas praias, "\n            "como Copacabana e Ipanema, e por monumentos como o Pão de Açúcar e o "\n            "Cristo Redentor, uma estátua de 38 metros no alto do Corcovado que foi "\n            "eleita uma das Sete Maravilhas do Mundo Moderno. O Rio também é a terra "\n            "do samba e do Carnaval mais famoso do planeta, além do estádio do "\n            "Maracanã, um dos maiores do mundo. A paisagem da cidade, com montanhas, "\n            "floresta e mar, é considerada Patrimônio da Humanidade pela UNESCO desde "\n            "2012, na categoria de paisagem cultural urbana. Apesar da beleza, a "\n            "cidade enfrenta desafios como a desigualdade social e a violência, que "\n            "contrastam com a alegria de seu povo, os cariocas. A cidade também tem uma vida cultural intensa, com rodas de samba, blocos de Carnaval, museus e teatros. O porto e o centro guardam marcas de diferentes períodos da história, enquanto bairros como Santa Teresa preservam ruas estreitas e casas antigas. As praias são espaços de encontro e esporte, mas o Rio não se resume às áreas turísticas: milhões de moradores vivem em bairros muito diversos, com desafios de transporte, moradia e acesso a serviços. Conhecer a cidade é olhar tanto para sua beleza natural quanto para a criatividade cotidiana de seus habitantes.'
        ),
        "texto_fr": (
            'Rio de Janeiro est l\'une des villes les plus célèbres et les plus belles "\n            "du monde. Elle a été la capitale du Brésil de 1763 à 1960. La ville est "\n            "connue pour ses plages, comme Copacabana et Ipanema, et pour des "\n            "monuments comme le Pain de Sucre et le Christ Rédempteur, une statue de "\n            "38 mètres au sommet du Corcovado, élue l\'une des sept merveilles du monde "\n            "moderne. Rio est aussi la terre de la samba et du carnaval le plus "\n            "célèbre de la planète, ainsi que du stade Maracanã, l\'un des plus grands "\n            "du monde. Le paysage de la ville, avec ses montagnes, sa forêt et sa mer, "\n            "est classé patrimoine de l\'humanité par l\'UNESCO depuis 2012, dans la "\n            "catégorie du paysage culturel urbain. Malgré sa beauté, la ville fait "\n            "face à des défis comme l\'inégalité sociale et la violence, qui contrastent "\n            "avec la joie de son peuple, les Cariocas. La ville possède aussi une vie culturelle intense, avec des rodas de samba, des groupes de carnaval, des musées et des théâtres. Le port et le centre gardent les traces de différentes périodes historiques, tandis que des quartiers comme Santa Teresa ont conservé leurs rues étroites et leurs vieilles maisons. Les plages sont des lieux de rencontre et de sport, mais Rio ne se résume pas aux sites touristiques : des millions d\'habitants vivent dans des quartiers très différents et rencontrent des difficultés de transport, de logement et d\'accès aux services. Découvrir la ville, c\'est admirer sa nature et la créativité quotidienne de ses habitants.'
        ),
                "quiz": [
            {
                "pergunta_pt": 'Qual é o apelido de quem nasce no Rio?',
                "pergunta_fr": 'Quel est le nom donné aux habitants de Rio ?',
                "opcoes_pt": ['Candango.', 'Paulista.', 'Carioca.'],
                "opcoes_fr": ['Candango.', 'Paulista.', 'Carioca.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'Qual festa marca a cidade?',
                "pergunta_fr": 'Quelle fête marque la ville ?',
                "opcoes_pt": ['A Festa da Uva.', 'O Carnaval.', 'A Oktoberfest.'],
                "opcoes_fr": ['La fête du raisin.', 'Le carnaval.', 'L’Oktoberfest.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'O que significa conhecer o Rio além dos pontos turísticos?',
                "pergunta_fr": 'Que signifie découvrir Rio au-delà des sites touristiques ?',
                "opcoes_pt": ['Conhecer a vida e os desafios dos moradores.', 'Visitar apenas as praias.', 'Evitar a cultura local.'],
                "opcoes_fr": ['Découvrir la vie et les défis des habitants.', 'Ne visiter que les plages.', 'Éviter la culture locale.'],
                "resposta": 0,
            },
        ],
"vocabulario": [
            {"pt": "praia", "fr": "plage"},
            {"pt": "cidade", "fr": "ville"},
            {"pt": "famosa", "fr": "célèbre"},
            {"pt": "monumento", "fr": "monument"},
        ],
    },
    {
        "slug": "sao-paulo",
        "categoria": "geografia",
        "nivel": "iniciante",
        "emoji": "🏙️",
        "titulo_pt": "São Paulo",
        "titulo_fr": "São Paulo",
        "texto_pt": (
            'São Paulo é a maior cidade do Brasil e uma das maiores do mundo, com "\n            "cerca de 12 milhões de habitantes na cidade e mais de 20 milhões na "\n            "região metropolitana. É o principal centro econômico, financeiro e "\n            "cultural do país. A cidade foi fundada em 1554 por padres jesuítas e "\n            "cresceu muito no século XIX e XX, impulsionada pelo café e, depois, pela "\n            "indústria. São Paulo é uma das cidades mais diversas do planeta, com "\n            "grandes comunidades de origem italiana, japonesa, libanesa, portuguesa e "\n            "de muitos outros povos, o que se reflete na gastronomia e na cultura. A "\n            "Avenida Paulista, o Museu de Arte de São Paulo (MASP), o Parque do "\n            "Ibirapuera e o Mercado Municipal são alguns dos pontos mais conhecidos. A "\n            "cidade também é um importante centro de negócios, educação, moda e "\n            "gastronomia da América do Sul. A diversidade também se vê na mesa: restaurantes de muitas regiões do Brasil convivem com cozinhas japonesa, italiana, árabe e boliviana. A cidade abriga museus importantes, como o MASP, além de salas de concerto, centros culturais e grandes feiras de rua. O trânsito intenso e as longas distâncias fazem parte da rotina de muitos moradores, que dependem de metrô, ônibus e trem. Mesmo com seus desafios, São Paulo oferece oportunidades de trabalho e estudo e continua mudando com a chegada de novas comunidades e ideias.'        ),
        "texto_fr": (
            'São Paulo est la plus grande ville du Brésil et l\'une des plus grandes "\n            "du monde, avec environ 12 millions d\'habitants dans la ville et plus de "\n            "20 millions dans la région métropolitaine. C\'est le principal centre "\n            "économique, financier et culturel du pays. La ville a été fondée en 1554 "\n            "par des pères jésuites et elle a beaucoup grandi aux XIXe et XXe siècles, "\n            "portée par le café puis par l\'industrie. São Paulo est l\'une des villes "\n            "les plus diverses de la planète, avec de grandes communautés d\'origine "\n            "italienne, japonaise, libanaise, portugaise et de bien d\'autres peuples, "\n            "ce qui se reflète dans la gastronomie et la culture. L\'avenue Paulista, "\n            "le musée d\'art de São Paulo (MASP), le parc Ibirapuera et le marché "\n            "municipal sont quelques-uns des lieux les plus connus. La ville est aussi "\n            "un important centre d\'affaires, d\'éducation, de mode et de gastronomie "\n            "d\'Amérique du Sud. La diversité se retrouve aussi à table : des restaurants de nombreuses régions du Brésil côtoient des cuisines japonaise, italienne, arabe et bolivienne. La ville abrite des musées importants, comme le MASP, ainsi que des salles de concert, des centres culturels et de grands marchés de rue. La circulation dense et les longues distances font partie du quotidien de nombreux habitants, qui dépendent du métro, des bus et des trains. Malgré ses difficultés, São Paulo offre des possibilités de travail et d\'études et continue d\'évoluer avec l\'arrivée de nouvelles communautés et de nouvelles idées.'        ),
                "quiz": [
            {
                "pergunta_pt": 'Qual é uma característica da população de São Paulo?',
                "pergunta_fr": 'Quelle est une caractéristique de la population de São Paulo ?',
                "opcoes_pt": ['Não recebe migrantes.', 'É muito diversa.', 'É formada por uma única comunidade.'],
                "opcoes_fr": ['Elle n’accueille pas de migrants.', 'Elle est très diverse.', 'Elle ne comprend qu’une seule communauté.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'Qual museu famoso é citado?',
                "pergunta_fr": 'Quel musée célèbre est mentionné ?',
                "opcoes_pt": ['MASP.', 'Louvre.', 'Prado.'],
                "opcoes_fr": ['Le MASP.', 'Le Louvre.', 'Le Prado.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'O que marca a rotina de muitos moradores?',
                "pergunta_fr": 'Qu’est-ce qui caractérise le quotidien de nombreux habitants ?',
                "opcoes_pt": ['Ausência de transporte público.', 'Neve durante todo o ano.', 'Longas distâncias e trânsito intenso.'],
                "opcoes_fr": ['L’absence de transports publics.', 'La neige toute l’année.', 'Les longues distances et une circulation dense.'],
                "resposta": 2,
            },
        ],
"vocabulario": [
            {"pt": "habitantes", "fr": "habitants"},
            {"pt": "fundada", "fr": "fondée"},
            {"pt": "café", "fr": "café"},
            {"pt": "diversidade", "fr": "diversité"},
        ],
    },
    {
        "slug": "salvador-e-a-bahia",
        "categoria": "cultura",
        "nivel": "intermediario",
        "emoji": "🥁",
        "titulo_pt": "Salvador e a Bahia",
        "titulo_fr": "Salvador et Bahia",
        "texto_pt": (
            'Salvador foi a primeira capital do Brasil, de 1549 a 1763, e é uma das "\n            "cidades coloniais mais antigas das Américas. Localizada na Bahia, no "\n            "Nordeste, a cidade é o coração da cultura afro-brasileira, presente na "\n            "música, na dança, na religião e na culinária. O Pelourinho, seu centro "\n            "histórico de casarões coloridos, foi declarado Patrimônio da Humanidade "\n            "pela UNESCO. A Bahia é o berço do axé, do samba de roda, da capoeira e do "\n            "candomblé, religião de origem africana. A culinária baiana é famosa por "\n            "pratos como o acarajé e a moqueca, feitos com azeite de dendê e leite de "\n            "coco. O Carnaval de Salvador, com seus trios elétricos e blocos como o "\n            "Olodum, é um dos maiores do mundo. A força da cultura negra faz da Bahia "\n            "um lugar único, fundamental para entender a identidade do Brasil. O centro histórico conserva igrejas, largos e casarões que contam diferentes capítulos da cidade, inclusive a riqueza produzida pelo trabalho escravizado. A presença africana está nas religiões, na música, na culinária e nas festas, mas também em movimentos e comunidades que mantêm vivas essas tradições. Salvador é uma cidade costeira, com praias e uma longa baía, e sua paisagem muda entre a Cidade Alta e a Cidade Baixa. Conhecer a Bahia pede tempo para ouvir histórias locais e compreender a força de sua herança afro-brasileira.'        ),
        "texto_fr": (
            'Salvador a été la première capitale du Brésil, de 1549 à 1763, et c\'est "\n            "l\'une des villes coloniales les plus anciennes des Amériques. Située à "\n            "Bahia, dans le Nordeste, la ville est le cœur de la culture "\n            "afro-brésilienne, présente dans la musique, la danse, la religion et la "\n            "cuisine. Le Pelourinho, son centre historique aux maisons colorées, a été "\n            "déclaré patrimoine de l\'humanité par l\'UNESCO. Bahia est le berceau de "\n            "l\'axé, de la samba de roda, de la capoeira et du candomblé, une religion "\n            "d\'origine africaine. La cuisine bahianaise est célèbre pour des plats "\n            "comme l\'acarajé et la moqueca, préparés avec de l\'huile de palme (dendê) "\n            "et du lait de coco. Le carnaval de Salvador, avec ses « trios elétricos » "\n            "et ses blocos comme l\'Olodum, est l\'un des plus grands du monde. La force "\n            "de la culture noire fait de Bahia un lieu unique, essentiel pour "\n            "comprendre l\'identité du Brésil. Le centre historique conserve des églises, des places et des maisons anciennes qui racontent plusieurs chapitres de la ville, notamment les richesses produites par le travail des personnes réduites en esclavage. La présence africaine se retrouve dans les religions, la musique, la cuisine et les fêtes, mais aussi dans les mouvements et les communautés qui font vivre ces traditions. Salvador est une ville côtière, bordée de plages et d\'une vaste baie, dont le paysage change entre la ville haute et la ville basse. Découvrir Bahia demande de prendre le temps d\'écouter les récits locaux et de comprendre la force de son héritage afro-brésilien.'       ),
                "quiz": [
            {
                "pergunta_pt": 'Qual cidade é descrita como centro histórico e cultural?',
                "pergunta_fr": 'Quelle ville est décrite comme un centre historique et culturel ?',
                "opcoes_pt": ['Salvador.', 'Brasília.', 'Manaus.'],
                "opcoes_fr": ['Salvador.', 'Brasília.', 'Manaus.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'Que ingrediente é comum na culinária baiana?',
                "pergunta_fr": 'Quel ingrédient est courant dans la cuisine bahianaise ?',
                "opcoes_pt": ['Xarope de bordo.', 'Creme de leite.', 'Azeite de dendê.'],
                "opcoes_fr": ['Le sirop d’érable.', 'La crème fraîche.', 'L’huile de dendê.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'Que herança é essencial para compreender a Bahia?',
                "pergunta_fr": 'Quel héritage est essentiel pour comprendre Bahia ?',
                "opcoes_pt": ['Andina.', 'Afro-brasileira.', 'Nórdica.'],
                "opcoes_fr": ['Andine.', 'Afro-brésilienne.', 'Nordique.'],
                "resposta": 1,
            },
        ],
"vocabulario": [
            {"pt": "herança", "fr": "héritage"},
            {"pt": "berço", "fr": "berceau"},
            {"pt": "culinária", "fr": "cuisine"},
            {"pt": "comida", "fr": "plat"},
        ],
    },
    {
        "slug": "carnaval",
        "categoria": "cultura",
        "nivel": "intermediario",
        "emoji": "🎭",
        "titulo_pt": "O Carnaval",
        "titulo_fr": "Le carnaval",
        "texto_pt": (
            'O Carnaval é a maior festa popular do Brasil e uma das maiores do mundo. "\n            "Ele acontece todos os anos, nos dias que antecedem a Quaresma, quarenta "\n            "dias antes da Páscoa. As origens da festa misturam tradições europeias, "\n            "como o entrudo, com influências africanas e indígenas, criando uma "\n            "celebração única. Cada região do Brasil tem seu próprio Carnaval. No Rio "\n            "de Janeiro, as escolas de samba desfilam no Sambódromo com carros "\n            "alegóricos, fantasias e baterias, em uma competição grandiosa. Em "\n            "Salvador, a festa acontece nas ruas, com trios elétricos que arrastam "\n            "multidões. Em Recife e Olinda, o destaque é o frevo e o maracatu, com os "\n            "famosos bonecos gigantes. Milhões de brasileiros e turistas participam da "\n            "festa, que movimenta a economia e expressa a alegria e a criatividade do "\n            "povo brasileiro. A preparação começa meses antes: compositores criam sambas-enredo, costureiras produzem fantasias e comunidades constroem carros alegóricos. Nas escolas de samba do Rio, cada desfile conta uma história escolhida pela agremiação e envolve milhares de participantes. Em outras cidades, moradores organizam blocos de rua e ensaiam músicas que todos podem cantar. A festa é também trabalho para músicos, técnicos, vendedores e trabalhadores do turismo. Para muita gente, o Carnaval combina celebração e pertencimento; para outras, é uma oportunidade de mostrar tradições que nem sempre recebem espaço durante o resto do ano.'
        ),
        "texto_fr": (
            'Le carnaval est la plus grande fête populaire du Brésil et l\'une des "\n            "plus grandes du monde. Il a lieu chaque année, dans les jours qui "\n            "précèdent le Carême, quarante jours avant Pâques. Les origines de la fête "\n            "mélangent des traditions européennes, comme l\'« entrudo », avec des "\n            "influences africaines et indigènes, créant une célébration unique. Chaque "\n            "région du Brésil a son propre carnaval. À Rio de Janeiro, les écoles de "\n            "samba défilent au Sambodrome avec des chars allégoriques, des costumes et "\n            "des batteries, dans une compétition grandiose. À Salvador, la fête se "\n            "déroule dans les rues, avec des « trios elétricos » qui entraînent des "\n            "foules. À Recife et à Olinda, le frevo et le maracatu sont à l\'honneur, "\n            "avec les célèbres bonshommes géants. Des millions de Brésiliens et de "\n            "touristes participent à la fête, qui fait tourner l\'économie et exprime "\n            "la joie et la créativité du peuple brésilien. La préparation commence des mois à l\'avance : les compositeurs écrivent les sambas-enredo, les couturières confectionnent les costumes et les communautés construisent les chars. À Rio, chaque école de samba raconte dans son défilé une histoire qu\'elle a choisie, avec des milliers de participants. Dans d\'autres villes, les habitants organisent des groupes de rue et répètent des chansons que tout le monde peut reprendre. La fête représente aussi du travail pour les musiciens, les techniciens, les vendeurs et les professionnels du tourisme. Pour beaucoup, le carnaval allie célébration et sentiment d\'appartenance ; pour d\'autres, il permet de mettre en lumière des traditions rarement visibles le reste de l\'année.'      ),
                "quiz": [
            {
                "pergunta_pt": 'Quando acontece o Carnaval?',
                "pergunta_fr": 'Quand a lieu le carnaval ?',
                "opcoes_pt": ['No meio do inverno europeu.', 'Somente em dezembro.', 'Nos dias antes da Quaresma.'],
                "opcoes_fr": ['Au milieu de l’hiver européen.', 'Uniquement en décembre.', 'Dans les jours précédant le Carême.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'O que as escolas de samba fazem no Rio?',
                "pergunta_fr": 'Que font les écoles de samba à Rio ?',
                "opcoes_pt": ['Fazem peças de teatro silenciosas.', 'Desfilam com enredos, fantasias e carros.', 'Organizam corridas de barco.'],
                "opcoes_fr": ['Elles montent des pièces de théâtre muettes.', 'Elles défilent avec des thèmes, des costumes et des chars.', 'Elles organisent des courses de bateaux.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'O que costuma acontecer antes da festa?',
                "pergunta_fr": 'Que se passe-t-il avant la fête ?',
                "opcoes_pt": ['Meses de preparação comunitária.', 'A cidade é fechada ao público.', 'As músicas são escolhidas no mesmo dia.'],
                "opcoes_fr": ['Des mois de préparation communautaire.', 'La ville est fermée au public.', 'Les chansons sont choisies le jour même.'],
                "resposta": 0,
            },
        ],
"vocabulario": [
            {"pt": "festa", "fr": "fête"},
            {"pt": "desfilar", "fr": "défiler"},
            {"pt": "rua", "fr": "rue"},
            {"pt": "turista", "fr": "touriste"},
        ],
    },
    {
        "slug": "futebol-no-brasil",
        "categoria": "cultura",
        "nivel": "iniciante",
        "emoji": "⚽",
        "titulo_pt": "O Futebol no Brasil",
        "titulo_fr": "Le football au Brésil",
        "texto_pt": (
            'O futebol é o esporte mais popular do Brasil e uma verdadeira paixão "\n            "nacional. O país é o maior campeão da Copa do Mundo, com cinco títulos "\n            "conquistados em 1958, 1962, 1970, 1994 e 2002. Pelé, considerado por "\n            "muitos o maior jogador da história, ajudou o Brasil a vencer três dessas "\n            "Copas e se tornou um ídolo mundial. O futebol chegou ao Brasil no final "\n            "do século XIX, trazido por Charles Miller, filho de brasileira e inglês. "\n            "Desde então, o esporte se espalhou por todo o país e virou parte da "\n            "cultura. O Brasil revelou craques como Garrincha, Zico, Romário, Ronaldo, "\n            "Ronaldinho, Neymar e Marta, considerada a rainha do futebol feminino. "\n            "Estádios como o Maracanã são verdadeiros templos. Para muitos "\n            "brasileiros, o futebol é mais que um esporte: é uma forma de expressão, "\n            "de alegria e de identidade. Em muitos bairros, basta uma bola e um espaço livre para começar uma partida. Crianças jogam em quadras, campos de terra e praias, aprendendo não só regras, mas também cooperação e improviso. Os campeonatos estaduais e nacionais atraem torcedores durante todo o ano, e os dias de jogo mudam o ritmo de algumas cidades. O futebol feminino também ganhou mais visibilidade, graças ao talento de atletas como Marta e ao trabalho de clubes e projetos de base. A paixão pelo esporte é grande, mas o acesso a treinamento e oportunidades ainda não é igual para todos.'
        ),
        "texto_fr": (
            'Le football est le sport le plus populaire du Brésil et une véritable "\n            "passion nationale. Le pays est le plus grand champion de la Coupe du "\n            "monde, avec cinq titres remportés en 1958, 1962, 1970, 1994 et 2002. "\n            "Pelé, considéré par beaucoup comme le plus grand joueur de l\'histoire, a "\n            "aidé le Brésil à gagner trois de ces Coupes et il est devenu une idole "\n            "mondiale. Le football est arrivé au Brésil à la fin du XIXe siècle, "\n            "apporté par Charles Miller, fils d\'une Brésilienne et d\'un Anglais. "\n            "Depuis, le sport s\'est répandu dans tout le pays et il fait partie de la "\n            "culture. Le Brésil a révélé des stars comme Garrincha, Zico, Romário, "\n            "Ronaldo, Ronaldinho, Neymar et Marta, considérée comme la reine du "\n            "football féminin. Des stades comme le Maracanã sont de véritables "\n            "temples. Pour beaucoup de Brésiliens, le football est plus qu\'un sport : "\n            "c\'est une forme d\'expression, de joie et d\'identité. Dans beaucoup de quartiers, un ballon et un espace libre suffisent pour commencer une partie. Les enfants jouent dans des gymnases, sur des terrains en terre ou sur la plage, en apprenant les règles, mais aussi la coopération et l\'improvisation. Les championnats régionaux et nationaux attirent des supporters toute l\'année, et les jours de match changent le rythme de certaines villes. Le football féminin est devenu plus visible grâce au talent d\'athlètes comme Marta et au travail des clubs et des centres de formation. La passion pour ce sport est forte, mais l\'accès aux entraînements et aux opportunités reste inégal.'        ),
                "quiz": [
            {
                "pergunta_pt": 'Quantas Copas do Mundo masculinas o Brasil venceu, segundo o texto?',
                "pergunta_fr": 'Combien de Coupes du monde masculines le Brésil a-t-il remportées selon le texte ?',
                "opcoes_pt": ['Duas.', 'Dez.', 'Cinco.'],
                "opcoes_fr": ['Deux.', 'Dix.', 'Cinq.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'Quem é citada como rainha do futebol feminino?',
                "pergunta_fr": 'Qui est citée comme reine du football féminin ?',
                "opcoes_pt": ['Zico.', 'Marta.', 'Pelé.'],
                "opcoes_fr": ['Zico.', 'Marta.', 'Pelé.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'O que pode iniciar uma partida em muitos bairros?',
                "pergunta_fr": 'Que faut-il pour commencer une partie dans beaucoup de quartiers ?',
                "opcoes_pt": ['Uma bola e um espaço livre.', 'Um estádio profissional.', 'Um uniforme oficial.'],
                "opcoes_fr": ['Un ballon et un espace libre.', 'Un stade professionnel.', 'Un uniforme officiel.'],
                "resposta": 0,
            },
        ],
"vocabulario": [
            {"pt": "esporte", "fr": "sport"},
            {"pt": "campeão", "fr": "champion"},
            {"pt": "jogador", "fr": "joueur"},
            {"pt": "título", "fr": "titre"},
        ],
    },
    {
        "slug": "capoeira",
        "categoria": "cultura",
        "nivel": "intermediario",
        "emoji": "🤸",
        "titulo_pt": "A Capoeira",
        "titulo_fr": "La capoeira",
        "texto_pt": (
            'A capoeira é uma manifestação cultural brasileira que mistura luta, "\n            "dança, música, acrobacia e jogo. Ela foi criada pelos africanos "\n            "escravizados e seus descendentes como forma de resistência e de "\n            "preservação da cultura. Por muito tempo, a capoeira foi perseguida e até "\n            "proibida por lei, sendo considerada crime no início do século XX. A roda "\n            "de capoeira é o círculo onde dois capoeiristas \'jogam\' ao som de "\n            "instrumentos como o berimbau, o atabaque e o pandeiro, acompanhados por "\n            "palmas e cantigas. Os movimentos são ágeis e acrobáticos, como a ginga, "\n            "os chutes e os floreios. Em 2014, a roda de capoeira foi declarada "\n            "Patrimônio Cultural Imaterial da Humanidade pela UNESCO. Hoje, a capoeira "\n            "é praticada no mundo inteiro e é um símbolo da cultura e da resistência "\n            "do povo brasileiro. A música orienta o jogo e ajuda a manter a memória da capoeira. O berimbau marca o ritmo e pode indicar se os movimentos serão lentos ou rápidos; as cantigas narram histórias, ensinam valores e convidam quem está na roda a responder em coro. Cada grupo tem seus mestres e modos de ensinar, transmitidos pela convivência e pela prática. Hoje há rodas em muitos países, mas o contexto brasileiro de escravidão, perseguição e resistência continua essencial para entender essa arte. Capoeira é exercício físico, mas também uma forma de aprender história e criar comunidade.'
        ),
        "texto_fr": (
            'La capoeira est une manifestation culturelle brésilienne qui mélange "\n            "combat, danse, musique, acrobaties et jeu. Elle a été créée par les "\n            "Africains réduits en esclavage et leurs descendants comme forme de "\n            "résistance et de préservation de la culture. Pendant longtemps, la "\n            "capoeira a été persécutée et même interdite par la loi, étant considérée "\n            "comme un crime au début du XXe siècle. La « roda de capoeira » est le "\n            "cercle où deux capoeiristes « jouent » au son d\'instruments comme le "\n            "berimbau, l\'atabaque et le pandeiro, accompagnés de claquements de mains "\n            "et de chants. Les mouvements sont agiles et acrobatiques, comme la ginga, "\n            "les coups de pied et les « floreios ». En 2014, la roda de capoeira a été "\n            "déclarée patrimoine culturel immatériel de l\'humanité par l\'UNESCO. "\n            "Aujourd\'hui, la capoeira est pratiquée dans le monde entier et elle est "\n            "un symbole de la culture et de la résistance du peuple brésilien. La musique guide le jeu et contribue à préserver la mémoire de la capoeira. Le berimbau marque le rythme et peut annoncer des mouvements lents ou rapides ; les chants racontent des histoires, transmettent des valeurs et invitent les participants à répondre en chœur. Chaque groupe a ses maîtres et ses façons d\'enseigner, transmises par la rencontre et la pratique. Il existe aujourd\'hui des rodas dans de nombreux pays, mais le contexte brésilien de l\'esclavage, de la persécution et de la résistance reste essentiel pour comprendre cet art. La capoeira est une activité physique, mais aussi une manière d\'apprendre l\'histoire et de créer une communauté.'       ),
                "quiz": [
            {
                "pergunta_pt": 'Que elementos a capoeira mistura?',
                "pergunta_fr": 'Quels éléments la capoeira mêle-t-elle ?',
                "opcoes_pt": ['Luta, dança e música.', 'Natação e esqui.', 'Teatro e culinária.'],
                "opcoes_fr": ['Combat, danse et musique.', 'Natation et ski.', 'Théâtre et cuisine.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'Qual instrumento marca o ritmo?',
                "pergunta_fr": 'Quel instrument marque le rythme ?',
                "opcoes_pt": ['Violoncelo.', 'Gaita de foles.', 'Berimbau.'],
                "opcoes_fr": ['Le violoncelle.', 'La cornemuse.', 'Le berimbau.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'O que as cantigas podem transmitir?',
                "pergunta_fr": 'Que peuvent transmettre les chants ?',
                "opcoes_pt": ['Regras de trânsito.', 'Histórias e valores.', 'Previsões meteorológicas.'],
                "opcoes_fr": ['Des règles de circulation.', 'Des histoires et des valeurs.', 'Des prévisions météo.'],
                "resposta": 1,
            },
        ],
"vocabulario": [
            {"pt": "luta", "fr": "combat"},
            {"pt": "dança", "fr": "danse"},
            {"pt": "resistência", "fr": "résistance"},
            {"pt": "círculo", "fr": "cercle"},
        ],
    },
    {
        "slug": "feijoada",
        "categoria": "cultura",
        "nivel": "intermediario",
        "emoji": "🍲",
        "titulo_pt": "A Feijoada",
        "titulo_fr": "La feijoada",
        "texto_pt": (
            'A feijoada é considerada o prato nacional do Brasil. É um cozido feito "\n            "com feijão-preto e diversas partes do porco, como linguiça, costela, "\n            "orelha e pé, servido tradicionalmente com arroz branco, couve refogada, "\n            "farofa de mandioca, laranja fatiada e torresmo. É um prato completo e "\n            "muito apreciado em todo o país. Existem várias histórias sobre a origem "\n            "da feijoada. Uma das mais conhecidas diz que ela foi criada pelos "\n            "africanos escravizados, que aproveitavam as partes do porco rejeitadas "\n            "pelos senhores, misturando-as ao feijão. Outros pesquisadores apontam "\n            "influências de cozidos europeus, como a cassoulet francesa. Seja qual for "\n            "a origem, a feijoada se tornou um símbolo da culinária brasileira e é "\n            "servida tradicionalmente às quartas-feiras e aos sábados em muitos "\n            "restaurantes, reunindo famílias e amigos à mesa. O preparo costuma levar várias horas, porque os ingredientes precisam cozinhar lentamente para que os sabores se misturem. Em muitas casas, cada família tem seu jeito de temperar e escolher os acompanhamentos. A laranja ajuda a equilibrar a refeição, e a farofa acrescenta textura. Embora seja associada a encontros de fim de semana, hoje existem versões vegetarianas e receitas diferentes em várias regiões. A história do prato é complexa: não há uma única origem comprovada, e pesquisadores lembram as influências africanas, portuguesas e indígenas presentes na cozinha brasileira. Mais do que uma receita, a feijoada virou ocasião de convivência.'       ),
        "texto_fr": (
            'La feijoada est considérée comme le plat national du Brésil. C\'est un "\n            "ragoût préparé avec des haricots noirs et diverses parties du porc, comme "\n            "la saucisse, les côtes, l\'oreille et le pied, servi traditionnellement "\n            "avec du riz blanc, du chou vert sauté (couve), de la farofa de manioc, "\n            "des tranches d\'orange et du torresmo (couenne frite). C\'est un plat "\n            "complet et très apprécié dans tout le pays. Il existe plusieurs histoires "\n            "sur l\'origine de la feijoada. L\'une des plus connues dit qu\'elle a été "\n            "créée par les Africains réduits en esclavage, qui utilisaient les parties "\n            "du porc rejetées par les maîtres en les mélangeant aux haricots. D\'autres "\n            "chercheurs soulignent des influences de ragoûts européens, comme la "\n            "cassoulet française. Quelle que soit son origine, la feijoada est devenue "\n            "un symbole de la cuisine brésilienne et elle est traditionnellement "\n            "servie le mercredi et le samedi dans de nombreux restaurants, réunissant "\n            "familles et amis autour de la table. La préparation prend souvent plusieurs heures, car les ingrédients doivent mijoter lentement pour que les saveurs se mêlent. Dans beaucoup de familles, chacun a sa façon d\'assaisonner le plat et de choisir les accompagnements. L\'orange équilibre le repas et la farofa ajoute du croquant. Associée aux repas du week-end, la feijoada existe aujourd\'hui aussi en versions végétariennes et sous différentes formes régionales. L\'histoire du plat est complexe : aucune origine unique n\'est prouvée, et les chercheurs rappellent les influences africaines, portugaises et indigènes présentes dans la cuisine brésilienne. Plus qu\'une recette, la feijoada est devenue une occasion de se retrouver.'
        ),
                "quiz": [
            {
                "pergunta_pt": 'Qual feijão é tradicional na feijoada?',
                "pergunta_fr": 'Quel haricot est traditionnel dans la feijoada ?',
                "opcoes_pt": ['Grão-de-bico.', 'Feijão-verde.', 'Feijão-preto.'],
                "opcoes_fr": ['Le pois chiche.', 'Le haricot vert.', 'Le haricot noir.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'Qual acompanhamento ajuda a equilibrar a refeição?',
                "pergunta_fr": 'Quel accompagnement aide à équilibrer le repas ?',
                "opcoes_pt": ['Pão doce.', 'Laranja.', 'Chocolate.'],
                "opcoes_fr": ['La brioche.', 'L’orange.', 'Le chocolat.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'O que se sabe sobre a origem da feijoada?',
                "pergunta_fr": 'Que sait-on de l’origine de la feijoada ?',
                "opcoes_pt": ['Há diferentes influências e não uma origem única comprovada.', 'Foi criada num único restaurante em 2001.', 'É uma receita exclusivamente francesa.'],
                "opcoes_fr": ['Elle a plusieurs influences et aucune origine unique prouvée.', 'Elle fut créée dans un seul restaurant en 2001.', 'C’est une recette exclusivement française.'],
                "resposta": 0,
            },
        ],
"vocabulario": [
            {"pt": "prato", "fr": "plat"},
            {"pt": "feijão", "fr": "haricot"},
            {"pt": "carne", "fr": "viande"},
            {"pt": "origem", "fr": "origine"},
        ],
    },
    {
        "slug": "samba-e-bossa-nova",
        "categoria": "cultura",
        "nivel": "avancado",
        "emoji": "🎶",
        "titulo_pt": "O Samba e a Bossa Nova",
        "titulo_fr": "La samba et la bossa nova",
        "texto_pt": (
            'O samba é um dos ritmos mais importantes e representativos do Brasil. Ele "\n            "nasceu no Rio de Janeiro, no início do século XX, a partir de influências "\n            "africanas trazidas pelos descendentes de escravizados. O samba de roda da "\n            "Bahia é reconhecido pela UNESCO como patrimônio imaterial. No Rio, o "\n            "samba se tornou a alma do Carnaval e deu origem às escolas de samba. Nos "\n            "anos 1950, surgiu a bossa nova, um estilo mais suave e sofisticado, "\n            "criado por artistas como Tom Jobim, Vinícius de Moraes e João Gilberto. A "\n            "bossa nova misturava o samba com o jazz e ganhou o mundo. A canção "\n            "\'Garota de Ipanema\', de 1962, é uma das músicas mais gravadas da história "\n            "e fez a bossa nova famosa internacionalmente. Tanto o samba quanto a "\n            "bossa nova são patrimônios da música brasileira e levaram a cultura do "\n            "país para todos os continentes. O samba tem muitas formas: há o samba-enredo das escolas, o samba de roda, o partido-alto e rodas informais em que músicos improvisam versos. Esses estilos nasceram em comunidades e espaços de encontro marcados pela presença negra, apesar de terem enfrentado preconceito e tentativas de repressão. A bossa nova, por sua vez, ficou conhecida por harmonias elaboradas, voz suave e violão sincopado. Os dois gêneros não são opostos: compartilham ritmos e histórias, mas expressam experiências diferentes. Até hoje, músicos misturam essas tradições a sons de outras regiões e países.'        ),
        "texto_fr": (
            'La samba est l\'un des rythmes les plus importants et les plus "\n            "représentatifs du Brésil. Elle est née à Rio de Janeiro au début du XXe "\n            "siècle, à partir d\'influences africaines apportées par les descendants "\n            "d\'esclaves. La samba de roda de Bahia est reconnue par l\'UNESCO comme "\n            "patrimoine immatériel. À Rio, la samba est devenue l\'âme du carnaval et a "\n            "donné naissance aux écoles de samba. Dans les années 1950 est née la "\n            "bossa nova, un style plus doux et plus sophistiqué, créé par des artistes "\n            "comme Tom Jobim, Vinícius de Moraes et João Gilberto. La bossa nova "\n            "mélangeait la samba avec le jazz et elle a conquis le monde. La chanson "\n            "« Garota de Ipanema », de 1962, est l\'une des chansons les plus "\n            "enregistrées de l\'histoire et elle a rendu la bossa nova célèbre dans le "\n            "monde entier. La samba comme la bossa nova sont des trésors de la musique "\n            "brésilienne et elles ont porté la culture du pays sur tous les continents. La samba prend de nombreuses formes : samba-enredo des écoles, samba de roda, partido-alto et rodas informelles où les musiciens improvisent des vers. Ces styles sont nés dans des communautés et des lieux de rencontre marqués par la présence noire, malgré les préjugés et les tentatives de répression. La bossa nova, quant à elle, est connue pour ses harmonies élaborées, sa voix douce et sa guitare syncopée. Les deux genres ne s\'opposent pas : ils partagent des rythmes et des histoires, tout en exprimant des expériences différentes. Aujourd\'hui encore, les musiciens mêlent ces traditions aux sons d\'autres régions et d\'autres pays.'       ),
                "quiz": [
            {
                "pergunta_pt": 'Que influência musical a bossa nova incorporou?',
                "pergunta_fr": 'Quelle influence musicale la bossa nova a-t-elle intégrée ?',
                "opcoes_pt": ['Jazz.', 'Reggae.', 'Polca.'],
                "opcoes_fr": ['Le jazz.', 'Le reggae.', 'La polka.'],
                "resposta": 0,
            },
            {
                "pergunta_pt": 'Quem são artistas importantes da bossa nova?',
                "pergunta_fr": 'Quels artistes sont importants pour la bossa nova ?',
                "opcoes_pt": ['Pelé, Marta e Zico.', 'Oscar Niemeyer e Lúcio Costa.', 'Tom Jobim, Vinícius de Moraes e João Gilberto.'],
                "opcoes_fr": ['Pelé, Marta et Zico.', 'Oscar Niemeyer et Lúcio Costa.', 'Tom Jobim, Vinícius de Moraes et João Gilberto.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'O samba possui...',
                "pergunta_fr": 'La samba comprend...',
                "opcoes_pt": ['Apenas músicas instrumentais.', 'Muitas formas e estilos.', 'Um único ritmo imutável.'],
                "opcoes_fr": ['Uniquement de la musique instrumentale.', 'De nombreuses formes et styles.', 'Un seul rythme immuable.'],
                "resposta": 1,
            },
        ],
"vocabulario": [
            {"pt": "ritmo", "fr": "rythme"},
            {"pt": "nascer", "fr": "naître"},
            {"pt": "canção", "fr": "chanson"},
            {"pt": "música", "fr": "musique"},
        ],
    },
    {
        "slug": "lingua-portuguesa-no-brasil",
        "categoria": "cultura",
        "nivel": "avancado",
        "emoji": "🗣️",
        "titulo_pt": "A Língua Portuguesa no Brasil",
        "titulo_fr": "La langue portugaise au Brésil",
        "texto_pt": (
            'O português é a língua oficial do Brasil, falado por mais de 200 milhões "\n            "de pessoas, o que faz do Brasil o maior país lusófono do mundo. A língua "\n            "chegou ao país com os colonizadores portugueses e, ao longo dos séculos, "\n            "se misturou com línguas indígenas, como o tupi, e africanas, criando o "\n            "português brasileiro, com suas particularidades. O português do Brasil "\n            "tem diferenças em relação ao de Portugal na pronúncia, no vocabulário e "\n            "na gramática. Por exemplo, no Brasil dizemos \'ônibus\', \'geladeira\' e "\n            "\'xícara\', enquanto em Portugal se diz \'autocarro\', \'frigorífico\' e "\n            "\'chávena\'. Também há diferenças no tratamento: o brasileiro usa muito o "\n            "\'você\', enquanto o português prefere o \'tu\'. Muitas palavras brasileiras "\n            "vêm do tupi, como \'abacaxi\' e \'mandioca\', e de línguas africanas, como "\n            "\'moleque\' e \'cafuné\'. Essa riqueza faz do português brasileiro uma língua "\n            "cheia de história. O país é tão grande que a pronúncia e algumas expressões mudam bastante de uma região para outra. No Nordeste, no Sul e na região Norte, por exemplo, há ritmos de fala, sotaques e palavras locais que revelam histórias de migração e contato entre comunidades. Mesmo assim, falantes de todo o Brasil conseguem se entender, embora às vezes precisem explicar uma gíria ou escolher outra palavra. A língua continua mudando com a música, a internet e as conversas do dia a dia. Aprender português brasileiro também é ouvir essa diversidade sem procurar um único sotaque correto.'        ),
        "texto_fr": (
            'Le portugais est la langue officielle du Brésil, parlée par plus de 200 "\n            "millions de personnes, ce qui fait du Brésil le plus grand pays lusophone "\n            "du monde. La langue est arrivée dans le pays avec les colonisateurs "\n            "portugais et, au fil des siècles, elle s\'est mélangée à des langues "\n            "indigènes, comme le tupi, et africaines, créant le portugais brésilien, "\n            "avec ses particularités. Le portugais du Brésil présente des différences "\n            "avec celui du Portugal dans la prononciation, le vocabulaire et la "\n            "grammaire. Par exemple, au Brésil on dit « ônibus », « geladeira » et "\n            "« xícara », tandis qu\'au Portugal on dit « autocarro », « frigorífico » "\n            "et « chávena ». Il y a aussi des différences dans le tutoiement : le "\n            "Brésilien utilise beaucoup le « você », alors que le Portugais préfère le "\n            "« tu ». Beaucoup de mots brésiliens viennent du tupi, comme « abacaxi » "\n            "et « mandioca », et de langues africaines, comme « moleque » et "\n            "« cafuné ». Cette richesse fait du portugais brésilien une langue pleine "\n            "d\'histoire. Le pays est si vaste que la prononciation et certaines expressions varient beaucoup d\'une région à l\'autre. Dans le Nordeste, le Sud ou la région Nord, par exemple, les rythmes de parole, les accents et les mots locaux racontent des histoires de migration et de contacts entre communautés. Les habitants de tout le Brésil se comprennent néanmoins, même s\'ils doivent parfois expliquer un mot familier ou en choisir un autre. La langue continue d\'évoluer avec la musique, Internet et les conversations quotidiennes. Apprendre le portugais brésilien, c\'est aussi écouter cette diversité sans chercher un accent unique qui serait le seul correct.'
        ),
                "quiz": [
            {
                "pergunta_pt": 'O que pode variar entre regiões do Brasil?',
                "pergunta_fr": 'Qu’est-ce qui peut varier entre les régions du Brésil ?',
                "opcoes_pt": ['O alfabeto inteiro.', 'A direção da escrita.', 'Pronúncia e expressões.'],
                "opcoes_fr": ['Tout l’alphabet.', 'Le sens de l’écriture.', 'La prononciation et les expressions.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'Por que existem palavras e sotaques diferentes?',
                "pergunta_fr": 'Pourquoi existe-t-il des mots et des accents différents ?',
                "opcoes_pt": ['Por causa de uma única língua antiga.', 'Histórias de migração e contato entre comunidades.', 'Porque as regiões não se comunicam.'],
                "opcoes_fr": ['À cause d’une seule langue ancienne.', 'À cause des migrations et des contacts entre communautés.', 'Parce que les régions ne communiquent pas.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'Como aprender a diversidade do português brasileiro?',
                "pergunta_fr": 'Comment apprendre la diversité du portugais brésilien ?',
                "opcoes_pt": ['Ouvindo diferentes formas de falar.', 'Procurando um único sotaque correto.', 'Evitando conversas.'],
                "opcoes_fr": ['En écoutant différentes façons de parler.', 'En cherchant un seul accent correct.', 'En évitant les conversations.'],
                "resposta": 0,
            },
        ],
"vocabulario": [
            {"pt": "língua", "fr": "langue"},
            {"pt": "falar", "fr": "parler"},
            {"pt": "palavra", "fr": "mot"},
            {"pt": "pronúncia", "fr": "prononciation"},
        ],
    },
    {
        "slug": "cafe-no-brasil",
        "categoria": "historia",
        "nivel": "avancado",
        "emoji": "☕",
        "titulo_pt": "O Café no Brasil",
        "titulo_fr": "Le café au Brésil",
        "texto_pt": (
            'O café chegou ao Brasil no século XVIII, trazido da Guiana Francesa, e "\n            "transformou a economia e a história do país. No século XIX, o café se "\n            "tornou o principal produto de exportação brasileiro. As fazendas se "\n            "concentraram primeiro no Vale do Paraíba, entre Rio e São Paulo, e depois "\n            "no interior paulista, aproveitando o solo avermelhado e fértil conhecido "\n            "como terra roxa. A riqueza do café financiou a construção de ferrovias, o "\n            "crescimento de cidades e a modernização do país, além de atrair milhões "\n            "de imigrantes, principalmente italianos, para trabalhar nas lavouras. O "\n            "ciclo do café também teve um lado sombrio: foi um dos motores da "\n            "escravidão e, depois, causou crises por excesso de produção. Hoje, o "\n            "Brasil é o maior produtor e exportador de café do mundo, responsável por "\n            "cerca de um terço da produção global, e o \'cafezinho\' é um símbolo da "\n            "hospitalidade brasileira. O café também mudou hábitos e cidades. Nas fazendas, o trabalho era organizado em torno da colheita, e as ferrovias levavam os grãos até os portos para exportação. A riqueza acumulada por produtores influenciou decisões políticas e ajudou a financiar a industrialização de São Paulo. Depois da abolição, a chegada de imigrantes alterou as relações de trabalho, embora muitos tenham enfrentado condições difíceis. Hoje, o café é cultivado em diferentes regiões e altitudes, e pequenos produtores investem em qualidade e métodos sustentáveis. O cafezinho oferecido a uma visita continua sendo um gesto cotidiano de acolhimento.'
        ),
        "texto_fr": (
            'Le café est arrivé au Brésil au XVIIIe siècle, apporté de Guyane "\n            "française, et il a transformé l\'économie et l\'histoire du pays. Au XIXe "\n            "siècle, le café est devenu le principal produit d\'exportation brésilien. "\n            "Les plantations se sont d\'abord concentrées dans la vallée du Paraíba, "\n            "entre Rio et São Paulo, puis à l\'intérieur de São Paulo, profitant du sol "\n            "rougeâtre et fertile connu sous le nom de « terra roxa ». La richesse du "\n            "café a financé la construction de chemins de fer, la croissance des "\n            "villes et la modernisation du pays, en plus d\'attirer des millions "\n            "d\'immigrants, surtout des Italiens, pour travailler dans les plantations. "\n            "Le cycle du café a aussi eu un côté sombre : il a été l\'un des moteurs de "\n            "l\'esclavage et, ensuite, il a provoqué des crises dues à la surproduction. "\n            "Aujourd\'hui, le Brésil est le plus grand producteur et exportateur de "\n            "café du monde, responsable d\'environ un tiers de la production mondiale, "\n            "et le « cafezinho » est un symbole de l\'hospitalité brésilienne. Le café transforma aussi les habitudes et les villes. Dans les plantations, le travail s\'organisait autour de la récolte, et les chemins de fer transportaient les grains vers les ports pour l\'exportation. La richesse des producteurs influença les décisions politiques et contribua à financer l\'industrialisation de São Paulo. Après l\'abolition, l\'arrivée d\'immigrants transforma les relations de travail, même si beaucoup connurent des conditions difficiles. Aujourd\'hui, le café est cultivé dans différentes régions et à différentes altitudes, et de petits producteurs investissent dans la qualité et des méthodes durables. Offrir un cafezinho à un visiteur reste un geste quotidien d\'hospitalité.'     ),
                "quiz": [
            {
                "pergunta_pt": 'O que as ferrovias transportavam?',
                "pergunta_fr": 'Que transportaient les chemins de fer ?',
                "opcoes_pt": ['Turistas até as praias.', 'Açúcar para a Amazônia.', 'Grãos de café até os portos.'],
                "opcoes_fr": ['Les touristes jusqu’aux plages.', 'Le sucre vers l’Amazonie.', 'Les grains de café jusqu’aux ports.'],
                "resposta": 2,
            },
            {
                "pergunta_pt": 'Que mudança ocorreu após a abolição?',
                "pergunta_fr": 'Quel changement eut lieu après l’abolition ?',
                "opcoes_pt": ['O café deixou de ser cultivado.', 'Chegaram imigrantes para trabalhar nas lavouras.', 'As fazendas desapareceram de imediato.'],
                "opcoes_fr": ['Le café ne fut plus cultivé.', 'Des immigrants arrivèrent pour travailler dans les plantations.', 'Les plantations disparurent immédiatement.'],
                "resposta": 1,
            },
            {
                "pergunta_pt": 'O que oferecer um cafezinho pode expressar?',
                "pergunta_fr": 'Que peut exprimer le fait d’offrir un cafezinho ?',
                "opcoes_pt": ['Hospitalidade.', 'Despedida formal.', 'Competição esportiva.'],
                "opcoes_fr": ['L’hospitalité.', 'Un adieu formel.', 'Une compétition sportive.'],
                "resposta": 0,
            },
        ],
"vocabulario": [
            {"pt": "economia", "fr": "économie"},
            {"pt": "exportação", "fr": "exportation"},
            {"pt": "produção", "fr": "production"},
            {"pt": "fazenda", "fr": "plantation"},
        ],
    },
{'slug': 'literatura-brasileira',
 'categoria': 'cultura',
 'nivel': 'intermediario',
 'emoji': '📚',
 'titulo_pt': 'Uma viagem pela literatura brasileira',
 'titulo_fr': 'Un voyage dans la littérature brésilienne',
 'texto_pt': 'A literatura brasileira é um grande encontro de vozes, regiões e épocas. Antes da '
             'escrita em português, povos indígenas já transmitiam conhecimentos, histórias de '
             'origem e ensinamentos por meio da oralidade. Com a colonização, surgiram textos '
             'ligados à vida colonial; nos séculos seguintes, escritores passaram a imaginar o '
             'país, discutir suas desigualdades e experimentar novas formas de escrever. No século '
             'XIX, o romantismo ajudou a construir imagens de uma identidade nacional, enquanto '
             'autores realistas, como Machado de Assis, observaram com ironia os costumes e as '
             'relações de poder. No século XX, o modernismo rompeu convenções e aproximou a '
             'literatura da fala e da diversidade brasileiras. Mais tarde, escritoras como Clarice '
             'Lispector exploraram a vida interior e os pequenos acontecimentos do cotidiano. '
             'Autores como Carolina Maria de Jesus deram forma literária à experiência da pobreza '
             'urbana e à voz de quem raramente era ouvido nos livros. Hoje, romances, contos, '
             'poemas, crônicas, literatura indígena e narrativas periféricas convivem em um campo '
             'muito diverso. Ler esses textos é viajar pelo país sem sair da página: cada obra '
             'revela uma época, uma maneira de falar e uma pergunta sobre como viver juntos.',
 'texto_fr': 'La littérature brésilienne est une grande rencontre de voix, de régions et '
             'd’époques. Avant l’écriture en portugais, les peuples autochtones transmettaient '
             'déjà des savoirs, des récits d’origine et des enseignements par la tradition orale. '
             'Avec la colonisation apparurent des textes liés à la vie coloniale ; au fil des '
             'siècles, des écrivains se mirent à imaginer le pays, à discuter de ses inégalités et '
             'à expérimenter de nouvelles formes d’écriture. Au XIXe siècle, le romantisme '
             'contribua à construire des images d’une identité nationale, tandis que des auteurs '
             'réalistes comme Machado de Assis observaient avec ironie les mœurs et les rapports '
             'de pouvoir. Au XXe siècle, le modernisme rompit avec les conventions et rapprocha la '
             'littérature de la parole et de la diversité brésiliennes. Plus tard, des écrivaines '
             'comme Clarice Lispector explorèrent la vie intérieure et les petits événements du '
             'quotidien. Des autrices comme Carolina Maria de Jesus donnèrent une forme littéraire '
             'à l’expérience de la pauvreté urbaine et à la voix de personnes rarement entendues '
             'dans les livres. Aujourd’hui, romans, nouvelles, poèmes, chroniques, littérature '
             'autochtone et récits des périphéries coexistent dans un paysage très divers. Lire '
             'ces textes, c’est voyager dans le pays sans quitter la page : chaque œuvre révèle '
             'une époque, une façon de parler et une question sur la vie en commun.',
 'vocabulario': [{'pt': 'oralidade', 'fr': 'tradition orale'},
                 {'pt': 'romance', 'fr': 'roman'},
                 {'pt': 'desigualdade', 'fr': 'inégalité'},
                 {'pt': 'cotidiano', 'fr': 'quotidien'}],
 'quiz': [{'pergunta_pt': 'Como muitos povos indígenas transmitiam histórias e conhecimentos?',
           'pergunta_fr': 'Comment de nombreux peuples autochtones transmettaient-ils les récits '
                          'et les savoirs ?',
           'opcoes_pt': ['Pela tradição oral.',
                         'Pelos jornais digitais.',
                         'Pelas novelas de televisão.'],
           'opcoes_fr': ['Par la tradition orale.',
                         'Par les journaux numériques.',
                         'Par les feuilletons télévisés.'],
           'resposta': 0},
          {'pergunta_pt': 'O que o modernismo buscou fazer?',
           'pergunta_fr': 'Que cherchait à faire le modernisme ?',
           'opcoes_pt': ['Eliminar a diversidade regional.',
                         'Romper convenções e explorar novas formas.',
                         'Repetir somente modelos antigos.'],
           'opcoes_fr': ['Éliminer la diversité régionale.',
                         'Rompre avec les conventions et explorer de nouvelles formes.',
                         'Répéter uniquement les anciens modèles.'],
           'resposta': 2},
          {'pergunta_pt': 'O que a literatura pode revelar ao leitor?',
           'pergunta_fr': 'Que peut révéler la littérature au lecteur ?',
           'opcoes_pt': ['Somente fatos inventados sem relação com a sociedade.',
                         'Épocas, vozes e formas de viver.',
                         'Apenas regras gramaticais.'],
           'opcoes_fr': ['Seulement des faits inventés sans lien avec la société.',
                         'Des époques, des voix et des façons de vivre.',
                         'Uniquement des règles de grammaire.'],
           'resposta': 1}]},
{'slug': 'machado-de-assis',
 'categoria': 'cultura',
 'nivel': 'avancado',
 'emoji': '✒️',
 'titulo_pt': 'Machado de Assis e o olhar irônico',
 'titulo_fr': 'Machado de Assis et son regard ironique',
 'texto_pt': 'Joaquim Maria Machado de Assis nasceu no Rio de Janeiro em 1839 e se tornou um dos '
             'nomes centrais da literatura em língua portuguesa. Filho de uma família humilde, '
             'começou a trabalhar ainda jovem e aprendeu muito por conta própria. Foi tipógrafo, '
             'revisor, jornalista, cronista, poeta e romancista; sua carreira mostra como a '
             'imprensa e os folhetins eram espaços importantes para a literatura do século XIX. Em '
             '1897, participou da fundação da Academia Brasileira de Letras e foi seu primeiro '
             'presidente. Entre suas obras mais conhecidas estão Memórias Póstumas de Brás Cubas, '
             'Quincas Borba e Dom Casmurro. Em Memórias Póstumas, o narrador conta sua vida depois '
             'de morto e conversa diretamente com quem lê. Esse recurso permite a Machado brincar '
             'com as expectativas do público e expor, com humor e ironia, a vaidade e os '
             'privilégios da elite. Em Dom Casmurro, o leitor acompanha a memória interessada de '
             'Bentinho e precisa decidir o quanto pode confiar em sua versão dos fatos. Machado '
             'não entrega respostas simples: seus narradores podem omitir, exagerar ou tentar '
             'convencer. Por isso, seus livros continuam provocando debates sobre memória, ciúme, '
             'classe social e o poder de contar uma história.',
 'texto_fr': 'Joaquim Maria Machado de Assis naquit à Rio de Janeiro en 1839 et devint l’une des '
             'figures majeures de la littérature de langue portugaise. Issu d’une famille modeste, '
             'il commença à travailler jeune et apprit beaucoup par lui-même. Il fut typographe, '
             'correcteur, journaliste, chroniqueur, poète et romancier ; son parcours montre '
             'l’importance de la presse et des feuilletons pour la littérature du XIXe siècle. En '
             '1897, il participa à la fondation de l’Académie brésilienne des lettres et en devint '
             'le premier président. Parmi ses œuvres les plus connues figurent Mémoires posthumes '
             'de Brás Cubas, Quincas Borba et Dom Casmurro. Dans Mémoires posthumes, le narrateur '
             'raconte sa vie après sa mort et s’adresse directement au lecteur. Ce procédé permet '
             'à Machado de jouer avec les attentes du public et de révéler, avec humour et ironie, '
             'la vanité et les privilèges des élites. Dans Dom Casmurro, le lecteur suit les '
             'souvenirs intéressés de Bentinho et doit décider dans quelle mesure il peut croire '
             'sa version des faits. Machado ne donne pas de réponses faciles : ses narrateurs '
             'peuvent omettre, exagérer ou chercher à convaincre. Ses livres suscitent ainsi '
             'encore des discussions sur la mémoire, la jalousie, les classes sociales et le '
             'pouvoir de raconter une histoire.',
 'vocabulario': [{'pt': 'cronista', 'fr': 'chroniqueur'},
                 {'pt': 'vaidade', 'fr': 'vanité'},
                 {'pt': 'narrador', 'fr': 'narrateur'},
                 {'pt': 'omitir', 'fr': 'omettre'}],
 'quiz': [{'pergunta_pt': 'Em que cidade Machado de Assis nasceu?',
           'pergunta_fr': 'Dans quelle ville Machado de Assis est-il né ?',
           'opcoes_pt': ['Salvador.', 'Rio de Janeiro.', 'Recife.'],
           'opcoes_fr': ['À Salvador.', 'À Rio de Janeiro.', 'À Recife.'],
           'resposta': 1},
          {'pergunta_pt': 'Quem narra Memórias Póstumas de Brás Cubas?',
           'pergunta_fr': 'Qui raconte les Mémoires posthumes de Brás Cubas ?',
           'opcoes_pt': ['Um narrador que conta a vida depois de morrer.',
                         'O próprio leitor.',
                         'Um historiador do século XXI.'],
           'opcoes_fr': ['Un narrateur qui raconte sa vie après sa mort.',
                         'Le lecteur lui-même.',
                         'Un historien du XXIe siècle.'],
           'resposta': 1},
          {'pergunta_pt': 'Por que Dom Casmurro ainda provoca debates?',
           'pergunta_fr': 'Pourquoi Dom Casmurro suscite-t-il encore des débats ?',
           'opcoes_pt': ['Porque o leitor precisa avaliar a versão do narrador.',
                         'Porque o romance não tem narrador.',
                         'Porque todos os fatos são explicados por documentos.'],
           'opcoes_fr': ['Parce que le lecteur doit évaluer la version du narrateur.',
                         'Parce que le roman n’a pas de narrateur.',
                         'Parce que tous les faits sont expliqués par des documents.'],
           'resposta': 0}]},
{'slug': 'clarice-lispector',
 'categoria': 'cultura',
 'nivel': 'avancado',
 'emoji': '🪞',
 'titulo_pt': 'Clarice Lispector: o cotidiano por dentro',
 'titulo_fr': 'Clarice Lispector : le quotidien vu de l’intérieur',
 'texto_pt': 'Clarice Lispector nasceu na Ucrânia, em 1920, e chegou ainda bebê ao Brasil com a '
             'família. Cresceu no Nordeste e viveu no Recife durante parte importante da infância; '
             'mais tarde, mudou-se para o Rio de Janeiro. Em 1943 publicou seu primeiro romance, '
             'Perto do Coração Selvagem, que chamou atenção pela linguagem singular e pela maneira '
             'de acompanhar os pensamentos de uma personagem. Clarice escreveu romances, contos, '
             'crônicas e livros para crianças, além de trabalhar como jornalista. Em obras como '
             'Laços de Família, A Paixão Segundo G.H. e A Hora da Estrela, acontecimentos comuns '
             'podem abrir perguntas profundas: uma conversa, um encontro ou uma tarefa doméstica '
             'faz a personagem olhar de outro modo para si e para o mundo. Sua prosa '
             'frequentemente acompanha a consciência em movimento, com frases que parecem pensar '
             'enquanto avançam. Em A Hora da Estrela, publicado em 1977, a história de Macabéa, '
             'uma jovem migrante nordestina que vive no Rio, também levanta questões sobre '
             'pobreza, invisibilidade e quem tem o direito de narrar a vida de outra pessoa. A '
             'escrita de Clarice pode parecer enigmática, mas começa muitas vezes com algo '
             'familiar. Ler devagar ajuda a perceber imagens, silêncios e mudanças de perspectiva '
             'que transformam o cotidiano em descoberta.',
 'texto_fr': 'Clarice Lispector naquit en Ukraine en 1920 et arriva bébé au Brésil avec sa '
             'famille. Elle grandit dans le Nordeste et vécut une partie importante de son enfance '
             'à Recife ; plus tard, elle s’installa à Rio de Janeiro. En 1943, elle publia son '
             'premier roman, Près du cœur sauvage, remarqué pour sa langue singulière et sa '
             'manière de suivre les pensées d’un personnage. Clarice écrivit des romans, des '
             'nouvelles, des chroniques et des livres pour enfants, et travailla aussi comme '
             'journaliste. Dans des œuvres comme Liens de famille, La Passion selon G.H. et '
             'L’Heure de l’étoile, des événements ordinaires peuvent ouvrir des questions '
             'profondes : une conversation, une rencontre ou une tâche ménagère amène le '
             'personnage à se regarder et à regarder le monde autrement. Sa prose suit souvent une '
             'conscience en mouvement, avec des phrases qui semblent réfléchir au fur et à mesure. '
             'Dans L’Heure de l’étoile, publié en 1977, l’histoire de Macabéa, une jeune migrante '
             'du Nordeste vivant à Rio, soulève aussi des questions sur la pauvreté, '
             'l’invisibilité et le droit de raconter la vie d’autrui. L’écriture de Clarice peut '
             'sembler énigmatique, mais elle part souvent d’un détail familier. Lire lentement '
             'aide à remarquer les images, les silences et les changements de perspective qui '
             'transforment le quotidien en découverte.',
 'vocabulario': [{'pt': 'consciência', 'fr': 'conscience'},
                 {'pt': 'enigmático', 'fr': 'énigmatique'},
                 {'pt': 'silêncio', 'fr': 'silence'},
                 {'pt': 'perspectiva', 'fr': 'perspective'}],
 'quiz': [{'pergunta_pt': 'Onde Clarice Lispector nasceu?',
           'pergunta_fr': 'Où Clarice Lispector est-elle née ?',
           'opcoes_pt': ['No Rio de Janeiro.', 'Na Ucrânia.', 'No Recife.'],
           'opcoes_fr': ['À Rio de Janeiro.', 'En Ukraine.', 'À Recife.'],
           'resposta': 1},
          {'pergunta_pt': 'O que pode acontecer a partir de uma cena comum em seus livros?',
           'pergunta_fr': 'Que peut-il se passer à partir d’une scène ordinaire dans ses livres ?',
           'opcoes_pt': ['Ela pode abrir perguntas profundas.',
                         'Ela sempre termina em uma aventura policial.',
                         'Ela não afeta os personagens.'],
           'opcoes_fr': ['Elle peut ouvrir des questions profondes.',
                         'Elle se termine toujours par une aventure policière.',
                         'Elle n’affecte pas les personnages.'],
           'resposta': 0},
          {'pergunta_pt': 'Quem é Macabéa?',
           'pergunta_fr': 'Qui est Macabéa ?',
           'opcoes_pt': ['Uma cientista da Fiocruz.',
                         'Uma jovem migrante nordestina em A Hora da Estrela.',
                         'A narradora de Dom Casmurro.'],
           'opcoes_fr': ['Une scientifique de Fiocruz.',
                         'Une jeune migrante du Nordeste dans L’Heure de l’étoile.',
                         'La narratrice de Dom Casmurro.'],
           'resposta': 1}]},
{'slug': 'carlos-chagas-ciencia',
 'categoria': 'ciencia',
 'nivel': 'avancado',
 'emoji': '🔬',
 'titulo_pt': 'Carlos Chagas e uma descoberta completa',
 'titulo_fr': 'Carlos Chagas et une découverte complète',
 'texto_pt': 'No início do século XX, o médico e pesquisador Carlos Chagas trabalhava em Lassance, '
             'no interior de Minas Gerais, durante uma campanha contra a malária. Em 1909, '
             'investigou um inseto conhecido como barbeiro, que se escondia nas paredes das casas '
             'e se alimentava de sangue. Chagas identificou no inseto um protozoário até então '
             'desconhecido, que chamou Trypanosoma cruzi em homenagem ao médico Oswaldo Cruz. '
             'Depois, encontrou o parasita no sangue de uma criança chamada Berenice e descreveu a '
             'doença que passou a levar seu nome. O trabalho se destacou porque Chagas identificou '
             'o agente causador, o inseto transmissor e a doença humana em um mesmo ciclo de '
             'pesquisa. Essa descoberta não foi obra de uma pessoa isolada: pesquisadores do '
             'Instituto Oswaldo Cruz contribuíram para estudar o parasita e compreender a doença. '
             'A investigação também mostrou como a ciência pode começar com perguntas sobre a vida '
             'cotidiana e as condições de moradia. A doença de Chagas continua sendo um problema '
             'de saúde pública em vários países, por isso a pesquisa, o diagnóstico e o acesso à '
             'informação seguem importantes. A história de Lassance é um exemplo de ciência feita '
             'no Brasil que dialogou com problemas locais e teve impacto internacional.',
 'texto_fr': 'Au début du XXe siècle, le médecin et chercheur Carlos Chagas travaillait à '
             'Lassance, dans l’intérieur du Minas Gerais, pendant une campagne contre le '
             'paludisme. En 1909, il étudia un insecte appelé barbeiro, qui se cachait dans les '
             'murs des maisons et se nourrissait de sang. Chagas identifia chez cet insecte un '
             'protozoaire jusque-là inconnu, qu’il nomma Trypanosoma cruzi en hommage au médecin '
             'Oswaldo Cruz. Il trouva ensuite le parasite dans le sang d’une enfant appelée '
             'Berenice et décrivit la maladie qui allait porter son nom. Ce travail fut '
             'remarquable parce que Chagas identifia l’agent responsable, l’insecte transmetteur '
             'et la maladie humaine dans un même cycle de recherche. Cette découverte ne fut pas '
             'l’œuvre d’une personne isolée : des chercheurs de l’Institut Oswaldo Cruz '
             'contribuèrent à étudier le parasite et à comprendre la maladie. L’enquête montra '
             'aussi comment la science peut partir de questions sur la vie quotidienne et les '
             'conditions de logement. La maladie de Chagas reste un problème de santé publique '
             'dans plusieurs pays ; la recherche, le diagnostic et l’accès à l’information restent '
             'donc importants. L’histoire de Lassance est un exemple de science menée au Brésil, '
             'en dialogue avec des problèmes locaux et ayant eu un impact international.',
 'vocabulario': [{'pt': 'pesquisador', 'fr': 'chercheur'},
                 {'pt': 'parasita', 'fr': 'parasite'},
                 {'pt': 'transmissor', 'fr': 'transmetteur'},
                 {'pt': 'diagnóstico', 'fr': 'diagnostic'}],
 'quiz': [{'pergunta_pt': 'Onde Carlos Chagas realizou parte importante de sua pesquisa?',
           'pergunta_fr': 'Où Carlos Chagas a-t-il mené une partie importante de ses recherches ?',
           'opcoes_pt': ['Em Lassance, Minas Gerais.', 'Em Manaus, Amazonas.', 'Em Brasília.'],
           'opcoes_fr': ['À Lassance, dans le Minas Gerais.',
                         'À Manaus, en Amazonie.',
                         'À Brasília.'],
           'resposta': 0},
          {'pergunta_pt': 'O que era o barbeiro na pesquisa?',
           'pergunta_fr': 'Quel rôle jouait le barbeiro dans cette recherche ?',
           'opcoes_pt': ['O nome do laboratório.',
                         'O inseto transmissor estudado por Chagas.',
                         'O remédio usado contra a malária.'],
           'opcoes_fr': ['Le nom du laboratoire.',
                         'L’insecte transmetteur étudié par Chagas.',
                         'Le médicament utilisé contre le paludisme.'],
           'resposta': 1},
          {'pergunta_pt': 'O que tornou a descoberta especialmente notável?',
           'pergunta_fr': 'Qu’est-ce qui rendit cette découverte particulièrement remarquable ?',
           'opcoes_pt': ['A criação de um novo hospital em Brasília.',
                         'A identificação do parasita, vetor e doença no mesmo ciclo de pesquisa.',
                         'A descoberta de uma vacina contra todas as doenças.'],
           'opcoes_fr': ['La création d’un nouvel hôpital à Brasília.',
                         'L’identification du parasite, du vecteur et de la maladie dans un même '
                         'cycle de recherche.',
                         'La découverte d’un vaccin contre toutes les maladies.'],
           'resposta': 1}]},
{'slug': 'ciencia-agricola-no-brasil',
 'categoria': 'ciencia',
 'nivel': 'intermediario',
 'emoji': '🌱',
 'titulo_pt': 'Ciência agrícola e o Cerrado',
 'titulo_fr': 'La recherche agricole et le Cerrado',
 'texto_pt': 'A pesquisa científica também transforma a agricultura. Em 1973, o Brasil inaugurou a '
             'Embrapa, uma instituição pública dedicada à pesquisa agropecuária. A ideia era '
             'desenvolver conhecimentos adaptados aos solos, ao clima e às necessidades do país, '
             'em colaboração com universidades, órgãos estaduais, técnicos e produtores. No '
             'Cerrado, por exemplo, pesquisadores estudaram a acidez e a fertilidade dos solos, '
             'variedades de plantas e técnicas de manejo. Esse trabalho ajudou a tornar possível o '
             'cultivo de algumas culturas em áreas onde antes a produção era limitada. A '
             'transformação aumentou a oferta de alimentos e mudou a economia de várias regiões, '
             'mas também trouxe consequências ambientais: a expansão agrícola pode pressionar a '
             'vegetação nativa, a água e a biodiversidade. Por isso, a pesquisa atual precisa '
             'considerar produtividade e conservação ao mesmo tempo. Ciência agrícola não acontece '
             'apenas em laboratórios; envolve testes em campo, observação de longo prazo, '
             'conhecimento local e decisões sobre como usar a terra. O exemplo do Cerrado mostra '
             'tanto a capacidade de pesquisa desenvolvida no Brasil quanto a responsabilidade de '
             'avaliar os custos e benefícios das mudanças. Produzir mais é importante, mas '
             'proteger ecossistemas e comunidades também faz parte do desafio.',
 'texto_fr': 'La recherche scientifique transforme aussi l’agriculture. En 1973, le Brésil '
             'inaugura l’Embrapa, un organisme public consacré à la recherche agricole et animale. '
             'L’objectif était de développer des connaissances adaptées aux sols, au climat et aux '
             'besoins du pays, en collaboration avec les universités, les organismes régionaux, '
             'les techniciens et les producteurs. Dans le Cerrado, par exemple, les chercheurs '
             'étudièrent l’acidité et la fertilité des sols, les variétés végétales et les '
             'techniques de gestion des cultures. Ces travaux contribuèrent à rendre certaines '
             'cultures possibles dans des zones où la production était auparavant limitée. Cette '
             'transformation augmenta l’offre alimentaire et changea l’économie de plusieurs '
             'régions, mais elle eut aussi des conséquences environnementales : l’expansion '
             'agricole peut exercer une pression sur la végétation native, l’eau et la '
             'biodiversité. La recherche actuelle doit donc considérer la productivité et la '
             'conservation ensemble. La recherche agricole ne se déroule pas uniquement en '
             'laboratoire ; elle implique des essais sur le terrain, une observation à long terme, '
             'les savoirs locaux et des choix sur l’utilisation des terres. L’exemple du Cerrado '
             'montre à la fois les capacités de recherche développées au Brésil et la '
             'responsabilité d’évaluer les coûts et les bénéfices des changements. Produire '
             'davantage est important, mais protéger les écosystèmes et les communautés fait aussi '
             'partie du défi.',
 'vocabulario': [{'pt': 'agropecuária', 'fr': 'agriculture et élevage'},
                 {'pt': 'fertilidade', 'fr': 'fertilité'},
                 {'pt': 'manejo', 'fr': 'gestion'},
                 {'pt': 'biodiversidade', 'fr': 'biodiversité'}],
 'quiz': [{'pergunta_pt': 'Quando a Embrapa foi inaugurada?',
           'pergunta_fr': 'Quand l’Embrapa a-t-elle été inaugurée ?',
           'opcoes_pt': ['Em 1909.', 'Em 1973.', 'Em 2000.'],
           'opcoes_fr': ['En 1909.', 'En 1973.', 'En 2000.'],
           'resposta': 1},
          {'pergunta_pt': 'O que pesquisadores estudaram no Cerrado?',
           'pergunta_fr': 'Qu’ont étudié les chercheurs dans le Cerrado ?',
           'opcoes_pt': ['A construção de ferrovias.',
                         'Solos, plantas e técnicas de manejo.',
                         'Somente a vida marinha.'],
           'opcoes_fr': ['La construction de chemins de fer.',
                         'Les sols, les plantes et les techniques de gestion.',
                         'Uniquement la vie marine.'],
           'resposta': 1},
          {'pergunta_pt': 'Que desafio a pesquisa agrícola precisa considerar?',
           'pergunta_fr': 'Quel défi la recherche agricole doit-elle prendre en compte ?',
           'opcoes_pt': ['Equilibrar produção e conservação.',
                         'Expandir a produção sem avaliar impactos.',
                         'Substituir toda a vegetação nativa.'],
           'opcoes_fr': ['Équilibrer production et conservation.',
                         'Étendre la production sans évaluer les impacts.',
                         'Remplacer toute la végétation native.'],
           'resposta': 0}]},

]
