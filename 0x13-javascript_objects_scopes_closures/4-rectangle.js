#!/usr/bin/node
class Rectangle {
  constructor (w, h) { if (w > 0 && h > 0) { this.width = w; this.height = h; } }
  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let k = 0; k < this.width; k++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () { const temp = this.width; this.width = this.height; this.height = temp; }
  double () { this.width = 2 * this.width; this.height = 2 * this.height; }
}
module.exports = Rectangle;
