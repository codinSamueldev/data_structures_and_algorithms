// First recurring element problem.

/*
Create function that takes an array of integers as parameter. Return the first found number that is repeated in the array.

Example 1:
    array = [1,2,3,4,1,2,7]
    should return 1.
    Explanation -> Even though there is two numbers that are repeated(1, 2) the first number repeated was 1.

Example 2:
    array = [77,41,95,36,54,56,95]
    should return 95

Example 3:
    array = [1,2,3,4,5]
    should return None or undefined if using JavaScript
*/


function first_recurring_element(array){
	const hash_table = {}

	for (let i = 0; i < array.length; i++){
		if (hash_table.hasOwnProperty(array[i])){ // If current number already exist in the hash_table then we found the first repeated number.
			return array[i]
		} else{
			hash_table[array[i]] = i // Add current iteration number to hash_table.
		}
	}
	
	return undefined
}


const array1 = [1,2,3,4,1,2,7]
const array2 = [77,41,95,36,54,56,95]
const array3 = [1,2,3,4,5]
const array4 = []

console.log(first_recurring_element(array1))
console.log(first_recurring_element(array2))
console.log(first_recurring_element(array3))
console.log(first_recurring_element(array4))

