#!/usr/bin/node

function getSecondMax(array) {
  let max = 0;
  let maxPosition = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] > max) {
      max = array[i];
      maxPosition = i;
    }
  }
  max = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] > max && i !== maxPosition) {
      max = array[i];
    }
  }
  return max;
}

console.log(getSecondMax([1, 5, 3, 9, 8, -1]));
