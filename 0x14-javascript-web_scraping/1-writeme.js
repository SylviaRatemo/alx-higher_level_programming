#!/usr/bin/node
// write file passed as arg
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], (err) => {
  err && console.log(err);
});
