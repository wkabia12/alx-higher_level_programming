#!/usr/bin/node
// print x times C is fun
let x = process.argv.slice(2)[0];
x = parseInt(x);
if (isNaN(x)) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
