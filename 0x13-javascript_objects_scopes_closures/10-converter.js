#!/usr/bin/node
exports.converter = function (base) {
  parser (num) {
    let number = parseInt(num, 10).toString(base);
    console.log(number);
  }  
}
