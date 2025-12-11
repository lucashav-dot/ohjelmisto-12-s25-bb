'use strict';

function synchronousFunction() {
    let number = 1;
    for (let i = 1; i < 100000; i++) {
        number += i;
    }
}

async function asynchronousFunction() {
    try {
        const response = await fetch('https://api.chucknorris.io/jokes/random');
        const jsonData = await response.json();
        console.log(jsonData.value);
        document.querySelector('.output').textContent = jsonData.value;
    } catch (error) {
        console.log(error.message);
    } finally {
        console.log('Haku valmis');
    }
}

asynchronousFunction();

fetch('pics.json').then(function (data) {
    console.log('response data: ', data);
    data.json().then(function (data) {
        console.log('json data', data);
    }).catch(function (error) {
        console.error(error);
    });
}).catch(function (error) {
    console.error(error);
});

async function fetchPics(){
    const picsDiv = document.querySelector('#pics');
    try {
        const response = await fetch('pics.json');
        if (!response.ok) {
            throw new Error('Status ei ok');
        }
        const pics = await response.json();
        console.log('pics', pics);
        for (const pic of pics) {
            const imgElem = document.createElement('img');
            imgElem.src = pic.address;
            imgElem.alt = pic.description;
            picsDiv.append(imgElem);
        }
    } catch (error) {
        console.log(error);
        picsDiv.innerHTML = '<p>Kuvien lataamisessa ongelma</p>'
    }
}

document.querySelector('button').addEventListener('click', function () {
    fetchPics();
});

async function searchTVMaze(searchString) {
    const response = await fetch('https://api.tvmaze.com/search/shows?q=' + searchString);
    const results = await response.json();
    console.log('tv maze results', results);
    return results;
}

const searchForm = document.querySelector('form#tvmaze');
const inputText = searchForm.querySelector('input');
searchForm.addEventListener('submit', async function(event) {
    event.preventDefault();
    if (inputText.value.length > 1 ) {
        const tvMazeResults = await searchTVMaze(inputText.value);
        console.log('event handler hakutulokset', tvMazeResults);
    }
});



console.log('the script ends');