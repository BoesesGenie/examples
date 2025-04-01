/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = function(s) {
  if (s.length === 0 || s.length === 1) {
    return s.length;
  }

  const currentMap = new Map();
  let result = 0;
  let foundIndex = -1;

  for (let index = 0; index < s.length; index++) {
    const letter = s[index];

    if (currentMap.has(letter) && currentMap.get(letter) > foundIndex) {
      foundIndex = currentMap.get(letter);
    }

    currentMap.set(letter, index);
    const currentLength = index - foundIndex;
    result < currentLength && result++;
  }

  return result;
};
