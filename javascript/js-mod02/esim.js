console.log('Moro')


let emptyArray = [];

// taulukko array
let items = [1, 2, 3, {name: 'ulla'}, [0,1,2], 'merkkijono'];
console.log(items);

// alkioon viitataan indeksillä
console.log(items[3]);

// alkion arvoa voidaan muuttaa indeksin avulla
items[0] = 99;
console.log(items);

items[9] = 'Olen uusi alkio';
console.log(items);

// välissä on nyt määrittelemätön alkio ei undefined
// ei tartte olla vielä tästä huolissaan
console.log(items[6]);

let fruits = ['Banaani', 'Mango', 'Päärynä', 'Omena'];
console.log(fruits);
console.log('Taulukon pituus:', fruits.length)

let elem = document.querySelector('#heading');
console.log(elem);
console.dir(elem);
elem.innerText = 'Mod 2 esimerkit';

// Taulukon looppaus eri tavoin
// perinteinen for
// yleinen tapa, tarvitaan indeksi
console.log('--------------------------');
console.log('Perinteinen FOR looppi')

for (let i = 0; i < fruits.length; i++) {
    console.log(`Hedelmä ${i+1} on ${fruits[i]}`);
}

// helppo ja nopea tapa iteroida ilman indeksiä
console.log('--------------------------');
console.log('Läpikäynti for / of rakenteella, jolla saadaan arvot');

for (let fruit of fruits) {
    console.log(fruit);
}

// harvemmin käytetään taukukoiden kanssa
// JS objektien kanssa jeba
console.log('--------------------------');
console.log('Läpikäynti for / in rakenteella, jolla saadaan arvot ja index');
for (const index in fruits) {
    console.log(index, fruits[index]);
}

/*
sort() sorts the array alphabetically
reverse() reverses the items in the array in reverse order
shift() deletes and returns the 1st item in the array
pop() deletes and returns the last item in the array
push(value) adds the value at the end of the array, multiple values separated by commas
includes(value) checks whether the array contains the given value
 */

fruits.sort()
console.log(fruits);
fruits.reverse()
console.log(fruits);

// ei toimi numeroiden kanssa kovinkaan hyvin
const ages = [2300, 28, 33, 19, 2000];
ages.sort();
console.log(ages);

// tämäm toimii numeroiden kanssa
ages.sort((a, b) => a - b)
console.log(ages);
ages.sort((a, b) => b - a)
console.log(ages);


let hedelmat= ['Banaani', 'Mango', 'Päärynä', 'Omena'];

// shift()  poistetaan taulukon eka arvo ja otetaan muuttuja talteen
const hedelma = hedelmat.shift();
console.log('Poistettiin', hedelma)
console.log(hedelmat);

// unshif lisää taulukon alkuun
hedelmat.unshift('Kiwi');
console.log(hedelmat);

// sama kuin shift mutta vika
const vika = hedelmat.pop();
console.log('Poistettiin', vika)
console.log(hedelmat);

hedelmat.push('Satsuma', 'Mandariini');
console.log(hedelmat);

// includes tsekkaa onko arvo taulukossa ja palauttaa true/false
console.log(hedelmat.includes('Kiwi'));

//object literal, olio
//samankaltainen kuin sanakirja pythinissa

const duck = {
    name: 'aku',
    age: 33
}
console.log(duck);
console.log(duck['name']);

//muutetaan arvoja
duck['name'] = 'aku ankka';
console.log(duck);

//haetaan nimi ja muutetaan nimi
console.log(duck.name);
duck.name = 'iines ankka';
console.log(duck);
console.log(duck.name);

//uusi ominaisuus
duck.profession = 'working like a duck';
// vaihdetaan arvo
duck.profession = 'swimming like a duck';
console.log(duck);

let sayhello = `hei ${duck.name}`;
console.log(sayhello);

//poistetaan ominaisuus,
delete duck.profession;
console.log(duck);

const duck2 = {
    name: 'roope ankka',
    age: 80,
    getinfo: function() {
        return this.name + ' on ' + this.age + '- vuotias';

    }
}

let info = duck2.getinfo();
console.log(info);

// JS funktiot

//Ns. perinteinen funktion määrittely
function greet(name) {
    const greeting = `Moikka ${name}`
    return greeting
}
console.log(greet('Ulla'));

//arrow / nuolifubktio, edellistä yksinkertaisempi
//uudempi ja moderni tapa käyttää funktioita
//voidaan kirjoittaa yksirivisenä, tällöin ei palauteta
//käytetä return sanaa

const nuolifunktio = () => {
    console.log('ollaan nuolifunktiossa')

};
nuolifunktio();
const quadraticSum = (a, b) => (a * a * b * b);
console.log(quadraticSum(3,5));

//forEach voidaan iteroida taulukon jäsenet läpi

const numerot = [12,22,33,45,67];
numerot.forEach((num, index) => {
    console.log(`indeksi on ${index}, arvo on ${num}`)
}) ;