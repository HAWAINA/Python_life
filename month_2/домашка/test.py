import numpy

random_integer_array = numpy.random.random_integers(1, 10, 5)
print("1-мерный массив случайных целых чисел \n", random_integer_array, "\n")

random_integer_array = numpy.random.random_integers(1, 10, size=(3, 2))
print("2-мерный массив случайных целых чисел \n", random_integer_array)