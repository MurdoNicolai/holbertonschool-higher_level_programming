#!/usr/bin/node

const request = require('request');

let numberApearances = 0;

function NumberInFilms (error, page) {
  if (error) {
    console.error('error:', error);
  }
  const JSONpage = JSON.stringify(page); // transform to JSON string
  const JSONbody = JSON.parse(JSONpage).body; // convert to dict and find body
  // const JSONbody = page;
  for (let idFilm = 0; idFilm < JSON.parse(JSONbody).results.length; idFilm++) {
    const characters = JSON.parse(JSONbody).results[idFilm].characters;
    for (let i = 0; i < characters.length; i++) {
      if (characters[i].endsWith('/18/')) {
        numberApearances += 1;
      }
    }
  }
}

const webpage = process.argv[2];
request(webpage, NumberInFilms);

// setTimeout(() => console.log(numberApearances), 1000);

// const filesystem = require('fs');

// const filename = process.argv[2];

// filesystem.readFile(filename, 'utf-8', NumberInFilms);

setTimeout(() => console.log(numberApearances), 1000);
