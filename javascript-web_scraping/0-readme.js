#!/usr/bin/node
const filesystem = require('fs');

const filename = process.argv[2];

const printFile = (error, fileContent) => {
  if (error) {
    console.log(error);
  } else {
    console.log(fileContent);
  }
};

filesystem.readFile(filename, 'utf-8', printFile);
