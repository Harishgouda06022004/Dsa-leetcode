/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let j=1
    let n = nums.length;
    for(let i=1; i<nums.length; i++){
        if(nums[i]!=nums[i-1]){
            nums[j]=nums[i]
            j+=1
        }
    }
    return j
};