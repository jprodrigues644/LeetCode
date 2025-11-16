/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0) return false;
    //Without converting to string
let reversed = 0 ; 
let original = x;
while(x > 0){
    let digit = x % 10;
    reversed = reversed * 10 + digit;
    x = Math.floor(x / 10);
}
return reversed === original;

    
};

//Example 1
//Input: x = 121
//Output: true      
console.log(isPalindrome(121)); // true

//Example 2
//Input: x = -121
//Output: false
console.log(isPalindrome(-121)); // false