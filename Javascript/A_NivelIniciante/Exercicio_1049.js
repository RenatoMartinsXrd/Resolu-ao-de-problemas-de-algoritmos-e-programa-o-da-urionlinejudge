var input = require("./readFile.js").input;
var lines = input.split('\n');
var arvore = {"vertebrado":{"ave":{"carnivoro":"aguia","onivoro":"pomba"},"mamifero":
{"onivoro":"homem","herbivoro":"vaca"}},"invertebrado":{"inseto":{"hematofago":"pulga","herbivoro":"lagarta"},"anelideo":
{"hematofago":"sanguessuga","onivoro":"minhoca"}}}
console.log((arvore[lines[0].trim()][lines[1].trim()][lines[2].trim()] || 0))