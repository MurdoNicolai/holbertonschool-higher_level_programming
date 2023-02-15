#!/usr/bin/node

$('#toggle_header').on('click', function () {
  alert($('header').toggleClass('green'));
  alert($('header').toggleClass('red'));
});
