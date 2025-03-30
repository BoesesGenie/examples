/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
  if (numRows === 1 || numRows >= s.length) {
    return s;
  }

  let rows = Array(numRows).fill('');
  let rIdx = 0;
  let down = false;

  for (const letter of s) {
    rows[rIdx] += letter;

    if (rIdx === 0 || rIdx === numRows - 1) {
      down = !down;
    }

    rIdx += down ? 1 : -1;
  }

  return rows.join('');
};

console.log(convert('PAYPALISHIRING', 4)); // 'PINALSIGYAHRPI'
console.log(convert('A', 1)); // 'A'
console.log(convert('AB', 1)); // 'A'
