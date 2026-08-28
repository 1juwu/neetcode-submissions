# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. 建立一個虛擬開頭節點（dummy），以及用來往後串接的指標 curr
        dummy = ListNode(-1) # 建立一個 dummy (指向None)
        curr = dummy # 建立一樣的 dummy 指標(可移動)

        # 2. 當兩個串列都還有節點時，比較大小
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1     # 接上比較小的 list1
                list1 = list1.next   # list1 往前進一步 (原本的list1刪除)
            else:
                curr.next = list2     # 接上比較小的 list2
                list2 = list2.next   # list2 往前進一步
            
            curr = curr.next    # curr 往前移到剛接好的節點

        # 3. 把剩下還沒走完的那一串直接接在尾端
        if list1 is not None:
            curr.next = list1
        else:
            curr.next = list2
        # 4. dummy 的下一個才是真正合併後的頭節點
        return dummy.next

