# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        if not p and not q:
            return True
        
        # 2. 如果其中一邊是空節點，另一邊不是（結構不同）；
        #    或者兩邊都有節點，但裡面的數值不一樣（數值不同），回傳 False
        if not p or not q or p.val != q.val:
            return False
        
        # 3. 按照剛才學到的「先左後右」非同步順序：
        #    先影分身去檢查兩顆樹的「左子樹」是否相同，都對了，才去檢查「右子樹」
        return self.isSameTree(p.left, q.left) and      self.isSameTree(p.right, q.right)