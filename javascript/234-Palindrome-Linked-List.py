# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        temp=head
        while temp!=None:
            stack.append(temp.val)
            temp=temp.next
        # stack=ListNode(stack)
        print(stack)
        print(stack)
        temp=head
        while temp!=None:
            if temp.val!=stack.pop():
                return False
            temp=temp.next
            # stack=stack.next
        return True

            