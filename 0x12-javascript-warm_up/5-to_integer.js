#!/usr/bin/node
// prints number if argument can be converted to number
let no = process.argv.slice(2)[0];
no = parseInt(no);
if (isNaN(no)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + no);
}
