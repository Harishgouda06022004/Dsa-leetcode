/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    nums.sort((a,b)=>b-a)
    n=nums[0]
    m=nums[1]
    return (n-1)*(m-1)
};