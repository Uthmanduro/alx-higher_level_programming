#!/usr/bin/node
// prints the title of a starwars movie where the episode number matches
// a given integer
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request.get(url, function (err, response, data) {
  if (err) throw err;
  const res = JSON.parse(data);
  console.log(res.title);
});
