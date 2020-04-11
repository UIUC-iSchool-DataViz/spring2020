---
title: Lecture 12, Part 2
layout: lecture
include_vega: true
visible_lec: true
visible_n: true
---

<!-- .slide: class="titleslide" -->

# Data Visualization

<div style="height: 6.0em;"></div>

## Jill P. Naiman
## Spring 2020
## Lecture 12, Part 2

---

## A Little Bit of d3

We're going to learn a very small bit of [d3.js](https://d3js.org/).

The easiest way to utilize D3 is through [observablehq.com](https://observablehq.com):

```
d3 = require("d3@5");
```

although it is straightforward to include the necessary code in an HTML page:

<code>
&lt;script src="https://d3js.org/d3.v5.min.js"&gt;&lt;/script&gt;
</code>

---

## Concepts in d3: outline

The basic concepts here we will convey:

 * `.select()` and `.selectAll()`
 * `.enter()`
 * `.attr()` and `.style()`
 * `d3.scaleLinear()`

---

## Concepts in d3: data and elements

When we manipulate items in d3, we connect the concept of a data item to an
element in a document.

Typically, this will be an element in an SVG -- for instance, a `line`,
`circle`, `rect` or `text` element.

Our typical workflow:

 1. Select all items of a specific criteria
 2. Bind these items to a set of data
 3. Update, append or remove items based on their corresponding item.

---

## Concepts in d3: accessors and setters

We will very frequently run into the case where we call something, and supply a
*function* to it, rather than supplying a value.  For instance, *both* of these
calls to `attr` are valid in a typical d3 workflow:

```javascript
.attr("cx", 1.0)

// or

.attr("cx", d => d.x)
```

In one, we are setting the value static; in the other, we base the value on the datapoint supplied.

---

## Concepts in d3: Let's make circles

For our first exploration, let's just make some circles.  I will demonstrate this in observable, but here is the key snippet of code:

```
var dataset = [ {'x': 100, 'y': 200, 'radius': 15},
                {'x': 150, 'y': 300, 'radius': 30} ];
svg.selectAll("circle").data(dataset).enter()
   .append("circle")
   .attr("cx", d => d.x)
   .attr("cy", d => d.y)
   .attr("r", d => d.radius)
   .style("fill", "black");
```

What does this do?

---

## Concepts in d3: Objects

We will mostly use the objects

 * [`rect`](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/rect) -- which has `x`, `y`, `width` and `height` 
 * [`circle`](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/circle) -- which has `cx`, `cy`, and `r`
 * [`line`](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/line) -- which has `x1`, `x2`, `y1` and `y2`.

Each of these objects can be controlled in style, appearance, position, etc, according to standard SVG and CSS rules.

Let's experiment!

---

## Concepts in d3: Scaling

To map from a given range to a different range in a linear fashion, we can construct a linear scale:

```javascript
var xScale = d3.scaleLinear().range([0, 100]).domain([0.0, 1.0]);
```

This is now an object we can use to map the values 0 .. 1 to 0 .. 100.  This is useful for, among other things, computing the position of a given value:

```javascript
.attr("cx", d => xScale(d.x))
```

---

## Additional Basic Topics

`d3.axisBottom(xScale)` can be used to create ticks and axes; however, it
requires manual translation using the `transform` attribute, using something
like `.attr("transform", "translate(0, 30)")`.  This then brings up our concept
of margins, width, height, and the like!  How can we manage these?

Let's try it out!

---

## There are lots of examples on the web we can build from!
