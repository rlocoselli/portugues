document.addEventListener('DOMContentLoaded', () => {
  const verbos = JSON.parse(document.querySelector('#grammar-data')?.textContent || '[]');
  const exercicios = JSON.parse(document.querySelector('#exercise-data')?.textContent || '[]');
  const lang = document.documentElement.lang === 'fr' ? 'fr' : 'pt';
  const pessoas = lang === 'fr' ? ['je', 'vous', 'il/elle', 'nous', 'ils/elles'] : ['eu', 'você', 'ele/ela', 'nós', 'eles/elas'];
  const tempoNomes = { presente: lang === 'fr' ? 'Présent' : 'Presente', preterito: lang === 'fr' ? 'Passé simple' : 'Pretérito perfeito', imperfeito: lang === 'fr' ? 'Imparfait' : 'Pretérito imperfeito', futuro: lang === 'fr' ? 'Futur' : 'Futuro' };
  const get = (selector) => document.querySelector(selector);
  const speak = (text) => { if (!text || !('speechSynthesis' in window)) return; window.speechSynthesis.cancel(); const voice = new SpeechSynthesisUtterance(text); voice.lang = 'pt-BR'; window.speechSynthesis.speak(voice); };

  let selectedId = verbos[0]?.infinitivo;
  let selectedTense = 'presente';
  const search = get('#verb-search');
  const levelFilter = get('#level-filter');
  const suggestions = get('#suggestions');
  const list = get('#verb-list');

  function findVerb(id) { return verbos.find((verb) => verb.infinitivo === id) || verbos[0]; }

  function selectVerb(id) {
    const verb = findVerb(id); if (!verb) return;
    selectedId = verb.infinitivo;
    document.querySelectorAll('.verb-directory-item').forEach((item) => item.classList.toggle('active', item.dataset.verbId === selectedId));
    get('#detail-level').textContent = verb.nivel;
    get('#detail-type').textContent = verb.tipo;
    get('#detail-infinitive').textContent = verb.infinitivo;
    get('#detail-translation').textContent = verb.traducao;
    get('#detail-example').textContent = verb.exemplo;
    renderConjugation();
  }

  function renderConjugation() {
    const verb = findVerb(selectedId); const forms = verb.conjugacoes[selectedTense] || [];
    const body = get('#conjugation-body'); body.innerHTML = '';
    pessoas.forEach((person, index) => {
      const row = document.createElement('tr');
      row.innerHTML = `<th>${person}</th><td><strong>${forms[index] || '—'}</strong></td><td>${person} <b>${forms[index] || '—'}</b></td>`;
      body.appendChild(row);
    });
    document.querySelectorAll('.tense-tab').forEach((tab) => tab.classList.toggle('active', tab.dataset.tense === selectedTense));
  }

  function filteredVerbs() {
    const query = (search?.value || '').trim().toLocaleLowerCase('pt-BR'); const level = levelFilter?.value || 'all';
    return verbos.filter((verb) => {
      const searchable = [verb.infinitivo, verb.traducao, verb.nivel, verb.tipo, ...Object.values(verb.conjugacoes).flat()].join(' ').toLocaleLowerCase('pt-BR');
      return (level === 'all' || verb.nivel === level) && (!query || searchable.includes(query));
    });
  }

  function filterVerbs() {
    const matches = filteredVerbs(); const ids = new Set(matches.map((verb) => verb.infinitivo));
    document.querySelectorAll('.verb-directory-item').forEach((item) => { item.hidden = !ids.has(item.dataset.verbId); });
    get('#verb-count').textContent = matches.length;
    if (!ids.has(selectedId) && matches[0]) selectVerb(matches[0].infinitivo);
    if (search?.value.trim()) {
      suggestions.innerHTML = '';
      matches.slice(0, 6).forEach((verb) => { const button = document.createElement('button'); button.type = 'button'; button.textContent = `${verb.infinitivo} · ${verb.traducao}`; button.onclick = () => { search.value = verb.infinitivo; filterVerbs(); selectVerb(verb.infinitivo); suggestions.innerHTML = ''; }; suggestions.appendChild(button); });
    } else suggestions.innerHTML = '';
  }

  search?.addEventListener('input', filterVerbs); levelFilter?.addEventListener('change', filterVerbs);
  get('#clear-search')?.addEventListener('click', () => { search.value = ''; levelFilter.value = 'all'; filterVerbs(); search.focus(); });
  list?.addEventListener('click', (event) => { const item = event.target.closest('.verb-directory-item'); if (item) selectVerb(item.dataset.verbId); });
  document.querySelectorAll('.tense-tab').forEach((tab) => tab.addEventListener('click', () => { selectedTense = tab.dataset.tense; renderConjugation(); }));
  get('#speak-verb')?.addEventListener('click', () => speak(findVerb(selectedId).infinitivo));
  get('#speak-example')?.addEventListener('click', () => speak(get('#detail-example').textContent));
  document.querySelectorAll('.phrase-pt').forEach((button) => button.addEventListener('click', () => speak(button.dataset.speak)));
  document.querySelectorAll('.irregular-chip').forEach((button) => button.addEventListener('click', () => { selectVerb(button.dataset.openVerb); document.querySelector('#conjugador').scrollIntoView({ behavior: 'smooth', block: 'start' }); }));
  document.querySelectorAll('[data-level-jump]').forEach((button) => button.addEventListener('click', () => startLesson(button.dataset.levelJump))); 

  const progressKey = 'fala-brasil-grammar-v2';
  let saved = {};
  try { saved = JSON.parse(localStorage.getItem(progressKey) || '{}') || {}; } catch { saved = {}; }
  let level = null, lesson = [], exerciseIndex = 0, score = 0, selected = '', answered = false, finished = false;
  const copy = lang === 'fr' ? { start: 'Commencer', continue: 'Reprendre', complete: 'Terminé', correct: 'Bonne réponse !', wrong: 'À revoir.', answer: 'Réponse :', done: 'Étape terminée !', result: 'Bonnes réponses', type: 'Écrivez votre réponse', remove: 'Retirer' } : { start: 'Começar', continue: 'Continuar', complete: 'Concluído', correct: 'Muito bem!', wrong: 'Vamos revisar.', answer: 'Resposta:', done: 'Etapa concluída!', result: 'Acertos', type: 'Digite sua resposta', remove: 'Remover' };
  const normalize = (value) => value.trim().toLocaleLowerCase('pt-BR').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[.!?]+$/g, '').replace(/\s+/g, ' ');
  const save = () => { try { localStorage.setItem(progressKey, JSON.stringify(saved)); } catch { /* storage may be unavailable */ } };
  function renderPicker() {
    document.querySelectorAll('[data-lesson]').forEach((button) => {
      const id = button.dataset.lesson, total = exercicios.filter((item) => item.nivel === id).length, state = saved[id];
      button.classList.toggle('active', id === level);
      button.classList.toggle('completed', !!state?.completed);
      button.querySelector('small').textContent = state?.completed ? `${copy.complete} · ${state.best}/${total}` : state?.index ? `${copy.continue} · ${state.index}/${total}` : `${total} ${lang === 'fr' ? 'défis' : 'desafios'} · ${copy.start}`;
    });
  }
  function setProgress(value) {
    const percent = Math.round(value / lesson.length * 100);
    get('#exercise-progress-bar').style.width = `${percent}%`;
    get('.lesson-stage .exercise-progress').setAttribute('aria-valuenow', percent);
  }
  function startLesson(id, reset = false) {
    level = id; lesson = exercicios.filter((item) => item.nivel === id);
    if (!lesson.length) return;
    const state = reset ? {} : saved[id] || {};
    exerciseIndex = state.completed ? 0 : Math.min(state.index || 0, lesson.length - 1);
    score = state.completed ? 0 : state.score || 0;
    finished = false;
    get('#lesson-stage').hidden = false;
    get('#score-value').textContent = score;
    renderPicker(); renderExercise();
    get('#exercicios').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  function renderExercise() {
    const exercise = lesson[exerciseIndex]; if (!exercise) return;
    answered = false; selected = '';
    get('#exercise-level').textContent = exercise.nivel;
    get('#exercise-topic').textContent = exercise.tema;
    get('#exercise-number').textContent = `${exerciseIndex + 1} / ${lesson.length}`;
    get('#exercise-prompt').textContent = exercise.frase;
    get('#exercise-feedback').replaceChildren();
    get('#exercise-feedback').className = 'exercise-feedback';
    get('#check-exercise').hidden = false; get('#check-exercise').disabled = true;
    get('#next-exercise').hidden = true;
    setProgress(exerciseIndex);
    const options = get('#exercise-options'); options.replaceChildren();
    if (exercise.tipo === 'escrever') {
      const input = document.createElement('input'); input.className = 'exercise-input'; input.type = 'text'; input.autocomplete = 'off'; input.setAttribute('aria-label', copy.type); input.placeholder = copy.type;
      input.addEventListener('input', () => { selected = input.value; get('#check-exercise').disabled = !selected.trim(); });
      input.addEventListener('keydown', (event) => { if (event.key === 'Enter' && !get('#check-exercise').disabled) checkAnswer(); });
      options.appendChild(input); input.focus();
    } else if (exercise.tipo === 'ordenar') {
      const answer = document.createElement('div'); answer.className = 'word-answer'; answer.setAttribute('aria-label', lang === 'fr' ? 'Votre phrase' : 'Sua frase');
      const bank = document.createElement('div'); bank.className = 'word-bank'; const picked = [];
      exercise.palavras.forEach((word, index) => {
        const token = document.createElement('button'); token.type = 'button'; token.textContent = word;
        token.addEventListener('click', () => { picked.push({ word, index }); token.hidden = true; update(); }); bank.appendChild(token);
      });
      function update() {
        answer.replaceChildren(); picked.forEach((item, position) => { const token = document.createElement('button'); token.type = 'button'; token.textContent = item.word; token.setAttribute('aria-label', `${copy.remove} ${item.word}`); token.addEventListener('click', () => { picked.splice(position, 1); bank.children[item.index].hidden = false; update(); }); answer.appendChild(token); });
        selected = picked.map((item) => item.word).join(' '); get('#check-exercise').disabled = picked.length !== exercise.palavras.length;
      }
      options.append(answer, bank);
    } else {
      exercise.opcoes.forEach((option) => { const button = document.createElement('button'); button.type = 'button'; button.textContent = option; button.addEventListener('click', () => { selected = option; options.querySelectorAll('button').forEach((item) => item.classList.toggle('chosen', item === button)); get('#check-exercise').disabled = false; }); options.appendChild(button); });
    }
  }
  function checkAnswer() {
    if (answered || !selected.trim()) return;
    answered = true; const exercise = lesson[exerciseIndex], correct = normalize(selected) === normalize(exercise.resposta);
    if (correct) score += 1;
    get('#score-value').textContent = score;
    get('#exercise-options').querySelectorAll('button, input').forEach((item) => { item.disabled = true; if (item.textContent === exercise.resposta) item.classList.add('correct-option'); });
    const feedback = get('#exercise-feedback'); feedback.classList.add(correct ? 'correct' : 'wrong');
    const heading = document.createElement('strong'); heading.textContent = correct ? copy.correct : `${copy.wrong} ${copy.answer} ${exercise.resposta}.`;
    const detail = document.createElement('span'); detail.textContent = ` ${exercise.explicacao}`; feedback.append(heading, detail);
    get('#check-exercise').hidden = true; get('#next-exercise').hidden = false;
    setProgress(exerciseIndex + 1);
    saved[level] = { index: exerciseIndex + 1, score, best: saved[level]?.best || 0, completed: false }; save(); renderPicker();
  }
  function nextExercise() {
    if (!answered || finished) return;
    if (exerciseIndex < lesson.length - 1) { exerciseIndex += 1; renderExercise(); return; }
    finished = true; saved[level] = { index: lesson.length, score, best: Math.max(score, saved[level]?.best || 0), completed: true }; save(); renderPicker();
    get('#exercise-prompt').textContent = copy.done;
    get('#exercise-options').replaceChildren();
    get('#exercise-feedback').textContent = `${copy.result}: ${score}/${lesson.length}.`;
    get('#exercise-feedback').className = 'exercise-feedback correct';
    get('#exercise-number').textContent = `${lesson.length} / ${lesson.length}`;
    get('#next-exercise').hidden = true;
  }
  document.querySelectorAll('[data-lesson]').forEach((button) => button.addEventListener('click', () => startLesson(button.dataset.lesson)));
  get('#check-exercise')?.addEventListener('click', checkAnswer);
  get('#next-exercise')?.addEventListener('click', nextExercise);
  get('#restart-exercises')?.addEventListener('click', () => { if (level) { delete saved[level]; save(); startLesson(level, true); } });
  selectVerb(selectedId); renderPicker();
});
