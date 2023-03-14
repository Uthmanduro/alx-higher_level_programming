#!/usr/bin/node
const argument = parseInt(process.argv[2]);
function factorial (arg) {
  if (!arg) {
    return (1);
  }
  return (arg * factorial(arg - 1));
}

console.log(factorial(argument));
