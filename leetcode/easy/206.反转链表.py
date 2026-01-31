#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2026/1/31 23:15
# @Author :  Allen
# 三指针
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next # 临时保存下一个节点指针
            current.next = prev  # 反指指针
            prev = current   # 移动指针1
            current = next_node  # 移动指针2
        return prev