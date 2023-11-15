#!/usr/bin/node
//console.log(process.argv.length < 4 ? 0 : process.argv.slice(2).sort((a, b) => b - a)[1]);
//#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  console.log(process.argv.splice(2, process.argv.length - 1).sort().reverse()[1]);
}
