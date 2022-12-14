#!/usr/bin/node

const request = require('request');

const usersTasksCompleted = {};

function NumbercompletedTasks (error, page) {
  if (error) {
    console.error('error:', error);
  }
  const JSONpage = JSON.stringify(page); // transform to JSON string
  const JSONbody = JSON.parse(JSON.parse(JSONpage).body); // convert to dict and find body
  for (let i = 0; i < JSONbody.length; i++) { // go through body to find users
    if (isNaN(usersTasksCompleted[JSONbody[i].userId])) {
      usersTasksCompleted[JSONbody[i].userId] = 1;
    } else if (JSONbody[i].completed) {
      usersTasksCompleted[JSONbody[i].userId] += 1;
    }
  }
}

const webpage = process.argv[2];
request(webpage, NumbercompletedTasks);

setTimeout(() => console.log(usersTasksCompleted), 1000);
