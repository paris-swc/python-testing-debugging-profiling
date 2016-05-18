---
layout: page
title: Debugging
subtitle: Post-mortem debugging
minutes: 10
---
> ## Learning Objectives {.objectives}
>
> -   Understand what is meant by "post-mortem debugging"
> -   Understand how to call Python's debugger after an exception was raised

One of the main reasons to start debugging is that the program exited with an
error message. Ideally, all the necessary information to find the cause of the
problem is in the error message but often this is not the case. In that
situation, it might be of interest to have access to the program state at the
point *where the exception was raised*. A common technique to investigate this
kind of problem is to edit the code, put `print` statements at the point
where the error was raised and then run the code again. This approach however
has several drawbacks:

* The code in question might be some library code that you cannot easily edit
  (e.g. you need administrator privileges to edit code in a system-wide
  installation of a library).
* You have to know in advance which variables are of interest to you which
  means that potentially you'll have to repeat the process several times.
* You'll have to clean up afterwards and make sure not to forget any `print`
  statements in the code.
* Depending on the program you are debugging, running everything again might
  take a long time.

There is an alternative approach using Python's built-in symbolic debugger. When
an exception is raised, its full context is stored and can be investigated. This
kind of debugging is called "post-mortem" (i.e. "after death"), because you only
use the debugger after the program has crashed as opposed to running it under
the control of the debugger from the start (as we'll do later). Let's have a
look at some erroneous code:

~~~ {.python}
import numpy
def find_first(data, element):
    """
    Return the index of the first appearance of ``element`` in
    ``data`` (or -1 if ``data`` does not contain ``element``).
    """
    counter = 0
    while counter <= len(data):
        if data[counter] == element:
            return counter
        counter += 1
    return -1

def check_data(target):
    test_data = [3, 2, 8, 9, 3, numpy.nan, 4, 7, 5]
    # We look for a zero in the data
    index = find_first(test_data, target)
    if index != -1:
        print('Data until first occurrence of', target, ':', test_data[:index])
    else:
        print('No occurrence of', target, 'in the data')
~~~

The `find_first` function finds the first occurrence of an element in a list (or
an array) of elements and returns its index. The `check_data` function uses this
function to find a certain value in the data and prints the data until that
point. It uses some fake "data" and takes an `target` argument to specify what
value to look for.

If we run the `check_data` function, all looks fine:

~~~ {.python}
check_data(5)
~~~
~~~ {.output}
Data until first occurrence of 5 : [3, 2, 8, 9, 3, nan, 4, 7]
~~~

Now let's run the function again but use a different target value:

~~~ {.python}
check_data(1)
~~~
~~~ {.output}
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-58-cb57f256f664> in <module>()
----> 1 check_data(1)

<ipython-input-56-610c1db03285> in check_data(target)
     16     test_data = [3, 2, 8, 9, 3, numpy.nan, 4, 7, 5]
     17     # We look for a zero in the data
---> 18     index = find_first(test_data, target)
     19     if index != -1:
     20         print('Data until first occurrence of', target, ':', test_data[:index])

<ipython-input-56-610c1db03285> in find_first(data, element)
      8     counter = 0
      9     while counter <= len(data):
---> 10         if data[counter] == element:
     11             return counter
     12         counter += 1

IndexError: list index out of range
~~~

There seems to be a problem and unfortunately the `IndexError` is not very
precise (note that the error message would have been more helpful if we had
used a numpy array instead of a list for the "data"). Let's investigate what
caused it by using the symbolic debugger (note that the following command only
works in ipython or the jupyter notebook):

~~~ {.python}
% debug
~~~
~~~ {.output}
<ipython-input-56-610c1db03285>(10)find_first()
      8     counter = 0
      9     while counter <= len(data):
---> 10         if data[counter] == element:
     11             return counter
     12         counter += 1

ipdb> 
~~~
We are now in an `ipdb` console (an improved interface to Python's built-in
`pdb` debugger) and can issue `ipdb` commands and investigate the state of
variables and expressions in the context pointed to by the arrow. To
distinguish the two, we can add a `!` to the start of the line when we are
interested in variables/expressions:

~~~ {.output}
ipdb> !counter
8
ipdb> !len(data)
8
~~~

This is not necessary when there is no possible confusion between `ipdb`
commands and Python expression, though:

~~~ {.output}
ipdb> counter
8
~~~

Sometimes, the values we are interested in are not accessible at the exact
point where the exception was raised. For example, we cannot access `test_data`
and `target` used in `check_data` (in the current example, this is of course
not an actual problem, since they are handed over to `find_first` as `data` and
`element`):

~~~ {.output}
ipdb> test_data
*** NameError: name 'test_data' is not defined
~~~

To access the data, we can move "up" in the exception stack and investigate the
variables there:

~~~ {.output}
ipdb> up
> <ipython-input-56-610c1db03285>(18)check_data()
     16     test_data = [3, 2, 8, 9, 3, numpy.nan, 4, 7, 5]
     17     # We look for a zero in the data
---> 18     index = find_first(test_data, target)
     19     if index != -1:
     20         print('Data until first occurrence of', target, ':', test_data[:index])
ipdb> test_data
     [3, 2, 8, 9, 3, nan, 4, 7, 5]
~~~

To get back to where we were before, we use `down` or alternatively `d`
(instead of `up` we can also use `u`):

~~~ {.output}
ipdb> d
> <ipython-input-56-610c1db03285>(10)find_first()
      8     counter = 0
      9     while counter <= len(data):
---> 10         if data[counter] == element:
     11             return counter
     12         counter += 1
~~~

We finished our debugging because we figured out that the problem lies in the
`counter` variable going one step too far -- instead of `counter <= len(data)`
the comparison should read `counter < len(data)`. We can therefore quit the
debugger with `q` (short for `quit`):

~~~ {.output}
ipdb> q
~~~

Now, if this were a real-life situation we would now take the time to add a
test to our test suite, checking for this condition (searching for an element
that is not present in the list). We'd make sure that this test fails and then
go on to fix the test. This way, we'd be sure not to re-introduce the same
error in future versions of our code (e.g. because of a code re-organization)
without noticing. Incidentally, there *is* a way to re-organize the code and
make it less error-prone:

~~~ {.python}
def find_first(data, element):
    """
    Return the index of the first appearance of ``element`` in
    ``data`` (or -1 if ``data`` does not contain ``element``).
    """
    for index, data_element in enumerate(data):
        if data_element == element:
            return index

    return -1
~~~

Using a counter and indexing into a list at every iteration of a loop is something
that might feel natural when you have experience in another programming language
but in Python it is often considered to be a so-called
"[anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern)".

> ## Post-mortem debugging with pytest {.callout}
> You can run your test suite with pytest and make pytest open a debugger
> session for you as soon as an error occurs:
>
> ~~~ {.bash}
> $ py.test --pdb
> ~~~
> ~~~ {.output}
> ============================= test session starts ==============================
> platform linux -- Python 3.5.1, pytest-2.8.5, py-1.4.31, pluggy-0.3.1
> rootdir: [...], inifile:
> collected 2 items
>
> test_whiten.py .F
> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> traceback >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>
>    def test_2d():
>         test_data = numpy.array([[1, 3, 5, 7],
>                                  [2, 3, 4, 1]])
>         whitened = whiten(test_data)
> >       assert_allclose(whitened.mean(), 0)
> E       AssertionError:
> E       Not equal to tolerance rtol=1e-07, atol=0
> E       
> E       (mismatch 100.0%)
> E        x: array(-2.7755575615628914e-17)
> E        y: array(0)
>
> test_whiten.py:17: AssertionError
> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> entering PDB >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
> > [...]/test_whiten.py(17)test_2d()
> -> assert_allclose(whitened.mean(), 0)
> (Pdb)
> ~~~

> ## Error debugging {.challenge}
> Copy & paste the following code and run `test_code_array`. It will fail with
> an error, use the debugger to find out why.
>
> ~~~ {.python}
> import numpy
> from numpy.testing.utils import assert_equal
>
> def code_array(codes):
>     '''Store airport codes in an array in numerical form'''
>     to_numerical_code = numpy.vectorize(lambda code: numpy.array([ord(c) for c in code]))
>     return numpy.vstack([to_numerical_code(c) for c in codes])
>
> def test_code_array():
>     airport_codes = ['TXL', 'LAX', 'PHX', 'CDG' 'ORY', 'JFK', 'JNB', 'WAW']
>     expected = numpy.array([[84, 88, 76],
>                             [76, 65, 88],
>                             [80, 72, 88],
>                             [67, 68, 71],
>                             [79, 82, 89],
>                             [74, 70, 75],
>                             [74, 78, 66],
>                             [87, 65, 87]])
>     assert_equal(code_array(airport_codes), expected)
> ~~~

Not every error in the code leads to an exception -- the ones that are most difficult to
debug usually don't! We will therefore next look at using the debugger right from the
start of a program.
