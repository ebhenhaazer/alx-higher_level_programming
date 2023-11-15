#!/usr/bin/node
// JS to check arguments passed into script
'use strict';
if (process.argv[3]) {
  console.log('Arguments found');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
