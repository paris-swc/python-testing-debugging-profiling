---
layout: page
title: Testing
subtitle: Summary
minutes: 5
---
> ## Learning Objectives {.objectives}
>
> *   Understand the place of testing in a scientific workflow.
> *   Understand that testing has many forms.

In this lesson, we have covered defensive programming and testing with unit
tests. Here is a little summary:

The first step toward getting the right answers from our programs is to assume
that mistakes *will* happen and to guard against them.  This is called
**defensive programming** and the most common way to do it is to add alarms and
tests into our code so that it checks itself.

**Testing** should be a seamless part of scientific software development process.
This is analogous to experiment design in the experimental science world:

- At the beginning of a new project, tests can be used to help guide the
  overall architecture of the project.
- The act of writing tests can help clarify how the software should be perform when you are done.
- In fact, starting to write the tests _before_ you even write the software
  might be advisable. (Such a practice is called _test-driven development_)

*Exceptions and Assertions*: While writing code, `exceptions` and `assertions`
can be added to sound an alarm as runtime problems come up. These kinds of
tests, are embedded in the software iteself and handle, as their name implies,
exceptional cases rather than the norm.

*Unit Tests*: Unit tests investigate the behavior of units of code (such as
functions, classes, or data structures). By validating each software unit
across the valid range of its input and output parameters, tracking down
unexpected behavior that may appear when the units are combined is made vastly
simpler.

Unit tests are not the only kind of test we can write. While unit tests are the
core of every test suite, there are at least two other kinds of tests:

*Regression Tests*: Regression tests defend against new bugs, or regressions,
which might appear due to new software and updates. A typical situation where
you need such tests is if you write simulation software: you can save the
result of a simulation run and then write a test that compares the result of
your simulation against the stored result. If at any time your results start to
differ from the stored results, this is a very important warning sign (note
that it could also mean that the previous result was wrong!).

*Integration Tests*: Integration tests check that various pieces of the
software work together as expected. In contrast to unit tests, they do not
test a single isolated piece of code but rather how those units work together.

The structure of integration tests is very similar to that of unit tests. There is an expected result, which is compared against the observed value. However, what goes in to creating the expected result or setting up the code to run can be considerably more complicated and more involved. Integration tests can also take much longer to run because of how much more work they do. This is a useful classification to keep in mind while writing tests. It helps separate out which test should be easy to write (unit) and which ones may require more careful consideration (integration).
