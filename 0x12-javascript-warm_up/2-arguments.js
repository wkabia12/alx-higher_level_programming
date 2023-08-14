#!/usr/bin/node
// prints a message depending of number of args passed
const no_Args = process.argv.slice(2).length;
if (no_Args === 0) {
  console.log('No argument');
} else if (no_Args === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
