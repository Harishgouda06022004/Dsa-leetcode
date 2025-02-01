# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        temp=head
        while temp!=None:
            stack.append(temp.val)
            temp=temp.next
        print(stack)
        # stack=set(stack)
        # print(stack)
        # stack=list(stack)
        # print(stack)
        
        # for val in stack:
        #     temp.val=val
        #     temp=temp.next
        # return temp
        # while temp!=None:
        #     temp.val=stack.pop()
        #     temp=temp.next
        # return head
        # s={}
        # temp=head
        # for val in stack:
        #     if val in s:
        #         temp.next=temp.next
        #     temp.val=val            
        #     temp=temp.next
        # return head
        seen=set()
        prev=None
        temp=head
        while temp!=None:
            if temp.val in seen:
                prev.next=temp.next
            else:
                seen.add(temp.val)
                prev=temp
            temp=temp.next
        return head
            