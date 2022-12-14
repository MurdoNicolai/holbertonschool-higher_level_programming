#!/usr/bin/node

const request = require('request');

let numberApearances = 0;

function NumberInFilms (error, page) {
  if (error) {
    console.error('error:', error);
  }
  const JSONpage = JSON.stringify(page); // transform to JSON string
  const JSONbody = JSON.parse(JSONpage).body; // convert to dict and find body
  for (let idFilm = 0; idFilm < 7; idFilm++) {
    const characters = JSON.parse(JSONbody).results[idFilm].characters;
    for (let i = 0; i < characters.length; i++) {
      if (characters[i] === 'https://swapi-api.hbtn.io/api/people/18/') {
        numberApearances += 1;
      }
    }
  }
}

const webpage = process.argv[2];
request(webpage, NumberInFilms);

setTimeout(() => console.log(numberApearances), 5000);
