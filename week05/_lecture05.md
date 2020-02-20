---
title: Lecture 5
layout: lecture
---
<!-- .slide: class="titleslide" -->

# Data Visualization

<div style="height: 6.0em;"></div>

## Matthew Turk
## Fall 2019
## Lecture 5

---

## Warm-Up Activity

1. What is the visualization trying to show?
1. What are its methods?
1. What are the strengths / weaknesses?


 * https://www.vox.com/policy-and-politics/2018/9/28/17914308/kavanaugh-ford-question-dodge-hearing-chart

---

# Interactivity

 * Interactivity -- brief review of terminology
 * Tools and frameworks
    * ipywidgets
    * bqplot
 * Web Viz
    * (Sort of) How the web works
    * (Very, very) Basic javascript
    * vega-lite

---

## Status Update: Concepts

 * Basic Visualizations
   * Plot components
   * Aggregation (binning, histograming)
 * Basic interactivity
   * Traitlets
   * Reactivity / data-binding

---

## Status Update: Tools

 * Python
   * matplotlib -- introduced
   * bqplot -- introduced
 * Javascript
   * vega-lite -- introducing today

---

## Status Update: What's Left

Today, we are introducing the *final* major tool we will use: [vega-lite](https://vega.github.io/vega-lite/).

We will likely explore, in brief one-offs, a handful of additional tools.

---

## Status Update: What's Left

 * Dynamic data (dashboarding)
 * Interactivity
 * Plot types
   * Heat maps / chloropleths
   * Geospatial data
   * Time-series and multi-series
   * etc
 * Advanced utilization of the tools

---

## Interactivity

This week, we'll talk about some basics principles of interactivity in
visualization, and you will get a whirlwind introduction to some interactive
visualization libraries in python.

What do you think of when you think of interactive visualizations?

---

## Interactivity: Parameters

<!-- .slide: data-background-image="images/brushlink_01.svg" data-background-size="80% auto" data-background-position="right 50% bottom 50%" -->

 * Point characteristics
 * Axis limits/bounds
 * Transform/scale

---

## Interactivity: Parameters

<!-- .slide: data-background-image="images/brushlink_01.svg" data-background-size="80% auto" data-background-position="right 50% bottom 50%" -->

 * Click-and-drag
 * Rectangle zoom
 * Adjustment

---

## Interactivity: Linking & Brushing

<!-- .slide: data-background-image="images/brushlink_02.svg" data-background-size="80% auto" data-background-position="right 50% bottom 50%" -->

---

## Interactivity: Linking & Brushing

<!-- .slide: data-background-image="images/brushlink_02.svg" data-background-size="80% auto" data-background-position="right 50% bottom 50%" -->

`filter( variable2 > variable1 )`

---

## Interactivity: Linking & Brushing

<!-- .slide: data-background-image="images/brushlink_03.svg" data-background-size="80% auto" data-background-position="right 50% bottom 50%" -->

`filter( variable2 > variable1 )`

---

## Interactivity: Linking & Brushing

<!-- .slide: data-background-image="images/brushlink_04.svg" data-background-size="80% auto" data-background-position="right 50% bottom 50%" -->

`filter( variable2 > variable1 )`

---

## Interactivity: Linking & Brushing

<!-- .slide: data-background-image="images/brushlink_05.svg" data-background-size="80% auto" data-background-position="right 50% bottom 50%" -->

---

## Interactivity: Linking & Brushing

<!-- .slide: data-background-image="images/brushlink_06.svg" data-background-size="80% auto" data-background-position="right 50% bottom 50%" -->

---

## Interactivity: Linking & Brushing

<!-- .slide: data-background-image="images/brushlink_07.svg" data-background-size="80% auto" data-background-position="right 50% bottom 50%" -->

---

<iframe width="1024" height="576"
src="https://www.youtube.com/embed/B7XoW2qiFUA" frameborder="0"
allow="autoplay; encrypted-media" allowfullscreen></iframe>

---

## Implementing This

Two main approaches to the selection process:

 * Concurrent filtering
 * Index-based selection

What are the pros and cons of each?

What are methods of showing "linked" and "brushed" data if you have:

 * Scatter plot
 * Histogram
 * Field / image plot

---

## bqplot review

Construct `Figure` objects from `Mark` objects.  Relate points to each other with `Scale` objects, display them using `Mark` objects that are keyed to a set of `Scale` objects, and apply interaction using `ipywidgets` and `traitlets`.

I've received feedback about past lectures, and so we will be moving more slowly today.

---

## bqplot objects

 * A mark is some mechanism for displaying data.  For example, we might have
   data that has a set of x and y values, which we can use `Lines` to
   represent.
 * `Scale` objects describe relationships between visual attributes (position)
   and data values.
 * `Axis` objects are where data are placed.
 * `Figure` objects contain marks and axes, as well as interaction.

---

## bqplot: Very Simple

Our first example will be a simple lineplot.

```#python
import bqplot
import numpy as np

x = np.arange(100)
y = np.random.random(100) + 5

x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
lines = bqplot.Lines(x = x, y = y, scales = {'x': x_sc, 'y': y_sc})
ax_x = bqplot.Axis(scale = x_sc, label = 'X value')
ax_y = bqplot.Axis(scale = y_sc, label = 'Y value', orientation = 'vertical')
fig = bqplot.Figure(marks = [lines], axes = [ax_x, ax_y])
display(fig)
```

---

## More bqplot

With bqplot, we construct a set of objects that are related:

 * Scales
 * Axes
 * Marks
 * Figures
 * Interactions

---

## Scales

We have dealt primarily with quantitative scales.  bqplot provides several
scales we can utilize:

 * `LogScale`
 * `LinearScale`
 * `DateScale`
 * `OrdinalScale`
 * `ColorScale`
 * A few more as well.

([documentation](https://bqplot.readthedocs.io/en/latest/_generate/bqplot.scales.Scale.html))

---

## Marks

bqplot has several different marks we can explore.  We will utilize a few more
today:

 * `HeatMap`
 * `GridHeatMap`
 * `Bars`
 * `Graph`

([documentation](https://bqplot.readthedocs.io/en/latest/_generate/bqplot.marks.Mark.html))

---

## bqplot interaction

As noted in the previous class, bqplot widgets are all based on ipywidgets.  This
means we use the same systems for describing the two.

We add an interaction to a given figure via the `interaction` keyword argument
to a figure.

---

## bqplot interactors

We will be able to use these different interaction methods:

 * `FastIntervalSelector`
 * `IndexSelector`
 * `BrushIntervalSelector` & `BrushSelector`
 * `MultiSelector` 
 * `LassoSelector`
 * `HandDraw`
 * `PanZoom`
 * `Tooltip`

---

## Datasets

This week we will use a dataset from
[FiveThirtyEight](https://fivethirtyeight.com/), specifically from their
[datasets repository](https://github.com/fivethirtyeight/data/).

Please take care to abide by their licensing terms (CC-BY 4.0).

Candidate datasets:

 * [librarians](https://github.com/fivethirtyeight/data/tree/master/librarians)
   (2014)
 * [bachelorette](https://github.com/fivethirtyeight/data/tree/master/bachelorette)
 * [comic-characters](https://github.com/fivethirtyeight/data/tree/master/comic-characters)
 * [bob-ross](https://github.com/fivethirtyeight/data/tree/master/bob-ross)

---

## Datasets

I have registered each of these datasets on the Whole Tale website under Week 5.  You may also use them locally.

Reminder:

  * `workspace` is shared, but writeable only by me
  * `data` is read-only
  * `home` is your personal home directory, shared across instances

---

## Group Work

We will split up into groups.

We will choose datasets and practice our filtering, brushing, linking and
visualizations using both bqplot.

---

# The Web

 * Content is transmitted from point-to-point
 * Content can be manipulated locally or remotely
 * Not all servers can manipulate data before sending

---

# Your Browser

 * Your browser contains -- essentially -- an entire operating system.  It can
   manage:
    * Display mechanisms
    * Interaction with you, the user
    * Input/output from files and file-like objects
    * Interpreter to execute code
 * Most of its activities are mediated via a document object model (DOM) and
   the programming language Javascript

---

# Things to Note

 * Javascript is "garbage collected"
 * Javascript is single-threaded
 * Asynchronous programming can be a real noodle-bender

---

# Document Object Model

The Document Object Model (DOM) is how we interact with the collection of HTML
objects in our document.

For instance, a page can be composed of `<div>` objects, `<p>` objects, etc,
and we can construct and interact with these.  This includes things like
modifying style sheets.  See, for example, the
[jsfiddle](https://jsfiddle.net/) for [jQuery
boilerplate](https://jsfiddle.net/boilerplate/jquery).

One alternative, as we will see, is to have rendering tied to data and data
values, and to have those automatically update as needed.

---

# Synchronous programming

In Python, we would fetch a website and wait for that to finish before we move
on.

```
import requests

r = requests.get("https://google.com/")
print(r.text)
print("Request completed!")
```

---

# Asynchronous programming

In Javascript, we would tell the code to fetch, but we would also tell it what
to do *after* it finished.

This uses jQuery, but you can [do it without
that](http://youmightnotneedjquery.com/#json).

```
$.get("https://google.com/", function(data, status){
      alert("Data: " + data + "\nStatus: " + status);
});
console.log("Hey, I've done the thing.");
```

Note that you can't always get this to work. In fact, that example won't even
work!

---

# Async and Event-Driven

Async is how we can think about event driven programming, as well.  We have
done this using `traitlets` and `ipywidgets` in Python, and we will do it here
as well.

```
var button = $("button");

button.on("click", function() {
    console.log("I've been clicked!");
});
```

---

# Basic Javascript

We will go over a few things, and then move on to vega-lite.

You can declare variables in Javascript implicitly or explicitly, depending on how you want them scoped.

```
var myArray = [1, 2, 3, 4];
var myString = "Hello there!";
var myConcatString = "Hi " + "there " + 5;
var myObject = {'a': 1, 'b': 2, 'c': [1, 2, 3, 4]};
```

---

# Updating variables

If you have an array of objects, there are three very handy functions you can
utilize: `slice`, `forEach` and `filter`.  If you have an object, you can
update it either by accessing a property with a period (`obj.something`) or by
accessing it like you would a dictionary in python (`obj['something']`).

---

# Arrays: `filter`

```
var myArray = [1, 5, 1, 3, 50, 14, 2];
myArrayFiltered = myArray.filter(val => val > 2);
```

Note that here I'm using `=>` as shorthand for declaring a function.

---

# Arrays: `forEach`

To execute something on every value in an array, you can call `forEach` with a
function.

```
var myArray = [1, 2, 3, 4, 5];
myArray.forEach(val => console.log(val * 2));
```

---

# Arrays: `slice`

You can set a start and a stop on an array with a `slice` call:

```
var myArray = ["Hello", "I", "am", "here", "now"];
myArray.slice(3).forEach(word => console.log(word));
```

---

# vega-lite editor

https://vega.github.io/editor/#/custom/vega-lite

---

# vega-lite syntax: basics

From the vega-lite examples, you can make a bar chart that is an aggregate like so:

```
{
  "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
  "data": {"url": "data/movies.json"},
  "mark": "bar",
  "encoding": {
    "x": {
      "bin": true,
      "field": "IMDB_Rating",
      "type": "quantitative"
    },
    "y": {
      "aggregate": "count",
      "type": "quantitative"
    }
  }
}
```

---

# vega-lite syntax

There are several mechanisms by which we describe data representations in
vega-lite, but the overarching principle is that it is declarative.  We define
what it does based on what we say we want it to look like.

The place where this is no longer true is when we modify `datum` values.

---

# vega-lite syntax

The syntax you will need to be the most familiar with:

 * `mark`: how to visually represent something
 * [`encoding`](https://vega.github.io/vega-lite/docs/encoding.html): the translation between data and the mark
 * `aggregate`: operating over a collection of points -- `mean`, `sum`, `median`,
   `min`, `max`, `count`
 * `type`: `quantitative`, `temporal`, `ordinal`, or `nominal`

---

# For Next Week

 * Install and get working a Jupyter environment on your local machine.  It must have:
   * bqplot
   * matplotlib
   * pandas
 * Set up a development environment using VSCode
