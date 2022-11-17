/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  let i;
  if(x<0)
    return false;
  data = x.toString();
  for(i=0; i<data.length; i++){
    if(data[i]!=data[data.length-i-1])
      return false;
  }
  return true;
};