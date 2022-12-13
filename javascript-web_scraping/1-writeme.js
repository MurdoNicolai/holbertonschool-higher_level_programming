#!/usr/bin/node
const filesystem = require('fs');

const filename = process.argv[2];
const input = process.argv[3];

const writeFile = (error) => {
  if (error) {
    console.log(error);
  }
};

filesystem.writeFile(filename, input, writeFile);
