#!/usr/bin/node
let count = 2;
let highest = 0;
if (process.argv.length <= 2) {
  console.log(0);
} else {
  while (process.argv[count]) {
    let value = process.argv[count];
    if (highest > value) {
      continue;
    } else {
      highest = value;
    }
    count++;
  }
  console.log(highest);
}
