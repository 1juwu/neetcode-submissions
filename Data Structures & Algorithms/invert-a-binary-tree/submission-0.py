# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 2. 交換當前節點的左右子樹
        # Python 的平行賦值寫法，可以不用寫暫存變數（temp），一行直接對調指標
        root.left, root.right = root.right, root.left
        
        # 3. 遞迴去翻轉左子樹和右子樹
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 4. 最後回傳翻轉完畢的根節點
        return root