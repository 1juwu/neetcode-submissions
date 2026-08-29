# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1. 快慢指針找中點: 快指針1次移動2個、慢指針1次移動1個，所以快指針如果到終點，則慢指針剛好在中間
        
        slow = head
        fast = head.next 

        while fast and fast.next:
            slow = slow.next  # 慢指針：走1步
            fast = fast.next.next  # 快指針：走2步

        # 2. 將後半段切斷，開始反轉後半段   
        second = slow.next
        slow.next = None  # 將前半段的尾端指向 None，斷開兩段

        tmp = None # 設立一個空指標
        
        while second: # 反轉後半段
            nxt = second.next # 儲存原本指向的指標 (6 "-> 8")
            second.next = tmp # 將原本的指標指向 None (6 "-> tmp")
            tmp = second # 原本的節點None，往前一個變成6
            second = nxt # 指向的節點6，往前移動一個變成8 (6 => 8 )

        # 完成後半段反轉(10->8->6->None)，且second停在None, tmp停在10
        second = tmp # 因此要把tmp賦值給10

        # 3. 後半段接到前半段 (2 -> 4)
        while second: # 後半段永遠大於前半段
            tmp1 = head.next #(2 "-> 4")
            tmp2 = second.next #( 10 "-> 8")
            
            head.next = second #(2->10->8..)
            second.next = tmp1 #(2->10->4..)

            head = tmp1
            second = tmp2

        return second

            







        

                    