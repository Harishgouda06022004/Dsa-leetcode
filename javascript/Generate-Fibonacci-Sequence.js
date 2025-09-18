/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let prev=0,curr=1
    while(true){
        yield prev
        let next=prev+curr
        prev=curr
        curr=next
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */