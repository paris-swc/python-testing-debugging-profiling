from numpy.testing.utils import assert_allclose
import numpy

from preprocess import whiten

def test_1d():
    test_data = numpy.array([1, 3, 5, 7])
    whitened = whiten(test_data)
    assert_allclose(whitened.mean(), 0)
    assert_allclose(whitened.std(), 1)
    assert_allclose(whitened*test_data.std() + test_data.mean(),
                    test_data)
def test_2d():
    test_data = numpy.array([[1, 3, 5, 7],
                             [2, 3, 4, 1]])
    whitened = whiten(test_data)
    assert_allclose(whitened.mean(), 0)
    assert_allclose(whitened.std(), 1)
    assert_allclose(whitened*test_data.std() + test_data.mean(),
                    test_data)
