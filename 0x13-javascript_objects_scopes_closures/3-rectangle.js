#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      let x = '';
      for (let j = 0; j < this.height; j++) {
        x += 'X';
      }
      console.log(x);
    }
  }
}
module.exports = Rectangle;
