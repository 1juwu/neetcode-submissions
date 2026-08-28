# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        prev = None # 指針


        # 只要還有節點沒處理就繼續
        while head:
            nxt = head.next     # 1. 先暫存下一個節點，避免指針轉向後迷路
            head.next = prev    # 2. 將當前節點反轉，指向前一個節點
            prev = head         # 3. prev 指標往前移一步
            head = nxt          # 4. curr 指標往前移一步

        # 走完後，prev 就是新的頭部節點
        return prev


        