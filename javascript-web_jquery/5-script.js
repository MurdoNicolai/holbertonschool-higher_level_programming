#!/usr/bin/node

$('#add_item').on('click', function () {
  alert($('ul.my_list').append('<li></li>'));
});
