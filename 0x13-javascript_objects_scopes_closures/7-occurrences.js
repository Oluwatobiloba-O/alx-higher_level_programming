#!/usr/bin/node

// returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
    let count = 0;
  
    for (let i = 0; i < list.length; i++) {
      if (list[i] === searchElement) {
        count = count + 1;
      }
    }
  
    return count;
  };