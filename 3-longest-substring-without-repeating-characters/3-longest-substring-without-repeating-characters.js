/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    let longestlength = 0;
    for (var i = 0; i < s.length; i++) {
        let currentStrings = new Set();
        for (var j = i; j < s.length; j++) {
            if (currentStrings.has(s[j]))
                break;
        
            else 
                currentStrings.add(s[j]);
        }
        longestlength = Math.max(longestlength, currentStrings.size)
    }
    return longestlength;
};