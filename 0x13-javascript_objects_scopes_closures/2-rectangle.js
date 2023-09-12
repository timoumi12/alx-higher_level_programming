#!/usr/bin/node
export class Rectangle {
  Rectangle (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}