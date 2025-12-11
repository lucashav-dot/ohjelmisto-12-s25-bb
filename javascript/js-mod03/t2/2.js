const targetList = document.getElementById('target');

const items = ['First item', 'Second item', 'Third item'];

for (let i = 0; i < items.length; i++) {
    const listItem = document.createElement('li');

    listItem.textContent = items[i];

    if (i === 1) {
        listItem.classList.add('my-item');
    }

    targetList.appendChild(listItem);
}