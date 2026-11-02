"""Conteúdo estruturado da trilha de gramática do Fala Brasil.

Os dados ficam fora do template para que a página continue simples de ampliar:
adicione uma conjugação ou exercício aqui, sem alterar a lógica do navegador.
"""

PRONOMES = ["eu", "você", "ele/ela", "nós", "eles/elas"]

TEMPOS = [
    {"id": "presente", "label_pt": "Presente", "label_fr": "Présent"},
    {"id": "preterito", "label_pt": "Pretérito perfeito", "label_fr": "Passé simple"},
    {"id": "imperfeito", "label_pt": "Pretérito imperfeito", "label_fr": "Imparfait"},
    {"id": "futuro", "label_pt": "Futuro", "label_fr": "Futur"},
]


def _v(infinitivo, traducao, nivel, tipo, exemplo, presente, preterito, imperfeito, futuro):
    return {
        "infinitivo": infinitivo,
        "traducao": traducao,
        "nivel": nivel,
        "tipo": tipo,
        "exemplo": exemplo,
        "conjugacoes": {
            "presente": presente,
            "preterito": preterito,
            "imperfeito": imperfeito,
            "futuro": futuro,
        },
    }


VERBOS = [
    _v("ser", "être", "A1", "irregular", "Eu sou brasileiro.", ["sou", "é", "é", "somos", "são"], ["fui", "foi", "foi", "fomos", "foram"], ["era", "era", "era", "éramos", "eram"], ["serei", "será", "será", "seremos", "serão"]),
    _v("estar", "être (état)", "A1", "irregular", "Nós estamos prontos.", ["estou", "está", "está", "estamos", "estão"], ["estive", "esteve", "esteve", "estivemos", "estiveram"], ["estava", "estava", "estava", "estávamos", "estavam"], ["estarei", "estará", "estará", "estaremos", "estarão"]),
    _v("falar", "parler", "A1", "regular", "Ela fala português.", ["falo", "fala", "fala", "falamos", "falam"], ["falei", "falou", "falou", "falamos", "falaram"], ["falava", "falava", "falava", "falávamos", "falavam"], ["falarei", "falará", "falará", "falaremos", "falarão"]),
    _v("comer", "manger", "A1", "regular", "Nós comemos cedo.", ["como", "come", "come", "comemos", "comem"], ["comi", "comeu", "comeu", "comemos", "comeram"], ["comia", "comia", "comia", "comíamos", "comiam"], ["comerei", "comerá", "comerá", "comeremos", "comerão"]),
    _v("fazer", "faire", "A2", "irregular", "O que você faz hoje?", ["faço", "faz", "faz", "fazemos", "fazem"], ["fiz", "fez", "fez", "fizemos", "fizeram"], ["fazia", "fazia", "fazia", "fazíamos", "faziam"], ["farei", "fará", "fará", "faremos", "farão"]),
    _v("ir", "aller", "A2", "irregular", "Amanhã eu vou estudar.", ["vou", "vai", "vai", "vamos", "vão"], ["fui", "foi", "foi", "fomos", "foram"], ["ia", "ia", "ia", "íamos", "iam"], ["irei", "irá", "irá", "iremos", "irão"]),
    _v("ter", "avoir", "A2", "irregular", "Eles têm uma ideia.", ["tenho", "tem", "tem", "temos", "têm"], ["tive", "teve", "teve", "tivemos", "tiveram"], ["tinha", "tinha", "tinha", "tínhamos", "tinham"], ["terei", "terá", "terá", "teremos", "terão"]),
    _v("abrir", "ouvrir", "A2", "irregular", "A loja abre às nove.", ["abro", "abre", "abre", "abrimos", "abrem"], ["abri", "abriu", "abriu", "abrimos", "abriram"], ["abria", "abria", "abria", "abríamos", "abriam"], ["abrirei", "abrirá", "abrirá", "abriremos", "abrirão"]),
    _v("poder", "pouvoir", "B1", "irregular", "Você pode repetir?", ["posso", "pode", "pode", "podemos", "podem"], ["pude", "pôde", "pôde", "pudemos", "puderam"], ["podia", "podia", "podia", "podíamos", "podiam"], ["poderei", "poderá", "poderá", "poderemos", "poderão"]),
    _v("vir", "venir", "B1", "irregular", "Nós viemos de longe.", ["venho", "vem", "vem", "viemos", "vêm"], ["vim", "veio", "veio", "viemos", "vieram"], ["vinha", "vinha", "vinha", "vínhamos", "vinham"], ["virei", "virá", "virá", "viremos", "virão"]),
    _v("dizer", "dire", "B2", "irregular", "Eu digo a verdade.", ["digo", "diz", "diz", "dizemos", "dizem"], ["disse", "disse", "disse", "dissemos", "disseram"], ["dizia", "dizia", "dizia", "dizíamos", "diziam"], ["direi", "dirá", "dirá", "diremos", "dirão"]),
    _v("saber", "savoir", "B2", "irregular", "Você sabe a resposta?", ["sei", "sabe", "sabe", "sabemos", "sabem"], ["soube", "soube", "soube", "soubemos", "souberam"], ["sabia", "sabia", "sabia", "sabíamos", "sabiam"], ["saberei", "saberá", "saberá", "saberemos", "saberão"]),
    _v("ver", "voir", "B2", "irregular", "Eu vejo o mar.", ["vejo", "vê", "vê", "vemos", "veem"], ["vi", "viu", "viu", "vimos", "viram"], ["via", "via", "via", "víamos", "viam"], ["verei", "verá", "verá", "veremos", "verão"]),
    _v("querer", "vouloir", "B2", "irregular", "Nós queremos aprender.", ["quero", "quer", "quer", "queremos", "querem"], ["quis", "quis", "quis", "quisemos", "quiseram"], ["queria", "queria", "queria", "queríamos", "queriam"], ["quererei", "quererá", "quererá", "quereremos", "quererão"]),
]

TRILHA = [
    {"id": "A1", "title_pt": "Primeiros passos", "title_fr": "Premiers pas", "intro_pt": "Frases simples, gênero, artigos, pronomes e o presente do indicativo.", "intro_fr": "Phrases simples, genre, articles, pronoms et présent de l’indicatif.", "topics_pt": ["ser × estar", "artigos e gênero", "presente", "negação"], "topics_fr": ["ser × estar", "articles et genre", "présent", "négation"]},
    {"id": "A2", "title_pt": "Conversas do dia a dia", "title_fr": "Conversations du quotidien", "intro_pt": "Conte o que aconteceu, faça pedidos e fale de planos próximos.", "intro_fr": "Racontez ce qui s’est passé, faites des demandes et parlez de projets.", "topics_pt": ["pretérito perfeito", "imperfeito", "perguntas", "pronomes"], "topics_fr": ["passé composé", "imparfait", "questions", "pronoms"]},
    {"id": "B1", "title_pt": "Mais precisão", "title_fr": "Plus de précision", "intro_pt": "Ligue ideias, dê conselhos e escolha entre modos e tempos verbais.", "intro_fr": "Reliez les idées, donnez des conseils et choisissez les modes et les temps.", "topics_pt": ["futuro", "condicional", "conectores", "subjuntivo"], "topics_fr": ["futur", "conditionnel", "connecteurs", "subjonctif"]},
    {"id": "B2", "title_pt": "Nuance e fluência", "title_fr": "Nuance et aisance", "intro_pt": "Entenda hipóteses, registros, voz passiva e escolhas mais naturais.", "intro_fr": "Comprenez les hypothèses, les registres, la voix passive et les usages naturels.", "topics_pt": ["hipóteses", "voz passiva", "discurso indireto", "colocações"], "topics_fr": ["hypothèses", "voix passive", "discours indirect", "collocations"]},
]

EXERCICIOS = [
    {"nivel": "A1", "tema": "Presente", "frase": "Nós ___ português todos os dias.", "opcoes": ["falamos", "fala", "falam"], "resposta": "falamos", "explicacao": "Com nós, a forma de falar no presente é falamos."},
    {"nivel": "A1", "tema": "Ser ou estar", "frase": "Hoje eu ___ muito cansado.", "opcoes": ["sou", "estou", "é"], "resposta": "estou", "explicacao": "Use estar para um estado momentâneo: estou cansado."},
    {"nivel": "A2", "tema": "Pretérito", "frase": "Ontem elas ___ ao cinema.", "opcoes": ["vão", "iam", "foram"], "resposta": "foram", "explicacao": "O pretérito perfeito de ir com elas é foram."},
    {"nivel": "A2", "tema": "Imperfeito", "frase": "Quando era criança, eu ___ muito.", "opcoes": ["brinquei", "brincava", "brincarei"], "resposta": "brincava", "explicacao": "O imperfeito descreve um hábito no passado: brincava."},
    {"nivel": "B1", "tema": "Futuro", "frase": "Amanhã nós ___ cedo.", "opcoes": ["saímos", "sairemos", "saíamos"], "resposta": "sairemos", "explicacao": "Para um plano futuro, use sairemos."},
    {"nivel": "B2", "tema": "Hipótese", "frase": "Se eu pudesse, ___ mais tempo.", "opcoes": ["viajaria", "viajei", "viajo"], "resposta": "viajaria", "explicacao": "A consequência de uma hipótese usa o condicional: viajaria."},
    {"nivel": "A1", "tema": "Artigos", "tipo": "escrever", "frase": "Complete: ___ casa é bonita. (artigo definido feminino)", "resposta": "A", "explicacao": "Casa é feminino singular; o artigo definido é a."},
    {"nivel": "A1", "tema": "Ordem da frase", "tipo": "ordenar", "frase": "Monte a frase: Je parle portugais.", "palavras": ["português", "Eu", "falo"], "resposta": "Eu falo português", "explicacao": "A ordem mais comum é sujeito + verbo + complemento."},
    {"nivel": "A1", "tema": "Negação", "tipo": "escrever", "frase": "Complete: Eu ___ gosto de café.", "resposta": "não", "explicacao": "Não vem antes do verbo para negar a frase."},
    {"nivel": "A2", "tema": "Pretérito", "tipo": "escrever", "frase": "Ontem eu ___ ao mercado. (ir)", "resposta": "fui", "explicacao": "No pretérito perfeito, eu fui indica uma ação concluída."},
    {"nivel": "A2", "tema": "Tradução", "tipo": "ordenar", "frase": "Traduza: Nous avons mangé tôt.", "palavras": ["cedo", "Nós", "comemos"], "resposta": "Nós comemos cedo", "explicacao": "Comemos pode ser presente ou pretérito; o contexto define o tempo."},
    {"nivel": "A2", "tema": "Perguntas", "frase": "___ você mora?", "opcoes": ["Quando", "Onde", "Quem"], "resposta": "Onde", "explicacao": "Onde pergunta por um lugar."},
    {"nivel": "B1", "tema": "Conectores", "frase": "Estudei bastante, ___ não passei na prova.", "opcoes": ["porque", "mas", "portanto"], "resposta": "mas", "explicacao": "Mas introduz uma ideia contrária à expectativa."},
    {"nivel": "B1", "tema": "Subjuntivo", "tipo": "escrever", "frase": "Espero que você ___ amanhã. (vir)", "resposta": "venha", "explicacao": "Depois de espero que, use o presente do subjuntivo: venha."},
    {"nivel": "B1", "tema": "Ordem da frase", "tipo": "ordenar", "frase": "Monte uma condição real.", "palavras": ["chover", "Se", "ficaremos", "em casa"], "resposta": "Se chover ficaremos em casa", "explicacao": "Se + futuro do subjuntivo apresenta a condição; ficaremos indica o resultado."},
    {"nivel": "B2", "tema": "Concessão", "frase": "___ estivesse cansada, ela continuou.", "opcoes": ["Porque", "Embora", "Portanto"], "resposta": "Embora", "explicacao": "Embora expressa concessão e pede subjuntivo."},
    {"nivel": "B2", "tema": "Voz passiva", "tipo": "ordenar", "frase": "Reorganize na voz passiva.", "palavras": ["foi", "O livro", "lido", "por Ana"], "resposta": "O livro foi lido por Ana", "explicacao": "A voz passiva usa ser + particípio: foi lido."},
    {"nivel": "B2", "tema": "Hipótese", "tipo": "escrever", "frase": "Se eles soubessem, ___ a verdade. (dizer, condicional)", "resposta": "diriam", "explicacao": "Na hipótese, a consequência usa o futuro do pretérito: diriam."},
]

FRASES = [
    {"pt": "Eu gostaria de reservar uma mesa para duas pessoas.", "fr": "J’aimerais réserver une table pour deux personnes.", "nivel": "A2", "foco": "pedido educado"},
    {"pt": "Se chover, vamos ficar em casa.", "fr": "S’il pleut, nous allons rester à la maison.", "nivel": "B1", "foco": "condição"},
    {"pt": "Embora seja difícil, vale a pena continuar.", "fr": "Même si c’est difficile, cela vaut la peine de continuer.", "nivel": "B2", "foco": "concessão"},
    {"pt": "Você pode falar mais devagar, por favor?", "fr": "Pouvez-vous parler plus lentement, s’il vous plaît ?", "nivel": "A1", "foco": "sala de aula"},
]

# Minilições de gramática para consulta antes dos desafios.
TOPICOS = [
    {"nivel": "A1", "titulo_pt": "Artigos e gênero", "titulo_fr": "Articles et genre", "regra_pt": "O artigo concorda com o substantivo em gênero e número: o/a, os/as, um/uma.", "regra_fr": "L’article s’accorde avec le nom en genre et en nombre : o/a, os/as, um/uma.", "exemplo": "A casa é bonita. Os livros são novos."},
    {"nivel": "A1", "titulo_pt": "Pronomes pessoais", "titulo_fr": "Pronoms personnels", "regra_pt": "Eu, você, ele/ela, nós e eles/elas indicam quem pratica a ação. Você usa o verbo na terceira pessoa.", "regra_fr": "Eu, você, ele/ela, nós et eles/elas indiquent le sujet. Você prend la troisième personne du verbe.", "exemplo": "Eu estudo. Você estuda. Nós estudamos."},
    {"nivel": "A1", "titulo_pt": "Negação e ordem", "titulo_fr": "Négation et ordre des mots", "regra_pt": "Em geral, a frase segue sujeito + verbo + complemento. Para negar, coloque não antes do verbo.", "regra_fr": "La phrase suit souvent sujet + verbe + complément. Pour nier, placez não avant le verbe.", "exemplo": "Eu não bebo café."},
    {"nivel": "A2", "titulo_pt": "Contrações com preposições", "titulo_fr": "Contractions des prépositions", "regra_pt": "De + o forma do; em + a forma na; a + a forma à. A contração faz parte da frase cotidiana.", "regra_fr": "De + o donne do ; em + a donne na ; a + a donne à. Ces contractions sont courantes.", "exemplo": "Moro na cidade. Vou à escola."},
    {"nivel": "A2", "titulo_pt": "Perguntas", "titulo_fr": "Questions", "regra_pt": "Onde pergunta por lugar; quando, por tempo; por que, por motivo. A ordem costuma ser palavra interrogativa + frase.", "regra_fr": "Onde interroge le lieu ; quando, le temps ; por que, la raison. Le mot interrogatif ouvre souvent la question.", "exemplo": "Onde você mora? Por que saiu cedo?"},
    {"nivel": "A2", "titulo_pt": "Pronomes possessivos", "titulo_fr": "Pronoms possessifs", "regra_pt": "Meu/minha e seu/sua concordam com o objeto possuído, não com a pessoa que possui.", "regra_fr": "Meu/minha et seu/sua s’accordent avec l’objet possédé, pas avec la personne qui le possède.", "exemplo": "Minha casa. Meus amigos."},
    {"nivel": "B1", "titulo_pt": "Conectores", "titulo_fr": "Connecteurs", "regra_pt": "Porque apresenta causa; mas, contraste; portanto, consequência. Escolha conforme a relação entre as ideias.", "regra_fr": "Porque indique la cause ; mas, l’opposition ; portanto, la conséquence.", "exemplo": "Choveu, portanto fiquei em casa."},
    {"nivel": "B1", "titulo_pt": "Comparações", "titulo_fr": "Comparaisons", "regra_pt": "Use mais... do que para superioridade, menos... do que para inferioridade e tão... quanto para igualdade.", "regra_fr": "Utilisez mais... do que, menos... do que et tão... quanto pour comparer.", "exemplo": "Ela é tão alta quanto o irmão."},
    {"nivel": "B1", "titulo_pt": "Condição", "titulo_fr": "Condition", "regra_pt": "Se + futuro do subjuntivo indica uma condição possível no futuro; a consequência pode vir no futuro.", "regra_fr": "Se + futur du subjonctif exprime une condition future possible ; la conséquence peut être au futur.", "exemplo": "Se chover, ficaremos em casa."},
    {"nivel": "B2", "titulo_pt": "Concessão", "titulo_fr": "Concession", "regra_pt": "Embora introduz um fato que não impede o resultado e normalmente pede o subjuntivo.", "regra_fr": "Embora introduit un fait qui n’empêche pas le résultat et appelle normalement le subjonctif.", "exemplo": "Embora esteja cansada, ela continua."},
    {"nivel": "B2", "titulo_pt": "Voz passiva", "titulo_fr": "Voix passive", "regra_pt": "Na voz passiva, o objeto vira sujeito. Use ser + particípio, que concorda com esse sujeito.", "regra_fr": "À la voix passive, l’objet devient sujet. Utilisez ser + participe accordé avec ce sujet.", "exemplo": "As cartas foram escritas por Ana."},
    {"nivel": "B2", "titulo_pt": "Discurso indireto", "titulo_fr": "Discours indirect", "regra_pt": "Ao relatar a fala de outra pessoa, ajuste pronomes e referências de tempo ao novo contexto.", "regra_fr": "Pour rapporter les propos de quelqu’un, adaptez les pronoms et les repères temporels au nouveau contexte.", "exemplo": "Ela disse: «Estou aqui.» → Ela disse que estava lá."},
]

EXERCICIOS.extend([
    {"nivel": "A1", "tema": "Gênero", "frase": "Escolha a concordância: ___ livro é interessante.", "opcoes": ["A", "O", "As"], "resposta": "O", "explicacao": "Livro é masculino singular: o livro."},
    {"nivel": "A1", "tema": "Plural", "frase": "Escolha: ___ casas são bonitas.", "opcoes": ["As", "A", "Os"], "resposta": "As", "explicacao": "Casas é feminino plural: as casas."},
    {"nivel": "A1", "tema": "Pronomes", "frase": "___ estudamos português juntos.", "opcoes": ["Eu", "Você", "Nós"], "resposta": "Nós", "explicacao": "Estudamos corresponde a nós."},
    {"nivel": "A1", "tema": "Adjetivos", "tipo": "escrever", "frase": "Complete: uma menina ___. (alto)", "resposta": "alta", "explicacao": "O adjetivo concorda com menina, feminino singular."},
    {"nivel": "A2", "tema": "Preposições", "frase": "Eu moro ___ cidade.", "opcoes": ["na", "da", "à"], "resposta": "na", "explicacao": "Morar em + a cidade forma na cidade."},
    {"nivel": "A2", "tema": "Contrações", "tipo": "escrever", "frase": "O livro é ___ professor. (de + o)", "resposta": "do", "explicacao": "De + o se contrai em do."},
    {"nivel": "A2", "tema": "Possessivos", "frase": "Ela trouxe ___ bolsa.", "opcoes": ["seu", "sua", "seus"], "resposta": "sua", "explicacao": "Bolsa é feminino singular; por isso, sua bolsa."},
    {"nivel": "A2", "tema": "Perguntas", "frase": "___ você chegou? Ontem.", "opcoes": ["Onde", "Quando", "Quem"], "resposta": "Quando", "explicacao": "Quando pede uma resposta de tempo."},
    {"nivel": "B1", "tema": "Conectores", "frase": "Não dormi bem; ___, estou cansado.", "opcoes": ["portanto", "mas", "embora"], "resposta": "portanto", "explicacao": "Portanto introduz uma consequência."},
    {"nivel": "B1", "tema": "Comparações", "frase": "Este caminho é ___ longo do que aquele.", "opcoes": ["tão", "mais", "quanto"], "resposta": "mais", "explicacao": "Mais... do que expressa superioridade."},
    {"nivel": "B1", "tema": "Comparações", "tipo": "escrever", "frase": "Ela é tão rápida ___ o irmão.", "resposta": "quanto", "explicacao": "Tão... quanto expressa igualdade."},
    {"nivel": "B1", "tema": "Conectores", "frase": "Fiquei em casa ___ estava doente.", "opcoes": ["portanto", "porque", "mas"], "resposta": "porque", "explicacao": "Porque apresenta a causa."},
    {"nivel": "B2", "tema": "Voz passiva", "frase": "As cartas foram ___ por Ana.", "opcoes": ["escrito", "escrita", "escritas"], "resposta": "escritas", "explicacao": "O particípio concorda com as cartas, feminino plural."},
    {"nivel": "B2", "tema": "Concessão", "frase": "___ chova, faremos a viagem.", "opcoes": ["Embora", "Portanto", "Porque"], "resposta": "Embora", "explicacao": "Embora introduz uma concessão; chova está no subjuntivo."},
    {"nivel": "B2", "tema": "Discurso indireto", "frase": "Ela disse: «Estou cansada.» → Ela disse que ___ cansada.", "opcoes": ["estava", "estarei", "estive"], "resposta": "estava", "explicacao": "Ao relatar uma fala passada, estou pode passar a estava."},
    {"nivel": "B2", "tema": "Discurso indireto", "tipo": "escrever", "frase": "Ele disse: «Moro aqui.» → Ele disse que morava ___.", "resposta": "lá", "explicacao": "Ao mudar o ponto de referência, aqui pode passar a lá."},
])

# As páginas completas seguem a mesma ordem dos cartões de consulta.
from data.gramatica_licoes import LESSONS
for topic, slug in zip(TOPICOS, LESSONS):
    topic["slug"] = slug
