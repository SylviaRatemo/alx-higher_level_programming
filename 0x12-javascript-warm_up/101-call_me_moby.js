#!/usr/bin/node
exports.callMeMoby = function callMeMoby (a, func) {
  while (a-- > 0) { func(); }
};
