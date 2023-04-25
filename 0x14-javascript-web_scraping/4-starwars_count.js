#!/usr/bin/node
// prints the number of movies where char "Wedge Antilles" is present
const request = require('request');

const url = process.argv[2];
request.get(url, function (err, res, data) {
  if (err) throw err;
  const response = JSON.parse(data);
  let count = 0;
  for (const i of response.results) {
    if (i.characters) {
      for (const chars of i.characters) {
        if (chars === 'https://swapi-api.alx-tools.com/api/people/18/') {
          count++;
        }
      }
    }
  }
  console.log(count);
});
