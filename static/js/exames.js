(() => {
  const lang = document.documentElement.lang === 'fr' ? 'fr' : 'pt';
  const copy = lang === 'fr' ? {
    best: 'Meilleur résultat', draft: 'activités enregistrées', missing: 'Répondez aux 16 questions à choix avant de corriger.',
    correct: 'Bonne réponse.', wrong: 'À revoir. Bonne réponse : ', result: 'Vous avez réussi', of: 'sur',
    reading: 'Lecture', grammar: 'Grammaire', usage: 'Usage de la langue', listening: 'Écoute', finished: 'Examen corrigé',
    unavailable: 'La reconnaissance vocale n’est pas disponible dans ce navigateur. Les questions orales restent facultatives.',
    micError: 'Le microphone ou le service de reconnaissance vocale n’est pas disponible. Réessayez ou vérifiez son autorisation.',
    listeningError: 'La lecture audio n’est pas disponible dans ce navigateur.', recording: 'Je vous écoute…',
    noSpeech: 'Aucune parole reconnue. Réessayez.', heard: 'Reconnu', estimate: 'Fluidité estimée',
    pace: 'rythme', average: 'Estimation orale moyenne', noRecording: 'Aucune phrase enregistrée. Les activités orales ne sont pas notées.',
    limit: 'Indication fondée sur la transcription et le rythme ; la prononciation n’est pas évaluée.',
  } : {
    best: 'Melhor resultado', draft: 'atividades salvas', missing: 'Responda às 16 questões de escolha antes de corrigir.',
    correct: 'Resposta certa.', wrong: 'Revise. Resposta certa: ', result: 'Você acertou', of: 'de',
    reading: 'Leitura', grammar: 'Gramática', usage: 'Uso da língua', listening: 'Escuta', finished: 'Exame corrigido',
    unavailable: 'O reconhecimento de voz não está disponível neste navegador. As questões de fala ficam opcionais.',
    micError: 'O microfone ou o serviço de reconhecimento de voz não está disponível. Tente novamente ou verifique a permissão.',
    listeningError: 'A reprodução de áudio não está disponível neste navegador.', recording: 'Estou ouvindo…',
    noSpeech: 'Nenhuma fala reconhecida. Tente novamente.', heard: 'Reconhecido', estimate: 'Fluência estimada',
    pace: 'ritmo', average: 'Estimativa média de fala', noRecording: 'Nenhuma frase gravada. As atividades de fala não recebem nota.',
    limit: 'Indicador baseado na transcrição e no ritmo; a pronúncia não é avaliada.',
  };
  const key = (level) => `fala-brasil-exam-v2-${level}`;
  const load = (level) => {
    try {
      const current = JSON.parse(localStorage.getItem(key(level)) || 'null');
      if (current) return current;
      const previous = JSON.parse(localStorage.getItem(`fala-brasil-exam-v1-${level}`) || 'null');
      if (previous?.draft) return { draft: { answers: previous.draft.answers || {}, writing: previous.draft.writing || '', speech: {} } };
    } catch { /* Storage is optional. */ }
    return {};
  };
  const save = (level, state) => {
    try { localStorage.setItem(key(level), JSON.stringify(state)); }
    catch { /* Storage is optional. */ }
  };
  const recordedCount = (state) => Object.values(state.draft?.speech || {}).filter((item) => item?.transcript).length;

  document.querySelectorAll('[data-exam-status]').forEach((node) => {
    const state = load(node.dataset.examStatus);
    if (Number.isInteger(state.best)) node.textContent = `${copy.best}: ${state.best}/16`;
    else if (state.draft) {
      const count = Object.keys(state.draft.answers || {}).length + recordedCount(state);
      if (count) node.textContent = `${count}/20 ${copy.draft}`;
    }
  });

  const root = document.querySelector('[data-exam]');
  if (!root) return;
  const level = root.dataset.exam;
  const dataNode = document.querySelector('#exam-data');
  const form = root.querySelector('.exam-form');
  if (!dataNode || !form) return;
  let exam;
  try { exam = JSON.parse(dataNode.textContent); }
  catch { return; }
  const questions = [...exam.questions, ...exam.listening.map((item) => ({ ...item, section: 'listening' }))];
  let state = load(level);
  if (!state.draft) state.draft = { answers: {}, writing: '', speech: {} };
  state.draft.answers ||= {};
  state.draft.speech ||= {};
  const writing = root.querySelector('#exam-writing-answer');
  const error = root.querySelector('[data-exam-error]');
  const result = root.querySelector('[data-exam-result]');
  const submit = form.querySelector('[type="submit"]');
  const micStatus = root.querySelector('[data-mic-status]');
  const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  let activeRecognition = null;

  Object.entries(state.draft.answers).forEach(([number, choice]) => {
    const input = form.querySelector(`input[name="question-${number}"][value="${choice}"]`);
    if (input) input.checked = true;
  });
  writing.value = state.draft.writing || '';

  function updateProgress() {
    const count = questions.filter((_, index) => form.querySelector(`input[name="question-${index}"]:checked`)).length + recordedCount(state);
    root.querySelector('[data-exam-progress]').textContent = `${count} / 20`;
    const bar = root.querySelector('.exam-progress');
    bar.setAttribute('aria-valuenow', count);
    bar.querySelector('span').style.width = `${count / 20 * 100}%`;
  }
  updateProgress();

  form.addEventListener('change', (event) => {
    if (!event.target.matches('input[type="radio"]')) return;
    const number = event.target.name.split('-')[1];
    state.draft.answers[number] = Number(event.target.value);
    save(level, state); updateProgress(); error.textContent = '';
  });
  writing.addEventListener('input', () => { state.draft.writing = writing.value; save(level, state); });

  function speak(text, onError) {
    if (!('speechSynthesis' in window)) { onError?.(); micStatus.textContent = copy.listeningError; return; }
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'pt-BR'; utterance.rate = level === 'A1' ? 0.86 : level === 'A2' ? 0.92 : 1;
    utterance.onerror = () => { onError?.(); micStatus.textContent = copy.listeningError; };
    window.speechSynthesis.speak(utterance);
  }
  root.querySelectorAll('[data-listen]').forEach((button) => {
    button.addEventListener('click', () => {
      const index = Number(button.dataset.listen);
      speak(exam.listening[index].audio, () => {
        const fallback = root.querySelector(`[data-audio-fallback="${index}"]`);
        fallback.textContent = exam.listening[index].audio;
        fallback.hidden = false;
      });
    });
  });
  root.querySelectorAll('[data-speak-model]').forEach((button) => {
    button.addEventListener('click', () => speak(exam.speaking[Number(button.dataset.speakModel)]));
  });

  const words = (text) => text.toLocaleLowerCase('pt-BR').normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9\s]/g, ' ').trim().split(/\s+/).filter(Boolean);
  function wordSimilarity(expected, heard) {
    const a = words(expected), b = words(heard);
    const row = Array.from({ length: b.length + 1 }, (_, index) => index);
    for (let i = 1; i <= a.length; i += 1) {
      let previous = row[0]; row[0] = i;
      for (let j = 1; j <= b.length; j += 1) {
        const old = row[j];
        row[j] = Math.min(row[j] + 1, row[j - 1] + 1, previous + (a[i - 1] === b[j - 1] ? 0 : 1));
        previous = old;
      }
    }
    return Math.max(0, 1 - row[b.length] / Math.max(a.length, b.length, 1));
  }
  function speechEstimate(target, transcript, durationMs) {
    const match = wordSimilarity(target, transcript);
    const wpm = durationMs && durationMs > 400 ? Math.round(words(transcript).length * 60000 / durationMs) : null;
    const rhythm = wpm === null ? null : Math.max(0, Math.min(1, wpm / 65, 210 / wpm));
    const estimate = Math.round((rhythm === null ? match : 0.85 * match + 0.15 * rhythm) * 100);
    return { transcript, match: Math.round(match * 100), wpm, estimate };
  }
  function renderSpeech(index) {
    const item = state.draft.speech[index];
    const feedback = root.querySelector(`[data-speech-item="${index}"] [data-speech-feedback]`);
    if (!item?.transcript) { feedback.textContent = ''; return; }
    feedback.textContent = `${copy.heard}: “${item.transcript}”. ${copy.estimate}: ${item.estimate}%` +
      (item.wpm ? ` · ${copy.pace}: ${item.wpm} palavras/min.` : '') + ` ${copy.limit}`;
  }
  function renderFluency() {
    const samples = Object.values(state.draft.speech).filter((item) => item?.transcript);
    const node = result.querySelector('[data-result-fluency]');
    node.textContent = samples.length
      ? `${copy.average}: ${Math.round(samples.reduce((sum, item) => sum + item.estimate, 0) / samples.length)}% (${samples.length}/4). ${copy.limit}`
      : copy.noRecording;
  }
  exam.speaking.forEach((_, index) => renderSpeech(index));
  if (!Recognition) {
    micStatus.textContent = copy.unavailable;
    root.querySelectorAll('[data-record]').forEach((button) => { button.disabled = true; });
  }
  root.querySelectorAll('[data-record]').forEach((button) => {
    button.addEventListener('click', () => {
      if (!Recognition) return;
      if (activeRecognition) { const previous = activeRecognition; activeRecognition = null; previous.abort(); }
      if ('speechSynthesis' in window) window.speechSynthesis.cancel();
      const index = Number(button.dataset.record);
      const recognition = new Recognition(); activeRecognition = recognition;
      recognition.lang = 'pt-BR'; recognition.continuous = false;
      recognition.interimResults = false; recognition.maxAlternatives = 1;
      let transcript = '', started = null, ended = null, failed = false;
      recognition.onstart = () => { micStatus.textContent = copy.recording; button.classList.add('recording'); };
      recognition.onspeechstart = () => { started = performance.now(); };
      recognition.onspeechend = () => { ended = performance.now(); };
      recognition.onresult = (event) => { transcript = event.results[0]?.[0]?.transcript?.trim() || ''; };
      recognition.onerror = (event) => {
        failed = true;
        micStatus.textContent = event.error === 'no-speech' ? copy.noSpeech : copy.micError;
      };
      recognition.onend = () => {
        button.classList.remove('recording');
        if (activeRecognition !== recognition) return;
        activeRecognition = null;
        if (!failed && transcript) {
          const duration = started && ended && ended > started ? ended - started : null;
          state.draft.speech[index] = speechEstimate(exam.speaking[index], transcript, duration);
          save(level, state); renderSpeech(index); updateProgress(); renderFluency();
          micStatus.textContent = '';
        } else if (!failed) micStatus.textContent = copy.noSpeech;
      };
      try { recognition.start(); }
      catch { activeRecognition = null; micStatus.textContent = copy.micError; }
    });
  });

  function showGrade(answers, saveResult) {
    let score = 0;
    const totals = Object.fromEntries(['reading', 'grammar', 'usage', 'listening'].map((name) => [name, { correct: 0, total: 0 }]));
    questions.forEach((question, index) => {
      const section = totals[question.section]; section.total += 1;
      const right = answers[index] === question.answer;
      if (right) { score += 1; section.correct += 1; }
      const fieldset = form.querySelector(`[data-question="${index}"]`);
      fieldset.querySelectorAll('.exam-option').forEach((option, optionIndex) => {
        option.classList.toggle('is-right', optionIndex === question.answer);
        option.classList.toggle('is-wrong', optionIndex === answers[index] && !right);
        option.querySelector('input').disabled = true;
      });
      const feedback = fieldset.querySelector('.exam-feedback');
      feedback.textContent = `${right ? copy.correct : copy.wrong + question.options[question.answer]} ${question.explanation}`;
      feedback.className = `exam-feedback ${right ? 'is-correct' : 'is-incorrect'}`;
    });
    submit.disabled = true; result.hidden = false;
    result.querySelector('[data-result-title]').textContent = copy.finished;
    result.querySelector('[data-result-score]').textContent = `${copy.result} ${score} ${copy.of} ${questions.length}.`;
    const grid = result.querySelector('[data-result-sections]'); grid.replaceChildren();
    Object.entries(totals).forEach(([name, values]) => {
      const card = document.createElement('div');
      const label = document.createElement('span'); label.textContent = copy[name];
      const value = document.createElement('strong'); value.textContent = `${values.correct}/${values.total}`;
      card.append(label, value); grid.appendChild(card);
    });
    renderFluency();
    if (saveResult) {
      state.last = { answers, score };
      state.best = Math.max(Number.isInteger(state.best) ? state.best : 0, score);
      save(level, state);
    }
  }
  if (state.last?.answers?.length === questions.length) showGrade(state.last.answers, false);

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (state.last) return;
    const answers = questions.map((_, index) => {
      const input = form.querySelector(`input[name="question-${index}"]:checked`);
      return input ? Number(input.value) : null;
    });
    const firstMissing = answers.indexOf(null);
    if (firstMissing >= 0) {
      error.textContent = copy.missing;
      form.querySelector(`input[name="question-${firstMissing}"]`)?.focus();
      return;
    }
    error.textContent = ''; showGrade(answers, true);
    result.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  root.querySelector('[data-exam-reset]').addEventListener('click', () => {
    if (activeRecognition) { const previous = activeRecognition; activeRecognition = null; previous.abort(); }
    if ('speechSynthesis' in window) window.speechSynthesis.cancel();
    const best = state.best;
    state = { draft: { answers: {}, writing: '', speech: {} } };
    if (Number.isInteger(best)) state.best = best;
    save(level, state);
    form.reset(); writing.value = '';
    form.querySelectorAll('input[type="radio"]').forEach((input) => { input.disabled = false; });
    form.querySelectorAll('.exam-option').forEach((option) => option.classList.remove('is-right', 'is-wrong'));
    form.querySelectorAll('.exam-feedback, .exam-speech-feedback').forEach((feedback) => { feedback.textContent = ''; feedback.className = feedback.className.replace(/ is-(correct|incorrect)/g, ''); });
    root.querySelectorAll('[data-audio-fallback]').forEach((fallback) => { fallback.textContent = ''; fallback.hidden = true; });
    submit.disabled = false; result.hidden = true; error.textContent = ''; micStatus.textContent = Recognition ? '' : copy.unavailable;
    updateProgress(); window.scrollTo({ top: 0, behavior: 'smooth' });
  });
})();
