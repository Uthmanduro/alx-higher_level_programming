#!/usr/bin/node
const Boss = require('./5-square');

class Square extends Boss {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let output = '';
      for (let j = 0; j < this.width; j++) {
        if (!c) {
          output += 'X';
        } else {
          output += c;
        }
      }
      console.log(output);
    }
  }
}
module.exports = Square;
