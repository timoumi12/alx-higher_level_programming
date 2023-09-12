#!/usr/bin/node
exports.esrever = function (list) {
  const _list = [];
  for (let i = list.length - 1; i >= 0; i--) {
    _list.push(list[i]);
  }
  return _list;
};
