#!/usr/bin/node
/*
Update this script to replace the value 12 with 89:

  #!/usr/bin/node
  let myObject = {
    type: 'object',
    value: 12
  };
  console.log(myObject);
  // YOUR CODE HERE
  console.log(myObject);

Requirements:
* You are not allowed to use var

*/

let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);
