var longestCommonPrefix = function(strs) {
  let max = 0, i, j, longest="", prefix = true;
  for (let i = 0; i < strs.length; i++) {
    val = strs[i].length;
    max = val > max ? val : max;
  }
  if (max == 0)
    return "";
  for (i = 1; i <= max; i++) {
    text = strs[0].substring(0, i)
    for (j = 0; j < strs.length; j++) {
      if (text != strs[j].substring(0, i)) {
        prefix = false;
      }
    }
    if (prefix) {
      longest = text;
    }
  }
  return longest;
};