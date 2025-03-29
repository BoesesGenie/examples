/**
 * @param {string} s
 * @return {string}
 */
const longestPalindrome = function(s) {
  let left = 0;
  let right = 0;
  let length = 0;

  const findPalindrome = (leftIdx, rightIdx) => {
    while (leftIdx >= 0 && rightIdx < s.length && s[leftIdx] === s[rightIdx]) {
      if (length < rightIdx - leftIdx + 1) {
        left = leftIdx;
        right = rightIdx + 1;
        length = rightIdx - leftIdx + 1;
      }

      leftIdx--;
      rightIdx++;
    }
  }

  for (let i = 0; i < s.length; i++) {
    findPalindrome(i, i);
    findPalindrome(i, i + 1);
  }

  return s.slice(left, right);
};
