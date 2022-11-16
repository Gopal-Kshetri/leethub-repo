/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
  var i, rev = "", neg = false, data = "";
  if (x < 0) {
    neg = true;
    x = -x;
  }
  data = x.toString();
  for (i = 0; i < data.length; i++) {
    rev = rev.concat(data[data.length - i - 1]);
  }
  if (neg == true)
    rev = -Number(rev)

  if (rev > -Math.pow(2, 31) && rev < Math.pow(2, 31) - 1)
    return Number(rev);
  else
    return 0;
};