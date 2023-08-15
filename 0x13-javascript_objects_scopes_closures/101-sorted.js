#!/usr/bin/node
// imports a dict and computes a dict by ocurrences
const dict = require('./101-data').dict;
const newDict = {};
let list1 = [];
for (const [key, value] of Object.entries(dict)) {
  if (!(value in newDict)) {
    list1 = [];
  } else {
    list1 = newDict[value];
  }
  list1.push(key);
  newDict[value] = list1;
}
console.log(newDict);
