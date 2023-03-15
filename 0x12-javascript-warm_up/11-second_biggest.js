#!/usr/bin/node
let count = 2;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = [];
  while (process.argv[count]) {
    arr.unshift(Number(process.argv[count]));
    count++;
  }
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
