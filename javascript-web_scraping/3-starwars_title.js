#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2];
const webpage = 'https://swapi-api.hbtn.io/api/films/' + filmNum + '/';

request(webpage, getFilm);

function getFilm (error, page) {
  if (error) {
    console.error('error:', error);
  }
  const JSONpage = JSON.stringify(page); // transform to JSON
  const JSONbody = JSON.parse(JSONpage).body; // convert to dict and find body
  const title = JSON.parse(JSONbody).title; // convert to dict and find title
  console.log(title);
}
