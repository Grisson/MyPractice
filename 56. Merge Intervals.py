class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        initialIntervals = len(intervals)
        result = []
        
        for newInterval in intervals:
            isNewInterval = True
            if len(result) > 0:
                i = 0
                while i < len(result):
                    targetInterval = result[i]
                    if targetInterval[1] < newInterval[0] or newInterval[1] < targetInterval[0]:
                        # pass check next targetInterval
                        # check next newInterval:
                        i = i + 1
                    else:
                        # there is overlap
                        result[i] = [min(targetInterval[0], newInterval[0]), max(targetInterval[1], newInterval[1])]
                        isNewInterval = False
                        i = i + 1
                        break
                    
                    
                
            if isNewInterval:
                result.append(newInterval)
                
                
            #print(result)
        
        
        mergedIntervals = len(result)
        
        if initialIntervals == mergedIntervals:
            return result
        else:
            return self.merge(result)

        
    def merge2(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        
        out = []
        if len(intervals)<2:
            return intervals
        
        intervals.sort(key = lambda x: x[0])
        low = intervals[0][0]
        high = intervals[0][1]
        
        out.append(intervals[0])
        for (x, y) in intervals:
            if high < x: # meaning no overallping
                out.append((x, y))
                low = x
                high = y
            else:
                out.pop()
                out.append((min(x, low), max(high, y)))
                low = min(low, x)
                high = max(high, y)
        return out 