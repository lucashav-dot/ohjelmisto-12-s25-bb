'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const targetSelect = document.getElementById('target');

for (let i = 0; i < students.length; i++) {
    const optionElement = document.createElement('option');

    optionElement.textContent = students[i].name;

    optionElement.value = students[i].id;

    targetSelect.appendChild(optionElement);
}