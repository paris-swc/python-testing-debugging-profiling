---
layout: page
title: Profiling
subtitle: Introduction
minutes: 5
---
> ## Quote by Donald Knuth {.callout}
> "We should forget about small efficiencies, say about 97% of the time:
> **premature optimization is the root of all evil**. Yet we should not pass
> up our opportunities in that critical 3%"

That a program works and gives the correct results is of course essential.
However, this alone might not be enough if running the program takes a very
long time. This is where you start about thinking how to make your program
faster and the first part of this process is called *profiling*, finding out
where the program spends its time and where the optimization effort should
therefore be spend. When confronted with a slowly running program most
programmers have an intuition about how to optimize the program and are
tempted to start working on it immediately, skipping the profiling process
completely. Unfortunately, these intuitions turn out to be wrong more often
than not: either in a fundamental way, i.e. the optimized code is actually
*slower* than before, or (and this is very common) the part of the code that
was optimized is not the "bottleneck" for the processing speed, and a lot of
development time was spent on achieving a small performance increase. Even
worth, optimization comes often with a cost (in addition to the development
time spent on it): the optimized code might be less readable, less general and
less robust against errors.

Here's a simple example showing the importance of profiling before Optimizing
(from the Wikipedia article on
[Amdahl's law](https://en.wikipedia.org/wiki/Amdahl's_law)): Assume a task has
two parts *A* and *B*. Without profiling, you might start to optimize task *B*
and after working on it for a long time, you succeed in making it run in only
1/5 of the original time. However, it turns out that *B* was only taking up a
small part of the original run time and therefore focussing on *A* would have
been the better approach. In this example, reducing the run time of *A* to 50%
of its original run time (presumably easier than optimizing *B* to 20%) would
have had a bigger impact on the total run time.

![Optimizing two tasks ([By Gorivero, Wikimedia, Public Domain](https://commons.wikimedia.org/w/index.php?curid=3366573))](img/Optimizing-different-parts.svg)

The general approach for profiling should therefore resemble the following:

1. Make sure that things are *correct* ("fast but wrong" does not help you)!
2. Write tests so that you can be confident that your code is still correct
  after optimzing it.
3. Measure the total run time, decide whether you need to optimize the code in
  the first place.
4. Profile the code to decide where an optimization could be the most useful.
5. Optimize it and go back

Never forget that for code that is only run once or few times, optimization
might not be a good use of your time:

![Is it worth the time? [XKCD comic by Randall Munroe](http://xkcd.com/1205/), licensed [CC BY-NC 2.5](http://creativecommons.org/licenses/by-nc/2.5/)](img/is_it_worth_the_time.png)
