#!/usr/bin/node

const request = require('request');
const filesystem = require('fs');

const fileName = process.argv[3];
const webpage = process.argv[2];

request(webpage, getBody);

function getBody (error, page) {
  if (error) {
    console.error('error:', error);
  }
  const input = page.body;
  filesystem.writeFile(fileName, input, writeFile);
}

const writeFile = (error) => {
  if (error) {
    console.log(error);
  }
};
