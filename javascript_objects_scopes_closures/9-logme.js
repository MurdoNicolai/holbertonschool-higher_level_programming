#!/usr/bin/node

let arg = 0;
exports.logMe = function (item) {
/* a function that prints the number of arguments already printed and
the new argument value. */
  console.log(arg + ': ' + item);
  arg += 1;
};
