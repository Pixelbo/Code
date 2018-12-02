import numpy as numpy

def NN (m1, m2, w1, w2, b):
    z = m1 * w1 + m2 * w2 + b
    return sigmoid(z)

def NN2 (m1, m2, w1, w2, b):
    a = m1 * w1 + m2 * w2 + b
    return sigmoid(a)

def NN1_2 (m1_2, m2_2, w1, w2, b):
    i = m1_2 * w1 + m2_2 * w2 + b
    return sigmoid(i)


def sigmoid(x):
    return 1/(1 + numpy.exp(-x))

w1_1 = numpy.random.randn()
w1_2 = numpy.random.randn()
w1_3 = numpy.random.randn()
w1_4 = numpy.random.randn()

w2_1 = numpy.random.randn()
w2_2 = numpy.random.randn()

m1 = 3
m2 = 6

b = numpy.random.randn()

N1 = NN (m1, m2, w1_1, w1_2, b)
N2 = NN2 (m1, m2, w1_3, w1_4, b)
N1_2 = NN1_2 (N1, N2, w2_1, w2_2, b)

print(N1)
print(N2)
print(N1_2)

if (N1_2 > 0.5):
    print("blue")
else:
    print("red")
