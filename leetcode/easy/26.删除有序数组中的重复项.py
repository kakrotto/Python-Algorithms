#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2026/2/2 19:31
# @Author :  Allen
# 快慢指针
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
