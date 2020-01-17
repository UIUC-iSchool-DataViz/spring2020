---
title: Lecture 6
layout: lecture
---
<!-- .slide: class="titleslide" -->

# Data Visualization

<div style="height: 6.0em;"></div>

## Matthew Turk
## Fall 2019
## Lecture 6

---

## Warm-Up Activity: Part 1

1. What is the visualization trying to show?
1. What are its methods?
1. What are the strengths / weaknesses?

 * https://www.reddit.com/r/dataisbeautiful/comments/d4mh5k/the_impact_of_smartphones_on_the_camera_industry/

---

## Warm-Up Activity: Part 2

1. What is the visualization trying to show?
1. What are its methods?
1. What are the strengths / weaknesses?

 * https://graphics.reuters.com/ENVIRONMENT-PLASTIC/0100B275155/index.html

---

# Interactivity

 * Interactivity and bqplot
    * Selection
    * Linked displays
    * Worked Example: Congressional district with timeline
 * Web Viz (again!)
    * (Sort of) How the web works
    * (Very, very) Basic javascript
    * vega-lite

---

## More Marks in bqplot

bqplot has several different marks we can explore.  We will utilize a few more
today:

 * `HeatMap`
 * `GridHeatMap`
 * `Bars`
 * `MarketMap`
 * `FlexLine`

([documentation](https://bqplot.readthedocs.io/en/latest/_generate/bqplot.marks.Mark.html))

---

## Bars

As you may have found, when doing histograms and binning *manually*, the bqplot
`Hist` mark is not as flexible as you may need.  The `Bars` plot is a useful
alternative.  Rather than taking `sample`, it takes `x` and `y` values.

If `y` is a list and the `type` attribute is not set to `"grouped"`, the bars
will be stacked.

 * `x`: x values
 * `y`: y values
 * `type`: `"stacked"` or `"grouped"`

---

## FlexLine

`FlexLine` marks allow the specification of both thickness and color that
change along the lines themselves.

This is useful to describe additional dimensions of data, but it is worth a
cautioning word that this can easily overwhelm the viewer and confuse them.

  * `x`: x values
  * `y`: y values
  * `color`: color values (requires `scales` for `color`)
  * `width`: thickness of the line (requires `scales` for `width`)

---

## Special Case: MarketMap

We will spend some time looking at a "market map" visualization today, which we
can use to provide a "table of contents" to other interactive visualizations.

MarketMap visualizations give us boxes, possibly colored and grouped, with selection opportunities.
We can use these to link our visualizations together based on broadly-specified categories.

  * `names`: Names of individual boxes
  * `ref_data`: reference dataframe for tooltips
  * `groups`: (optional) groups for the boxes
  * `color`: (not `colors`) data for the box colors; requires `scales`

---
## Dashboard for Buildings in bqplot

Today we will collaboratively build out a visualization dashboard in bqplot.

I want to be able to see when buildings were built in each district, by which
department, and how big they were.

 * What might this look like?
 * What kind of interaction should we have?

---

## Let's get started!

Remember, we can use `MarketMap` 

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

## Assignment 4:

 * Create a building inventory display -- not interactive -- using vega-lite.
 * Include: 
   * Timeline of years constructed/acquired
   * The total square footage by congressional district
   * Top five departments, aggregate square footage over time
 * Avoid any preprocessing of the data

This one is due in one week.
