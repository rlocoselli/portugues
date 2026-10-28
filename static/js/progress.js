(function () {
  'use strict';
  var key = 'fala-brasil-completed-v1';
  var completed = {};
  try { completed = JSON.parse(localStorage.getItem(key) || '{}') || {}; } catch (error) { completed = {}; }

  function update() {
    var count = document.querySelector('[data-completed-count]');
    if (count) count.textContent = Object.keys(completed).filter(function (slug) { return completed[slug]; }).length;
    document.querySelectorAll('[data-lesson-card]').forEach(function (card) {
      card.classList.toggle('is-complete', !!completed[card.getAttribute('data-lesson-card')]);
    });
    var lesson = document.querySelector('[data-lesson]');
    var button = document.querySelector('[data-mark-complete]');
    if (lesson && button) {
      var done = !!completed[lesson.getAttribute('data-lesson')];
      button.textContent = done ? button.dataset.labelDone : button.dataset.labelDefault;
      button.setAttribute('aria-pressed', String(done));
      button.classList.toggle('is-done', done);
    }
  }

  var button = document.querySelector('[data-mark-complete]');
  if (button) button.addEventListener('click', function () {
    var slug = document.querySelector('[data-lesson]').getAttribute('data-lesson');
    completed[slug] = !completed[slug];
    try { localStorage.setItem(key, JSON.stringify(completed)); } catch (error) { /* Private browsing may disable storage. */ }
    update();
  });
  update();
})();
