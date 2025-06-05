/**
 * @param {number[]} nums
 * @return {boolean}
 */
/* var containsDuplicate = function(nums) {
    nums.sort();
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] === nums[i + 1]) return true;
    }
    return false;
}; */
var containsDuplicate = function(nums) {
    const seen = new Set();
    for (let num of nums) {
        if (seen.has(num)) return true;
        seen.add(num);
    }
    return false;
};


console.log(containsDuplicate([1,2,3,1]))