let sentance='a new sentance.';

console.log(typeof sentance);

let includenew= sentance.includes('new')
console.log(includenew)

console.log(sentance[4])

let startwithA = sentance.startsWith('A')
console.log(startwithA)

let endwithA = sentance.endsWith('a')
console.log(startwithA)

let updated_sentance= sentance.replace('new','unique')
console.log(updated_sentance)

let words_in_sentance = sentance.split(' ')
console.log(words_in_sentance)

let upper_sentance=sentance.toUpperCase();
console.log(upper_sentance)

let lower_sentance = sentance.toLowerCase()
console.log(lower_sentance)