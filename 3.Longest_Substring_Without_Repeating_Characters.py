class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = {}
        maxLength = 0
        currentLength = 0;
        for i in range(len(s)):
            if s[i] in tmp:
                # duplicate happens
                # last seen position for the character
                lastPosition = tmp[s[i]]
                # start position for current substring
                currentStartPosition = i - currentLength
                if lastPosition < currentStartPosition:
                    # extent current Length
                    currentLength += 1
                else:
                    # log current Length
                    if maxLength < currentLength:
                        maxLength = currentLength
                    # reset current length
                    currentLength = i - lastPosition
            else:
                currentLength += 1
                
            # set/reset last seen position for the character
            tmp[s[i]] = i
        
        if maxLength < currentLength:
            maxLength = currentLength
         
        return maxLength
        #return max(maxLength, currentLength)
        
            