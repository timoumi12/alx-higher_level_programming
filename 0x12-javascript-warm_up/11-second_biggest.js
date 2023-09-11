#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number).sort();
  console.log(args[args.length - 2]);
}
