import numpy


def test_matmul():

    A = numpy.ones((5, 5))

    B = numpy.diag(numpy.arange(5) + 1)

    print()
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)

    result = A @ B

    assert False

    print(result)

