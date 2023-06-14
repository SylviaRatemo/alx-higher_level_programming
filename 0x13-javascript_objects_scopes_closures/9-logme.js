#!/usr/bin/node
exports.logMe = function (item) {
  this.times = (this.times || 0) + 1;
  console.log(this.times + ': ' + item);
};
