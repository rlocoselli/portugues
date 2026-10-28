"""Bilingual educational guides with dated, attributed indicators."""

SOURCES = {
    "gdp": "https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/45968-pib-cresce-2-3-em-2025-e-fecha-o-ano-em-r-12-7-trilhoes",
    "work": "https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/45920-pnad-continua-taxas-anuais-de-desocupacao-sao-as-menores-da-serie-em-20-unidades-da-federacao",
    "education": "https://www.ibge.gov.br/indicadores",
    "hdi": "https://hdr.undp.org/system/files/documents/global-report-document/hdr2025reporten.pdf",
    "language": "https://ciberduvidas.iscte-iul.pt/consultorio/perguntas/20-palavras-semanticamente-diferentes-em-portugal-e-no-brasil/14050",
    "language_abl": "https://www2.academia.org.br/artigos/pronuncias-daqui-e-de-la",
    "language_grammar": "https://repositorio.ul.pt/entities/publication/45fde740-d921-46c8-9d79-eaf174aee4b4",
    "language_treatment": "https://revistas.usp.br/linhadagua/pt_BR/article/view/204428",
    "history": "https://www.senado.gov.br/noticias/especiais/constituicao25anos/historia-das-constituicoes.htm",
    "memory": "https://www.gov.br/memoriasreveladas/pt-br/assuntos/comissoes-da-verdade/sindicatos/relatoriodacomissaonacionaldamemoriaverdadeejusticadacut.pdf",
}

INDICATORS = [
    {
        "slug": "pib", "group": "economia", "value": "R$ 12,7 tri", "value_fr": "12,7 billions R$", "year": "2025", "source": "gdp",
        "label_pt": "Produto Interno Bruto", "label_fr": "Produit intérieur brut",
        "text_pt": "Em 2025, o Produto Interno Bruto do Brasil somou R$ 12,7 trilhões em valores correntes. O PIB reúne o valor dos bens e serviços finais produzidos no país durante o ano. Ele ajuda a observar a dimensão da economia, mas não mostra, sozinho, como a renda foi distribuída entre as pessoas.",
        "text_fr": "En 2025, le produit intérieur brut du Brésil a atteint 12,7 billions de réaux en valeur courante. Le PIB rassemble la valeur des biens et services finaux produits dans le pays pendant l’année. Il aide à mesurer la taille de l’économie, mais ne montre pas, à lui seul, comment les revenus sont répartis entre les personnes.",
    },
    {
        "slug": "crescimento", "group": "economia", "value": "+2,3%", "year": "2025", "source": "gdp",
        "label_pt": "Crescimento real do PIB", "label_fr": "Croissance réelle du PIB",
        "text_pt": "O PIB cresceu 2,3% em 2025 em relação a 2024. Essa comparação considera o volume produzido, descontando o efeito da variação de preços. Agropecuária, indústria e serviços tiveram resultados positivos, mas em ritmos diferentes. Crescimento econômico é uma medida importante; não é uma medida direta da qualidade de vida.",
        "text_fr": "Le PIB a progressé de 2,3 % en 2025 par rapport à 2024. Cette comparaison porte sur le volume produit, en retirant l’effet de la variation des prix. L’agriculture, l’industrie et les services ont tous progressé, mais à des rythmes différents. La croissance est un indicateur important ; elle ne mesure pas directement la qualité de vie.",
    },
    {
        "slug": "desocupacao", "group": "economia", "value": "5,6%", "year": "2025", "source": "work",
        "label_pt": "Taxa anual de desocupação", "label_fr": "Taux annuel de chômage",
        "text_pt": "A taxa média anual de desocupação foi de 5,6% em 2025, segundo a PNAD Contínua. Ela considera pessoas sem trabalho que procuraram uma ocupação e estavam disponíveis para trabalhar. Por isso, o indicador não inclui todas as situações de trabalho precário ou de quem desistiu de procurar emprego.",
        "text_fr": "Le taux annuel moyen de chômage était de 5,6 % en 2025 selon l’enquête PNAD Contínua. Il concerne les personnes sans emploi qui en ont cherché un et étaient disponibles pour travailler. Cet indicateur ne couvre donc pas toutes les formes d’emploi précaire ni les personnes qui ont renoncé à chercher un emploi.",
    },
    {
        "slug": "escolarizacao", "group": "educacao", "value": "99,5%", "year": "2025", "source": "education",
        "label_pt": "Escolarização dos 6 aos 14 anos", "label_fr": "Scolarisation de 6 à 14 ans",
        "text_pt": "Em 2025, 99,5% das crianças e adolescentes de 6 a 14 anos frequentavam a escola. A taxa mede a presença na escola nessa faixa etária, não a aprendizagem alcançada nem a conclusão do ensino. Para entender a educação brasileira, é preciso olhar também para permanência, desigualdades e resultados de aprendizagem.",
        "text_fr": "En 2025, 99,5 % des enfants et adolescents de 6 à 14 ans fréquentaient l’école. Ce taux mesure la fréquentation scolaire à cet âge, pas les acquis des élèves ni l’achèvement d’un cycle d’études. Pour comprendre l’éducation au Brésil, il faut aussi examiner la continuité des parcours, les inégalités et les apprentissages.",
    },
    {
        "slug": "analfabetismo", "group": "educacao", "value": "4,9%", "year": "2025", "source": "education",
        "label_pt": "Analfabetismo a partir de 15 anos", "label_fr": "Analphabétisme à partir de 15 ans",
        "text_pt": "A taxa de analfabetismo das pessoas de 15 anos ou mais foi de 4,9% em 2025. Isso representa pessoas que declararam não saber ler e escrever um bilhete simples. A média nacional esconde diferenças por idade, região e condições sociais; por isso, um único percentual não conta toda a história.",
        "text_fr": "Le taux d’analphabétisme des personnes de 15 ans ou plus était de 4,9 % en 2025. Il correspond aux personnes déclarant ne pas savoir lire et écrire un message simple. La moyenne nationale masque des différences selon l’âge, la région et les conditions sociales ; un seul pourcentage ne raconte donc pas toute l’histoire.",
    },
    {
        "slug": "idh", "group": "idh", "value": "0,786", "year": "2023 · relatório 2025", "year_fr": "2023 · rapport 2025", "source": "hdi",
        "label_pt": "Índice de Desenvolvimento Humano", "label_fr": "Indice de développement humain",
        "text_pt": "O IDH do Brasil foi de 0,786 nos dados de 2023 publicados no Relatório de Desenvolvimento Humano de 2025 do PNUD. O índice combina saúde, educação e renda em uma escala de zero a um. O resultado nacional resume três dimensões, mas não mostra todas as desigualdades entre grupos e territórios. IDH nacional e IDHM municipal são indicadores diferentes.",
        "text_fr": "L’IDH du Brésil était de 0,786 pour l’année 2023, selon le Rapport sur le développement humain 2025 du PNUD. Cet indice combine santé, éducation et revenu sur une échelle de zéro à un. Le résultat national résume trois dimensions, mais ne décrit pas toutes les inégalités entre groupes et territoires. L’IDH national et l’indice municipal IDHM sont distincts.",
    },
]

INDICATOR_GROUPS = [
    {"slug": "economia", "icon": "↗", "title_pt": "Economia", "title_fr": "Économie", "intro_pt": "A economia pode ser observada pelo que o país produz e pelas oportunidades de trabalho. Cada número responde a uma pergunta diferente.", "intro_fr": "On peut observer l’économie à travers la production du pays et les possibilités d’emploi. Chaque chiffre répond à une question différente."},
    {"slug": "educacao", "icon": "✎", "title_pt": "Educação", "title_fr": "Éducation", "intro_pt": "Frequentar a escola e saber ler são medidas diferentes. Juntas, elas ajudam a entender conquistas e desafios.", "intro_fr": "Fréquenter l’école et savoir lire sont deux mesures différentes. Ensemble, elles éclairent les progrès et les défis."},
    {"slug": "idh", "icon": "◇", "title_pt": "Desenvolvimento humano", "title_fr": "Développement humain", "intro_pt": "O IDH combina três dimensões da vida. Leia o ano de referência antes de comparar o índice com outros dados.", "intro_fr": "L’IDH réunit trois dimensions de la vie. Vérifiez son année de référence avant de le comparer à d’autres données."},
]

VARIETIES = [
    {
        "slug": "vocabulario", "icon": "↔", "title_pt": "Palavras do cotidiano", "title_fr": "Les mots du quotidien",
        "text_pt": "Brasil e Portugal compartilham a língua portuguesa, mas nem sempre escolhem as mesmas palavras para objetos comuns. No Brasil, é frequente dizer trem, ônibus e sorvete; em Portugal, comboio, autocarro e gelado. Se uma palavra soar desconhecida, o contexto muitas vezes ajuda. Essas diferenças não tornam uma variedade mais correta que a outra.",
        "text_fr": "Le Brésil et le Portugal partagent le portugais, mais n’emploient pas toujours les mêmes mots pour les objets du quotidien. Au Brésil, on dit souvent trem, ônibus et sorvete ; au Portugal, comboio, autocarro et gelado. Quand un mot est inconnu, le contexte aide souvent. Aucune de ces variétés n’est plus correcte que l’autre.",
        "pairs": [("trem", "comboio", "train"), ("ônibus", "autocarro", "bus"), ("sorvete", "gelado", "glace"), ("goleiro", "guarda-redes", "gardien de but")],
        "source": "language",
    },
    {
        "slug": "acao", "icon": "◷", "title_pt": "Uma ação acontecendo agora", "title_fr": "Une action en cours",
        "text_pt": "Para falar de uma ação em andamento, é muito comum ouvir “estou estudando” no Brasil e “estou a estudar” em Portugal. As duas construções expressam a mesma ideia neste contexto. Também há variação dentro dos países: o gerúndio aparece em variedades do português europeu, e brasileiros reconhecem a construção com “a” mais infinitivo. Observe o padrão predominante sem tratá-lo como regra absoluta.",
        "text_fr": "Pour parler d’une action en cours, on entend très souvent « estou estudando » au Brésil et « estou a estudar » au Portugal. Les deux constructions expriment ici la même idée. Il existe aussi des variations à l’intérieur de chaque pays : le gérondif est utilisé dans certaines variétés européennes, et les Brésiliens comprennent la construction avec « a » suivi de l’infinitif. Il s’agit de tendances, pas de règles absolues.",
        "pairs": [("Estou estudando.", "Estou a estudar.", "J’étudie en ce moment.")],
        "source": "language_grammar",
    },
    {
        "slug": "tratamento", "icon": "✳", "title_pt": "Como falar com alguém", "title_fr": "Comment s’adresser à quelqu’un",
        "text_pt": "“Você” é muito comum em grande parte do Brasil; “tu” também existe e varia bastante conforme a região. Em Portugal, “tu” é corrente em muitas relações de proximidade, mas as formas de tratamento dependem da situação e podem ser delicadas. Antes de escolher uma forma, escute como as pessoas ao redor se dirigem umas às outras. O uso real é mais rico que uma regra simples de país para país.",
        "text_fr": "« Você » est très courant dans une grande partie du Brésil ; « tu » existe aussi et varie selon les régions. Au Portugal, « tu » est fréquent dans les relations de proximité, mais les formes d’adresse dépendent de la situation et peuvent être délicates. Avant de choisir une forme, écoutez comment les personnes autour de vous se parlent. L’usage réel est plus riche qu’une simple règle opposant deux pays.",
        "pairs": [("Você quer um café?", "Queres um café?", "Tu veux un café ?")],
        "source": "language_treatment",
    },
    {
        "slug": "som", "icon": "♪", "title_pt": "Ritmo e pronúncia", "title_fr": "Rythme et prononciation",
        "text_pt": "Muitos ouvintes percebem que o português europeu reduz mais certas vogais sem acento, enquanto em muitas falas brasileiras elas soam mais claramente. O ritmo e a melodia também variam. Não existe um único sotaque brasileiro nem um único sotaque português: cidades, regiões, gerações e situações de fala mudam a maneira de pronunciar as palavras.",
        "text_fr": "Beaucoup d’auditeurs remarquent que le portugais européen réduit davantage certaines voyelles non accentuées, tandis qu’elles sont souvent plus audibles dans des parlers brésiliens. Le rythme et la mélodie varient aussi. Il n’existe pas un seul accent brésilien ni un seul accent portugais : les villes, les régions, les générations et les situations influencent la prononciation.",
        "pairs": [], "source": "language_abl",
    },
]

HISTORY = [
    {
        "slug": "antes", "date": "Antes de 1889", "title_pt": "Antes da República", "title_fr": "Avant la République", "icon": "◌",
        "text_pt": "A história do Brasil não começa em 1500: povos indígenas viviam no território muito antes da chegada dos portugueses. A colonização trouxe violência, escravização de africanos e profundas transformações. Depois da independência, em 1822, o Brasil tornou-se uma monarquia. A escravidão foi abolida em 1888; a liberdade legal, porém, não veio acompanhada de reparação e igualdade para a população negra. Esse contexto ajuda a entender as disputas que cercaram o fim do Império.",
        "text_fr": "L’histoire du Brésil ne commence pas en 1500 : des peuples autochtones vivaient sur ce territoire bien avant l’arrivée des Portugais. La colonisation entraîna violences, esclavage des Africains et profondes transformations. Après l’indépendance, en 1822, le Brésil devint une monarchie. L’esclavage fut aboli en 1888, mais cette liberté juridique ne s’accompagna ni de réparation ni d’égalité pour la population noire. Ce contexte éclaire les conflits qui entourèrent la fin de l’Empire.",
    },
    {
        "slug": "primeira", "date": "1889–1930", "title_pt": "Primeira República", "title_fr": "Première République", "icon": "Ⅰ",
        "text_pt": "A República foi proclamada em 15 de novembro de 1889. A Constituição de 1891 estabeleceu o federalismo e a separação entre Estado e Igreja. O voto e a participação política, porém, eram limitados; mulheres e pessoas analfabetas ficaram excluídas das eleições nacionais. Elites regionais tiveram grande influência, e conflitos sociais revelaram que a mudança de regime não significou cidadania igual para todos.",
        "text_fr": "La République fut proclamée le 15 novembre 1889. La Constitution de 1891 instaura le fédéralisme et la séparation de l’État et de l’Église. Le vote et la participation politique restaient pourtant limités : les femmes et les personnes analphabètes étaient exclues des élections nationales. Les élites régionales conservaient une grande influence, et les conflits sociaux montraient que le changement de régime ne donnait pas à tous une citoyenneté égale.",
    },
    {
        "slug": "vargas", "date": "1930–1945", "title_pt": "Era Vargas e Estado Novo", "title_fr": "Ère Vargas et Estado Novo", "icon": "Ⅱ",
        "text_pt": "A Revolução de 1930 levou Getúlio Vargas ao poder. Em 1934, uma nova Constituição consolidou mudanças na organização política e reconheceu direitos sociais e eleitorais. Em 1937, Vargas instaurou o Estado Novo, uma ditadura com concentração de poder e censura. O período também teve industrialização e legislação trabalhista. Para compreendê-lo, é preciso olhar tanto para as transformações sociais quanto para a perda de liberdades políticas.",
        "text_fr": "La révolution de 1930 porta Getúlio Vargas au pouvoir. En 1934, une nouvelle Constitution consolida des changements politiques et reconnut des droits sociaux et électoraux. En 1937, Vargas instaura l’Estado Novo, une dictature marquée par la concentration du pouvoir et la censure. La période connut aussi une industrialisation et une législation du travail. Il faut considérer à la fois ces transformations sociales et la perte des libertés politiques.",
    },
    {
        "slug": "democracia", "date": "1945–1964", "title_pt": "Experiência democrática", "title_fr": "Expérience démocratique", "icon": "Ⅲ",
        "text_pt": "O fim do Estado Novo, em 1945, abriu caminho para eleições e para a Constituição de 1946. Partidos, sindicatos e movimentos sociais disputaram projetos para o país. A urbanização avançou e Brasília foi inaugurada em 1960. Essa experiência democrática conviveu com desigualdades e tensões políticas. Em 1964, um golpe interrompeu o governo constitucional e iniciou uma ditadura militar.",
        "text_fr": "La fin de l’Estado Novo, en 1945, ouvrit la voie à des élections et à la Constitution de 1946. Partis, syndicats et mouvements sociaux défendirent des projets différents pour le pays. L’urbanisation progressa et Brasília fut inaugurée en 1960. Cette expérience démocratique coexistait avec des inégalités et des tensions politiques. En 1964, un coup d’État mit fin au gouvernement constitutionnel et ouvrit une dictature militaire.",
    },
    {
        "slug": "ditadura", "date": "1964–1985", "title_pt": "Ditadura militar", "title_fr": "Dictature militaire", "icon": "Ⅳ",
        "text_pt": "Durante a ditadura militar, presidentes não foram escolhidos pelo voto popular direto. Houve censura, perseguição política, prisões, tortura e desaparecimentos forçados. Ao mesmo tempo, movimentos estudantis, trabalhadores, artistas e muitos outros grupos resistiram e defenderam eleições e direitos. Lembrar esse período exige atenção às pessoas atingidas pela violência do Estado e às lutas pela volta da democracia.",
        "text_fr": "Pendant la dictature militaire, les présidents ne furent pas élus au suffrage populaire direct. Il y eut censure, persécutions politiques, emprisonnements, torture et disparitions forcées. En parallèle, étudiants, travailleurs, artistes et de nombreux autres groupes résistèrent et défendirent les élections et les droits. Se souvenir de cette période suppose de prêter attention aux victimes de la violence d’État et aux luttes pour le retour de la démocratie.",
    },
    {
        "slug": "redemocratizacao", "date": "1985–hoje", "title_pt": "Redemocratização e Constituição", "title_fr": "Retour à la démocratie et Constitution", "icon": "Ⅴ",
        "text_pt": "Em 1985 terminou o regime militar e começou a transição civil. A Constituição de 1988 ampliou direitos e estabeleceu bases para a democracia atual. Em 1989 ocorreu a primeira eleição presidencial direta desde 1960. A vida republicana continuou marcada por debates, crises e mobilização social. Estudar essa trajetória ajuda a perceber que instituições democráticas dependem de participação, memória e proteção constante dos direitos.",
        "text_fr": "En 1985, le régime militaire prit fin et une transition civile commença. La Constitution de 1988 élargit les droits et établit les bases de la démocratie actuelle. En 1989 eut lieu la première élection présidentielle directe depuis 1960. La vie républicaine continua d’être traversée par des débats, des crises et des mobilisations sociales. Étudier ce parcours rappelle que les institutions démocratiques dépendent de la participation, de la mémoire et de la protection des droits.",
    },
]


def guide_audio_text(section, item, lang):
    """Return only known, authored text for speech generation."""
    if section == "dados":
        record = next((entry for entry in INDICATORS if entry["slug"] == item), None)
        if record:
            value = record.get("value_" + lang, record["value"])
            year = record.get("year_" + lang, record["year"])
            return f'{record["label_" + lang]}. {value}. {year}. {record["text_" + lang]}'
    if section == "variedades":
        record = next((entry for entry in VARIETIES if entry["slug"] == item), None)
        if record:
            return f'{record["title_" + lang]}. {record["text_" + lang]}'
    if section == "historia":
        record = next((entry for entry in HISTORY if entry["slug"] == item), None)
        if record:
            return f'{record["date"]}. {record["title_" + lang]}. {record["text_" + lang]}'
    return None
