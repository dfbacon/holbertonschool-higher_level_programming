#!/usr/bin/node
/*
Update the 103-object_fct.js script by adding a new function `incr`
that increments the integer value.

Base code:
  #!/usr/bin/node
  let myObject = {
    type: 'object',
    value: 12
  };
  console.log(myObject);

  // YOUR CODE HERE

  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);

Requirements:
* You are not allowed to use var

*/

let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function () {
  return this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
