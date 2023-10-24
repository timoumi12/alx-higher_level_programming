#!/usr/bin/node
// request object
const request = require('request');
request(process.argv[2], function (error, response) {
  console.log(`code: ${response.statusCode}`);
});
