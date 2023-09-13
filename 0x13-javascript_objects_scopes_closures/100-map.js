#!/usr/bin/node
const list = require('100-data.js').list;
const newlist = list.map(
  function (value, i) {
    return i * value;
  }
);
console.log(list);
console.log(newlist);
