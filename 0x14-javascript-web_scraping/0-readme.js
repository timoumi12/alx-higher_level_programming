#!/usr/bin/node
// file system object
const fs = require('fs');

// read file
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
