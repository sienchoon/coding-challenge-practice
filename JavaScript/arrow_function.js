// arrow function 
const hello = function () {
    console.log('Greetings!');
}

hello();
// we store the function in the constant hello
// when we call the function, it prings the message
//------ arrow function -------------------
// const hello = () => console.log('hello');
// hello(); 

// declare variables in arrow function
// define the function with parameters
const person = (name, age, occupation) => {console.log(`Hello ${name}`)
    console.log(`You are ${age} years old`)
    console.log(`You are a ${occupation}`)};

person('Kevin', 30, 'Student');


const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
//map function with arrow function
// map returns a new array with the same length as the original
const squares = numbers.map((x) => Math.pow(x, 2));

// filter with arrow function
// filter returns a new array with conditional elements
const even = numbers.filter((even) => even % 2 === 0);
const odd = numbers.filter((odd) => odd % 2 !== 0);
console.log(squares);
console.log(even);
console.log(odd);