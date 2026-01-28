#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2026/1/28 23:20
# @Author :  Allen
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (str(x)[::-1]) == str(x)
