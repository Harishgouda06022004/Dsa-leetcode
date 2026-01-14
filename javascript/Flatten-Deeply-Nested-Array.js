1/**
2 * @param {Array} arr
3 * @param {number} depth
4 * @return {Array}
5 */
6var flat = function (arr, n) {
7    if(n==0){
8        return arr
9    }
10    let result=[]
11    for(let el of arr){
12        if(Array.isArray(el)){
13            result.push(...flat(el,n-1));
14        }else{
15            result.push(el)
16        }
17
18    } 
19    return result
20    // return arr.flat(n)
21};