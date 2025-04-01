/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
const findMedianSortedArrays = function(nums1, nums2) {
  if (!nums1.length && !nums2.length) {
    return 0;
  }

  if (!nums1.length) {
    const middleIdx = Math.floor(nums2.length / 2);

    return nums2.length % 2 === 0 ?
      (nums2[middleIdx - 1] + nums2[middleIdx]) / 2 :
      nums2[middleIdx];
  }

  if (!nums2.length) {
    const middleIdx = Math.floor(nums1.length / 2);

    return nums1.length % 2 === 0 ?
      (nums1[middleIdx - 1] + nums1[middleIdx]) / 2 :
      nums1[middleIdx];
  }

  let nums1ordered = nums1;
  let nums2ordered = nums2;

  if (nums2ordered[0] < nums1ordered[0]) {
    const tmp = nums2ordered;

    nums2ordered = nums1ordered;
    nums1ordered = tmp;
  }

  if (nums1ordered[nums1ordered.length - 1] <= nums2ordered[0]) {
    const merged = nums1ordered.concat(nums2ordered);
    const middleIdx = Math.floor(merged.length / 2);

    return merged.length % 2 === 0 ?
      (merged[middleIdx - 1] + merged[middleIdx]) / 2 :
      merged[middleIdx];
  }

  const mergedLength = nums1ordered.length + nums2ordered.length;
  const merged = [];

  for (let i = 0, j = 0; i + j < mergedLength;) {
    if (nums1ordered[i] !== undefined && nums1ordered[i] < nums2ordered[0]) {
      merged.push(nums1ordered[i]);

      i++;

      continue;
    }

    if (nums1ordered[i] !== undefined && nums2ordered[j] !== undefined) {
      merged.push(Math.min(nums1ordered[i], nums2ordered[j]));

      nums1ordered[i] <= nums2ordered[j] ? i++ : j++;

      continue;
    }

    if (nums1ordered[i] !== undefined) {
      merged.push(nums1ordered[i]);

      i++;

      continue;
    }

    if (nums2ordered[j] !== undefined) {
      merged.push(nums2ordered[j]);

      j++;
    }
  }

  const middleIdx = Math.floor(mergedLength / 2);

  return mergedLength % 2 === 0 ?
    (merged[middleIdx - 1] + merged[middleIdx]) / 2 :
    merged[middleIdx];
};
