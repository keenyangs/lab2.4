#!/usr/bin/env python3
# -*- coding: utf-8 -*-

A = []
for i in range(10):
    A.append(int(input()))
diff_sum = 0
count = 0
for element in A:
    if element > 0 and element % 11 == 0:
        diff_sum += element
        count += 1
print("Разность положительных элементов кратных 11: ", diff_sum)
print("Их количество : ", count)