#!/usr/bin/node
// computes the number of task completed by user id
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, res, data) {
  if (err) throw err;
  const dict = JSON.parse(data);
  const newdict = {};
  for (const users of dict) {
    const newid = users.userId;
    if (users.completed) {
      if (newid in newdict) {
        newdict[newid]++;
      } else {
        newdict[newid] = 1;
      }
    }
  }
  console.log(newdict);
});
