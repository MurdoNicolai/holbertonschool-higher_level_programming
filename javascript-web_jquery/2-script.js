#!/usr/bin/node

$('#red_header').on('click', function () {
  alert($('header').css('color', '#FF0000'));
});
