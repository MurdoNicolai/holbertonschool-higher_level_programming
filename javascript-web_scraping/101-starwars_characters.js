#!/usr/bin/node

const request = require('request');

async function printCharacterInFilm (error, page) {
  if (error) {
    console.error('error:', error);
  }
  const JSONpage = JSON.stringify(page); // transform to JSON string
  const JSONbody = JSON.parse(JSONpage).body; // convert to dict and find body
  // find caracters of film given as input, convert to list
  const characters = JSON.parse(JSONbody).results[process.argv[2] - 1].characters;
  for (let characterLink = 0; characterLink < characters.length; characterLink++) {
    // print character name using link, "characterLink * 50" sets a  extra delay on each print so they print in order
    setTimeout(request, characterLink * 50, characters[characterLink], getname);
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
