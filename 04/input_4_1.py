#! /usr/bin/env python3

import re


total = 0
for number in range(193651, 649729):
    number = str(number)
    if re.search(r"(.)\1", number):
        if number[0] <= number[1] <= number[2] <= number[3] <= number[4] <= number[5]:
            total += 1

print(total)
