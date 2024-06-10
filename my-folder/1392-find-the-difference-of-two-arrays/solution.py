class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        # method 1
        # answer = []
        # nums1_set = set(nums1)
        # nums2_set = set(nums2)
        # same = set.intersection(nums1_set,nums2_set)
        # answer.append(nums1_set - same) 
        # answer.append(nums2_set - same)

        # method 2
        return [set(nums1)-set(nums2), set(nums2)- set(nums1)]
        
