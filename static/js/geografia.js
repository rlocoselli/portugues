(function () {
  'use strict';
  var dataNode = document.getElementById('geo-data');
  if (!dataNode) return;
  var data = JSON.parse(dataNode.textContent);
  var states = Object.fromEntries(data.states.map(function (state) { return [state.sigla, state]; }));
  var paths = Array.from(document.querySelectorAll('.map-state'));
  var filters = Array.from(document.querySelectorAll('[data-region-filter]'));
  var select = document.getElementById('geo-state-select');
  var infoEyebrow = document.querySelector('[data-info-eyebrow]');
  var infoTitle = document.querySelector('[data-info-title]');
  var infoDescription = document.querySelector('[data-info-description]');
  var facts = document.querySelector('[data-state-facts]');
  var infoCapital = document.querySelector('[data-info-capital]');
  var infoRegion = document.querySelector('[data-info-region]');
  var gameAction = document.querySelector('[data-game-action]');
  var gamePrompt = document.querySelector('[data-game-prompt]');
  var gameFeedback = document.querySelector('[data-game-feedback]');
  var activeRegion = 'all';
  var selectedCode = '';
  var game = { targets: [], round: -1, score: 0, awaiting: false };

  function regionName(code) { return data.regions[code][data.lang]; }

  function renderMap() {
    paths.forEach(function (path) {
      var isSelected = path.dataset.state === selectedCode;
      path.classList.toggle('is-selected', isSelected);
      path.classList.toggle('is-muted', activeRegion !== 'all' && path.dataset.region !== activeRegion);
      path.setAttribute('aria-pressed', String(isSelected));
    });
    filters.forEach(function (button) {
      var active = button.dataset.regionFilter === activeRegion;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
  }

  function showRegion(code) {
    activeRegion = code;
    selectedCode = '';
    select.value = '';
    infoEyebrow.textContent = data.copy.region;
    infoTitle.textContent = code === 'all' ? data.copy.all : regionName(code);
    infoDescription.textContent = code === 'all' ?
      (data.lang === 'fr' ? 'Choisissez une région ou un État sur la carte.' : 'Escolha uma região ou um estado no mapa.') :
      data.regions[code]['description_' + data.lang];
    facts.hidden = true;
    renderMap();
  }

  function showState(code) {
    var state = states[code];
    if (!state) return;
    selectedCode = code;
    activeRegion = state.regiao;
    select.value = code;
    infoEyebrow.textContent = data.copy.state;
    infoTitle.textContent = state.nome + ' · ' + code;
    infoDescription.textContent = data.regions[state.regiao]['description_' + data.lang];
    infoCapital.textContent = state.capital;
    infoRegion.textContent = regionName(state.regiao);
    facts.hidden = false;
    renderMap();
    answerGame(code);
  }

  filters.forEach(function (button) {
    button.addEventListener('click', function () { showRegion(button.dataset.regionFilter); });
  });
  paths.forEach(function (path) {
    path.addEventListener('click', function () { showState(path.dataset.state); });
    path.addEventListener('keydown', function (event) {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        showState(path.dataset.state);
      }
    });
  });
  select.addEventListener('change', function () {
    if (select.value) showState(select.value);
    else showRegion(activeRegion);
  });

  function beginGame() {
    var shuffled = data.states.slice();
    for (var i = shuffled.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var temp = shuffled[i]; shuffled[i] = shuffled[j]; shuffled[j] = temp;
    }
    game.targets = shuffled.slice(0, 5);
    game.round = 0;
    game.score = 0;
    nextRound();
  }

  function nextRound() {
    game.awaiting = true;
    gameFeedback.textContent = '';
    paths.forEach(function (path) { path.classList.remove('is-answer'); });
    showRegion('all');
    var target = game.targets[game.round];
    gamePrompt.textContent = data.copy.gameRound + ' ' + (game.round + 1) + '/5 · ' +
      data.copy.gameCapital + ' ' + target.capital + '?';
    gameAction.hidden = true;
  }

  function answerGame(code) {
    if (!game.awaiting) return;
    game.awaiting = false;
    var target = game.targets[game.round];
    var correct = code === target.sigla;
    if (correct) game.score++;
    else document.getElementById('geo-' + target.sigla).classList.add('is-answer');
    gameFeedback.textContent = correct ?
      data.copy.gameCorrect + ' ' + target.nome + '! ' + data.copy.gameScore + ': ' + game.score + '/5.' :
      data.copy.gameWrong + ' ' + states[code].nome + '. ' + data.copy.gameAnswer + ' ' + target.nome + '. ' + data.copy.gameScore + ': ' + game.score + '/5.';
    if (game.round === 4) {
      gamePrompt.textContent = data.copy.gameDone + ' ' + data.copy.gameScore + ': ' + game.score + '/5.';
      gameAction.textContent = data.copy.gameRestart;
    } else {
      gameAction.textContent = data.copy.gameNext;
    }
    gameAction.hidden = false;
  }

  gameAction.addEventListener('click', function () {
    if (game.round < 0 || game.round === 4) beginGame();
    else { game.round++; nextRound(); }
  });
  renderMap();
})();
