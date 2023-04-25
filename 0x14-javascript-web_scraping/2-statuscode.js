#!/usr/bin/node
//a nodejs script that displays the status of a code of a get request
//import the request module
const request = require('request');

//get the comman line argument
const url = process.argv[3];

request.get(url, function (err, res, body) {
    if (err) throw err;
    console.log("code: " + res.statusCode);
});
