let numbers = [];

// Prompt the user for 5 numbers
for (let i = 0; i < 5; i++) {
    let num = Number(prompt("Enter a number:"));
    numbers.push(num);
}

// Print numbers in reverse order
console.log("Numbers in reverse order:");
for (let i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);
}




let numbers1 = [];
let input;

// Keep asking until user enters 0
while (true) {
    input = Number(prompt("Enter a number (0 to stop):"));

    if (input === 0) {
        break;
    }

    numbers1.push(input);
}

// Sort from largest to smallest
numbers1.sort((a, b) => b - a);

// Print in console
console.log("Numbers from largest to smallest:");
for (let num of numbers1) {
    console.log(num);
}


let numbers2 = [];
let input1;

while (true) {
    input1 = Number(prompt("Enter a number:"));

    // Check if number was already entered
    if (numbers2.includes(input1)) {
        console.log("The number has already been given. Stopping...");
        break;
    }

    numbers2.push(input1);
}

// Sort numbers in ascending order
numbers2.sort((a, b) => a - b);

// Print to console
console.log("Numbers in ascending order:");
for (let num of numbers2) {
    console.log(num);
}
