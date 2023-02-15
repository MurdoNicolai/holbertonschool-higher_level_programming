#!/usr/bin/node

/* Analysis of string that is done in argument */
const b = parseInt(process.argv[2]);
/* if b is not a number, print 'Missin...' */
if (isNaN(b)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < b; i++) {
    console.log('C is fun');
  }
}
