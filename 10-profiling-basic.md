---
layout: page
title: Profiling
subtitle: Total runtime measurements
minutes: 10
---

Ipython offers two useful commands to measure the time a single line or cell of
code takes to execute:

* `%time` will time the total runtime in a simple way
(much like the command `time` in a UNIX shell) -- if your command/script takes
a very long time to run, this is what you want to use.
* `%timeit` will repeat the time measurements many times: by default it will do
  3 trials, where each trial will execute the command N times. The number N is
  chosen so that the total test run takes a couple of seconds and the reported
  time will be the one of the best trial. This gives much more precise
  measurements for short-running commands.

~~~ {.python}
In [2]: square_ar = numpy.random.rand(1000, 1000)
In [3]: %time w, v =  numpy.linalg.eig(square_ar)
~~~
~~~ {.output}
CPU times: user 4.54 s, sys: 240 ms, total: 4.78 s
Wall time: 2.44 s
~~~

For small computations that are repeated many times, `timeit` is the better
tool:

~~~ {.python}
In [4]: %timeit square_ar.var()
~~~
~~~ {.output}
The slowest run took 5.01 times longer than the fastest. This could mean that an intermediate result is being cached.
100 loops, best of 3: 6.05 ms per loop
~~~

We get a warning message, most likely because the very first run was much slower
than the other runs due to cache effects (data that was previously used is in
a fast memory and can be reused very efficiently). Nowadays a lot of performance
optimization revolves around the efficient use of memory in general and caches
in particular. Whether we are interested in the results including these effects
or not depends on our question, but if we are only interested in the "pure
computation" time then one strategy is to scale up the problem size:

~~~ {.python}
In [5]: square_ar = numpy.random.rand(3000, 3000)
In [6]: %timeit square_ar.var()
~~~
~~~ {.output}
10 loops, best of 3: 101 ms per loop
~~~

For the timing of a series of statements, `%%timeit` can be used in the first
line of a jupyter notebook cell to time the full cell.

> ## sum vs. sum  {.challenge}
> numpy has a `sum` function, but `sum` is also a standard built-in function
> in Python. Both can be used with all kind of Python sequences, e.g. with
> Python lists or numpy arrays. Use `a = numpy.arange(1000000)` and
> `l = list(range(1000000))` as example data and compare the runtime of `sum`
> vs. `numpy.sum` for the two variables. Which function is faster. Can you guess
> why?
