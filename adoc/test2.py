#!/usr/bin/env python3
from copy import deepcopy


def process(code):
    pos = 0
    while pos < len(code):
        if code[pos] == 99:
            break
        elif code[pos] == 1:
            code[code[pos + 3]] = code[code[pos + 1]] + code[code[pos + 2]]
        elif code[pos] == 2:
            code[code[pos + 3]] = code[code[pos + 1]] * code[code[pos + 2]]
        else:
            raise ValueError(code[pos])
        pos += 4
    return code


def find(value, code):
    for input1 in range(len(code)):
        for input2 in range(len(code)):
            new_code = deepcopy(code)
            new_code[1], new_code[2] = input1, input2
            res = process(new_code)[0]
            if value == res:
                return input1, input2
    return None, None


if __name__ == "__main__":

    tests = [[1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
             [1, 0, 0, 0, 99],
             [2, 3, 0, 3, 99],
             [2, 4, 4, 5, 99, 0],
             [1, 1, 1, 4, 99, 5, 6, 0, 99]
    ]

    example = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 5, 19, 23, 1, 23, 5,
          27, 1, 27, 13, 31, 1, 31, 5, 35, 1, 9, 35, 39, 2, 13, 39, 43, 1, 43, 10, 47, 1, 47, 13,
          51, 2, 10, 51, 55, 1, 55, 5, 59, 1, 59, 5, 63, 1, 63, 13, 67, 1, 13, 67, 71, 1, 71, 10,
          75, 1, 6, 75, 79, 1, 6, 79, 83, 2, 10, 83, 87, 1, 87, 5, 91, 1, 5, 91, 95, 2, 95, 10, 99,
          1, 9, 99, 103, 1, 103, 13, 107, 2, 10, 107, 111, 2, 13, 111, 115, 1, 6, 115, 119, 1, 119, 10,
          123, 2, 9, 123, 127, 2, 127, 9, 131, 1, 131, 10, 135, 1, 135, 2, 139, 1, 10, 139, 0, 99, 2, 0, 14, 0]

    example_fix = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 5, 19, 23, 1, 23, 5,
          27, 1, 27, 13, 31, 1, 31, 5, 35, 1, 9, 35, 39, 2, 13, 39, 43, 1, 43, 10, 47, 1, 47, 13,
          51, 2, 10, 51, 55, 1, 55, 5, 59, 1, 59, 5, 63, 1, 63, 13, 67, 1, 13, 67, 71, 1, 71, 10,
          75, 1, 6, 75, 79, 1, 6, 79, 83, 2, 10, 83, 87, 1, 87, 5, 91, 1, 5, 91, 95, 2, 95, 10, 99,
          1, 9, 99, 103, 1, 103, 13, 107, 2, 10, 107, 111, 2, 13, 111, 115, 1, 6, 115, 119, 1, 119, 10,
          123, 2, 9, 123, 127, 2, 127, 9, 131, 1, 131, 10, 135, 1, 135, 2, 139, 1, 10, 139, 0, 99, 2, 0, 14, 0]

    for t in tests:
        print(t)
        res = process(t)
        print(res)
        print("=" * 80)

    res = process(example_fix)
    print(",".join([str(el) for el in res]))

    i1, i2 = find(19690720, example)
    print(i1, i2, 100 * i1 + i2)