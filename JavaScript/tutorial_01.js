var x =  10;
var x = 20; // re-declare with a new value
var beginning = "This is the beginning";
console.log(x);
console.log(beginning)

// function
function addition(a, b) {
    return a + b;
}
console.log(addition(10, 10));

// arrow function
const add = (a, b) => a + b;
console.log(add(10, 10));


// for loops
for (let i = 0; i < 5; i++){
    console.log(i);
}

// while loops 
let counter = 0;

while (counter < 5) {
    console.log(counter);
    counter++;
}

// conditionals
if (x > 10) {
    console.log("x is greater than 10");}   
    else {
    console.log("x is less than 10");
    }
