1/**
2 * @param {number} n
3 * @return {Function} counter
4 */
5var createCounter = function(n) {
6    
7    return function(){
8        return n++
9    }
10};
11
12/** 
13 * const counter = createCounter(10)
14 * counter() // 10
15 * counter() // 11
16 * counter() // 12
17 */