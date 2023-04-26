#!/usr/bin/node
// prints all characters of a starwars movie
const request = require('request');
const { promisify } = require('util');
const promisifiedRequest = promisify(request);

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';

(async function () {
  try {
    const body = await promisifiedRequest(url);
    const chars = JSON.parse(body.body);
    for (const links of chars.characters) {
      const newreq = await promisifiedRequest(links);
      const newbody = JSON.parse(newreq.body);
      console.log(newbody.name);
    }
  } catch (err) {
    console.error(err);
  }
})();
