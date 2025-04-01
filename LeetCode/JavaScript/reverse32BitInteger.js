/**
 * @param {number} x
 * @return {number}
 */
const reverse32BitInteger = function(x) {
  const MAX = ['2', '1', '4', '7', '4', '8', '3', '6', '4', '8'];
  const IS_NEG = x < 0;
  const inputAsArray = x.toString().replace('-', '').split('');
  let mayBeOutOfRange = inputAsArray.length === MAX.length;
  const result = [];

  if (!IS_NEG) {
    MAX[9] = '7';
  }

  for (let i = inputAsArray.length - 1, j = 0; i >= 0; i--, j++) {
    if (mayBeOutOfRange) {
      if (MAX[j] > inputAsArray[i]) {
        mayBeOutOfRange = false;
      } else if (MAX[j] < inputAsArray[i]) {
        return 0;
      }
    }

    result.push(inputAsArray[i]);
  }

  return parseInt(result.join('')) * (IS_NEG ? -1 : 1);
};
