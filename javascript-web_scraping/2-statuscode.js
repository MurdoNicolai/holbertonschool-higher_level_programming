#!/usr/bin/node

const request = require('request');

const webpage = process.argv[2];
request(webpage, function (error, response) {
  if (error) {
    console.error('error:', error);
  }
  console.log('code:', response && response.statusCode);
});
