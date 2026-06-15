"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head

        cur = head
        hashMap = {}

        while cur != None:
            newNode = Node(cur.val)
            hashMap[cur] = newNode 
            cur = cur.next 

        cur = head
        while cur != None:
            if cur.next is None:
                hashMap[cur].next = None
            else: 
                hashMap[cur].next = hashMap[cur.next]
            
            if cur.random is None:
                hashMap[cur].random = None 
            else:
                hashMap[cur].random = hashMap[cur.random]

            cur = cur.next 
        
        return hashMap[head]

        

        

            
            

