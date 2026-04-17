# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s , f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next
        
        #found mid point, now assing start of 2nd part and destroy link
        second_half = s.next
        s.next = None
        prev = None

        while second_half:
            second_half_next = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = second_half_next
        
        #time to merge them both
        first_half, second_half = head, prev
        
        while first_half and second_half:
            #store values of next
            temp1 = first_half.next
            temp2 = second_half.next
            #change the linking for 1st part
            first_half.next = second_half
            second_half.next = temp1
            #move pointer forward
            first_half = temp1
            second_half = temp2