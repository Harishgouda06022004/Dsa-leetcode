/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let v = _.chunk(arr, size); 
    return v

    // store = []
    // for(let i = 0; i < arr.length; i+=size){
    //     store.push(arr.slice(i, i + size))
    // }

    // return store
};
