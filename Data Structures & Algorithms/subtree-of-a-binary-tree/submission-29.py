# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def serialize(node):
            if not node:
                return ",#"  # 如果節點是空的，用 '#' 代表空節點
            # 格式：,當前值 + 左子樹字串 + 右子樹字串
            return f",{node.val}" + serialize(node.left) + serialize(node.right)
        
        # 只要 subRoot 的字串出現在 root 的字串裡面，就是 True
        return serialize(subRoot) in serialize(root)
                
                





