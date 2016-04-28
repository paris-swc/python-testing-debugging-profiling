---
layout: page
title: Testing
subtitle: Exceptions
minutes: 10
---

> ## Learning Objectives {.objectives}
>
> * Learn when and how to raise exceptions in your own code
> * Understand "re-raising" an exception

Exceptions are the standard error
messaging system in most modern programming languages.  When an
error is encountered, an informative exception is 'thrown' or 'raised'. When
we program in Python, we encounter such exceptions all the time, but we can
also raise them from our own code. One of the main use cases is argument
checking: when a function receives input that does not make sense, it should
raise an error to inform the user (ideally with a clear error message) instead
of just going on and producing non-sensical results.

For example, consider the following function that rescales a numpy array to a
given range:

~~~ {.python}
def rescale(data, lower=0.0, upper=1.0):
    """
    (Linearly) rescale the data so that it fits into the given range.

    Parameters
    ----------
    data : ndarray
        The data to rescale.
    lower : number, optional
        The lower bound for the data. Defaults to 0.
    upper : number, optional
        The upper bound for the data. Defaults to 1.

    Returns
    -------
    rescaled : ndarray
        The data rescaled between ``lower`` and ``upper``.
    """
    data_min = numpy.min(data)
    data_max = numpy.max(data)
    normalized_data = (data - data_min) / (data_max - data_min)
    rescaled_data = lower + (upper - lower) * normalized_data
    return rescaled_data
~~~

What is this function supposed to do for an array where all elements are
identical? If we don't handle this case, we will not get any error message but
a "not-a-number" result because of the division by zero, together with a
somewhat cryptical warning from numpy:

~~~ {.python}
print(rescale(numpy.array([1, 1, 1])))
~~~
~~~ {.output}
[...]/lib/python3.5/site-packages/ipykernel/__main__.py:21: RuntimeWarning: invalid value encountered in true_divide
[ nan,  nan,  nan]
~~~

Imagine that we use the `rescale` function as part of a complex analysis script --
in the end we might end up with a lot of `nan` values not knowing where
they came from.  

So instead, let's handle that case explicitly and raise a `ValueError` (a
built-in error class for "an argument that has the right type but an
inappropriate value"):

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

Once an exception is raised, it will be passed upward in the program scope:

~~~ {.python}
rescaled = rescale(numpy.array([1, 1, 1]))
~~~
~~~ {.output}
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-21-8f4a617cc5ab> in <module>()
----> 1 rescale(numpy.array([1, 1, 1]))

<ipython-input-20-032c2e2b8094> in rescale(data, lower, upper)
     20     data_max = numpy.max(data)
     21     if not data_max > data_min:
---> 22         raise ValueError('Cannot rescale data: all values are identical.')
     23     normalized_data = (data - data_min) / (data_max - data_min)
     24     rescaled_data = lower + (upper - lower) * normalized_data

ValueError: Cannot rescale data: all values are identical.
~~~

An exception can be used to trigger additional error messages or an alternative
behavior. Rather than immediately halting code
execution, the exception can be 'caught' upstream with a try-except block.
When wrapped in a try-except block, the exception can be intercepted before it reaches
global scope and halts execution.

To add information or replace the message before it is passed upstream, the try-catch
block can be used to catch-and-reraise the exception. We can use this at the
beginning of our function. Note that trying to calculate the minimum of an empty
array will raise a `ValueError`:

~~~ {.python}
empty_array = numpy.array([])
print(numpy.min(empty_array))
~~~
~~~ {.output}
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-26-bfb6cf9e1059> in <module>()
      1 empty_array = numpy.array([])
----> 2 print(numpy.min(empty_array))

[...]/lib/python3.5/site-packages/numpy/core/_methods.py in _amin(a, axis, out, keepdims)
     27
     28 def _amin(a, axis=None, out=None, keepdims=False):
---> 29     return umr_minimum(a, axis, None, out, keepdims)
     30
     31 def _sum(a, axis=None, dtype=None, out=None, keepdims=False):

ValueError: zero-size array to reduction operation minimum which has no identity
~~~

This error message is rather cryptic and someone (ourselves included)
accidentally calling the `rescale` function with an empty array will probably
not directly see the problem:

~~~ {.python}
rescaled = rescale(empty_array)
~~~
~~~ {.output}
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-28-138793fc8d38> in <module>()
----> 1 rescaled = rescale(empty_array)

<ipython-input-20-032c2e2b8094> in rescale(data, lower, upper)
     17         The data rescaled between ``lower`` and ``upper``.
     18     """
---> 19     data_min = numpy.min(data)
     20     data_max = numpy.max(data)
     21     if not data_max > data_min:

[...]]/lib/python3.5/site-packages/numpy/core/_methods.py in _amin(a, axis, out, keepdims)
     27
     28 def _amin(a, axis=None, out=None, keepdims=False):
---> 29     return umr_minimum(a, axis, None, out, keepdims)
     30
     31 def _sum(a, axis=None, dtype=None, out=None, keepdims=False):

ValueError: zero-size array to reduction operation minimum which has no identity
~~~

We can catch this exception and provide a more "friendly" error message:

~~~ {.python}
def rescale(data, lower=0.0, upper=1.0):
    try:
        data_min = numpy.min(data)
    except ValueError:
        raise ValueError('Could not calculate the minimum of the input data -- maybe it is empty?')
    data_max = numpy.max(data)
    if not data_max > data_min:
        raise ValueError('Cannot rescale data: all values are identical.')
    normalized_data = (data - data_min) / (data_max - data_min)
    rescaled_data = lower + (upper - lower) * normalized_data
    return rescaled_data
~~~

Now the problem should be clear and at the same time we don't lose any
information about the original error:

~~~ {.python}
rescaled = rescale(empty_array)
~~~
~~~ {.output}
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-29-addc726e55bb> in rescale(data, lower, upper)
     19     try:
---> 20         data_min = numpy.min(data)
     21     except ValueError:

[...]/lib/python3.5/site-packages/numpy/core/_methods.py in _amin(a, axis, out, keepdims)
     28 def _amin(a, axis=None, out=None, keepdims=False):
---> 29     return umr_minimum(a, axis, None, out, keepdims)
     30

ValueError: zero-size array to reduction operation minimum which has no identity

During handling of the above exception, another exception occurred:

ValueError                                Traceback (most recent call last)
<ipython-input-30-138793fc8d38> in <module>()
----> 1 rescaled = rescale(empty_array)

<ipython-input-29-addc726e55bb> in rescale(data, lower, upper)
     20         data_min = numpy.min(data)
     21     except ValueError:
---> 22         raise ValueError('Could not calculate the minimum of the input data -- maybe it is empty?')
     23     data_max = numpy.max(data)
     24     if not data_max > data_min:

ValueError: Could not calculate the minimum of the input data -- maybe it is empty?
~~~

Alternatively, the exception can simply be handled intelligently. If an
alternative behavior is preferred, the exception can be disregarded and a
responsive behavior can be implemented like so:

~~~ {.python}
def rescale(data, lower=0.0, upper=1.0):
    try:
        data_min = numpy.min(data)
    except ValueError:
        return numpy.array([])
    data_max = data.max()
    if not data_max > data_min:
        raise ValueError('Cannot rescale data: all values are identical.')
    normalized_data = (data - data_min) / (data_max - data_min)
    rescaled_data = lower + (upper - lower) * normalized_data
    return rescaled_data
~~~

If a single function might raise more than one type of exception, each can be
caught and handled separately.

~~~ {.python}
def rescale(data, lower=0.0, upper=1.0):
    try:
        data_min = numpy.min(data)
    except ValueError:
        return numpy.array([])
    except TypeError:
      raise TypeError('Can only re-scale numerical data.')
    data_max = numpy.max(data)
    if not data_max > data_min:
        raise ValueError('Cannot rescale data: all values are identical.')
    normalized_data = (data - data_min) / (data_max - data_min)
    rescaled_data = lower + (upper - lower) * normalized_data
    return rescaled_data
~~~

~~~ {.python}
print('rescaled empty array: ', rescale(empty_array))
print('rescaled non-numerical array:', rescale(numpy.array(['not', 'numbers'])))
~~~
~~~ {.output}
rescaled empty array:  []

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-31-76a2830c5c37> in rescale(data, lower, upper)
     19     try:
---> 20         data_min = numpy.min(data)
     21     except ValueError:

/home/marcel/anaconda/envs/swc_lesson/lib/python3.5/site-packages/numpy/core/fromnumeric.py in amin(a, axis, out, keepdims)
   2358         return _methods._amin(a, axis=axis,
-> 2359                               out=out, keepdims=keepdims)
   2360

/home/marcel/anaconda/envs/swc_lesson/lib/python3.5/site-packages/numpy/core/_methods.py in _amin(a, axis, out, keepdims)
     28 def _amin(a, axis=None, out=None, keepdims=False):
---> 29     return umr_minimum(a, axis, None, out, keepdims)
     30

TypeError: cannot perform reduce with flexible type

During handling of the above exception, another exception occurred:

TypeError                                 Traceback (most recent call last)
<ipython-input-39-6122b616c671> in <module>()
      1 print('rescaled empty array: ', rescale(empty_array))
----> 2 print('rescaled non-numerical array:', rescale(numpy.array(['not', 'numbers'])))

<ipython-input-31-76a2830c5c37> in rescale(data, lower, upper)
     22         return numpy.array([])
     23     except TypeError:
---> 24         raise TypeError('Can only re-scale numerical data.')
     25     data_max = numpy.max(data)
     26     if not data_max > data_min:

TypeError: Can only re-scale numerical data.
~~~

> ## Catch all {.challenge}
> Sometimes it is not obvious what type of exception to catch and an easy
> solution seems to be to catch *any* exception with `except Exception`. Why is
> this not a good idea?

> ## Checking or trying? {.challenge}
> What is the advantage of using `try`/`except` over an explicit type check?
> Compare these two functions that return the minimum and maximum as a tuple:
> ```
> def minmax1(data):
>    try:
>        data_min = numpy.min(data)
>        data_max = numpy.max(data)
>    except TypeError:
>        raise TypeError('Need numerical data.')
>    return (data_min, data_max)
>
> def minmax2(data):
>    if not isinstance(data, numpy.ndarray):
>        raise TypeError('Need numerical data.')
>    data_min = numpy.min(data)
>    data_max = numpy.max(data)
>    return (data_min, data_max)
> ```
> Hint: Could the input `data` be something else than a numpy array and still be
> meaningful?

Exceptions can be very helpful to the user. However, for checking the internal
consistency of an algorithm, a simpler mechanism called *assertions* can be
used.
