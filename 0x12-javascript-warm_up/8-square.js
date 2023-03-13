#!/usr/bin/node
const size = process.argv[2];
if (!parseInt(size)) {
  console.log('Missing size');
}
for (let row = 0; row < size; row++) {
  let output = '';
  for (let column = 0; column < size; column++) {
    output += 'X';
  }
  console.log(output);
}
