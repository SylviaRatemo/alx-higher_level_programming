#!/usr/bin/node
// read file content
const fs = require('fs');
function readAndPrintFile(filePath) {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

// Usage
if (process.argv.length < 3) {
  console.error("Please provide the file path as a command-line argument.");
} else {
  const filePath = process.argv[2];
  readAndPrintFile(filePath);
}
