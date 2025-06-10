/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    
    let count = 0;
    while (n) {
        count += n & 1; 
        n >>= 1; 
    }
    return count; 
};

// Example usage:

console.log(hammingWeight(11)); 
console.log(hammingWeight(128));   