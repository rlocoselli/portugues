# Fala Brasil — Aprender Português / Apprendre le portugais

Site bilíngue (português / francês) para aprender português com textos sobre o
Brasil (natureza, história, geografia e cultura). Cada texto inclui:

- o texto em português;
- a tradução em francês;
- áudio (texto para fala) gerado no servidor com **gTTS** (arquivos MP3, com cache em disco);
- um pequeno vocabulário português → francês.
- um quiz de compreensão com três perguntas e correção imediata.

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

## Estrutura do projeto

```
app.py                  # aplicação Flask (rotas e textos da interface)
data/textos.py          # banco de textos (sem banco de dados)
templates/              # páginas HTML (base, index, texto, sobre, 404)
static/css/style.css    # estilos
static/js/tts.js        # reprodução de áudio (player + frases/palavras clicáveis)
static/js/quiz.js       # correção e pontuação dos quizzes de compreensão
requirements.txt        # dependências
```
