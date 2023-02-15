#!/usr/bin/node

$(function () {
  const webpage = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.get(webpage, getName, dataType = 'Json');
});

// request(webpage, getName);
// const request = require('request');

// const webpage = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
// let charName = 'nope';

// function getName (error, page) {
//   if (error) {
//     console.error('error:', error);
//   }
//   const JSONbody = JSON.parse(page.body); // convert to dict and find body
//   charName = JSONbody.name; // convert to dict and find name
// }
// console.log(charName);

function getName (data, status) {
  if (status !== 'success') {
    console.error('error:', error);
  }
  alert("Data: " + data + "\nStatus: " + status);
  $('#character').html(data);
  const JSONbody = JSON.parse(page.body); // convert to dict and find body
  const charName = JSONbody.name; // convert to dict and find name
  $('#character').html('charName');
}
