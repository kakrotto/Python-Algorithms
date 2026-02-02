#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2026/2/2 22:36
# @Author :  Allen
# 快慢指针
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return slow

