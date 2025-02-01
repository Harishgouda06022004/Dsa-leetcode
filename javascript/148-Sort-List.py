# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        temp=head
        while temp!=None:
            stack.append(temp.val)
            temp=temp.next
        # print(stack)
        temp1=head
        stack=sorted(stack)
        print(stack)
        for val in stack:
            temp1.val=val
            temp1=temp1.next
           
        return head