// Array.filter()
let Array = [1, 2, 3, 4, 5].filter(d => d < 3)
console.log(Array) // [ 1, 2 ]
//  filter says that the value in the array, d, must be less than 3
// d is used as a parameter in callback function passed to filter
// we can use any name as a parameter

// Array.map()
myData = [
    {name: 'Paul', city: 'Denver'},
    {name: 'Robert', city: 'Denver'},
    {name: 'Ian', city: 'Boston'},
    {name: 'Cobus', city: 'Boston'},
    {name: 'Ayodele', city: 'New York'},
    {name: 'Mike', city: 'New York'},
  ]
  myNewArray = myData.map(d => d.name)
  console.log(myNewArray) // [ 'Paul', 'Robert', 'Ian', 'Cobus', 'Ayodele', 'Mike' ]

  