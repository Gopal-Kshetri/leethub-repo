/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
  if (numRows == 1) return s;
  var i, row = 0, down = true;
  let array = [];
  for (var i = 0; i < numRows; i++) {
    array[i] = "";
  }
  for (i = 0; i < s.length; i++) {
    array[row] += s[i];

    if (row == 0)
      down = true;
    if (row == numRows - 1)
      down = false;
    down ? row++ : row--;
  }

  let answer = "";
  for (i = 0; i < numRows; i++)
    answer += array[i];

  return answer;
};