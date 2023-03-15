#!/usr/bin/node
const fs = require('fs');
const fileA = require('process.argv[3]');
const fileB = require('process.argv[4]');
fs.readfile(process.argv[3], 'utf8', (err, data) => {
  if (err) throw err;
  fs.writeFile('process.argv[5]', data, (err) => {
    if (err) throw err;
  });
});
fs.readfile(process.argv[4], 'utf8', (err, data) => {
  if (err) throw err;
  fs.writeFile('process.argv[5]', data, (err) => {
    if (err) throw err;
  });
});
