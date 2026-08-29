# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        dummy = ListNode(0, head) #在原本的head前面建立一個新的節點
        #dummy: 0->1->2->3->4

        while head: 
            head = head.next
            length += 1 # 算出總長度
        # 此時，head指向的是 None, 因此需要用dummy在跑一次

        # 計算出需要被刪除的node位置

        delete = length - n 
        curr = dummy

        for _ in range(delete):
            curr = curr.next # 跑到2之後
        curr.next = curr.next.next # 2->4

        return dummy.next 



        
