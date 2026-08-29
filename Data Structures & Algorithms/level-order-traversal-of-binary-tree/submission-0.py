# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        # 初始化最終的二維列表，用來存放每一層的節點值列表
        result = []
        # 初始化佇列（Queue），並將根節點作為第一個元素放進佇列中
        queue = deque([root])
        
        # 當佇列內還有節點時，代表還有層級尚未處理完畢，繼續迴圈
        while queue:
            # 取得當前佇列長度，此長度剛好等於「當前層」所擁有的節點總數（關鍵步驟）
            level_size = len(queue)
            # 初始化一個列表，專門儲存「當前這一層」所有節點的數值
            current_level = []
            
            # 依序處理當前層的每一個節點（固定執行 level_size 次）
            for _ in range(level_size):
                # 從佇列最左端（頭部）取出一個節點，時間複雜度為 O(1)
                node = queue.popleft()
                # 將取出的節點數值加入當前層的列表中
                current_level.append(node.val)
                
                # 若該節點存在左子節點，將左子節點加入佇列尾端（供下一層處理）
                if node.left:
                    queue.append(node.left)
                # 若該節點存在右子節點，將右子節點加入佇列尾端（維持從左到右的順序）
                if node.right:
                    queue.append(node.right)
            
            # 當整層節點都處理完畢後，將當前層的結果列表加入最終結果 result 中
            result.append(current_level)
            
        # 佇列清空後，回傳包含每一層節點值的二維列表
        return result