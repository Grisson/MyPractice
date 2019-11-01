# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        sum = 0
        if root:
            if R < root.val:
                return self.rangeSumBST(root.left, L, R)
            elif root.val < L:
                return self.rangeSumBST(root.right, L, R)
            else:
                sum = sum + root.val
                if L < root.val:
                    sum = sum + self.rangeSumBST(root.left, L, root.val)
                
                if root.val < R:
                    sum = sum + self.rangeSumBST(root.right, root.val, R)
            
        return sum
                    
        