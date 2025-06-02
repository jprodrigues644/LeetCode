
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    
    const n = nums.length;
    const expectedSum = (n * (n + 1)) / 2; // Sum of first n natural numbers
    const actualSum = nums.reduce((acc, num) => acc + num, 0); // Sum of elements in nums
    return expectedSum - actualSum; // The missing number is the difference
};
// Example usage:
console.log(missingNumber([3, 0, 1,2])); // Output: 2