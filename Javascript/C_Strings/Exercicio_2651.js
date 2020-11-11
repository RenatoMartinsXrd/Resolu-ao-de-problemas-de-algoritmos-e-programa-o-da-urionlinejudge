var input = require("./readFile.js").input;
var lines = input.split('\n');


var a = lines.shift().toLowerCase().indexOf("zelda");
a==-1?console.log("Link Tranquilo") : console.log("Link Bolado");
