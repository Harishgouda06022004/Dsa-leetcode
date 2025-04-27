# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy=ListNode()
        # current=dummy
        # while list1 and list2:
        #     if list1.val<list2.val:
        #         current.next=list1
        #         list1=list1.next
        #     else:
        #         current.next=list2
        #         list2=list2.next
        #     current=current.next
        # if list1:
        #     dummy.next=list1
        # if list2:
        #     dummy.next=list2
        # print(dummy)
        # return dummy
    #     dummy = ListNode()
    #     current = dummy  # Pointer to build the new merged list
        
    #     print(\Starting merge process\)
    #     print(\Initial List1:\, self.printList(list1))
    #     print(\Initial List2:\, self.printList(list2))
        
    #     # Iterate through both lists and merge them
    #     while list1 and list2:
    #         print(f\\
Comparing: List1 node {list1.val} with List2 node {list2.val}\)
            
    #         if list1.val < list2.val:
    #             print(f\Adding {list1.val} from list1 to merged list\)
    #             current.next = list1  # Add the node from list1
    #             list1 = list1.next  # Move list1 to the next node
    #         else:
    #             print(f\Adding {list2.val} from list2 to merged list\)
    #             current.next = list2  # Add the node from list2
    #             list2 = list2.next  # Move list2 to the next node

    #         # Move current to the last node in the merged list
    #         current = current.next

    #         print(\Current merged list:\, self.printList(dummy.next))

    #     # If any nodes are left in either list, append them
    #     if list1:
    #         print(f\\
Appending remaining nodes from list1: {self.printList(list1)}\)
    #         current.next = list1
    #     if list2:
    #         print(f\\
Appending remaining nodes from list2: {self.printList(list2)}\)
    #         current.next = list2

    #     print(\Final merged list:\, self.printList(dummy.next))
        
    #     return dummy.next  # Return the merged list, starting from the node after dummy

    # # Helper function to print linked list from a given node
    # def printList(self, node: Optional[ListNode]) -> str:
    #     values = []
    #     while node:
    #         values.append(str(node.val))
    #         node = node.next
    #     return \ -> \.join(values) if values else \None\
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1
        
        # # Compare the current nodes of list1 and list2
        # if list1.val < list2.val:
        #     # list1's current node is smaller, merge list1's next with list2
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     # list2's current node is smaller, merge list1 with list2's next
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val<list2.val:
            list1.next=self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next=self.mergeTwoLists(list1,list2.next)
            return list2