#!/usr/bin/node
// export a function that executes a function and increments by 1
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
