#!/usr/bin/node
function factorial (b) {
  if (isNaN(b) || b < 2) { return 1; } else { return (b * factorial(b - 1)); }
}

console.log(factorial(process.argv[2]));
