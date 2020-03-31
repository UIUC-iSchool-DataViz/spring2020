---
title: Lecture 10
layout: lecture
visible_lec: true
visible_n: true
---
<!-- .slide: class="titleslide" -->

# Data Visualization

<div style="height: 6.0em;"></div>

## Jill P. Naiman
## Spring 2020
## Lecture 10

---

## Warm-Up Activity

1. What is the visualization trying to show?
1. What are its methods?
1. What are the strengths / weaknesses?

<br/>

https://coronavirus.jhu.edu/map.html

(Don't click if you are coronavirus-news saturated!)

---

## Bureaucracy

 * Final parts posted
 * We will be dropping a HW grade

---

## Last Week

<img src="../week09/images/this_week.png">

---

## This Week

<img src="images/this_week.png">

---

## Today

 1. Choosing your viz
 1. Intro to Vega/Vega-lite
 1. Iodide

---

<br />
<br />
<br />

# TOPIC 1: Choosing your viz

notes:
we've gone through a bunch of different sorts of viz, so its worth taking a moment to think about which kind to use in each instance

---

## Composition

Don't use a pie chart.

<!-- .slide: data-background-image="images/piechart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
pie charts force you to analyze things by area or angle, which are multidimensional attributes that are easy to confuse.

which is the most popular zoo animal in this pie chart? Elephants, otters, or lions?

---

## Composition

Don't use a pie chart.

<!-- .slide: data-background-image="images/piechartlabels.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
we can make a marginal improvement by labeling the values.

But we wouldn't be doing visualization if we were interested in just reading text.

---

## Composition

Don't use a pie chart.

<!-- .slide: data-background-image="images/3dpiechart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
And if 2-dimensional area is difficult to understand, then 3-dimensional volume is even worse. 

3 dimensional values violate the principle of proportional ink, which states that:

 The sizes of shaded areas in a visualization need to be proportional to the data values they represent. 

---

## Alternatives

<!-- .slide: data-background-image="images/donutchart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
Some people will try to sell you on a modified version of a pie chart called a donut chart that has a hole in the middle. This is a slight improvement because it helps you see the values in the circle as 1-dimensional arc length instead of area. 

But circles are still hard to decipher.

---

## Alternatives

<!-- .slide: data-background-image="images/treemap.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
We can reduce some of the confusion associated with using circles by creating proportional *rectangular* area. Now we can compare along the dimensions of height and width for certain values.

But area is still problematic because it asks us to compare two dimensions - width and height - simultaneously.

---

## Alternatives

<!-- .slide: data-background-image="images/barchart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
you can show comparitive values more effectively with a bar chart though. These values are easily compared along just one dimension.

---

## Alternatives

<!-- .slide: data-background-image="images/waterfallchart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
there are really quite a few alternatives. There are many ways to show data stacking up progressively. This waterfall chart shows how each value is part of a whole, which was sort of the idea of the pie chart.

---

## Comparison

<!-- .slide: data-background-image="images/columnchart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
to compare values from multiple sources, you could use collected columns

---

## Comparison

<!-- .slide: data-background-image="images/stackedcolumnchart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
Or to show they're part of a whole, use a stacked column chart

---

## Comparison

<!-- .slide: data-background-image="images/stackedareachart.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
or to show a time-series, use connected lines that stack on top of each other to show area across the whole canvass. This shows you trends and specific vertical values.

---

## Comparison

JUST NOT THIS!

<img src="images/comparepiecharts.png" width="900"/>

notes:
Just do not compare pie charts!

Zomygod what is even happening right now.

---

## Hierarchical data

<!-- .slide: data-background-image="images/hierarchical_zoos.png" data-background-size="auto 65%" data-background-position="right 50% bottom 50%" -->

notes:
Sometimes we want to show data in a proportion and show connections.
This often happens for hierarcical data.

Here in this example we want to show proportions of land based mammals that
are popular at the zoo and then as we move out we subdivide by the individual
animal species.

---


## Hierarchical data: example packages

 * Sunbursts (e.g., [snakeviz](https://jiffyclub.github.io/snakeviz/) )
 * Nested box area (e.g., [callgrind](https://kcachegrind.github.io/html/Home.html) ) - for
 showing flowchart like structures for things like code programs

<table>
<tr>
<td>
<img src="images/sunburst.png" width="450"/></td><td><img src="images/callgrind.gif" width="450"/></td>
</tr>
</table>

notes:
For heirarchical data, you can nest some of these other formats.

---

<br>
<br>
<br>

# TOPIC 2: Intro to Vega/Vega-lite

---

## Engines

Thus far we have used `bqplot` as our primary imperative method, but we'll start looking at `vega-lite` this week

 * `bqplot` - both imperative & declaritive methods
 * `vega-lite` - declaritive

---

## vega-lite

vega-lite is a high-level method for describing visualizations independently of
their data.

We will be exploring this using [Iodide](https://alpha.iodide.io/).

You can also use `vega-lite` directly with the online editor at:

https://vega.github.io/editor/

---

## vega-lite in context - Web Viz

 * Tools and frameworks covered
    * ipywidgets
    * bqplot
 * Intro to Web Viz
    * (Sort of) How the web works
    * (Very, very) Basic javascript
    * vega-lite

notes:
First we'll review a bit about what we've already done using bqplot

Then we'll have a *very* hand-wavy intro to how javascript/web dev works

---

## Status Update: What's Left

Today, we are introducing the *second to last* major tool we will use: [vega-lite](https://vega.github.io/vega-lite/).

After this: [Idyll](https://idyll-lang.org/) and some [React](https://reactjs.org/)/[D3](https://d3js.org/) Javascript dev within

---

## bqplot review

Declarative:

 * Construct `Figure` objects from `Mark` objects.
 * Relate points to each other with `Scale` objects, display them using `Mark` objects that are keyed to a set of `Scale` objects, and
 * Apply interaction using `ipywidgets` and `traitlets`.

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

Here is a reminder about that sort of basic setup:

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

`bqplot` provides several scales we can utilize:

 * `LogScale`
 * `LinearScale`
 * `DateScale`
 * `OrdinalScale`
 * `ColorScale`
 * A few more as well.

([documentation](https://bqplot.readthedocs.io/en/latest/_generate/bqplot.scales.Scale.html))

---

## Marks

bqplot has several different marks we can explore.  We have utilized a few:

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

We have used several of these different interaction methods:

 * `FastIntervalSelector`
 * `IndexSelector`
 * `BrushIntervalSelector` & `BrushSelector`
 * `MultiSelector` 
 * `LassoSelector`
 * `HandDraw`
 * `PanZoom`
 * `Tooltip`

---

## The Web: A *very* hand-wavy overview

 * Content is transmitted from point-to-point (PPP)
 * Content can be manipulated locally or remotely
 * Not all servers can manipulate data before sending

notes:
this will be an EXTREMELY hand wavy overview

PPP just is a fancy way of saying a communcations protocol that supports transmision between two routers w/ or w/o any host - https://en.wikipedia.org/wiki/Point-to-Point_Protocol

---

## Your Browser

 * Your browser contains -- essentially -- an entire operating system.  It can
   manage:
    * Display mechanisms
    * Interaction with you, the user
    * Input/output from files and file-like objects
    * Interpreter to execute code
 * Most of its activities are mediated via a [document object model (DOM)](https://www.w3schools.com/js/js_htmldom.asp) and
   the programming language Javascript

---

## Things to Note

 * Javascript is "garbage collected"
 * Javascript is [single-threaded](https://dev.to/steelvoltage/if-javascript-is-single-threaded-how-is-it-asynchronous-56gd)
 * Asynchronous programming can be a real noodle-bender (good news is we already handled this with `bqplot` callbacks!)

notes:
here "garbage collected" just means JS handles memory management - we don't have to explicitly allocate and deallocate regions in memory for variables

the "garbage collector" is basically the part of JS that goes and figures out what memory to release

"single-threaded" means that code executes in order, except ...

"asynchronous" means that *some* code gets handed off some code to the browser to be excecuted "in the background" - when the browser is finished, the tasks are "returned" -- we essentially already did thsi with some of our "on_change" and "on_click" stuff with bqplot!

---

## Document Object Model

The Document Object Model (DOM) is how we interact with the collection of HTML
objects in our document.

For instance, a page can be composed of `<div>` objects, `<p>` objects, etc,
and we can construct and interact with these.  This includes things like
modifying style sheets.

![](https://www.w3schools.com/js/pic_htmltree.gif)

(See, for example, the
[jsfiddle](https://jsfiddle.net/) for [jQuery
boilerplate](https://jsfiddle.net/boilerplate/jquery) ).

notes:

for example, we can specify the layout of a document in HTML with different components like the header, title, and body

the body will have different elements like `<div>` and `<a>`, etc.

---

## Document Object Model

The Document Object Model (DOM) is how we interact with the collection of HTML
objects in our document.

For instance, a page can be composed of `<div>` objects, `<p>` objects, etc,
and we can construct and interact with these.  This includes things like
modifying style sheets.

![](https://www.w3schools.com/js/pic_htmltree.gif)

One alternative is to have rendering tied to data and data
values, and to have those automatically update as needed -- `vega-lite`.

---

## Synchronous programming

In Python, we would fetch a website and wait for that to finish before we move
on.

```
import requests

r = requests.get("https://google.com/")
print(r.text)
print("Request completed!")
```

---

## Asynchronous programming

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

## Async and Event-Driven

Async is how we can think about event driven programming, as well.  We have
done this using `traitlets` and `ipywidgets` using callbacks in Python, and we will do it here
as well.

```
var button = $("button");

button.on("click", function() {
    console.log("I've been clicked!");
});
```

---

## Basic Javascript

We will go over a few things, and then move on to vega-lite.

You can declare variables in Javascript implicitly or explicitly, depending on how you want them scoped.

```
var myArray = [1, 2, 3, 4];
var myString = "Hello there!";
var myConcatString = "Hi " + "there " + 5;
var myObject = {'a': 1, 'b': 2, 'c': [1, 2, 3, 4]};
```

---

## Updating variables

If you have an array of objects, there are three very handy functions you can
utilize: `slice`, `forEach` and `filter`.  If you have an object, you can
update it either by accessing a property with a period (`obj.something`) or by
accessing it like you would a dictionary in python (`obj['something']`).

We will use this more next week, but here is the overview...

---

## Next week

### Arrays: `filter`

```
var myArray = [1, 5, 1, 3, 50, 14, 2];
myArrayFiltered = myArray.filter(val => val > 2);
```

Note that here I'm using `=>` as shorthand for declaring a function.

notes:
we will use the filtering especially for data and plots next week!

---

## Next week

### Arrays: `forEach`

To execute something on every value in an array, you can call `forEach` with a
function.

```
var myArray = [1, 2, 3, 4, 5];
myArray.forEach(val => console.log(val * 2));
```

---

## Next week

### Arrays: `slice`

You can set a start and a stop on an array with a `slice` call:

```
var myArray = ["Hello", "I", "am", "here", "now"];
myArray.slice(3).forEach(word => console.log(word));
```

---

## vega-lite editor

https://vega.github.io/editor/

notes:
we'll start by making a quick plot in the vega-lite editor

---

## vega-lite syntax: basics

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

Data available [list is here](https://github.com/vega/vega-datasets/tree/master/data).

notes:
here, we just specify what version of vega-lite we are using

then specify where the data is (this is stored on the vega-lite github of this schema)

then say we are making a "mark" of a "barplot"

then say what we are 

---

## vega-lite syntax

There are several mechanisms by which we describe data representations in
`vega-lite`, but the overarching principle is that it is *declarative*.  We define
what it does based on what we say we want it to look like.

The place where this is no longer true is when we modify `datum` values.

---

## vega-lite syntax

The syntax you will need to be the most familiar with:

 * `mark`: how to visually represent something
 * [`encoding`](https://vega.github.io/vega-lite/docs/encoding.html): the translation between data and the mark
 * `aggregate`: operating over a collection of points -- `mean`, `sum`, `median`,
   `min`, `max`, `count` (next week)
 * `filtering`: for plotting subsets of data (next week)
 * `type`: `quantitative`, `temporal`, `ordinal`, or `nominal`

---

<br>
<br>
<br>

# TOPIC 3: Iodide

---

## Iodide

<img src="https://user-images.githubusercontent.com/95735/54166135-08936e00-4421-11e9-9817-aca915831f42.png" width="800px">

To the internet!

notes:
make sure you go over all these things!