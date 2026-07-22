# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tmp = head
        tmp_fast = head
        while tmp_fast is not None and tmp_fast.next is not None:
            tmp = tmp.next
            tmp_fast = tmp_fast.next.next
            if tmp_fast == tmp:
                return True
        return False

        