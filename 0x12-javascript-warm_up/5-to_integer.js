#!/usr/bin/node
const nb = Number(process.argv[2]);
console.log(isNaN(nb) ? 'Not a number' : 'My number: ' + nb);
