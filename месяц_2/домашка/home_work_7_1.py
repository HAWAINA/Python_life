import sys
import numpy

A = random_integer_array = numpy.random.random_integers(1, 1000, 999)
print(random_integer_array, "\n")

for i in range(len(A)):

    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print("Finish Sort")
for i in range(len(A)):
    print("%d" % A[i], end=" ""\n")