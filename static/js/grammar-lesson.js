document.querySelectorAll('[data-speak-example]').forEach((button) => {
  button.addEventListener('click', () => {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(button.dataset.speakExample);
    utterance.lang = 'pt-BR';
    window.speechSynthesis.speak(utterance);
  });
});
