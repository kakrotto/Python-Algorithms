#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2026/1/24 00:47
# @Author :  Allen
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], idx]
            d[num] = idx
        return []