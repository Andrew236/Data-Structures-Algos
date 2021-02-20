import statistics

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    median_array = nums1 + nums2
    value = statistics.median(median_array)
    return value 


findMedianSortedArrays([1,3], [2]))
