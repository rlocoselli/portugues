# Fala Brasil — Aprender Português / Apprendre le portugais

Site bilíngue (português / francês) para aprender português com textos sobre o
Brasil (natureza, história, geografia, cultura e ciência), além de uma seção de
poesias originais em português com traduções para o francês. Cada texto inclui:

- o texto em português;
- a tradução em francês;
- áudio (texto para fala) gerado no servidor com **gTTS** (arquivos MP3, com cache em disco);
- um pequeno vocabulário português → francês.
- um quiz de compreensão e vocabulário com quatro ou seis perguntas, correção imediata e melhor resultado salvo no navegador.

A página inicial inclui um pequeno vídeo ilustrado sem áudio. É possível marcar
uma leitura como concluída; o progresso fica salvo apenas no navegador usado.
As cinco leituras mais curtas receberam passagens bilíngues adicionais em
`data/enriquecimento.py`.

A seção **Geografia** (`/geografia`) traz um mapa interativo com as 27 unidades
da Federação, filtro por região, capitais e um desafio de cinco rodadas. Três
vídeos locais e silenciosos explicam regiões, relevo e bacias hidrográficas;
cada um tem transcrição em português e francês. O mapa e os vídeos são
servidos localmente, sem depender de uma API externa durante a visita.

Três guias adicionais estão disponíveis no menu:

- **Dados** (`/dados`): PIB, trabalho, educação e IDH, com ano de referência e
  link para a fonte em cada indicador.
- **Brasil × Portugal** (`/variedades`): vocabulário, construções, tratamento
  e pronúncia, com exemplos comparados.
- **História** (`/historia`): linha do tempo da Primeira República à
  redemocratização, com contexto anterior a 1889.

Cada bloco desses guias tem texto em português, tradução francesa e botões
para ouvir nas duas línguas. O áudio usa gTTS com cache por conteúdo; se o
servidor de síntese estiver indisponível, o navegador pode tentar sua própria
síntese de voz.

Os agrupamentos regionais e as capitais seguem o [IBGE Educa](https://educa.ibge.gov.br/jovens/conheca-o-brasil/territorio/19637-divisao-territorial.html).
Os contornos simplificados vêm do conjunto [br-geojson (CC0)](https://github.com/henriquemalvar/br-geojson),
derivado das malhas do IBGE. `data/estados.geojson` guarda a cópia usada para
gerar o SVG local.

> O áudio é gerado no servidor com **gTTS** (Google Text-to-Speech), que exige
> conexão com a internet na primeira vez que cada texto/frase/palavra é
> reproduzido. Os arquivos MP3 ficam salvos na pasta `audio_cache/` (criada
> automaticamente) para não serem gerados de novo. Para ouvir, use o player ou
> clique em cada frase/palavra.

## Como executar

```bash
cd /home/locoselli/portugues
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abra <http://127.0.0.1:5000> no navegador.

## Como adicionar novos textos (sem banco de dados)

Todos os textos ficam em **`data/textos.py`**, dentro da lista `TEXTOS`.
Basta copiar um bloco existente e preencher os campos:

| Campo          | Descrição                                                    |
| -------------- | ------------------------------------------------------------ |
| `slug`         | Identificador único (letras minúsculas e hífens).            |
| `categoria`    | `natureza`, `historia`, `geografia`, `cultura` ou `ciencia`. |
| `nivel`        | `iniciante`, `intermediario` ou `avancado`.                   |
| `titulo_pt`    | Título em português.                                         |
| `titulo_fr`    | Título em francês.                                           |
| `texto_pt`     | Texto em português (usado também para o áudio).              |
| `texto_fr`     | Tradução em francês.                                         |
| `vocabulario`  | Lista de pares `{"pt": "...", "fr": "..."}`.                 |

Depois de editar, reinicie o servidor Flask. O novo texto aparece automaticamente
na página inicial, nos filtros e na busca.

## Regerar mapa e vídeos de geografia

Os arquivos gerados já estão incluídos no projeto. Para recriá-los após mudar
os dados ou os roteiros, instale `Pillow` e `CairoSVG` no ambiente de edição,
além do executável `ffmpeg`, e execute:

```bash
python scripts/build_geography_map.py
python scripts/build_geography_videos.py
```

## Estrutura do projeto

```
app.py                  # aplicação Flask (rotas e textos da interface)
data/textos.py          # banco de textos (sem banco de dados)
data/poesias.py         # poemas originais em português e traduções francesas
templates/              # páginas HTML (base, index, textos, poesias, sobre, 404)
static/css/style.css    # estilos
static/js/tts.js        # reprodução de áudio (player + frases/palavras clicáveis)
static/js/quiz.js       # correção e pontuação dos quizzes de compreensão
static/js/progress.js   # progresso local das leituras
data/enriquecimento.py  # extensões bilíngues das leituras curtas
data/geografia.py       # regiões, estados, capitais e roteiros bilíngues
data/estados.geojson    # contornos simplificados dos estados (CC0)
data/guias.py           # indicadores, variedades, história e fontes
scripts/build_geography_map.py    # gera o SVG navegável do mapa
scripts/build_geography_videos.py # gera três vídeos didáticos locais
static/js/geografia.js  # interação do mapa e desafio
static/js/guide-audio.js # áudio dos novos guias em PT/FR
static/video/           # vídeos e capas locais
requirements.txt        # dependências
```
