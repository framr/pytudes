#!/usr/bin/env python3
import sys

def compute_fuel(mass):
    res = 0
    while mass > 0:
        mass = int(mass / 3) - 2
        if mass > 0:
            res += mass
    return res


if __name__ == "__main__":
    res = 0
    for line in open(sys.argv[1]):
        val = int(line.strip())
        res += compute_fuel(val)
    print(res)
