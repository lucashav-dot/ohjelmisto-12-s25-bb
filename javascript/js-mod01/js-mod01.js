console.log("I'm printing to console!");

let person = prompt("Please enter your name");
document.getElementById("demo").innerHTML = "Hello, " + person + "!";






let num1 = parseInt(prompt("Enter the first number: "));
let num2 = parseInt(prompt("Enter the second number: "));
let num3 = parseInt(prompt("Enter the third number: "));

let sum = num1 + num2 + num3;
let product = num1 + num2 + num3;
let avg = sum / 3;
document.getElementById("sum").innerHTML = "The sum is: " +sum;
document.getElementById("prod").innerHTML = "The product is: " +product;
document.getElementById("avg").innerHTML = "The average is: " +avg;

name = prompt("Tell me your name");
random = Math.floor(Math.random()* 4);

if(random <= 0) {
    document.getElementById("Gryffindor").innerHTML = name +", you are Gryffindor";
}
else if(random <= 1) {
    document.getElementById("Slytherin").innerHTML = name +", you are Slytherin";
}
else if(random <= 2) {
    document.getElementById("Hufflepuff").innerHTML = name +", you are Hufflepuff";
}
else if(random <= 3) {
    document.getElementById("Ravenclaw").innerHTML = name +", you are Ravenclaw";
}


year = prompt("Enter year")

if ((0 == year % 4) && (0 != year % 100) || (0 == year % 400)) {
    document.getElementById("leapyear").innerHTML = year + ' is a leap year';
} else {
    document.getElementById("notleapyear").innerHTML = year + ' is not a leap year';
}




