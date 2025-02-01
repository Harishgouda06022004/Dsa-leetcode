# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow=head
        # fast=head
        # prev=None
        # while fast and fast.next:
        #     prev=slow
        #     slow=slow.next
        #     fast=fast.next.next
            
        #     # slow=slow.next
        # prev.next=slow.next
        # return head
        if head and head.next is None:
            return None
        cnt=0
        temp=head
        while temp!=None:
            cnt+=1
            temp=temp.next
        print(cnt)
        mid=(cnt//2)+1
        temp=head
        prev=None
        while temp!=None:
            mid=mid-1
            if mid==0:
               prev.next=temp.next
            prev=temp
            temp=temp.next
        return head
            