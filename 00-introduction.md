---
layout: page
title: Testing/Debugging/Profiling
subtitle: Introduction
minutes: 5
---
> ## Learning Objectives {.objectives}
> * Know the meaning of testing, debugging, profiling
> * Understand their place in the scientific workflow

This lesson serves as a brief introduction to the following topics (each well
worthy of a lesson of their own):

* **testing**: the process of making sure that a program does what it is suppposed
  to do. Achieved by 1) writing code (a *test*) that runs a part of the main
  code and compares the result to the expected result and 2) automatizing the
  process of running those tests.
* **debugging**: the process of finding the source of errors in the code, in
  particular with the help of a *symbolic debugger*.
* **profiling**: the first step of optimizing the execution speed of a program
  by measuring its runtime. These measures can be taken on various levels, e.g.:
  the complete runtime of the full code or a part of it; the runtime for each
  function in the code; the runtime of each line of code in a function.

A simplified process of code development, involving all the three elements can
look like the following:

1. Write code that solves a specific problem
2. Write *tests* for that code, showing that it actually solves the problem
   (taking special care of corner and edge cases)
3. When tests fail, *debug* the code to find the root cause.
4. If the code runs too slowly for the purpose at hand, *profile* it to find out
   where the time is spent and optimize the code (using the test suite to
   verify that everything is still working correctly)

Some developers recommend to switch step 1 and 2 around, i.e. to actually write
the tests *before* the code (therefore starting with a test suite full of
failing tests). This is called
[test-driven development](https://en.wikipedia.org/wiki/Test-driven_development)
and adopting it at least partially is certainly a good idea: whenever a bug
occurs, writing first a test that reliably fails can dramatically help in the
later stages of debugging it.
