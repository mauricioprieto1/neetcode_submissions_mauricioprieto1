# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        2 pointers
        L, R

        R to the end of the LL

        L one place behind n (n - 1)

        [1,2,3,4,5] n = 2
             L        
                 R


        [3, 4, 5]
         P

        1. loop over n, move R n times
        2. keep moving 1 at a time, until R.next = null
        3. L.next = L.next.next
        4 return head
        
        node with
        """
        dummy = ListNode(0,head)
        l,r = dummy, dummy # handle the edge case of having to remove the head of the LL
        for i in range(n): # walk R "n" steps into the LL
            r = r.next
        
        while r.next:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next