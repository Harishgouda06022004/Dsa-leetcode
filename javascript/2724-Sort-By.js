/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    let v=arr.sort((a,b)=>fn(a)-fn(b))
    return v
};