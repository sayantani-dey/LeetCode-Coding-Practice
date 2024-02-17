class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        array = nums1 + nums2
        array.sort() 
        if len(array) % 2 == 0:
            mid1 = array[len(array) // 2]
            mid2 = array[len(array) // 2 - 1]
            return (float(mid1) + float(mid2)) / 2.0
        else:
            return float(array[len(array) // 2])
