# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            head = None 
            return head
        
        # go to the end of the list and find the size of the linked list, N
        # remove N - n th node
        size = 0
        cur = head
        while cur != None:
            cur = cur.next 
            size += 1
        
        removal = size - n - 1
        cur = head
        if removal == 0:
            cur.next = cur.next.next 
            return head

        if removal == -1:
            head = head.next 
            return head

        while removal != 0:
            cur = cur.next
            removal -= 1
        
        cur.next = cur.next.next 

        return head
        
        
        
        
            





        
