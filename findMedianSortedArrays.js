/**
 * @param {number[]} nums1in
 * @param {number[]} nums2in
 * @return {number}
 */
const findMedianSortedArrays = function(nums1in, nums2in) {
  const middle = [];
  const middleNeg = [];
  let i = nums1in.length, j = 0;
  let nums1 = nums1in;
  let nums2 = nums2in;

  if (nums1.length && nums2.length) {
    if (nums2[0] < nums1[0]) {
      const tmp = nums2;

      nums2 = nums1;
      nums1 = tmp;
    }

    for (i = nums1.length - 1, j = 0; i >= 0 || j < nums2.length; i--, j++) {
      if (i >= 0 && nums1[i] >= 0) {
        Array.isArray(middle[nums1[i]]) ?
          middle[nums1[i]].push(nums1[i]) :
          middle[nums1[i]] = [nums1[i]];
      } else if (i >= 0) {
        const idx = -nums1[i];

        Array.isArray(middleNeg[idx]) ?
          middleNeg[idx].push(nums1[i]) :
          middleNeg[idx] = [nums1[i]];
      }

      if (j < nums2.length && nums2[j] >= 0) {
        Array.isArray(middle[nums2[j]]) ?
          middle[nums2[j]].push(nums2[j]) :
          middle[nums2[j]] = [nums2[j]];
      } else if (j < nums2.length) {
        const idx = -nums2[j];

        Array.isArray(middleNeg[idx]) ?
          middleNeg[idx].push(nums2[j]) :
          middleNeg[idx] = [nums2[j]];
      }

      if ((!middleNeg.length || middleNeg[0] < nums2[j < nums2.length ? j : nums2.length - 1]) &&
        (!middle.length || middle[middle.length - 1] < nums2[j < nums2.length ? j : nums2.length - 1])
      ) {
        i--;
        j++;
        break;
      }
    }
  }

  middleNeg.reverse();

  i = i >= 0 ? i + 1 : 0;
  j = j < nums2.length ? j : nums2.length;

  const merged = nums1
    .slice(0, i)
    .concat(middleNeg.filter((item) => Array.isArray(item)).reduce((acc, item) => acc.concat(item), []))
    .concat(middle.filter((item) => Array.isArray(item)).reduce((acc, item) => acc.concat(item), []))
    .concat(nums2.slice(j));
  const middleIdx = parseInt(merged.length / 2);

  return merged.length % 2 === 0 ?
    (merged[middleIdx - 1] + merged[middleIdx]) / 2 :
    merged[middleIdx];
};
