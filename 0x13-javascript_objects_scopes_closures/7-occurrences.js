#!/usr/bin/Node
// returns number of ocurrencies
exports.nbOccurences = function (list, query) {
  if (Array.isArray(list)) {
    let occurrences = 0;
    for (let i = 0; i < list.length; i++) {
      if (query === list[i]) {
        occurrences += 1;
      }
    }
    return occurrences;
  }
};
