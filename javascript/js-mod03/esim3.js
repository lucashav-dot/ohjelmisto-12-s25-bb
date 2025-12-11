'use strict';

// hae viittaus kaikkiin outout class elementteihin taulukkona
const outputElemet= document.getElementsByClassName('output');
console.log(outputElemet);

// viittaus yhteen elementtiin id:n perusteella
const outputElemet2= document.getElementById('output');
console.log(outputElemet2);

// viittaus kaikkiin p-elementteihin tagin perusteella
const outputElement3 = document.querySelector('p');
console.log(outputElement3);

// viittaus koko body-elementtiin
const body = document.querySelector("body");
body.querySelector('#output');

// listan (ul) käsittely
const ulElement = document.querySelector('ul');
const newLi = document.createElement('li');
ulElement.appendChild(newLi);
newLi.textCintent = 'Uusi itemi';

//innerHTML-esimerkki
//ulElement.innerHTML = '<li>uusi itemi</li><li>Toinen uusi</li>;

//haetaan viittaus kaikkiin li-elementteihin listan sisällä
const liElems = ulElement.querySelectorAll('li');
for (let i = 0; i<liElems.length; i++) {
    liElems[i].textContent = `${i+1}. itemi`;
}

// lisätään sisältöä js-taulukosta
const inventory = ['kynä', 'kumi', 'läppäri'];
const inventoryOlElem = document.createElement('ol');
for (const item of inventory) {
    // luodaan html li-elementit ja sijoitetaan ol-elementti lapsiksi
    const liElem = document.createElement('li');
    liElem.textContent = item;
    inventoryOlElem.appendChild(liElem);
}
// lisätään luotu lista DOMiin käyttäen aiemmin haettu viittausta body-elementtiin
const inventoryHeader = document.createElement('h2');
inventoryHeader.textContent = 'Inventaario';
body.appendChild(inventoryHeader);
body.appendChild(inventoryOlElem);
inventoryHeader.classList('red');

// tapahtumakäsittely

const button = document.querySelector('button');
//sidotaan tapahtuma ja tapahtumakäsittelijä yhteen
button.addEventListener('click', buttonClick);
// erillinen tapahtumankäsittelyfunktio
function buttonClick() {
    console.log('nappulaa klikattu');
}
// nimetön funktio tapahtumakäsittelijä
inventoryHeader.addEventListener('click', function(){
    console.log('otsikkoa klikattu');
    inventoryHeader.classList.toggle('red');
});

//näppis-tapahtumaesimerkki
document.addEventListener('keypress', function (event){
    console.log('näppäintä painettu', event);
    inputString += event.key;
    if (event.key === 'Enter') {
        outputElemet2.classList.remove('blue');
        outputElemet2.classList.add('red');
    }

    outputElemet2.classList.add('blue');
    outputElemet2.textContent = 'nappeja painettu: ' + inputString;
});

// hiiritapahtuma
document.addEventListener('mousemove', function(event) {
    console.log('hiiri liikkuu', + event);
    outputElemet[0].textContent = `Hiiren sijainti: ${event.screenX}, ${event.screenY}`;

})
