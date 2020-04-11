---
title: Lecture 12
layout: lecture
---

<!-- .slide: class="titleslide" -->

# Data Visualization

<div style="height: 6.0em;"></div>

## Matthew Turk
## Fall 2019
## Lecture 12

---

# Housekeeping

 * Your lowest coding assignment will be dropped.
 * This is your final weekly visualization assignment.
 * You will be presenting in groups, and I will announce the order in advance.
   Send your group name to me and Naveen.

---

# Assignment Highlights

 * [How Migration is Changing Our World](https://www.bloomberg.com/graphics/2019-how-migration-is-changing-our-world/)
 * [15 Visualizations](https://blog.udacity.com/2015/01/15-data-visualizations-will-blow-mind.html), especially:
   * Shooting stars, satellites, workday, music timeline
 * [Citibike Data](https://twitter.com/CraigTaylorGIS/status/1191282070380789760)
 * [Opiod Overdoes](https://medium.com/@chaitupramod/redesigning-a-bad-graph-spaghetti-to-micromaps-374d68b5df6c)
 * [Letter Frequency](https://public.tableau.com/en-us/gallery/frequency-letters)

---

## Today

 1. Scientific Visualization
 2. Big-ish Data
 3. Portfolio Building

---

## Scientific Visualization

What characterizes "scientific" visualization?

 * Spatial organization - distance metrics
 * Dimensionality reduction or mapping
 * Multiple overlapping quantities with implicit or explicit extent

---

## Scientific Visualization - Data Representations

<div class="multiCol">
<div class="col">
<div class="fig-container" data-style="height: 600px;" data-file="figures/blank_axes.html" data-markdown=true>
</div>
</div>
<div class="col" data-markdown=true>

Commonly, data will be represented in "scientific visualization" through one of a few mechanisms:

 * Discrete points
 * Volume-filling information
 * Meshed values

</div>
</div>

---

## Discrete Points: Data

<div class="multiCol">
<div class="col">
<div class="fig-container" data-style="height: 600px;" data-file="figures/scatter.html" data-markdown=true>
</div>
</div>
<div class="col" data-markdown=true>

 * Associated field values
 * May have extent
 * Values can be either
   * Locally defined
   * Integrated over neighbors
</div>
</div> 

---

## Discrete Points: Techniques


<div class="multiCol">
<div class="col">
<div class="fig-container" data-style="height: 600px;" data-file="figures/discrete_tech.html" data-markdown=true>
</div>
</div>
<div class="col" data-markdown=true>

 * Associated field values
 * May have extent
 * Values can be either
   * Locally defined
   * Integrated over neighbors
</div>
</div> 

---

## Discrete Points: Density Estimates

 * Searching
   * Quadtree
   * kD-tree
 * Integration
   * Kernels
   * Nearest-neighbor

---

## Volume-filling: Data

For this, we will be using Python to collaboratively explore what volume-filling data is.

Install yt and ipyvolume.

```
conda install -c conda-forge yt ipyvolume
```

---

## data for yt

We will acquire a bit of data.

Go to https://yt-project.org/data/ and download "[IsolatedGalaxy](http://yt-project.org/data/IsolatedGalaxy.tar.gz)" and uncompress it.

```python
import yt
ds = yt.load("IsolatedGalaxy/galaxy0030/galaxy0030")

ds.r[:].max("density", axis="z")

```

---

## Volume data: strategies

To analyze volume data, typically we conduct one or more of these operations:

 * Select data based on spatial or non-spatial criteria
 * Reduce the dimensionality of that data either along spatial or other axes
 * Aggregate data

This can include operations such as volume rendering, axial projection, histogramming/binning and resampling.

Let's try some of this out.

---

## Big-ish Data

How do we deal with data that is too large to fit into memory?

 * Can we cycle our operations?
 * Can we use tools to cycle operations?

---

## Operations

Some operations we can manually cycle through, storing only reductions in
memory rather than the full dataset.

Clear candidates:

 * Mean
 * Extrema
 * Histograms and "binning"

Is this the same as incremental updates to a dataset?

(What about the median?)

---

## Portfolio Building

GitHub pages is a simple, straightforward way to publish websites.

 * Static-site generation using Jekyll
 * Manual HTML building
 * Integration with other systems (Idyll)

---

## Publishing Notebooks

Jupyter Notebooks can be published online.  The simplest way:

 * Commit them to a github repository
 * View them using nbviewer.jupyter.org

Widget state can be saved in many cases.

http://ipywidgets.readthedocs.io/en/latest/embedding.html

---

## Your First Github Page

 * We will use Jekyll to build a github page
 * Create the repository `[username].github.io`
 * Clone this repository.
 * Let's talk about the branches `gh-pages` and `master`

---

## A Little Tiny Bit of D3

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

The basic concepts here we will convey, focusing on *static* visualizations:

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

## Next Time: Final lecture!

We'll cover more d3, as well as some additional fun topics.
