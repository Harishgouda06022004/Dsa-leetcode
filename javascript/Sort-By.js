1/**
2 * @param {Array} arr
3 * @param {Function} fn
4 * @return {Array}
5 */
6var sortBy = function(arr, fn) {
7    let v=arr.sort((a,b)=>fn(a)-fn(b))
8    return v
9};