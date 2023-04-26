#!/usr/bin/node
// computes the number of task completed by user id
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, res, data) {
  const dict = JSON.parse(data);
  let newdict = {};
  let count = 0;
  for (const users of dict) {
    let newid = users.userId;
    if (newid in newdict && users.completed === true)
      newdict[newid] = count++;
    else if (!(newid in newdict))
      newdict[newid] = count;
  }
  console.log(newdict);
});
