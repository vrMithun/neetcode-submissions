# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev=None
        curr=head
        nxt=curr.next
        while curr:
            if nxt==None:
                head=curr
            curr.next=prev
            prev=curr
            curr=nxt
            if nxt:
                nxt=curr.next
        return head


        