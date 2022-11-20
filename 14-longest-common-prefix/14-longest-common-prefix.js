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
    // console.log("text:",text);
    for (j = 0; j < strs.length; j++) {
      // console.log('check strings');
      if (text != strs[j].substring(0, i)) {
        // console.log('false');
        prefix = false;
      }
    }
    if (prefix) {
      longest = text;
      console.log("longest:", longest);
    }
  }
  return longest;
};