---
layout: page
title: Debugging
subtitle: Introduction
minutes: 5
---
> ## Quote by Brian Kernighan
> "Everyone knows that debugging is twice as hard as writing a program in the
> first place. So if you’re as clever as you can be when you write it, how will
> you ever debug it?”

Everyone writing programs will be debugging them at some point, i.e. trying to
find out why an error or an otherwise unexpected results occurs.

Some general remarks and strategies for debugging can be found in the [section on
debugging in the "Programming with Python" software carpentry lesson](http://swcarpentry.github.io/python-novice-inflammation/09-debugging.html).
To quickly summarize some of the principles:

* **Narrow things down**: try to reproduce the bug with simplified data,
  simplified processing, be sure you know what the correct result would be in
  that situation. Have a set of explicit steps that reproduce the bug *every
  time* (if possible).
* **Change things systematically**: change one thing at a time and test it
  before moving on
* **Keep track of what you've done**: version control is a great tool to
  explore possible fixes and not to worry about making things worse -- if
  it did not work out, simply go back to the stored state.


The tools presented in this part of the lesson can be helpful in narrowing
down where and under what circumstances bugs occur and can therefore save you
time in finding the source for a bug. Still, they are just *tools*, following
the principles laid out in the lesson referenced above is much more important
than an in-depth knowledge of these tools.
