# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #step 1 is to count everytime if k nodes exist
        counter = head
        for _ in range(k):
            if not counter:
                return head
            counter = counter.next
        
        #step 2 is to reset the head and reverse k nodes
        cur = head
        prev = None

        for _ in range(k):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        next_group_leader = self.reverseKGroup(cur, k)
        head.next = next_group_leader

        return prev