#!/usr/bin/env python3

def process(code):
    pos = 0
    while pos < len(code):
        if code[pos] == 99:
            break
        elif code[pos] == 1:
            code[pos + 3] = code[pos + 1] + code[pos + 2]
        elif code[pos] == 2:
            code[pos + 3] = code[pos + 1] * code[pos + 2]
        else:
            raise ValueError(code[pos])
        pos += 4
    return code


if __name__ == "__main__":

    tests = []