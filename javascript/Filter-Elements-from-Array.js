/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    // let fill=[]
    // for (let i=0; i<arr.length; i++){
    //     if(fn(arr[i],i)){
    //         fill.push(arr[i])
    //     }
    // }
    // return fill
    return arr.filter(fn)
};