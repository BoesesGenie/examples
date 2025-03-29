/**
 * @param {string} s
 * @return {string}
 */
const longestPalindrome = function(s) {
  if (s.length === 1) {
    return s;
  }

  if (s.length === 2 && s[0] === s[1]) {
    return s;
  }

  if (s.length === 2) {
    return s[0];
  }

  let leftIdx = leftBorder = 0;
  let rightIdx = rightBorder = s.length - 1;
  let isPalindrome = false;
  let offset;

  while (true) {
    offset = s.length - 1 - rightBorder;
    leftIdx = leftBorder + offset;
    rightIdx = rightBorder + offset;

    do {
      if (rightIdx - leftIdx <= 1 && s[leftIdx] === s[rightIdx]) {
        return s.slice(leftBorder + offset, rightBorder + offset + 1);
      }

      isPalindrome = s[leftIdx] === s[rightIdx];

      if (isPalindrome) {
        leftIdx++;
        rightIdx--;

        continue;
      }

      offset--;
      leftIdx = leftBorder + offset;
      rightIdx = rightBorder + offset;
    } while (offset >= 0);

    rightBorder--;
  }
};
