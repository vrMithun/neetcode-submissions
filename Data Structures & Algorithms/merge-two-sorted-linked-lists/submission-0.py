# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result=None
        curr=None
        if not list1:
            return list2
        if not list2:
            return list1
        while list1 and list2:
            tempnode=ListNode()
            if list1.val<list2.val:
                tempnode=list1
                list1=list1.next
            else:
                tempnode=list2
                list2=list2.next
            if not result:
                result=tempnode
                curr=result
            else:
                if tempnode:
                    curr.next=tempnode
                    curr=curr.next
        if list1:
            curr.next=list1
        if list2:
            curr.next=list2
        return result
