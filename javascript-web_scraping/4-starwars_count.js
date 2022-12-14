#!/usr/bin/node

const request = require('request');

let numberApearances = 0;

function isInFilm (error, page) {
  if (error) {
    console.error('error:', error);
  }
  const JSONpage = JSON.stringify(page); // transform to JSON string
  const JSONbody = JSON.parse(JSONpage).body; // convert to dict and find body
  const characters = JSON.parse(JSONbody).characters;
  for (let i = 0; i < characters.length; i++) {
    if (characters[i] === 'https://swapi-api.hbtn.io/api/people/18/') {
      numberApearances += 1;
    }
  }
}

let filmpath = '';

let filmID = 1;
while (filmID < 8) {
  const webpage = process.argv[2] + '/' + filmID + '/';
  filmpath = request(webpage, isInFilm).path;
  console.log(filmpath, numberApearances);
  filmID++;
}

setTimeout(() => console.log(numberApearances), 500);
