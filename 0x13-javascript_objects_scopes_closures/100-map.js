#!/usr/bin/node
const data = require('./100-data.js');

console.log(data.list);
const processedData = data.list.map((item, index) => {
  return item * index;
});

console.log(processedData);
