/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let maxAltitude=0
    let altitude=0
    for (const g of gain) {
        altitude += g;
        maxAltitude = Math.max(maxAltitude, altitude);
    }
    return maxAltitude
};