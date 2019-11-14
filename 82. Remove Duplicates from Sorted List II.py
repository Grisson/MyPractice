# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return head
        
        result = None
        resultTail = None
        currentNode = head
        nextNode = head.next
        isDuplicate = False
        
        if nextNode is None:
            return head
        
        
        while nextNode is not None:
            # find a duplicated val
            if currentNode.val == nextNode.val:
                isDuplicate = True
            else:
                # find a new val
                # check if previous value is duplicated
                if not isDuplicate:
                    # add currentNode to result list
                    if result is None:
                        result = currentNode
                        
                    if resultTail is None:
                        resultTail = currentNode
                    else:
                        resultTail.next = currentNode
                        resultTail = resultTail.next
                    
                # update current Node
                isDuplicate = False
                currentNode = nextNode
            
            # move nextNode
            nextNode = nextNode.next
                    
        if not isDuplicate:
            if result is None:
                result = currentNode
                        
            if resultTail is None:
                resultTail = currentNode
            else:
                resultTail.next = currentNode
                resultTail = resultTail.next
                
        if resultTail is not None:
            resultTail.next = None
            
        return result
