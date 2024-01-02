#!/usr/bin/node
let i = 0;
const number = Number(process.argv[2]);
if (number) {
  while (i < number) {
    console.log(Array(number + 1).join('X'));
    i++;
  }
} else {
  console.log('Missing size');
}
