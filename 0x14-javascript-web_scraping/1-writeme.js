#!/usr/bin/node
//a nodejs script that writes to a file

//import the module that reads and write file
const fs = require('fs');

//get the command line arguments
const filepath = process.argv[2];
const filecontent = process.argv[3];

//write the file
fs.writeFile(filepath, filecontent, 'utf-8', (err) => {
    if (err) throw err;
});
