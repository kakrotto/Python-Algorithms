#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2026/2/24 13:49
# @Author :  Allen
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(x):
            total = 0
            while x > 0:
                x, digit = divmod(x, 10)
                total += digit * digit
            return total
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = get_next(n)
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(3))

