# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = head
# null-0-1-2-3-null
# prev cur
# null-3-2-1-0-null

        while cur:
            tmp = cur.next #tmp =1
            cur.next = prev #
            prev = cur
            cur = tmp
        return prev