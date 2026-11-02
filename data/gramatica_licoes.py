"""Guias completos e exercícios por assunto da gramática brasileira."""

# Cada lição tem três seções, exemplos comentados e questões próprias.
LESSONS = {
    "artigos-genero": {
        "title_pt": "Artigos e gênero", "title_fr": "Articles et genre", "level": "A1",
        "intro_pt": "Aprenda a escolher o artigo e a fazer substantivos e adjetivos concordarem.", "intro_fr": "Choisissez l’article et accordez noms et adjectifs.",
        "sections": [
            ("O que é gênero?", "Em português, os substantivos são masculinos ou femininos. Livro é masculino; casa é feminino. O gênero é uma propriedade da palavra e nem sempre se deduz pelo final: o dia, a mão.", "Le nom possède un genre grammatical. Livro est masculin et casa est féminin. La terminaison ne suffit pas toujours : o dia, a mão."),
            ("Artigos definidos e indefinidos", "Use o, a, os, as quando a referência é identificável; um, uma, uns, umas para apresentar algo. O artigo concorda com o substantivo em gênero e número.", "Utilisez o, a, os, as pour une référence identifiable et um, uma, uns, umas pour introduire un élément. L’article s’accorde en genre et en nombre."),
            ("Concordância", "O adjetivo também costuma concordar: um livro novo, duas casas novas. Observe primeiro o substantivo; depois escolha as formas das palavras que o acompanham.", "L’adjectif s’accorde aussi : um livro novo, duas casas novas. Repérez d’abord le nom, puis accordez les mots qui l’accompagnent."),
        ], "examples": [("O livro novo está na mesa.", "Livro é masculino singular: o e novo."), ("As casas antigas são bonitas.", "Casas é feminino plural: as, antigas e bonitas.")],
        "quiz": [("Qual combinação está correta?", ["a livro", "o livro", "as livro"], 1), ("Complete: ___ meninas são altas.", ["Os", "A", "As"], 2), ("Qual é o feminino de novo?", ["nova", "novos", "novas"], 0)],
    },
    "pronomes-pessoais": {
        "title_pt": "Pronomes pessoais", "title_fr": "Pronoms personnels", "level": "A1",
        "intro_pt": "Identifique quem fala, com quem se fala e de quem se fala.", "intro_fr": "Identifiez qui parle, à qui l’on parle et de qui l’on parle.",
        "sections": [
            ("Quem pratica a ação", "Eu indica quem fala; você indica a pessoa a quem se fala; ele e ela indicam outra pessoa. Nós e eles/elas são formas plurais. No Brasil, você é muito frequente na conversa cotidiana.", "Eu désigne celui qui parle ; você, l’interlocuteur ; ele et ela, une autre personne. Nós et eles/elas sont des pluriels. Au Brésil, você est fréquent à l’oral."),
            ("Pronome e verbo", "A forma do verbo muda conforme o sujeito: eu falo, você fala, nós falamos. Você e ele/ela usam a mesma forma verbal, embora se refiram a pessoas diferentes.", "La forme verbale change avec le sujet : eu falo, você fala, nós falamos. Você et ele/ela prennent la même forme verbale."),
            ("Sujeito omitido", "É possível omitir o pronome quando a forma verbal ou o contexto esclarece quem age: Falamos português. Use o pronome para dar ênfase ou evitar ambiguidade.", "On peut omettre le pronom si le verbe ou le contexte suffit : Falamos português. Gardez-le pour insister ou éviter une ambiguïté."),
        ], "examples": [("Eu estudo; você estuda.", "Você pede a forma da terceira pessoa."), ("Nós moramos em Recife.", "Nós indica um grupo que inclui quem fala.")],
        "quiz": [("Qual pronome combina com estudamos?", ["eu", "nós", "você"], 1), ("Complete: Você ___ português.", ["falo", "fala", "falamos"], 1), ("Qual pronome indica quem fala?", ["eu", "ela", "eles"], 0)],
    },
    "negacao-ordem": {
        "title_pt": "Negação e ordem da frase", "title_fr": "Négation et ordre des mots", "level": "A1",
        "intro_pt": "Forme frases claras e transforme uma afirmação em negação.", "intro_fr": "Formez des phrases claires et transformez une affirmation en négation.",
        "sections": [
            ("Ordem básica", "A ordem mais comum em frases afirmativas é sujeito + verbo + complemento: Ana lê livros. Essa estrutura ajuda a entender quem age e o que acontece.", "L’ordre courant est sujet + verbe + complément : Ana lê livros. Il indique qui agit et ce qui se passe."),
            ("Onde entra não", "Coloque não antes do verbo: Ana não lê livros. O complemento permanece depois do verbo na maioria das frases simples.", "Placez não avant le verbe : Ana não lê livros. Le complément reste généralement après le verbe."),
            ("Ênfase e contexto", "Outras ordens são possíveis para destacar informações, mas comece pela estrutura básica. Em respostas curtas, não pode aparecer sozinho: Você quer café? Não.", "D’autres ordres servent à mettre un élément en relief. Pour commencer, gardez l’ordre de base. Dans une réponse brève, não peut être employé seul."),
        ], "examples": [("Eu não bebo café.", "Não vem imediatamente antes de bebo."), ("A turma aprende português.", "Sujeito, verbo e complemento aparecem nessa ordem.")],
        "quiz": [("Qual frase está na ordem básica?", ["Português aprende Ana.", "Ana aprende português.", "Aprende Ana português."], 1), ("Onde fica não?", ["Antes do verbo", "Depois do complemento", "Antes do sujeito"], 0), ("Qual frase é negativa?", ["Eu gosto de chá.", "Eu não gosto de chá.", "Gosto eu de chá."], 1)],
    },
    "preposicoes-contracoes": {
        "title_pt": "Preposições e contrações", "title_fr": "Prépositions et contractions", "level": "A2",
        "intro_pt": "Entenda como de, em e a se unem aos artigos.", "intro_fr": "Comprenez comment de, em et a se combinent avec les articles.",
        "sections": [
            ("Relações entre palavras", "Preposições ligam termos e indicam origem, lugar, destino e outras relações. De pode indicar origem ou posse; em, localização; a, destino em certas construções.", "Les prépositions relient les mots et expriment l’origine, le lieu ou la destination. De marque souvent l’origine ou la possession ; em, le lieu."),
            ("Contrações frequentes", "De + o = do; de + a = da; em + o = no; em + a = na. Com artigos plurais, surgem dos, das, nos e nas.", "De + o = do ; de + a = da ; em + o = no ; em + a = na. Au pluriel : dos, das, nos, nas."),
            ("A crase em contexto", "Quando a preposição a encontra o artigo feminino a, escreve-se à: vou à escola. Não há crase antes de um artigo masculino: vou ao mercado.", "Quand la préposition a rencontre l’article féminin a, on écrit à : vou à escola. Au masculin : vou ao mercado."),
        ], "examples": [("Moro na cidade.", "Em + a forma na."), ("Vou à escola; volto da escola.", "A + a forma à; de + a forma da.")],
        "quiz": [("Complete: Moro ___ cidade.", ["da", "na", "à"], 1), ("De + o forma...", ["do", "no", "ao"], 0), ("Complete: Vou ___ escola.", ["à", "na", "da"], 0)],
    },
    "perguntas": {
        "title_pt": "Perguntas", "title_fr": "Questions", "level": "A2",
        "intro_pt": "Pergunte por pessoas, lugares, tempo e motivos.", "intro_fr": "Posez des questions sur les personnes, les lieux, le temps et les raisons.",
        "sections": [
            ("Palavras interrogativas", "Quem pergunta por pessoas; onde, por lugares; quando, por tempo; como, por maneira; por que, por motivo. Escolha a palavra conforme o tipo de resposta esperado.", "Quem interroge les personnes ; onde, les lieux ; quando, le temps ; como, la manière ; por que, la raison."),
            ("Pergunta completa", "A palavra interrogativa geralmente aparece no começo: Onde você mora? Em perguntas de sim ou não, a entonação e o ponto de interrogação bastam: Você mora aqui?", "Le mot interrogatif apparaît souvent au début : Onde você mora ? Pour une réponse oui/non, l’intonation et le point d’interrogation suffisent."),
            ("Por que e porque", "Por que aparece em perguntas de motivo; porque introduz a explicação na resposta: Por que saiu? Porque estava tarde.", "Por que s’emploie dans la question de raison ; porque introduit la réponse : Por que saiu ? Porque estava tarde."),
        ], "examples": [("Onde você mora?", "A resposta esperada é um lugar."), ("Por que você saiu?", "A resposta esperada é um motivo.")],
        "quiz": [("Qual palavra pede um lugar?", ["Quando", "Onde", "Quem"], 1), ("Qual palavra pede uma pessoa?", ["Quem", "Como", "Onde"], 0), ("Complete: ___ você chegou? Ontem.", ["Quando", "Onde", "Por que"], 0)],
    },
    "possessivos": {
        "title_pt": "Pronomes possessivos", "title_fr": "Pronoms possessifs", "level": "A2",
        "intro_pt": "Diga a quem algo pertence e faça a concordância correta.", "intro_fr": "Exprimez la possession et accordez correctement.",
        "sections": [
            ("Pessoa e objeto", "Meu/minha indica posse ligada a eu; nosso/nossa, a nós. Seu/sua pode se referir a você, ele ou ela: use o contexto para identificar a pessoa.", "Meu/minha renvoie à eu ; nosso/nossa, à nós. Seu/sua peut renvoyer à você, ele ou ela : le contexte aide à préciser."),
            ("Concordância", "A forma concorda com o objeto possuído: meu livro, minha casa, meus livros, minhas casas. O gênero de quem possui não muda essa escolha.", "La forme s’accorde avec l’objet possédé : meu livro, minha casa, meus livros, minhas casas. Le genre du possesseur ne change rien."),
            ("Evitar ambiguidade", "Quando seu/sua não deixa claro quem possui, diga dele ou dela: a casa dela. Em muitas regiões do Brasil, essa forma é mais clara na conversa.", "Si seu/sua est ambigu, utilisez dele ou dela : a casa dela. À l’oral brésilien, cette forme est souvent plus claire."),
        ], "examples": [("Minha irmã e meus irmãos.", "O possessivo concorda com o substantivo seguinte."), ("A bicicleta dela é azul.", "Dela identifica a pessoa que possui.")],
        "quiz": [("Complete: ___ casa é grande. (eu)", ["Meu", "Minha", "Meus"], 1), ("Complete: ___ amigos chegaram. (eu)", ["Meus", "Minhas", "Meu"], 0), ("Qual forma evita ambiguidade?", ["a casa seu", "a casa dela", "a casa eu"], 1)],
    },
    "conectores": {
        "title_pt": "Conectores", "title_fr": "Connecteurs", "level": "B1",
        "intro_pt": "Ligue ideias de causa, contraste e consequência.", "intro_fr": "Reliez les idées de cause, d’opposition et de conséquence.",
        "sections": [
            ("Causa", "Porque apresenta o motivo de uma ação: Fiquei em casa porque choveu. A segunda parte explica a primeira.", "Porque indique la raison : Fiquei em casa porque choveu. La seconde proposition explique la première."),
            ("Contraste", "Mas apresenta uma ideia oposta à expectativa: Estudei, mas errei. O contraste não apaga o primeiro fato.", "Mas introduit un contraste : Estudei, mas errei. La seconde idée diffère de ce que l’on attendait."),
            ("Consequência", "Portanto marca uma conclusão ou resultado: Choveu; portanto, fiquei em casa. Observe a pontuação quando o conector inicia a segunda oração.", "Portanto marque une conclusion : Choveu ; portanto, fiquei em casa. Observez la ponctuation."),
        ], "examples": [("Saí porque precisava trabalhar.", "Porque apresenta a causa."), ("Estava frio; portanto, levei um casaco.", "Portanto apresenta a consequência.")],
        "quiz": [("Qual conector apresenta causa?", ["mas", "porque", "portanto"], 1), ("Complete: Choveu; ___, fiquei em casa.", ["portanto", "mas", "porque"], 0), ("Qual conector expressa contraste?", ["porque", "portanto", "mas"], 2)],
    },
    "comparacoes": {
        "title_pt": "Comparações", "title_fr": "Comparaisons", "level": "B1",
        "intro_pt": "Compare pessoas e coisas com mais, menos e tão.", "intro_fr": "Comparez personnes et objets avec mais, menos et tão.",
        "sections": [
            ("Superioridade", "Use mais + adjetivo + do que: Este livro é mais longo do que aquele. A comparação pode envolver quantidade ou qualidade.", "Utilisez mais + adjectif + do que : Este livro é mais longo do que aquele."),
            ("Inferioridade", "Use menos + adjetivo + do que: Esta rua é menos movimentada do que a outra. O adjetivo ainda concorda com o substantivo.", "Utilisez menos + adjectif + do que : Esta rua é menos movimentada do que a outra."),
            ("Igualdade", "Use tão + adjetivo + quanto: Ana é tão alta quanto Bia. Para quantidade, use tanto/tanta/tantos/tantas + substantivo + quanto.", "Utilisez tão + adjectif + quanto : Ana é tão alta quanto Bia. Pour une quantité, utilisez tanto/tanta/tantos/tantas."),
        ], "examples": [("Ela é tão rápida quanto ele.", "Tão... quanto indica igualdade."), ("Este caminho é menos longo do que aquele.", "Menos... do que indica inferioridade.")],
        "quiz": [("Complete: tão alto ___ ele.", ["do que", "quanto", "porque"], 1), ("Qual palavra indica superioridade?", ["mais", "menos", "tão"], 0), ("Complete: menos caro ___ o outro.", ["quanto", "do que", "mas"], 1)],
    },
    "condicao": {
        "title_pt": "Condições", "title_fr": "Conditions", "level": "B1",
        "intro_pt": "Fale sobre possibilidades reais e seus resultados.", "intro_fr": "Parlez des possibilités réelles et de leurs conséquences.",
        "sections": [
            ("A palavra se", "Se introduz uma condição: Se chover, ficaremos em casa. A segunda oração informa o que acontece caso a condição se realize.", "Se introduit une condition : Se chover, ficaremos em casa. La seconde proposition indique la conséquence."),
            ("Futuro do subjuntivo", "Depois de se, uma condição futura costuma usar o futuro do subjuntivo: se eu tiver, se ela vier, se nós pudermos. Alguns verbos têm formas irregulares.", "Après se, une condition future prend souvent le futur du subjonctif : se eu tiver, se ela vier, se nós pudermos."),
            ("Resultado", "A consequência pode usar o futuro ou uma construção com ir + infinitivo: Se houver tempo, visitaremos o museu; Se houver tempo, vamos visitar o museu.", "La conséquence peut être au futur ou employer ir + infinitif : Se houver tempo, visitaremos o museu."),
        ], "examples": [("Se você vier, vamos conversar.", "Vier é o futuro do subjuntivo de vir."), ("Se chover, ficaremos em casa.", "A condição vem antes do resultado.")],
        "quiz": [("Qual palavra introduz uma condição?", ["mas", "se", "portanto"], 1), ("Complete: Se ela ___, conversaremos.", ["vem", "veio", "vier"], 2), ("Qual frase apresenta condição futura?", ["Se chover, sairemos depois.", "Choveu ontem.", "Embora chova, saio."], 0)],
    },
    "concessao": {
        "title_pt": "Concessão", "title_fr": "Concession", "level": "B2",
        "intro_pt": "Mostre que um fato não impediu outro resultado.", "intro_fr": "Montrez qu’un fait n’a pas empêché un résultat.",
        "sections": [
            ("Embora", "Embora introduz uma dificuldade ou fato contrário à expectativa: Embora esteja cansada, ela trabalha. O trabalho acontece apesar do cansaço.", "Embora présente un fait contraire à l’attente : Embora esteja cansada, ela trabalha. Le travail a lieu malgré la fatigue."),
            ("Modo verbal", "Depois de embora, use normalmente o subjuntivo: embora seja, embora tenha, embora estivesse. A forma varia conforme o tempo da situação.", "Après embora, utilisez normalement le subjonctif : embora seja, embora tenha, embora estivesse."),
            ("Apesar de", "Apesar de também expressa concessão e costuma vir antes de substantivo ou infinitivo: Apesar da chuva, saímos; Apesar de chover, saímos.", "Apesar de exprime aussi la concession et précède souvent un nom ou un infinitif : Apesar da chuva, saímos."),
        ], "examples": [("Embora esteja frio, vamos sair.", "O frio não impede a saída."), ("Apesar da chuva, fomos ao parque.", "Apesar de vem antes de um substantivo.")],
        "quiz": [("Qual palavra expressa concessão?", ["embora", "portanto", "porque"], 0), ("Complete: Embora ___ difícil, tentaremos.", ["é", "seja", "será"], 1), ("Qual frase é concessiva?", ["Choveu, portanto saí.", "Embora chovesse, saí.", "Saí porque choveu."], 1)],
    },
    "voz-passiva": {
        "title_pt": "Voz passiva", "title_fr": "Voix passive", "level": "B2",
        "intro_pt": "Mude o foco de quem age para quem recebe a ação.", "intro_fr": "Déplacez l’attention de l’agent vers ce qui subit l’action.",
        "sections": [
            ("Ativa e passiva", "Na voz ativa, Ana escreveu as cartas. Na passiva, As cartas foram escritas por Ana. O objeto da frase ativa passa a ser o sujeito da frase passiva.", "À l’actif : Ana escreveu as cartas. Au passif : As cartas foram escritas por Ana. L’objet devient sujet."),
            ("Estrutura", "A passiva analítica usa ser + particípio. O tempo de ser indica quando ocorreu a ação: é escrito, foi escrito, será escrito.", "La voix passive analytique emploie ser + participe. Le temps de ser situe l’action : é escrito, foi escrito, será escrito."),
            ("Concordância e agente", "O particípio concorda com o novo sujeito: carta escrita, cartas escritas. O agente pode ser introduzido por por, mas pode ser omitido quando não interessa.", "Le participe s’accorde avec le nouveau sujet : carta escrita, cartas escritas. L’agent, introduit par por, peut être omis."),
        ], "examples": [("O relatório foi publicado ontem.", "O agente não precisa aparecer."), ("As cartas foram escritas por Ana.", "Escritas concorda com cartas.")],
        "quiz": [("Qual estrutura forma a passiva analítica?", ["ser + particípio", "ter + infinitivo", "estar + gerúndio"], 0), ("Complete: As cartas foram ___.", ["escrito", "escritas", "escrita"], 1), ("Qual é o sujeito em As cartas foram escritas?", ["cartas", "foram", "escritas"], 0)],
    },
    "discurso-indireto": {
        "title_pt": "Discurso indireto", "title_fr": "Discours indirect", "level": "B2",
        "intro_pt": "Relate o que alguém disse, ajustando tempo, pessoa e lugar.", "intro_fr": "Rapportez les paroles d’autrui en adaptant temps, personne et lieu.",
        "sections": [
            ("Da citação ao relato", "Na fala direta, reproduzimos as palavras: Ela disse: «Estou cansada.» No relato, podemos dizer: Ela disse que estava cansada.", "Au discours direct, on cite les mots : Ela disse: «Estou cansada.» Au discours indirect : Ela disse que estava cansada."),
            ("Mudanças de tempo", "Quando o verbo de dizer está no passado, uma situação simultânea pode passar do presente para o imperfeito: moro → morava, estou → estava. O contexto determina a mudança.", "Si le verbe introducteur est au passé, une situation simultanée peut passer du présent à l’imparfait : moro → morava."),
            ("Pessoa e lugar", "Ajuste pronomes e referências espaciais: Eu moro aqui, dito por Ana, pode virar Ana disse que morava lá. Aqui e lá dependem do lugar de quem relata.", "Adaptez pronoms et repères spatiaux : Eu moro aqui peut devenir Ana disse que morava lá, selon le lieu du narrateur."),
        ], "examples": [("«Estou aqui.» → Ela disse que estava lá.", "Tempo verbal e lugar mudam com a perspectiva."), ("«Moro no Rio.» → Ele disse que morava no Rio.", "Moro passa a morava no relato passado.")],
        "quiz": [("Complete: Ela disse que ___ cansada.", ["estava", "estou", "estarei"], 0), ("No relato passado, moro pode virar...", ["morava", "morarei", "morei"], 0), ("Qual palavra pode substituir aqui em outro lugar?", ["lá", "ontem", "porque"], 0)],
    },
}


def quiz_for_lesson(lesson):
    """Adapt simple authoring tuples to the shared bilingual quiz component."""
    return [
        {
            "pergunta_pt": question,
            "pergunta_fr": question,
            "opcoes_pt": options,
            "opcoes_fr": options,
            "resposta": answer,
        }
        for question, options, answer in lesson["quiz"]
    ]
