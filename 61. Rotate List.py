# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # head is empty
        # only one element
        # k is zero
        if head is None or head.next is None or k == 0:
            return head
        
        
        anchor = None
        point = head
        count = 1
        
        while point.next != None:
            point = point.next
            count = count + 1
            
            if count > k:
                if anchor is None:
                    anchor = head
                else:
                    anchor = anchor.next
        
        # no need to change
        if count == k :
            return head
        elif count < k:
            newK = k % count
            # no need to change
            if newK == 0:
                return head
            # move the anchor
            moving = count - newK
            for i in range(moving):
                if anchor is None:
                    anchor = head
                else:
                    anchor = anchor.next
        
        # do the rotation
        result = anchor.next
        point.next = head
        anchor.next = None
        
        return result
        