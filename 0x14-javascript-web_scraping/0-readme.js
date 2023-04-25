#!/usr/bin/node
// a nodejs script that reades and prints the content of a file
const fs = require('fs');
const filepath = process.argv[2];

fs.readFile(filepath, 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
