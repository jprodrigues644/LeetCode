/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {

    let maxprofit = 0 ; 
    let min_price =Infinity;

    for ( let price of prices ) {
        if (price < min_price) {
            min_price = price;
        }
        else if (price - min_price > maxprofit ) {maxprofit = price - min_price;}
    }
     return maxprofit;
};


prices = [7, 8, 9, 5, 100, 14,79];

console.log( maxProfit(prices));