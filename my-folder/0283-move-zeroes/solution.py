class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer2 = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pointer2] = nums[pointer2], nums[i]
                pointer2+=1



                
      

  
        
