/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
const zigZagConversion = function(s, numRows) {
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

console.log(zigZagConversion('PAYPALISHIRING', 4)); // 'PINALSIGYAHRPI'
console.log(zigZagConversion('A', 1)); // 'A'
console.log(zigZagConversion('AB', 1)); // 'A'
