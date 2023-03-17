#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  for (let i = 0; i < list.length; i++) {
    arr.unshift(list[i]);
  }
  return (arr);
};
