# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low, high):
            # 空節點視為合法 BST
            if not node:
                return True
            
            # 當前節點值必須嚴格落在 (low, high) 範圍內
            if not (low < node.val < high):
                return False
            
            # 左子樹所有節點必須 < node.val (上限更新為 node.val)
            # 右子樹所有節點必須 > node.val (下限更新為 node.val)
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
            
        return validate(root, -1000000000, 1000000000)
        
            