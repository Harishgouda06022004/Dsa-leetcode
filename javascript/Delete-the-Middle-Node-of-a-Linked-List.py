1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if head and head.next is None:
9            return None
10        cnt=0
11        temp=head
12        while temp!=None:
13            cnt+=1
14            temp=temp.next
15        print(cnt)
16        mid=(cnt//2)+1
17        temp=head
18        prev=None
19        while temp!=None:
20            mid=mid-1
21            if mid==0:
22               prev.next=temp.next
23            prev=temp
24            temp=temp.next
25        return head