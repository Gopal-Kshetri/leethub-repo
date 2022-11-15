/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
    let mergedArray = nums1.concat(nums2);
    mergedArray = mergedArray.sort(function(a,b) {return a-b;});
    let n = mergedArray.length;
    if (mergedArray.length % 2 === 0) {
        return (mergedArray[n / 2 - 1] + mergedArray[n / 2]) / 2.0;
    }
    else{
        return mergedArray[(n-1) / 2];

    }
};