1/**
2 * @param {Function} fn
3 * @param {Array} args
4 * @param {number} t
5 * @return {Function}
6 */
7var cancellable = function(fn, args, t) {
8    let TimerId
9    TimerId=setTimeout(()=>fn(...args),t)
10    return function cancelFn(){
11        clearTimeout(TimerId)
12    }
13};
14
15/**
16 *  const result = [];
17 *
18 *  const fn = (x) => x * 5;
19 *  const args = [2], t = 20, cancelTimeMs = 50;
20 *
21 *  const start = performance.now();
22 *
23 *  const log = (...argsArr) => {
24 *      const diff = Math.floor(performance.now() - start);
25 *      result.push({"time": diff, "returned": fn(...argsArr)});
26 *  }
27 *       
28 *  const cancel = cancellable(log, args, t);
29 *
30 *  const maxT = Math.max(t, cancelTimeMs);
31 *           
32 *  setTimeout(cancel, cancelTimeMs);
33 *
34 *  setTimeout(() => {
35 *      console.log(result); // [{"time":20,"returned":10}]
36 *  }, maxT + 15)
37 */