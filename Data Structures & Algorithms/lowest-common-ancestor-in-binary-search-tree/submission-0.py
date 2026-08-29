# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        
        while curr:
            # 情況 1: p 與 q 都在左子樹
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # 情況 2: p 與 q 都在右子樹
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # 情況 3: 找到分歧點（一個在左、一個在右，或 curr 就是 p 或 q）
            else:
                return curr

