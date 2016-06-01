---
layout: page
title: Testing
subtitle: Assertions
minutes: 15
---
> ## Learning Objectives {.objectives}
>
> *   Assertions are one line tests embedded in code.
> *   Assertions can halt execution if something unexpected happens.
> *   Assertions are the building blocks of tests.

Assertions are the simplest type of test. They are used as a tool for bounding
acceptable behavior during runtime. The assert keyword in python has the
following behavior:

~~~ {.python}
x = 3
assert x != 3
~~~
~~~ {.output}
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-49-f14d9f94696e> in <module>()
      1 x = 3
----> 2 assert x != 3

AssertionError:
~~~
~~~ {.python}
assert x == 3
~~~
~~~ {.output}

~~~

That is, assertions halt code execution instantly if the comparison is false.
It does nothing at all if the comparison is true. These are therefore a very
good tool for checking our whether everything is going according to our expectations. Let's reuse our `rescale` function from before:

~~~ {.python}
def rescale(data, lower=0.0, upper=1.0):
    data_min = numpy.min(data)
    data_max = numpy.max(data)
    if not data_max > data_min:
      raise ValueError('Cannot rescale data: all values are identical.')
    normalized_data = (data - data_min) / (data_max - data_min)
    rescaled_data = lower + (upper - lower) * normalized_data
    return rescaled_data
~~~

The advantage of assertions is their ease of use and their "compactness" -- they are rarely more than one
line of code. They are therefore especially useful in situations where you think that the specific error condition will never be fulfilled and it therefore seems to be wasteful to check it and raise an exception. Imagine for example that the `rescale` function is only ever called from within one of your algorithms, and it is guaranteed that it will not be called with an array of identical values. In that case, you might not want to bother with the error message we put in previously. Adding an assertion is "cheaper" but will still guard you from problems in the future (e.g. when you decide to reuse your function in a different context):

~~~ {.python}
def rescale(data, lower=0.0, upper=1.0):
    data_min = numpy.min(data)
    data_max = numpy.max(data)
    assert data_max > data_min
    normalized_data = (data - data_min) / (data_max - data_min)
    rescaled_data = lower + (upper - lower) * normalized_data
    return rescaled_data
~~~

The general approach to check your expectations (be it with exceptions or with assertions) is called "defensive coding" and is a good habit to get into. Especially in complex algorithms assertions can also serve as documentation in the code and will greatly help with debugging by making your expections clear:

~~~ {.python}
def rescale(data, lower=0.0, upper=1.0):
    data_min = numpy.min(data)
    data_max = numpy.max(data)
    assert data_max > data_min
    normalized_data = (data - data_min) / (data_max - data_min)
    assert numpy.min(normalized_data) == 0.0
    assert numpy.max(normalized_data) == 1.0
    rescaled_data = lower + (upper - lower) * normalized_data
    return rescaled_data
~~~

Let's run our function and make sure that none of the assertions is raised:

~~~ {.python}
ar = numpy.array([0.3, 0.6, 0.9])
print(rescale(ar, lower=0.5, upper=1.5))
~~~
~~~ {.output}
[ 0.5  1.   1.5]
~~~

There is a potential problem with our last two assertions, though: we deal with floating point values and comparing them for equality is rarely a good idea:

~~~ {.python}
0.3 == 3*0.1
~~~
~~~ {.output}
False
~~~

In fact, just re-writing our function in a mathematically (but not numerically!) equivalent way, will make the assertion fail:

~~~ {.python}
def rescale(data, lower=0.0, upper=1.0):
    data_min = numpy.min(data)
    data_max = numpy.max(data)
    assert data_max > data_min
    normalized_data = data / (data_max - data_min) - data_min / (data_max - data_min)
    assert numpy.min(normalized_data) == 0.0
    assert numpy.max(normalized_data) == 1.0
    rescaled_data = lower + (upper - lower) * normalized_data
    return rescaled_data
~~~

This should not have changed anything, but in fact the assertion is now failing:

~~~ {.python}
ar = numpy.array([0.3, 0.6, 0.9])
print(rescale(ar, lower=0.5, upper=1.5))
~~~
~~~ {.output}
AssertionError                            Traceback (most recent call last)
<ipython-input-3-48e53c12007e> in <module>()
      1 ar = numpy.array([0.3, 0.6, 0.9])
----> 2 print(rescale(ar, lower=0.5, upper=1.5))

<ipython-input-2-49242bbbe0b1> in rescale(data, lower, upper)
      5     normalized_data = data / (data_max - data_min) - data_min / (data_max - data_min)
      6     assert numpy.min(normalized_data) == 0.0
----> 7     assert numpy.max(normalized_data) == 1.0
      8     rescaled_data = lower + (upper - lower) * normalized_data
      9     return rescaled_data

AssertionError:
~~~

Since this an issue that one has to deal with all the time in testing numerical code, `numpy` provides a few helpful functions in the `numpy.testing.utils` package that check for equality up to a certain precision:

~~~ {.python}
values = numpy.array([0.3, 3*0.1, 0.1+0.1+0.1, 0.6/2])
print(values == 0.3)
~~~
~~~ {.output}
[ True False False  True]
~~~
~~~ {.python}
from numpy.testing.utils import assert_allclose
assert_allclose(values, 0.3, rtol=1e-12)
print('no assertion raised')
~~~
~~~ {.output}
no assertion raised
~~~

There are more helpful `assert_…` functions in that package, we'll use them later in the lesson.

> ## The final touch {.challenge}
> * Replace the problematic assertions with `assert_allclose`
> * Before returning the result -- what assertion(s) could we use to check the result?

Assertions are a great tool to embed checks into your code quickly and
non-intrusively. However, the checks they perform are necessarily simple (they
are executed during the run of the program, making computationally intensive
checks would therefore slow the program down) and they are therefore only the
first step towards writing code we can trust to give correct results. The next
step is to write explicit *tests*, covered in the following section. 
