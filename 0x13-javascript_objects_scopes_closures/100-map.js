#!/usr/bin/node
const data = require('./100-data.js');

console.log(data.list);
const processedData = data.list.map((item, index) => {
  if (index > 0) {
    const previousItem = data.list[index - 1];
    return item * previousItem;
  }

  return 0;
});

console.log(processedData);
