class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) <= 2:
            return len(nums)
        
        changablePosition = 1
        preNumber = nums[0]
        preNumberCount = 1
        i = 1
        
        numsLen = len(nums)
        while i < numsLen:
            if nums[i] == preNumber:
                # same as previous number
                # check the apperance count
                if preNumberCount < 2:
                    nums[changablePosition] = nums[i]
                    changablePosition += 1
                preNumberCount += 1
            else:
                # different number
                nums[changablePosition] =nums[i]
                changablePosition += 1
                
                preNumber = nums[i]
                preNumberCount = 1
            
            i += 1
        
        return changablePosition
                    