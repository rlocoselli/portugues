(function () {
  'use strict';
  var shell = document.querySelector('[data-guide-player]');
  var player = document.getElementById('guide-audio');
  var now = document.querySelector('[data-guide-now]');
  var stop = document.querySelector('[data-guide-stop]');
  if (!shell || !player) return;
  var activeButton = null;
  var fallbackUsed = false;

  function reset() {
    player.pause();
    player.removeAttribute('src');
    player.load();
    if ('speechSynthesis' in window) window.speechSynthesis.cancel();
    if (activeButton) activeButton.setAttribute('aria-pressed', 'false');
    activeButton = null;
    shell.classList.remove('is-speech-fallback');
    shell.hidden = true;
  }

  function fallback() {
    if (fallbackUsed || !activeButton || !('speechSynthesis' in window)) return;
    fallbackUsed = true;
    player.pause();
    shell.classList.add('is-speech-fallback');
    now.textContent += ' · ' + shell.dataset.fallbackLabel;
    var currentButton = activeButton;
    var utterance = new SpeechSynthesisUtterance(currentButton.dataset.speechText);
    utterance.lang = activeButton.dataset.speechLang;
    utterance.rate = 0.92;
    utterance.onend = function () { if (activeButton === currentButton) reset(); };
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(utterance);
  }

  document.querySelectorAll('[data-guide-audio]').forEach(function (button) {
    button.setAttribute('aria-pressed', 'false');
    button.addEventListener('click', function () {
      if (activeButton === button) { reset(); return; }
      reset();
      activeButton = button;
      fallbackUsed = false;
      button.setAttribute('aria-pressed', 'true');
      var card = button.closest('.indicator-card, .variety-card, .history-era-card');
      var title = card && card.querySelector('h2, .indicator-top span');
      now.textContent = (title ? title.textContent.trim() + ' · ' : '') + button.textContent.trim();
      shell.hidden = false;
      player.src = button.dataset.guideAudio;
      player.load();
      var playing = player.play();
      if (playing && playing.catch) playing.catch(fallback);
    });
  });
  player.addEventListener('error', fallback);
  player.addEventListener('ended', reset);
  stop.addEventListener('click', reset);
})();
