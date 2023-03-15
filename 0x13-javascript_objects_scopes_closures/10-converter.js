#!/usr/bin/node
exports.converter = function (base) {
  return (num) => {
    return parseInt(num, 10).toString(base);
  };
}
