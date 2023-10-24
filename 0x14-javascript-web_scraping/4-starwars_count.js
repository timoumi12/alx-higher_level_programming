#!/usr/bin/node
// request object
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  let i = 0;
  const data = JSON.parse(body).results;
  for (const movie of data) {
    if (movie.characters.find((character) => character.endsWith('/18/'))) { i++; }
  }
  console.log(i);
});
