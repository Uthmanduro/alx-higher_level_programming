#!/usr/bin/node
// gets the content of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

request.get(url, function (err, response, data) {
  if (err) throw err;
  fs.writeFile(filepath, data, 'utf-8', (err) => {
    if (err) throw err;
  });
});
