#!/usr/bin/node
const _list = require('100-data.js').list;
const newlist = _list.map(
  function (num, index) {
    return num * index;
  }
);
console.log(_list);
console.log(newlist);
