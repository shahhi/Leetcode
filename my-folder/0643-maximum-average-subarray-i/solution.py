import math
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max = float('-inf')
        var = sum(nums[0:k])
        if max < var:
            max = var
        for i in range(1, len(nums)-k + 1):
            var += nums[k+i - 1]
            var -= nums[i-1]
            if max < var:
                max = var
        return max/k



        
