const person = [
    {
    name:'John',
    age:35,
    occupation :"student"},
    {
    name:'Jane',
    age:32,
    occupation :"teacher"},
    {
    name:'Bob',
    age:40,
    occupation:"developer"},
]
// const person is object array
// `name` , `age` and  `occupation` is the property of the object
let personName = person.map(person => person.name)
console.log(personName) // [ 'John', 'Jane', 'Bob' ]

// declare a variable with person array and assign .map() method
// inside the argument, the variable with arrow function to map the property of the object
// map creates a new array and is the result of applying provided function

const student = ['John', 'Jane', 'Bob']; // original array
const numbers = [1, 2, 3, 4, 5]; // original array

function square(element){
    return Math.pow(element, 2);
}
function cube(element){
    return Math.pow(element, 3);
}
function upperCase(element){
    return element.toUpperCase();
}

// 
const squared = numbers.map(square); // new aray
const cubes = numbers.map(cube); // new aray
const upper = student.map(upperCase); // new aray
// array = original array .method( pass in callback function)
// callback is the function element

console.log(squared); // [ 1, 4, 9, 16, 25 ]
console.log(cubes); // [ 1, 8, 27, 64, 125 ]
console.log(upper); // [ 'JOHN', 'JANE', 'BOB' ]



// FILTER METHOD .filter() = creates a new array by filtering out elements
// creates a new array containing only the elements that return true
let numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let evenNumbers = numberlist.filter(isEven);
let oddNumbers = numberlist.filter(isOdd);

function isEven(element){
    return element % 2 === 0;
}
function isOdd(element){
    return element % 2 !== 0;
}

console.log(evenNumbers); // [ 2, 4, 6, 8, 10 ]
console.log(oddNumbers); // [ 1, 3, 5, 7, 9 ]

const age = ['16', '17', '18', '19', '20', '21', '22'];
const adults = age.filter(isAdult);
const teen = age.filter(isTeen);

function isAdult(element) {
    return element >= 18;
}
function isTeen(element) {
    return element < 18;
}

console.log(adults); // [ '18', '19', '20', '21', '22' ]
console.log(teen); // [ '16', '17' ]