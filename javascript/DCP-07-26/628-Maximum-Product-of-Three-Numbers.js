/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function(nums) {
    let n = nums.sort((a, b) => b - a);

    let max1 = n[0] * n[1] * n[2];

    let max2 = n[0] * n[n.length - 1] * n[n.length - 2];

    return Math.max(max1, max2);
};