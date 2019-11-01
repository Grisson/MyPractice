class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        result = [-1,-1]
        start = 0
        end = len(nums) - 1
        
        if (len(nums) == 0) or (target < nums[start]) or (nums[end] < target):
            return result
        
        while start <= end:
            
            middlePoint = (start + end)/2
            print("[{0}-{1}-{2}]".format(start, middlePoint, end))
            
            if nums[middlePoint] < target:
                # check the range
                start = middlePoint + 1
            elif target < nums[middlePoint]:
                end = middlePoint - 1
            else: #(nums[middlePoint] == target)
                start = middlePoint
                end = middlePoint
                
                # check previous
                while 0 < start:
                    if nums[start-1] == target:
                        start = start - 1
                    else:
                        break
                
                # check after
                while end < (len(nums) - 1):
                    if nums[end+1] == target:
                        end = end + 1
                    else:
                        break
                
                # return
                return [start, end]
        
        return result
            