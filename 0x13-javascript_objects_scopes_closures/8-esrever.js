#!/usr/bin/node
exports.esrever = function (list) {
  const myList = [];
  let k = 0;
  for (let i = list.length - 1; i > -1; i--) {
    myList[k] = list[i];
    k++;
  }

  return myList;
};
