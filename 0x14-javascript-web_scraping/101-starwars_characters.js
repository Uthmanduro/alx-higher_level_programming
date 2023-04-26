#!/usr/bin/node
// prints all characters of a starwars movie
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';
request.get(url, function (err, response, data) {
  if (err) throw err;
  const body = JSON.parse(data);
  const chars = body.characters;
  for (let links = 0; links < chars.length; links++) {
    const newurl = chars[links];
    request.get(newurl, function (err, response, data) {
      if (err) throw err;
      const newbody = JSON.parse(data);
      console.log(newbody.name);
    });
  }
});
