var x =  10;
var x = 20; // re-declare with a new value
var beginning = "This is the beginning";
console.log(x);
console.log(beginning)
// OBJECTS
let myObject = {name: "Kevin", age: 30};
// object has 2 keys, name and age. Value of name is "Kevin" and value of age is 30
// if we want to access just the name value in myObject, we specify the key => myObject.name
console.log(myObject.name) // Kevin

const myArrayOfObjects = [
    {year: 2022, city: 'New York', population: 8380000},
    {year: 2021, city: 'New York', population: 8419000},
    {year: 2020, city: 'New York', population: 8444000},
  ]
// select an object using index notation
const firstObject = myArrayOfObjects[0]
console.log("First Object:", firstObject)
// filter through the object array and select objects from 2020
const year2020Objects = myArrayOfObjects.filter(obj => obj.year === 2020);
console.log('Objects from 2020:', year2020Objects);

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
