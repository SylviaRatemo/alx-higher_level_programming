#!/usr/bin/node
const parentSquare = require('./5-square');
class Square extends parentSquare {
  charPrint (c) {
    if (typeof c === 'undefined') { 
      c = 'X';
    }
    process.stdout.write((c.repeat(this.width) + '\n').repeat(this.height));
  }
}

module.exports = Square;
