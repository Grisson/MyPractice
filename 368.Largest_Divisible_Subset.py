'''
dynamic programming
O(n^2)
no short cut

Result:
Runtime: 388 ms, faster than 79.64% of Python online submissions for Largest Divisible Subset.
Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Largest Divisible Subset.
'''
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        maxLengths = [];
        maxLengthsPre = [];
        
        maxSubsetLength = 0
        maxSubsetLengthEnd = 0;
        
        #
        for i in range(len(nums)):
            maxLengthOfI = 1;
            maxLengthPre = i;
            # check all i-1 elements and find max previous length
            for j in range(i):
                if (nums[i] % nums[j] == 0):
                    # update maxLengthOfI to max (previous length + 1)
                    if maxLengthOfI < maxLengths[j] + 1:
                        maxLengthOfI = maxLengths[j] + 1
                        maxLengthPre = j
            # update memory table for each element
            maxLengths.append(maxLengthOfI)
            maxLengthsPre.append(maxLengthPre)
            # check it is max length
            if maxSubsetLength < maxLengthOfI:
                maxSubsetLength = maxLengthOfI
                maxSubsetLengthEnd = i
                
        # get result array
        if maxSubsetLength <= 0:
            return []
        
        #print(maxLengths)
        #print(maxLengths)
        #print(maxLengthsPre)
        
        result = [0]*maxSubsetLength
        resultIndex = maxSubsetLengthEnd
        for i in range(maxSubsetLength):
            tmp = (i+1)*-1
            result[tmp] = nums[resultIndex]
            #print(result)
            previousNum = maxLengthsPre[resultIndex]
            
            if maxLengthsPre[resultIndex] == resultIndex:
                break
            
            resultIndex = maxLengthsPre[resultIndex]
            
           
        
        return result
                        