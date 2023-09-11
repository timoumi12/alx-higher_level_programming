#!/usr/bin/node
const size = Number(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  let x = '';
  for (let j = 0; j < size; j++) {
    x += 'X';
  }
  console.log(x);
}
