#!/usr/bin/env python3
from itertools import groupby


def valid_number2(num):
    nums = [int(dd) for dd in str(num)]
    collapsed = []
    for dd, it in groupby(nums):
        collapsed.append((dd, len(list(it))))

    prev = -1
    have_same = False
    for digit, cnt in collapsed:
        if digit < prev:
            return False
        if cnt == 2:
            have_same = True
        prev = digit
    if not have_same:
        return False
    return True


def check(min_val, max_val):
    cnt = 0
    for num in range(min_val, max_val + 1):
        if valid_number2(num):
            cnt += 1
    return cnt


if __name__ == "__main__":


    #tests = [(111111, True), (223450, False), (123789, False)]
    tests = [(112233, True), (123444, False), (111122, True)]


    for num, res in tests:
        print(num, res, valid_number2(num))

    print(check(356261, 846303))