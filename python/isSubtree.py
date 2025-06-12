# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, s, t):
        # If both are None, they're the same
        if not s and not t:
            return True
        # If one is None or values don't match, not the same
        if not s or not t or s.val != t.val:
            return False
        # Recursively compare left and right children
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
# Example usage:
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)) 
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
solution = Solution()
print(solution.isSubtree(root, subRoot))  # Output: True   