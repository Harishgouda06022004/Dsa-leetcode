# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict1={}
        temp=head
        
        while temp:
            if temp in dict1:
                return temp
            dict1[temp]=True
            temp=temp.next
            
        return None