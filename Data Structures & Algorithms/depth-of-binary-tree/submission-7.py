# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
     
        # 1. 關鍵防線：如果是空節點，立刻回傳深度 0，阻止它繼續讀取 .left
        if not root:
            return 0
        
        # 2. 只有確定 root 不是 None，才可以安全地讀取 root.left 和 root.right
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 3. 這一層的深度就是：左右子樹比較深的那個 + 1（代表當前這一層）
        return max(left_depth, right_depth) + 1
        