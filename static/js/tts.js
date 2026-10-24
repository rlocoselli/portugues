/* Reprodução de áudio — usa arquivos MP3 gerados no servidor (gTTS). */
(function () {
  'use strict';

  function playUrl(url) {
    var player = document.getElementById('audio-player');
    if (!player || !url) { return; }
    player.src = url;
    player.load();
    var p = player.play();
    if (p && p.catch) { p.catch(function () {}); }
  }

  function initTextoPage() {
    var frases = document.querySelectorAll('.frase');
    for (var i = 0; i < frases.length; i++) {
      (function (el) {
        el.addEventListener('click', function () {
          playUrl(el.getAttribute('data-src'));
        });
      })(frases[i]);
    }

    var palavras = document.querySelectorAll('.vocab-word');
    for (var j = 0; j < palavras.length; j++) {
      (function (el) {
        el.addEventListener('click', function () {
          playUrl(el.getAttribute('data-src'));
        });
      })(palavras[j]);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTextoPage);
  } else {
    initTextoPage();
  }
})();
