#!/usr/bin/node

/*
 *function that increments and calls a function
 */

let myObject = {
	type: 'object',
	value: 12
};
console.log(myObject);

myObject.incr = function () {
	this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
