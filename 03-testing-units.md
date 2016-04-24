---
layout: page
title: Testing
subtitle: Unit Tests
minutes: 10
---
> ## Learning Objectives {.objectives}
>
> -   Understand that functions are the atomistic unit of software.
> -   Understand that simpler units are easier to test than complex ones.
> -   Understand how to write a single unit test.
> -   Understand how to run a single unit test.

In the previous section, we have included assertions directly in the code of
the function. We have even (as part of the exercise) included code that checks
some properties of the result. However, if this were our only approach to
testing, we'd have two problems:

1. We are still not sure the result is actually correct! We cannot test the
correctness of the solution in the function itself, because for that we'd need
a solution for all possible inputs -- if we already had this, we'd not need the
function in the first place...
2. We do not know whether the code works before we actually run it. The
assertions might guard us against incorrect results (which is already great) but
it would be better to have some more confidence in our code before we, say,
run it overnight to analyse our data.

This is where unit tests come in.
Unit tests are so called because they exercise the functionality of the code by
interrogating individual functions and methods. Fuctions and methods can often
be considered the atomic units of software because they are indivisble.
However, what is considered to be the smallest code _unit_ is subjective. The
body of a function can be long or short, and shorter functions are arguably
more unit-like than long ones.

Thus what reasonably constitutes a code unit typically varies from project to
project and language to language.  A good guideline is that if the code cannot
be made any simpler logically (you cannot split apart the addition operator) or
practically (a function is self-contained and well defined), then it is a unit.

> ## Functions are Like Paragraphs {.callout}
>
> Recall that humans can only hold a few ideas in our heads at once. Paragraphs
> in books, for example, become unwieldy after a few lines. Functions, generaly,
> shouldn't be longer than paragraphs.
> Robert C. Martin, the author of "Clean Code" said : "The first rule of
> functions is that _they should be small_. The second rule of functions is that
> _they should be smaller than that_."

The desire to unit test code often has the effect of encouraging both the
code and the tests to be as small, well-defined, and modular as possible.  
In Python, unit tests typically take the form of test functions that call and make
assertions about methods and functions in the code base.  To run these test
functions, a test framework is often required to collect them together. For
now, we'll write some tests for the rescale function and simply run them
individually to see whether they fail. In the next session, we'll use a test
framework to collect and run them.

## Unit Tests Are Just Functions

Unit tests are typically made of three pieces, sometimes called "given, when,
then": *Given* some data, *when* an action is performed *then* the result should
be as expected. The first step therefore consists of setting the stage (which
can be as simple as creating a numpy array with some data, but could also mean
creating a test file). The second steps usually calls the function that is
tested on the prepared data and the third step consists of checking our
expectations about the results using assertions. Let's use this to test our
rescale function:

~~~ {.python}
def test_rescale():
    data = numpy.array([1.0, 2.0, 3.0])
    rescaled = rescale(data)
    expected = numpy.array([0.0, 0.5, 1.0])
    assert_allclose(rescaled, expected)
~~~

The test above:
- sets up the input parameters (the array [1.0, 2.0, 3.0]).
- collects the observed result
- declares the expected result (calculated with our human brain).
- and compares the two with an assertion.

A unit test suite is made up of many tests just like this one. A single
implemented function may be tested in numerous ways.

When writing such unit tests, special care should be taken to test *edge cases*,
i.e. what happens at the boundaries of the input space. A function may assume
a positive value for one of its argument, but what happens if it is 0? Or
negative? Another typical edge case is an empty list or array as an argument.
Often you will think about those cases only when writing the tests which then
forces you to make a decision about how to handle the edge case (which you
should then of course include in your function documentation). For example,
what should `rescale` do for an empty array, should it raise an error or should
it maybe rather return another empty array?


> ## Write a File Full of Tests {.challenge}
>
> 1. In a file called `test_rescale.py`, write several tests like the
> `test_rescale` function from above (name every test function `test_…`). Try
> to test what you think is the most important
>
> 2. Import `test_rescale` and run its tests.
>

Well, running all those tests manually was tediuous…
