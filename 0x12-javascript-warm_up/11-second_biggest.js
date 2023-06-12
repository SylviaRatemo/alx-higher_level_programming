#!/usr/bin/node
const args = process.argv.slice(2);
const len = process.argv.length - 2;

if (len === 1 || len === 0) { console.log(0); } else {
  const intArray = args.map(str => Number(str)); let largest = Math.max(...intArray);
  let secondLargest = Math.min(...intArray);
  for (let i = 0; i < intArray.length; i++) {
    if (intArray[i] > largest) {
      secondLargest = largest;
      largest = intArray[i];
    } else if (intArray[i] > secondLargest && intArray[i] < largest) {
      secondLargest = intArray[i];
    }
  } console.log(secondLargest);
}
