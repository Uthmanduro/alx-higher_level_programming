#!/usr/bin/node
const list = require('./100-data');
const newList = list.map((i, index) => {
   i * index;
});
consloe.log(list);
console.log(newList);
