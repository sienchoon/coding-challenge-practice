// DOM 
document.title = "My Website"
document.body.style.backgroundColor = "hsl(255, 255, 255)";

const username = "CS Wong";
const Msg = document.getElementById("welcome-msg");
Msg.textContent += username === "" ? `Guest`: username; 

console.log(document);
console.dir(document);

// 1. document.getElementById()                 // ELEMENT OR NULL
// 2. document.getElementsClassName()           // HTML COLLECTION
// 3. document.getElementsByTagName()           // HTML COLLECTION
// 4. document.querySelector()                  // FIRST ELEMENT OR NULL
// 5. document.querySelectorAll()               // NODELIST

const myHeading = document.getElementById("welcome-msg");

myHeading.style.backgroundColor = "yellow";
myHeading.style.textAlign = "center";

console.log(myHeading);


const leagues = document.getElementsByClassName("league");

// fruits[0].style.backgroundColor = "yellow";

for(let leagues of league) {
    fruit.style.backgroundColor = "yellow";
    fruit.style.textAlign = "center";
}

console.log(leagues);

