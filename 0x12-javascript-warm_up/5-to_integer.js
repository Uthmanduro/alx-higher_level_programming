#!/usr/bin/node
const value = process.argv[2];
const output = parseInt(value);
if (!output) {
  console.log('Not a number');
} else {
  console.log('My number: ' + output);
}
