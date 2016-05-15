---
layout: page
title: Testing
subtitle: Running Tests with pytest
minutes: 10
---
> ## Learning Objectives {.objectives}
>
> -   Understand how to run a test suite using the pytest framework
> -   Understand how to read the output of a pytest test suite


We created a suite of tests for our rescale function, but it was annoying to run
them one at a time. It would be a lot better if there were some way to run them
all at once, just reporting which tests fail and which succeed.

Thankfully, that exists. Let us test the following function that we will put
into a file `preprocess.py`:

~~~ {.python}
def whiten(data):
    """
    Return a whitened copy of the data, i.e. data with zero mean and unit
    variance.

    Parameters
    ----------
    data : ndarray
        The data to whiten.

    Returns
    -------
    whitened : ndarray
        The whitened data.
    """
    centered = data - data.mean()
    whitened = centered / data.std()
    return whitened
~~~

We will test this function in a file `test_whiten.py`:

~~~ {.python}
from numpy.testing.utils import assert_allclose, assert_equal
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
~~~

Now we can run the [*pytest* utility](http://pytest.org) in the directory where
we stored the test file:

~~~ {.bash}
$ py.test
~~~
~~~ {.output}
================================= test session starts ==================================
platform linux -- Python 3.5.1, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: [...], inifile:
collected 2 items

test_whiten.py .F

======================================= FAILURES =======================================
_______________________________________ test_2d ________________________________________

    def test_2d():
        test_data = numpy.array([[1, 3, 15],
                                 [12, 3, 4]])
        whitened = whiten(test_data)
>       assert_allclose(whitened.mean(), 0)
E       AssertionError:
E       Not equal to tolerance rtol=1e-07, atol=0
E       
E       (mismatch 100.0%)
E        x: array(6.47630097698008e-17)
E        y: array(0)

test_whiten.py:17: AssertionError
========================== 1 failed, 1 passed in 0.12 seconds ==========================
~~~

> ## Alternatives to pytest {.callout}
> An alternative to `pytest` are the [*nose*](https://nose.readthedocs.io) and
> [*nose2*](https://nose2.readthedocs.io) testing frameworks. In the
> examples shown here, they (and their command line tools `nosetests` and
> `nose2`) can be used mostly interchangeably with *pytest*, but *pytest* makes
> it somewhat easier to set up more complex tests as well and provides in general
> a more helpful display of failed assertions.
> Finally, unit testing can also be done based exclusively on Python's standard library
> (most other testing frameworks are built on top of that approach). For this, the
> library includes the *unittest* module, but this module requires more
["boilerplate" code](https://en.wikipedia.org/wiki/Boilerplate_code)
> to create unit tests (simple functions named `test_...` are not enough).

In the above case, the pytest package 'sniffed-out' the tests in the
directory and ran them together to produce a report of the sum of the files and
functions matching having the name `test_*`.

The major boon a testing framework provides is exactly that, a utility to find and run the
tests automatically. With `pytest`, this is the command-line tool called
`py.test`.  When `py.test` is run, it will search all the directories whose names start or
end with the word `test`, find all of the Python modules in these directories
whose names start or end with `test`, import them, and run all of the functions and classes
whose names start with `test`.
This automatic registration of test code saves tons of human time and allows us to
focus on what is important: writing more tests.

When you run `py.test`, it will print first some general information about the
setup and then the name of every test file togehter with a dot (`.`) for every test
that passes, and an `F` for every test that fails. After the dots, `py.test`
will print summary information.

> ## More information / less information {.callout}
> To see more information, such as the name of every test function, use the `-v` (for "verbose") command line argument. To see less, use `-q` (for "quiet").

In the above case, our failing test case is actually a result of a test that is
too strict. While we have thought of using `assert_allclose` instead of a `==`
comparison, it tells us that the result is not
`equal to tolerance rtol=1e-07, atol=0`. Apparently, the default *absolute*
tolerance is 0 and only a relative tolerance is used. Normally, this should be
fine, but it is obviously very strict when comparing to zero. Adding `atol=1e-15` to our assertion
should fix the test:

~~~ {.python}
...
    assert_allclose(whitened.mean(), 0, atol=1e-15)
...
~~~
~~~ {.bash}
$ py.test
~~~
~~~ {.output}
================================= test session starts ==================================
platform linux -- Python 3.5.1, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: [...], inifile:
collected 2 items

test_whiten.py ..

=============================== 2 passed in 0.10 seconds ===============================
~~~

> ## Add more tests {.challenge}
>
> Add more tests to `test_whiten.py` and take care of the edge cases.

As we write more code, we would write more tests, and `py.test` would produce
more dots.  Each passing test is a small, satisfying reward for having written
quality scientific software.
