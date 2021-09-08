# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        def _flatten(root):
            if root is None:
                return
            _flatten(root.left)
            _flatten(root.right)
            
            if root.left is not None:
                l, r = root.left, root.right
                root.left, root.right = None, root.left
                while l.right is not None:
                    l = l.right
                l.right = r
        
        _flatten(root)
