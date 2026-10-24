/* Interactive, client-side comprehension quiz for each reading. */
(function () {
  'use strict';

  var copy = document.documentElement.lang === 'fr' ? {
    correct: 'Bonne réponse !',
    wrong: 'Pas encore. Bonne réponse : ',
    score: 'Vous avez trouvé',
    of: 'sur',
    questions: 'questions',
    missing: 'Répondez à toutes les questions avant de vérifier.'
  } : {
    correct: 'Correto!',
    wrong: 'Ainda não. Resposta certa: ',
    score: 'Você acertou',
    of: 'de',
    questions: 'perguntas',
    missing: 'Responda a todas as perguntas antes de conferir.'
  };

  function initQuiz(root) {
    var form = root.querySelector('.quiz-form');
    var dataNode = root.querySelector('.quiz-data');
    var result = root.querySelector('.quiz-result');
    if (!form || !dataNode || !result) return;

    var questions;
    try {
      questions = JSON.parse(dataNode.textContent);
    } catch (error) {
      return;
    }

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var answers = [];
      for (var i = 0; i < questions.length; i++) {
        var selected = form.querySelector('input[name="question-' + i + '"]:checked');
        if (!selected) {
          result.textContent = copy.missing;
          result.className = 'quiz-result is-incomplete';
          return;
        }
        answers.push(Number(selected.value));
      }

      var score = 0;
      var lang = document.documentElement.lang === 'fr' ? 'fr' : 'pt';
      var fieldsets = form.querySelectorAll('.quiz-question');
      for (var j = 0; j < questions.length; j++) {
        var right = questions[j].resposta;
        var feedback = fieldsets[j].querySelector('.quiz-feedback');
        var options = fieldsets[j].querySelectorAll('.quiz-option');
        for (var k = 0; k < options.length; k++) {
          options[k].classList.remove('is-right', 'is-wrong');
          if (k === right) options[k].classList.add('is-right');
          if (k === answers[j] && k !== right) options[k].classList.add('is-wrong');
        }
        if (answers[j] === right) {
          score++;
          feedback.textContent = copy.correct;
          feedback.className = 'quiz-feedback is-correct';
        } else {
          feedback.textContent = copy.wrong + questions[j]['opcoes_' + lang][right];
          feedback.className = 'quiz-feedback is-incorrect';
        }
      }
      result.textContent = copy.score + ' ' + score + ' ' + copy.of + ' ' + questions.length + ' ' + copy.questions + '.';
      result.className = 'quiz-result ' + (score === questions.length ? 'is-perfect' : 'is-scored');
    });

    form.addEventListener('reset', function () {
      window.setTimeout(function () {
        result.textContent = '';
        result.className = 'quiz-result';
        var feedback = form.querySelectorAll('.quiz-feedback');
        var options = form.querySelectorAll('.quiz-option');
        for (var i = 0; i < feedback.length; i++) {
          feedback[i].textContent = '';
          feedback[i].className = 'quiz-feedback';
        }
        for (var j = 0; j < options.length; j++) {
          options[j].classList.remove('is-right', 'is-wrong');
        }
      }, 0);
    });
  }

  var quizzes = document.querySelectorAll('[data-quiz]');
  for (var i = 0; i < quizzes.length; i++) initQuiz(quizzes[i]);
})();
