#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head
        l, cur = 0, head
        while cur:
            l += 1
            cur = cur.next
        k %= l
        if k == 0: return head
        fast, slow = head, head
        while k:
            fast = fast.next
            k -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head
# @lc code=end

