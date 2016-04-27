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

Know what to optimize, spend the time where it is worth it:

![Optimizing two tasks ([By Gorivero, Wikimedia, Public Domain](https://commons.wikimedia.org/w/index.php?curid=3366573))](img/Optimizing-different-parts.svg)

General approach:

1. Make sure that things are *correct* (fast but wrong does not help you)!
2. Write tests so that you can be confident that your code is still correct
  after optimzing it.
3. Measure the total run time, decide whether you need to optimize the code in
  the first place (see graphic below).
4. Profile the code to decide where an optimization could be the most useful.
5. Optimize it and go back

![Is it worth the time? [XKCD comic](http://xkcd.com/1205/), licensed [CC BY-NC 2.5](http://creativecommons.org/licenses/by-nc/2.5/)](img/is_it_worth_the_time.png)
