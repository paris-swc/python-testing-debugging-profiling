---
layout: page
title: Profiling
subtitle: Detailed runtime measurements
minutes: 15
---

The tools from the previous section can help us decide the question whether we
need to optimize in the first place (is the total run time fast enough?) and it
can guide when we want to replace code by a better-performing alternative (such
as a more specialized numpy function instead of a general built-in function).
They do not tell us *what* to optimize, though.

As a first example, let's us have a look at the classical
[Fibonaci sequence](https://en.wikipedia.org/wiki/Fibonacci_number "Fibonacci number (wikipedia)") ,
where each number is the sum of the two preceding numbers. This can be directly
written down in a recursive function (note that for simplicity we leave away
all error checking, e.g. for negative numbers):

~~~ {.python}
def fibonacci(n):
  if n < 2:
    return n  # fibonacci(0) == 0, fibonacci(1) == 1
  else:
    return fibonacci(n - 2) + fibonacci(n - 1)
~~~

This seems to work fine, but the runtime increases with `n` in a dramatic
fashion:

```python
%time factorial(10)
```

    CPU times: user 0 ns, sys: 0 ns, total: 0 ns
    Wall time: 52.7 µs

    89

```python
%time factorial(20)
```

    CPU times: user 12 ms, sys: 0 ns, total: 12 ms
    Wall time: 9.63 ms

    10946

```python
%time factorial(30)
```

    CPU times: user 696 ms, sys: 0 ns, total: 696 ms
    Wall time: 695 ms

    1346269

```python
%time factorial(35)
```

    CPU times: user 7.49 s, sys: 24 ms, total: 7.52 s
    Wall time: 7.52 s

    14930352

To get an idea what is going on, we can use `%prun`, which runs a command with
Python's built-in profiler:

~~~ {.python}
% prun factorial(35)
~~~
~~~ {.output}
29860706 function calls (4 primitive calls) in 10.621 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
29860703/1   10.621    0.000   10.621   10.621 <ipython-input-6-b471b8bf6ddb>:1(factorial)
        1    0.000    0.000   10.621   10.621 {built-in method builtins.exec}
        1    0.000    0.000   10.621   10.621 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
~~~

The output gives us three pieces of information for every function called during
the execution of the command: the number of times the function was called
(`ncalls`), the total time spend in that function itself (`tottime`) and the
time spend in that function, including all time spend in functions called by
that function (`cumtime`). It is not surprising that all of the time is spend
in the `factorial` function (after all, that's the only function we have) but
the function got called 29860703 times! There is no way we are going to get a
decent performance from this function without changing the approach fundamentally.

> ## A better Fibonacci sequence  {.challenge}
> Do you know of a better way to write the Fibonacci function? Can you imagine
> specific ways of using that function where you would prefer yet another
> approach?

Optimizing a calculation by using a fundamentally different approach is called
"algorithmic optimization" and it is the potentially most powerful way to
increase the performance of a program. Whenever the runtime of a program appears
to be slow, the first check should be whether there is a function that takes a
lot of time and is called more often than expected (e.g. we calculate a measure
on 1000 values and expect a function to be called about a 1000 times as well
but it is called 1000*1000 times instead).

TODO: Show an example with a nested loop

TODO: Demonstrate snakeviz

TODO: Demonstrate line profiler
