# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # 1. 建立一個集合，用來記錄「拜訪過的節點物件」
        visited = set()
        
        # 2. 開始走訪鏈結串列
        while head:
            # 3. 如果當前這個節點物件已經在集合裡了，代表「有環」！
            if head in visited:
                return True
            
            # 4. 如果沒出現過，把「整個節點物件」加進集合中
            visited.add(head)
            
            # 5. 關鍵！一定要讓指標往前走，否則會變成死迴圈（MemoryError）
            head = head.next
            
        # 6. 如果順利走到 None（終點），代表沒有環
        return False   