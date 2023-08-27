#!/usr/bin/env python3
# -*- coding: utf-8 -*-

A = [-3.5, 6.2, 1.8, -8.1, 0, 10.5, -4.7, 2.6, 7.9, -11.3]
C = 4.2

count = 0
for element in A:
    if element > C:
        count += 1
print("Count: ", count)

max_index = A.index(max(A, key=abs))
product = 1
for element in A[max_index+1:]:
    product *= element
print("Product: ", product)

A.sort()
negatives = [x for x in A if x < 0]
positives = [x for x in A if x >= 0]
sorted_A = negatives + positives
print("Sorted A: ", sorted_A)