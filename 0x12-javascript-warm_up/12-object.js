#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
const newValue = 'value';
myObject[newValue] = 89;
console.log(myObject);
