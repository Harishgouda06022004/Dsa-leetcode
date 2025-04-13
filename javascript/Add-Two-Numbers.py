# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummyNode=ListNode(-1)
        # temp1=l1
        # temp2=l2
        # curr=dummyNode
        # carry=0
        # while temp1!=None or temp2!=None:
        #     sum=carry
        #     if temp1:
        #         sum+=temp1.val
        #         temp1=temp1.next
        #     if temp2:
        #         sum+=temp2.val
        #         temp2=temp2.next
        #     newNode=ListNode(sum%10)
        #     carry=sum//10
        #     curr.next=newNode
        #     curr=curr.next
        #     # if temp1:
        #     #     temp1.next
        #     # if temp2:
        #     #     temp2.next
        # if carry:
        #     newNode=ListNode(carry)
        #     curr.next=newNode
        # return dummyNode.next
        dummyNode=ListNode(-1)
        carry=0
        curr=dummyNode
        temp1=l1
        temp2=l2
        while temp1!=None or temp2!=None:
            sum1=carry
            if temp1:
                sum1+=temp1.val
                temp1=temp1.next
            if temp2:
                sum1+=temp2.val
                temp2=temp2.next
            newNode=ListNode(sum1%10)
            carry=sum1//10
            curr.next=newNode
            curr=curr.next
        if carry:
            newNode=ListNode(carry)
            curr.next=newNode
        return dummyNode.next

        