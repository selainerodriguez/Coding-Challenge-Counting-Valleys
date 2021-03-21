#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    num_of_valleys = 0
    current_altitude = 0
    next_altitude = 0
    moves = []
    for i in range(steps):
        if path[i] == "U":
            moves.append(1)
        elif path[i] == "D":
            moves.append(-1)
    for i in range(len(moves) - 1):
        current_altitude += moves[i]
        next_altitude = current_altitude + moves[i + 1]
        if next_altitude >= 0 and current_altitude < 0:
            num_of_valleys += 1
    return num_of_valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
 
