#!/usr/bin/node
const { list } = require('./100-data');
const newList = list.map((i, index) => {
  return i * index;
});
console.log(list);
console.log(newList);
