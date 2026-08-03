# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        '''
            p
              c1    
        [1,2,4]
                p
                  c2
        S -> [1,3,5]
        '''
        # use a sentinel node
        sentinel = ListNode()
        curr1 = list1
        curr2 = list2
        pointer = sentinel
        while curr1 and curr2:
            #print('curr1: ', curr1.val)
            #print('curr2: ', curr2.val, '\n')
            if curr1.val >= curr2.val:
                #print('curr 1 is greater or equal')
                pointer.next = curr2
                pointer = pointer.next   
                curr2 = curr2.next   
                continue          
            if curr1.val < curr2.val:
                #print('curr 1 is less than')
                pointer.next = curr1
                pointer = pointer.next 
                curr1 = curr1.next
                continue
        if curr1:
            pointer.next = curr1
        if curr2:
            pointer.next = curr2
        return sentinel.next