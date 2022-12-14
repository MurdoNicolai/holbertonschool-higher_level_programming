#!/usr/bin/node

const request = require('request');

function printCharacterInFilm (error, page) {
  if (error) {
    console.error('error:', error);
  }
  const JSONpage = JSON.stringify(page); // transform to JSON string
  const JSONbody = JSON.parse(JSONpage).body; // convert to dict and find body
  // find caracters of film given as input, convert to list
  const characters = JSON.parse(JSONbody).results[process.argv[2]].characters;
  for (let characterLink = 0; characterLink < characters.length; characterLink++) {
    request(characters[characterLink], getname); // print character name using link
  }
}

// print name of character with given link
function getname (error, page) {
  if (error) {
    console.error('error:', error);
  }
  const JSONpage = JSON.stringify(page); // transform to JSON string
  const JSONbody = JSON.parse(JSONpage).body; // convert to dict and find body
  console.log(JSON.parse(JSONbody).name);
}
const webpage = 'https://swapi-api.hbtn.io/api/films';
request(webpage, printCharacterInFilm);
