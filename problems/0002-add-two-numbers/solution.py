from __future__ import annotations
# 2. Add Two Numbers  (Medium)
# https://leetcode.com/problems/add-two-numbers/

class Node:
    def __init__(self, value: int = 0, next: Node | None = None):
        self.value: int = value
        self.next: Node | None = next

class Solution:
    @classmethod
    def add_two_numbers(cls, l1_node: Node, l2_node: Node) -> Node | None:
        l1_temp: Node | None = l1_node
        l2_temp: Node | None = l2_node
        head: Node = Node()
        tail: Node | None = head
        carry: int = 0
        while l1_temp or l2_temp or carry:
            result: int = 0
            if carry:
                result += carry
                carry = 0
            if l1_temp:    
                result += l1_temp.value
                l1_temp = l1_temp.next
            if l2_temp:
                result += l2_temp.value 
                l2_temp = l2_temp.next
            tail.next = Node(result % 10)
            tail = tail.next
            if result >= 10:
                carry += 1
            result = 0
        return head.next

# if __name__ == "__main__":
#     l1 = Node(9, Node(9, Node(9, Node(9, Node(9, Node(9, Node(9)))))))
#     l2 = Node(9, Node(9, Node(9, Node(9))))
#     head = Solution.add_two_numbers(l1, l2)
#     # print(head.value if head else None) 
    
#     result: list[int] = []
#     temp = head
#     while temp:
#         result.append(temp.value)
#         temp = temp.next
        
#     print(result)
        