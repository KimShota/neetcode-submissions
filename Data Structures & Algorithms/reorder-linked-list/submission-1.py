# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        array = []

        cur = head 
        while cur != None:
            array.append(cur)
            cur = cur.next 
        
        left = 0
        right = len(array) - 1

        while left < right:
            array[left].next = array[right]
            left += 1
            array[right].next = array[left]
            right -= 1
        
        array[left].next = None 


        
