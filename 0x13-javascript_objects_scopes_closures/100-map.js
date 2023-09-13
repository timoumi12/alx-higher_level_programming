#!/usr/bin/node
const _list = require('100-data.js').list;
const newlist = _list.map(
  function (value, i) {
    return i * value;
  }
);
console.log(_list);
console.log(newlist);
