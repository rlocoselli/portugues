"""Exames formativos de português por nível, com leitura e feedback."""


def question(section, prompt, options, answer, explanation):
    return {"section": section, "prompt": prompt, "options": options, "answer": answer, "explanation": explanation}


EXAMS = {
    "A1": {
        "title_pt": "Primeiros passos", "title_fr": "Premiers pas",
        "intro_pt": "Compreenda avisos curtos e use frases simples sobre o cotidiano.",
        "intro_fr": "Comprenez de courts avis et utilisez des phrases simples du quotidien.",
        "reading_title": "Aviso da biblioteca",
        "reading": "A biblioteca abre de segunda a sexta, das 9h às 17h. Aos sábados, abre das 10h às 13h. Domingo: fechada. Para fazer o cartão, traga um documento com foto.",
        "writing_pt": "Escreva 4 a 6 frases para se apresentar: nome, cidade, profissão ou estudo e algo de que você gosta.",
        "writing_fr": "Écrivez 4 à 6 phrases pour vous présenter : nom, ville, métier ou études et quelque chose que vous aimez.",
        "writing_check_pt": ["Usei frases completas.", "Conferi artigos e gênero.", "Usei o presente para falar de mim."],
        "writing_check_fr": ["J’ai écrit des phrases complètes.", "J’ai vérifié les articles et le genre.", "J’ai utilisé le présent pour parler de moi."],
        "questions": [
            question("reading", "Em quais dias a biblioteca abre das 9h às 17h?", ["Segunda a sexta", "Sábado", "Domingo"], 0, "O aviso informa que esse horário vale de segunda a sexta."),
            question("reading", "Qual é o horário de sábado?", ["9h às 17h", "10h às 13h", "13h às 17h"], 1, "Aos sábados, a biblioteca abre das 10h às 13h."),
            question("reading", "O que é necessário para fazer o cartão?", ["Um livro", "Dinheiro", "Um documento com foto"], 2, "O aviso pede um documento com foto."),
            question("reading", "A biblioteca abre no domingo?", ["Sim, de manhã", "Não", "Sim, o dia inteiro"], 1, "O domingo aparece como dia de fechamento."),
            question("grammar", "Complete: Eu ___ português.", ["estuda", "estudo", "estudamos"], 1, "Com eu, a forma é estudo."),
            question("grammar", "Escolha a frase correta.", ["A casa bonita", "O casa bonita", "As casa bonita"], 0, "Casa é feminino singular, por isso a casa bonita."),
            question("grammar", "Complete: Nós ___ no Brasil.", ["moro", "mora", "moramos"], 2, "Nós pede moramos no presente."),
            question("grammar", "Qual frase é negativa?", ["Eu gosto de chá.", "Eu não gosto de chá.", "Eu gosto não chá."], 1, "Não aparece antes do verbo."),
            question("usage", "Como perguntar pelo lugar onde alguém mora?", ["Onde você mora?", "Quando você mora?", "Quem você mora?"], 0, "Onde pergunta por um lugar."),
            question("usage", "Qual resposta combina com «Bom dia»?", ["Boa noite", "Bom dia", "Até ontem"], 1, "Bom dia pode ser respondido com o mesmo cumprimento."),
            question("usage", "Complete: ___ livro está na mesa.", ["A", "As", "O"], 2, "Livro é masculino singular: o livro."),
            question("usage", "Qual frase apresenta uma pessoa?", ["Ela se chama Ana.", "São oito horas.", "A loja está fechada."], 0, "Ela se chama Ana informa o nome da pessoa."),
        ],
    },
    "A2": {
        "title_pt": "Dia a dia", "title_fr": "Vie quotidienne",
        "intro_pt": "Leia uma mensagem, localize informações e fale sobre passado e planos.",
        "intro_fr": "Lisez un message, repérez des informations et parlez du passé et de projets.",
        "reading_title": "Mensagem de Marina",
        "reading": "Oi, Paulo! Ontem fui ao centro comprar um presente para minha irmã. A loja estava fechada quando cheguei, então voltei para casa. Amanhã vou sair mais cedo e tentar de novo. Você pode ir comigo? Podemos nos encontrar às 10h na estação. Abraço, Marina.",
        "writing_pt": "Escreva uma mensagem curta a um amigo: conte o que fez ontem e proponha um encontro para amanhã.",
        "writing_fr": "Écrivez un court message à un ami : racontez ce que vous avez fait hier et proposez un rendez-vous pour demain.",
        "writing_check_pt": ["Separei ontem e amanhã com tempos adequados.", "Indiquei lugar e horário do encontro.", "Fiz um convite claro."],
        "writing_check_fr": ["J’ai distingué hier et demain avec des temps adaptés.", "J’ai indiqué le lieu et l’heure du rendez-vous.", "J’ai formulé une invitation claire."],
        "questions": [
            question("reading", "Por que Marina foi ao centro?", ["Para trabalhar", "Para comprar um presente", "Para encontrar Paulo"], 1, "Ela queria comprar um presente para a irmã."),
            question("reading", "Por que ela voltou para casa?", ["A loja estava fechada", "Perdeu o ônibus", "Estava chovendo"], 0, "A mensagem diz que a loja estava fechada."),
            question("reading", "Quando Marina vai tentar de novo?", ["Hoje à noite", "Ontem", "Amanhã"], 2, "Ela escreve: amanhã vou sair mais cedo."),
            question("reading", "Onde ela propõe encontrar Paulo?", ["Na loja", "Na estação", "Em casa"], 1, "Ela sugere a estação às 10h."),
            question("grammar", "Complete: Ontem eu ___ ao centro.", ["vou", "fui", "ia"], 1, "Fui indica a ação concluída de ontem."),
            question("grammar", "Complete: Quando cheguei, a loja ___ fechada.", ["estava", "estará", "esteve"], 0, "Estava descreve o estado da loja naquele momento passado."),
            question("grammar", "Complete: Eu moro ___ cidade.", ["da", "à", "na"], 2, "Em + a cidade forma na cidade."),
            question("grammar", "Qual frase fala de um plano próximo?", ["Fui ontem.", "Vou sair amanhã.", "Saía sempre."], 1, "Vou sair + amanhã expressa um plano futuro."),
            question("usage", "Como fazer um convite?", ["Você pode ir comigo?", "Onde fica a loja?", "A loja fechou."], 0, "A pergunta convida outra pessoa a acompanhar Marina."),
            question("usage", "Complete: O presente é ___ minha irmã.", ["para", "em", "de"], 0, "Para indica a destinatária do presente."),
            question("usage", "Qual pergunta busca um horário?", ["Quem vai?", "A que horas nos encontramos?", "Onde você mora?"], 1, "A que horas solicita o horário."),
            question("usage", "Qual expressão encerra informalmente a mensagem?", ["Abraço", "Prezada Senhora", "Atenciosamente"], 0, "Abraço é um encerramento informal."),
        ],
    },
    "B1": {
        "title_pt": "Ideias conectadas", "title_fr": "Idées liées",
        "intro_pt": "Entenda argumentos claros e escolha conectores e formas verbais adequados.",
        "intro_fr": "Comprenez des arguments clairs et choisissez les connecteurs et les formes verbales adaptés.",
        "reading_title": "Uma horta no bairro",
        "reading": "Há dois anos, moradores de um bairro transformaram um terreno vazio em uma horta comunitária. No começo, faltavam ferramentas e poucas pessoas participavam. Uma escola próxima começou a organizar visitas; depois disso, mais famílias se juntaram ao projeto. Hoje a horta produz verduras, mas seu objetivo vai além da comida: ela criou um espaço de encontro. Se a prefeitura oferecer apoio, os moradores poderão ampliar as atividades. O grupo, porém, quer manter as decisões nas mãos da comunidade.",
        "writing_pt": "Escreva um parágrafo sobre uma iniciativa útil para seu bairro. Apresente o problema, uma proposta e uma possível consequência.",
        "writing_fr": "Écrivez un paragraphe sur une initiative utile pour votre quartier. Présentez le problème, une proposition et une conséquence possible.",
        "writing_check_pt": ["Apresentei uma ideia principal clara.", "Usei pelo menos dois conectores.", "Expliquei uma condição ou consequência."],
        "writing_check_fr": ["J’ai présenté une idée principale claire.", "J’ai utilisé au moins deux connecteurs.", "J’ai expliqué une condition ou une conséquence."],
        "questions": [
            question("reading", "O que havia no local antes da horta?", ["Uma escola", "Um terreno vazio", "Uma feira"], 1, "O texto informa que o grupo transformou um terreno vazio."),
            question("reading", "O que ajudou a aumentar a participação?", ["As visitas organizadas pela escola", "A venda do terreno", "A mudança de bairro"], 0, "Após as visitas escolares, mais famílias se juntaram."),
            question("reading", "Qual é um objetivo da horta além da produção de verduras?", ["Fechar a escola", "Criar um espaço de encontro", "Construir uma estrada"], 1, "O texto destaca o encontro entre moradores."),
            question("reading", "O que os moradores querem preservar?", ["O terreno vazio", "As decisões na comunidade", "A falta de ferramentas"], 1, "Eles querem manter as decisões nas mãos da comunidade."),
            question("grammar", "Complete: Se a prefeitura ___ apoio, o projeto crescerá.", ["oferecer", "ofereceu", "oferecia"], 0, "Após se, a condição futura usa oferecer, forma do futuro do subjuntivo."),
            question("grammar", "Qual conector expressa contraste?", ["porque", "portanto", "mas"], 2, "Mas opõe duas ideias."),
            question("grammar", "Complete: Espero que o projeto ___ .", ["cresce", "cresça", "cresceu"], 1, "Espero que pede o presente do subjuntivo: cresça."),
            question("grammar", "Complete: A horta é tão útil ___ a escola.", ["quanto", "do que", "porque"], 0, "Tão... quanto expressa igualdade."),
            question("usage", "Qual frase apresenta uma consequência?", ["Faltavam ferramentas.", "Por isso, o grupo buscou apoio.", "Embora houvesse apoio."], 1, "Por isso introduz um resultado."),
            question("usage", "Qual verbo indica uma possibilidade dependente de condição?", ["poderão", "faltavam", "transformaram"], 0, "Poderão depende de a prefeitura oferecer apoio."),
            question("usage", "Qual expressão retoma a ideia anterior no texto?", ["Depois disso", "No terreno", "Duas famílias"], 0, "Depois disso remete às visitas organizadas pela escola."),
            question("usage", "Qual resumo respeita o texto?", ["A horta só produz comida.", "A comunidade criou a horta e quer decidir seu futuro.", "A prefeitura criou e dirige a horta."], 1, "O projeto surgiu dos moradores, que querem manter as decisões."),
        ],
    },
    "B2": {
        "title_pt": "Argumentos e nuances", "title_fr": "Arguments et nuances",
        "intro_pt": "Leia um texto de opinião, identifique ressalvas e use estruturas mais complexas.",
        "intro_fr": "Lisez un texte d’opinion, repérez les nuances et utilisez des structures plus complexes.",
        "reading_title": "O espaço público e a cidade",
        "reading": "A criação de áreas verdes costuma ser apresentada como solução automática para melhorar as cidades. De fato, parques podem reduzir o calor e oferecer lugares de convivência. Entretanto, seus benefícios não se distribuem igualmente quando o planejamento ignora os bairros mais afastados. Além disso, a valorização do entorno pode elevar os custos de moradia e pressionar antigos moradores a sair. Isso não significa que se deva abandonar novos parques. Significa que é preciso combiná-los com transporte acessível, proteção à moradia e participação dos moradores nas decisões. Uma política urbana só será justa se considerar quem pode usufruir do espaço e quem corre o risco de ser excluído dele.",
        "writing_pt": "Escreva dois parágrafos: apresente uma proposta para melhorar espaços públicos e discuta um possível efeito indesejado, com uma solução.",
        "writing_fr": "Écrivez deux paragraphes : proposez une amélioration des espaces publics et discutez d’un effet indésirable possible, avec une solution.",
        "writing_check_pt": ["Defendi uma posição com justificativa.", "Incluí uma ressalva ou contra-argumento.", "Propus uma solução coerente com o problema."],
        "writing_check_fr": ["J’ai défendu un point de vue avec une justification.", "J’ai inclus une réserve ou un contre-argument.", "J’ai proposé une solution cohérente."],
        "questions": [
            question("reading", "Qual é a tese central do texto?", ["Parques devem ser abandonados.", "Parques precisam integrar uma política urbana atenta à desigualdade.", "Parques resolvem sozinhos todos os problemas."], 1, "O texto defende parques acompanhados de outras medidas de justiça urbana."),
            question("reading", "Que risco a valorização do entorno pode trazer?", ["Redução do calor", "Mais convivência", "Pressão para antigos moradores saírem"], 2, "O aumento dos custos de moradia pode expulsar antigos moradores."),
            question("reading", "Qual função tem «Entretanto» no texto?", ["Introduzir uma ressalva", "Confirmar sem nuance", "Indicar tempo passado"], 0, "Entretanto contrapõe os benefícios gerais à distribuição desigual deles."),
            question("reading", "O que a frase «Isso não significa...» evita?", ["Uma conclusão simplista contra os parques", "Uma proposta de transporte", "A participação dos moradores"], 0, "O autor esclarece que criticar efeitos injustos não equivale a rejeitar parques."),
            question("grammar", "Complete: Embora os parques ___ benefícios, podem gerar pressões.", ["trazem", "tragam", "trouxeram"], 1, "Embora normalmente pede subjuntivo: tragam."),
            question("grammar", "Complete: Se o planejamento ___ os moradores, seria mais justo.", ["ouvisse", "ouve", "ouvirá"], 0, "Uma hipótese irreal ou distante usa se + imperfeito do subjuntivo: ouvisse."),
            question("grammar", "Qual frase está na voz passiva?", ["Os moradores decidiram.", "A decisão foi tomada pelos moradores.", "Os moradores vão decidir."], 1, "Foi tomada é ser + particípio na voz passiva."),
            question("grammar", "Complete: É preciso que todos ___ participar.", ["podem", "pudessem", "possam"], 2, "É preciso que pede subjuntivo: possam."),
            question("usage", "Qual expressão introduz uma informação adicional?", ["Além disso", "Entretanto", "Apesar de"], 0, "Além disso acrescenta outro argumento."),
            question("usage", "A quem se refere «seus benefícios» no segundo período?", ["Aos parques", "Aos custos", "Aos moradores"], 0, "O possessivo retoma parques."),
            question("usage", "Qual formulação mantém a nuance do texto?", ["Parques sempre prejudicam.", "Parques podem ajudar, desde que o acesso seja justo.", "Transporte substitui todo parque."], 1, "A frase reconhece o benefício e a condição de justiça."),
            question("usage", "Qual expressão indica condição para uma política justa?", ["só será justa se", "de fato", "além disso"], 0, "Só... se estabelece uma condição necessária."),
        ],
    },
}

SECTION_LABELS = {
    "reading": {"pt": "Leitura", "fr": "Lecture"},
    "grammar": {"pt": "Gramática", "fr": "Grammaire"},
    "usage": {"pt": "Uso da língua", "fr": "Usage de la langue"},
}

# A escuta é corrigida objetivamente; a fala usa transcrição e ritmo indicativos.
EXAMS["A1"]["listening"] = [
    {"audio": "A padaria abre às sete horas.", "prompt": "A que horas a padaria abre?", "options": ["Às sete", "Às nove", "Às dez"], "answer": 0, "explanation": "A frase diz que a padaria abre às sete horas."},
    {"audio": "Meu nome é Lucas e moro em Salvador.", "prompt": "Onde Lucas mora?", "options": ["Recife", "Salvador", "São Paulo"], "answer": 1, "explanation": "Lucas diz que mora em Salvador."},
    {"audio": "Quero um café sem açúcar, por favor.", "prompt": "Como a pessoa quer o café?", "options": ["Com leite", "Com açúcar", "Sem açúcar"], "answer": 2, "explanation": "A pessoa pede café sem açúcar."},
    {"audio": "Hoje é segunda-feira.", "prompt": "Que dia é hoje?", "options": ["Segunda-feira", "Sexta-feira", "Domingo"], "answer": 0, "explanation": "A frase informa que hoje é segunda-feira."},
]
EXAMS["A1"]["speaking"] = [
    "Bom dia, meu nome é Ana.", "Eu moro no Brasil.",
    "Gosto de estudar português.", "A biblioteca abre às nove horas.",
]
EXAMS["A2"]["listening"] = [
    {"audio": "Ontem comprei frutas no mercado, mas esqueci o pão.", "prompt": "O que a pessoa esqueceu?", "options": ["As frutas", "O pão", "O dinheiro"], "answer": 1, "explanation": "Ela comprou frutas e esqueceu o pão."},
    {"audio": "O ônibus para o centro sai às oito e meia da plataforma três.", "prompt": "De qual plataforma sai o ônibus?", "options": ["Um", "Dois", "Três"], "answer": 2, "explanation": "O anúncio informa plataforma três."},
    {"audio": "Se não chover amanhã, vamos caminhar no parque.", "prompt": "O que o grupo pretende fazer?", "options": ["Caminhar no parque", "Ir ao cinema", "Ficar na escola"], "answer": 0, "explanation": "O plano é caminhar no parque se não chover."},
    {"audio": "A reunião mudou de terça para quinta-feira.", "prompt": "Quando será a reunião?", "options": ["Terça-feira", "Quinta-feira", "Sábado"], "answer": 1, "explanation": "A reunião foi transferida para quinta-feira."},
]
EXAMS["A2"]["speaking"] = [
    "Ontem fui ao mercado com minha irmã.", "Amanhã vamos nos encontrar na estação.",
    "Você pode me ajudar, por favor?", "Quando cheguei, a loja estava fechada.",
]
EXAMS["B1"]["listening"] = [
    {"audio": "A oficina começará meia hora mais tarde porque a professora está presa no trânsito.", "prompt": "Por que a oficina vai começar mais tarde?", "options": ["Por falta de alunos", "Por causa do trânsito", "Por causa da chuva"], "answer": 1, "explanation": "A professora está presa no trânsito."},
    {"audio": "O projeto recebeu apoio da escola, embora ainda precise de novos voluntários.", "prompt": "O que o projeto ainda precisa?", "options": ["De uma escola", "De voluntários", "De um terreno"], "answer": 1, "explanation": "Apesar do apoio, ainda faltam voluntários."},
    {"audio": "Se os moradores participarem da reunião, poderão decidir como usar o espaço.", "prompt": "Qual é a condição para decidir sobre o espaço?", "options": ["Participar da reunião", "Construir uma escola", "Mudar de bairro"], "answer": 0, "explanation": "Os moradores precisam participar da reunião."},
    {"audio": "A biblioteca não vai fechar; apenas reduzirá o horário durante as férias.", "prompt": "O que mudará na biblioteca?", "options": ["Ela fechará definitivamente", "Ela reduzirá o horário", "Ela mudará de endereço"], "answer": 1, "explanation": "A biblioteca apenas reduzirá o horário."},
]
EXAMS["B1"]["speaking"] = [
    "Embora estivesse chovendo, fomos à reunião da comunidade.",
    "Se tivermos mais voluntários, poderemos ampliar a horta.",
    "O projeto é útil porque aproxima os moradores do bairro.",
    "A escola organizou visitas e, por isso, mais famílias participaram.",
]
EXAMS["B2"]["listening"] = [
    {"audio": "A proposta foi aprovada, mas sua execução dependerá de recursos que ainda não foram garantidos.", "prompt": "Qual ressalva acompanha a aprovação?", "options": ["Os recursos ainda não estão garantidos", "A proposta foi rejeitada", "A execução já terminou"], "answer": 0, "explanation": "A execução depende de recursos ainda incertos."},
    {"audio": "Embora a medida possa reduzir o trânsito, especialistas alertam para seus efeitos sobre os bairros periféricos.", "prompt": "Que contraste a frase apresenta?", "options": ["A medida não afeta ninguém", "Um possível benefício e uma preocupação", "Apenas uma vantagem confirmada"], "answer": 1, "explanation": "Há um benefício possível e um alerta sobre efeitos desiguais."},
    {"audio": "A pesquisadora afirmou que os dados seriam revistos antes da publicação do relatório.", "prompt": "O que aconteceria antes da publicação?", "options": ["Uma reunião pública", "A revisão dos dados", "O cancelamento da pesquisa"], "answer": 1, "explanation": "Os dados seriam revistos antes da publicação."},
    {"audio": "A participação dos moradores é essencial, desde que suas sugestões influenciem de fato as decisões.", "prompt": "Qual condição torna a participação significativa?", "options": ["Que as sugestões influenciem as decisões", "Que as reuniões sejam curtas", "Que todos concordem previamente"], "answer": 0, "explanation": "As sugestões precisam ter efeito real nas decisões."},
]
EXAMS["B2"]["speaking"] = [
    "Embora os parques tragam benefícios, seu acesso ainda é desigual.",
    "A decisão foi tomada depois que os moradores apresentaram suas propostas.",
    "Se o planejamento ouvisse a comunidade, a política seria mais justa.",
    "É importante que os novos espaços públicos sejam acessíveis a todos.",
]
