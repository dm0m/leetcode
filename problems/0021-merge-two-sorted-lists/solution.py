from __future__ import annotations

# 21. Merge Two Sorted Lists  (Easy)
# https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next
        
class Solution:
    @classmethod
    def mergeTwoLists(cls, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1 and not list2:
            return None
        head: ListNode = ListNode()
        tail: ListNode = head
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            elif list1:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            elif list2:
                tail.next = list2
                list2 = list2.next        
                tail = tail.next
        return head.next
                
                
if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    head = Solution.mergeTwoLists(l1, l2)
    
    result: list[int] = []
    temp = head
    while temp:
        result.append(temp.val)
        temp = temp.next
    print(result)