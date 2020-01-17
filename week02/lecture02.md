---
title: Lecture 2
layout: lecture
---
<!-- .slide: class="titleslide" -->

# Data Visualization

<div style="height: 6.0em;"></div>

## Matthew Turk
## Fall 2019

---

## Warm-Up Activity

1. What is the visualization trying to show?
1. What are its methods?
1. What are the strengths / weaknesses?
1. (Bonus) Where is the outright error?

https://www.axios.com/the-latest-on-harveys-energy-toll-2479055875.html

---

## Today's Topics

 * How does drawing work?
 * Data Formats
 * Operational Palette
   * Filtering
   * Sampling
   * Mutation
   * Histograms and aggregations
   * Splitting
 * Data types in a visualization
 * Distributions
 * Elements of a visualization

---

## Drawing

How do we draw an image?

---

<iframe width="1024" height="576"
src="https://www.youtube.com/embed/qfDxiVpgjiM" frameborder="0"
allow="autoplay; encrypted-media" allowfullscreen></iframe>

---

## Let's draw a line.

<!-- .slide: data-background-image="images/line.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Let's draw a line.

<!-- .slide: data-background-image="images/line.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

```
start = (x0, y0)
end   = (x1, y1)
width = 1.0
```
<!-- .element: class="left_abs" style="width: 50%"-->

---

## Let's draw a line.

Convert to an 8x8 image.

<!-- .slide: data-background-image="images/line_grid.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Let's draw a line.

Convert to an 8x8 image.

<!-- .slide: data-background-image="images/line_grid_fill.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Let's draw a line.

Convert to an 16x16 image.

<!-- .slide: data-background-image="images/line_grid_fine2.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Let's draw a line.

Convert to an 16x16 image.

<!-- .slide: data-background-image="images/line_grid_fine2_fill.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Let's draw a line.

Convert to an 32x32 image.

<!-- .slide: data-background-image="images/line_grid_fine4.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Let's draw a line.

Convert to an 32x32 image.

<!-- .slide: data-background-image="images/line_grid_fine4_fill.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Representations

We will concern ourselves with understanding two representations of an image:
the **raster** representation and the **vector** representation.

---

## Representations: raster

 * Each pixel is represented as a color
 * Common file formats such as GIF, JPG, PNG
 * Compression can be lossy (JPG) or lossless (PNG)

In a raster image, you describe precisely what to display.

---

## Representations: vector

 * Each component is defined as a "drawing" component, or some action to be
   taken by the rendering engine.  This can include paths, patterns,
   shapes, and text.  Components have properties associated with them.
 * Common file formats are SVG, PDF, EPS
 * The display does not exist until it is "rendered."
 * Options for compression include (lossless) text compression, although
   the rendering engine can simplify display

---

## Raster Representation

| | | | | |
|-:|-|-|-|-|
| | 1 Line | 2 Lines | 30 Lines | 1000 Lines |
|`600x600` | 45kb | 45kb | 45kb | 45kb |
|`1200x1200` | 180kb | 180kb | 180kb | 180kb |
|`2400x2400` | 720kb | 720kb | 720kb | 720kb |

(uncompressed, 1-bit images)

---

## Vector Representation

| | | | | |
|-:|-|-|-|-|
| | 1 Line | 2 Lines | 30 Lines | 1000 Lines |
|`600x600` | 5 bytes | 10 bytes | 150 bytes | 5000 bytes |
|`1200x1200` | 5 bytes | 10 bytes | 150 bytes | 5000 bytes |
|`2400x2400` | 5 bytes | 10 bytes | 150 bytes | 5000 bytes |

(uncompressed, single precision)

---

## Let's draw a circle.

<!-- .slide: data-background-image="images/single_circle.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

```
center = (x0, y0)
radius = 1.0
```
<!-- .element: class="left_abs" style="width: 50%"-->

---

## Let's draw many circles.

<!-- .slide: data-background-image="images/dots.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Let's draw many circles.

<!-- .slide: data-background-image="images/dots_grid.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Let's draw many circles.

<!-- .slide: data-background-image="images/dots_grid_fill.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Let's draw many circles.

<!-- .slide: data-background-image="images/dots_grid_fine2.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Let's draw many circles.

<!-- .slide: data-background-image="images/dots_grid_fine2_fill.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Let's draw many circles.

<!-- .slide: data-background-image="images/dots_grid_fine4.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Let's draw many circles.

<!-- .slide: data-background-image="images/dots_grid_fine4_fill.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

---

## Raster Representation

| | | | | |
|-:|-|-|-|-|
| | 1 Circle | 2 Circles | 30 Circles | 1000 Circles |
|`600x600` | 45kb | 45kb | 45kb | 45kb |
|`1200x1200` | 180kb | 180kb | 180kb | 180kb |
|`2400x2400` | 720kb | 720kb | 720kb | 720kb |

(uncompressed, 1-bit images)

---

## Vector Representation

| | | | | |
|-:|-|-|-|-|
| | 1 Circle | 2 Circles | 1000 Circles | 1e6 Circles |
|`600x600` | 3 bytes | 6 bytes | 3000 bytes | 3 Mb |
|`1200x1200` | 3 bytes | 6 bytes | 3000 bytes | 3 Mb |
|`2400x2400` | 3 bytes | 6 bytes | 3000 bytes | 3 Mb |

(uncompressed, single precision)

---

## Text

Modern fonts are composed of glyphs defined by functional forms of their shape.
Font rendering engines such as freetype2 can generate bitmaps for fonts
rendered at specific resolutions.

In raster image file formats, fonts do not need to be embedded: the rasterized,
rendered version is the one that is transmitted to the viewer.

In vector file formats, fonts can either be embedded (in whole or in part) or
fallback fonts available to the rendering engine can be used.

---

<img src="images/font_A.png">

<img src="images/font_O.png">

<img src="images/font_T.png">

<img src="images/font_X.png">

---

<!-- .slide: data-background-image="images/viz_diagram.svg" data-background-size="contain"-->

---

<!-- .slide: class="two-floating-elements" -->

## Files, Data, and Organization

* Text
  * ASCII (raw)
  * CSV / TSV
  * JSON
* Binary
  * HDF5
  * PNG/BMP/GIF/JPG/etc
  * Excel
  * Arrow
* Query-based
  * SQL
  * JSON/REST

<div class="right" markdown=1>

![](diagrams/row_col.svg)

</div>

---

## Organization

| | Column 1 | Column 2 | Column 3 | Column 4 |
|-|-|-|-|-|
|Row 1|11|21|31|41|
|Row 2|12|22|32|42|
|Row 3|13|23|33|43|

Internally, this data is stored linearly, with one value immediately following
another.  We can do this in two methods:

||||||||||||||
|:-|-|-|-|-|-|-|-|-|-|-|-|-|
| Row | 11 | 21 | 31 | 41 | 12 | 22 | 32 | 42 | 13 | 23 | 33 | 43 |
| Column | 11 | 12 | 13 | 21 | 22 | 23 | 31 | 32 | 33 | 41 | 42 | 43 |

<!-- .element: class="fragment" -->

---

### Organization: Row

| | | | | | | | | | | |
|-|-|-|-|-|-|-|-|-|-|-|
| 11 <!--.element: class="table-hl" -->| <!--.element: class="table-hl" -->21 | 31 | 41 | 12 | 22 | 32 | 42 | 13 | 23 | 33 | 43 |

In row-oriented storage, successive _fields_ for a single _record_ are
adjacent.

<div style="height: 2.0em;"></div>

### Organization: Column

| | | | | | | | | | | |
|-|-|-|-|-|-|-|-|-|-|-|
| 11 <!--.element: class="table-hl" -->| 12 | 13 | <!-- .element: class="table-hl" --> 21 | 22 | 23 | 31 | 32 | 33 | 41 | 42 | 43 |

In column-oriented storage, successive _records_ for a single _field_ are
adjacent.

---

## CSV (Comma-separated values)

| Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
|-|-|-|-|-|
| . | . | . | . | . |
| . | . | . | . | . |
| . | . | . | . | . |
| . | . | . | . | . |

<div style="height: 2.0em;"></div>

 * Lowest-common denominator format
 * Flexible delimiters
 * Ad hoc comments and headers
 * Row-oriented
 * Row-size can vary: no implicit indexing

---

```
...
390,1.83970e-003,-4.53930e-004,1.21520e-002
395,4.61530e-003,-1.04640e-003,3.11100e-002
400,9.62640e-003,-2.16890e-003,6.23710e-002
405,1.89790e-002,-4.43040e-003,1.31610e-001
410,3.08030e-002,-7.20480e-003,2.27500e-001
415,4.24590e-002,-1.25790e-002,3.58970e-001
420,5.16620e-002,-1.66510e-002,5.23960e-001
425,5.28370e-002,-2.12400e-002,6.85860e-001
...
```

---

```

390,1.83970e-003,-4.53930e-004,1.21520e-002
```

If we assume ASCII encoding, this becomes:

| | | |
|-|-|-|
|"390" <!-- .element: class="table-hl" --> |51 |57 |48 |
<!-- .element: style="margin-left: 0.2em;" -->

Breaking this further down, we encode each character:

||||||||||
|-|-|-|-|-|-|-|-|-|
|51 <!-- .element: class="table-hl" --> | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
|57 <!-- .element: class="table-hl" --> | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
|48 <!-- .element: class="table-hl" --> | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
<!-- .element: style="margin-left: 0.2em;" -->

---
```

390,1.83970e-003,-4.53930e-004,1.21520e-002
```

This is then translated into a floating point number:

||||||||||
|-|-|-|-|-|-|-|-|-|
|390.0 <!-- .element: class="table-hl" --> | 0 | 0 | 0 | 0 | 0 | 96 | 120 | 64 |
<!-- .element: style="margin-left: 0.2em;" -->

---
```

390,1.83970e-003,-4.53930e-004,1.21520e-002
```

|||||||||||||
|-|-|-|-|-|-|-|-|-|-|-|-|
| "1.83970e-03" <!-- .element: class="table-hl" -->| 49 | 46 | 56 | 51 | 57 | 55 | 48 | 101 | 45 | 48 | 51 |
<!-- .element: style="margin-left: 0.2em;"-->

And this is translated into a floating pointer number as well:

||||||||||
|-|-|-|-|-|-|-|-|-|
|1.83970e-003 <!-- .element: class="table-hl" -->  | 2 | 166 | 103 | 213 | 66 | 36 | 94 | 63 |
<!-- .element: style="margin-left: 0.2em;"-->

---

## JSON

| | | |
|:-|:-|:-|
| Record 1 | Record 2 | Record 3 |

<div style="height: 2.0em;"></div>

 * Row-oriented
 * Potentially-unknown subcomponent sizes (lists of lists)
 * Common response to REST APIs
 * Multiple types
   * String
   * Number
   * Object (JSON)
   * Array (list)
   * Boolean
   * null

---

```
[
 ...
 {"Agency Name":"University of Illinois",
  "Address":"501 E Daniel",
  "City":"Champaign",
  "Zip code":61820,
  "Year Acquired":1992,
  "Year Constructed":1935,
  "Square Footage":21845,
  "Total Floors":5
 }, 
 ...
]
```

<div style="height: 2.0em;"></div>

 * `[` and `]` indicate an array
 * `{` and `}` indicate a JSON object (or mapping)
 * `"` indicates a string
 * Numbers are, well, numbers.

---

## HDF5

| | | |
|:-|:-|:-|
| Column 1 | Column 2 | Column 3 |

<div style="height: 2.0em;"></div>

 * Columnar, chunked store
 * Flexible data types in-memory and on-disk
 * Hyperslab and boolean indexing
 * Fine-grained key/val metadata
 * Groups & hierarchies
 * Extensible types:
   * Numeric
   * Fixed-length strings
   * Variable strings

---

## Doing Stuff with Data

Now that we understand a few ways that data can be stored, and
how we draw with it, let's do some things to it.

---

<div class="left" data-markdown="true">

![](images/palette.svg)<!-- .element: style="height: 20em;" -->

</div>

<div class="right" style="font-size: 150%;">
<div style="height: 4.0em;"></div>
You have a palette of operations to apply.
</div>

---

## Filtering Operations

 * Relationships:
   * Equality, inequality
   * Quantitative value (less than, greater than)
   * Intersection, disjoint
 * Subsampling
   * Regular sampling
   * Randomized sampling
   * Nyquist frequency
 * Related data queries
   * Queries on other columns at fixed row location
   * External membership queries

|||||||||||||
|-|-|-|-|-|-|-|-|-|-|-|-|
|&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" -->|
|&nbsp;<!-- .element: class="table-hl" --> |&nbsp; |&nbsp; |&nbsp; |&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" --> |&nbsp; |&nbsp;<!-- .element: class="table-hl" --> |&nbsp; |&nbsp; |&nbsp;<!-- .element: class="table-hl" --> |&nbsp;<!-- .element: class="table-hl" -->|

---

## Relationships Examples

 * Equality
   * Identity
   * Quantitative values
 * Ordering or quantitative
   * Less than (or equal)
   * Greater than (or equal)
   * "Comes before" and "Comes after"
 * Set-based operations
   * "Is a member"
   * "Is not a member"
   * "Shares members"
   * "Shares no members"

---

## Examples

### Equality

```
value == "hello"
value == 10
```

### Ordering and Quantitative

```
value < 30
value > July 1, 2010
```

### Set-Based

```
value in ("red", "blue")
value not in (3.141, 2.7)
```

---

## Sampling

We can choose a subset of points and use those to explore our data.  This is
not without its possible faults, however.

---

<!-- .slide: data-background-image="images/sampling_fig1.png" data-background-size="contain" -->

---

<!-- .slide: data-background-image="images/sampling_fig2.png" data-background-size="contain" -->

---

<!-- .slide: data-background-image="images/sampling_fig3.png" data-background-size="contain" -->

---

<!-- .slide: data-background-image="images/sampling_fig4.png" data-background-size="contain" -->

---

<!-- .slide: data-background-image="images/sampling_fig5.png" data-background-size="contain" -->

---

<!-- .slide: data-background-image="images/sampling_fig6.png" data-background-size="contain" -->

---

## Mutation Operations

 * Mathematical operations, such as injective operations.
   * Logarithmic versus linear representations
   * Arithmetic or multiplicative relationships
   * Manifold remapping
 * Smoothing (reduction; not injective)
 * Histograms (reduction; not injective)

---

## Binning and Histograms

<!-- .slide: data-background-image="images/circles.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

<div style="width: 50%">
We can aggregate data points according to their position along defined
dimensions.
</div>

---

## Binning and Histograms

<!-- .slide: data-background-image="images/circles_grid.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

<div style="width: 50%">
We can aggregate data points according to their position along defined
dimensions.
</div>


---

## Binning and Histograms

<!-- .slide: data-background-image="images/circles_grid_filled.svg" data-background-size="auto 75%" data-background-position="right 10% bottom 50%"-->

* $\Sigma 1$ (count)
* $\Sigma v_i$ (sum)
* $\frac{\Sigma v_i }{ \Sigma 1}$ (average)
* $\frac{\Sigma v_i w_i}{\Sigma w_i}$ (weighted average)

---

## Splitting Operations

We can split or group collections of data based on some characteristic.

<!-- .slide: data-background-image="images/split.svg" data-background-size="65% auto" data-background-position="top 5.0em center"-->

---

## Splitting Operations

We can split or group collections of data based on some characteristic.

<!-- .slide: data-background-image="images/split_finished.svg" data-background-size="65% auto" data-background-position="top 5.0em center"-->

---

## Data Types

When we are examining data, what can we look for?

 * Does this data describe a **geometric** object?
 * Are the data points **connected** to each other?
 * Can we describe data points with a fixed set of **categories**?
 * Is there a **quantity** associated with the data?
 * Are the datapoints **continuous** along one or more dimensions?

---

## Example: Geometric Object

<div class="left" data-markdown="true">

| v1 | v2 | cat |
|:-|:-|-:-|
|8.5|-9| r |
|10|-8| r |
|11.5|-7| r |
|12.5|-5.5| r |
|13|-4| r |
| ... | ... | ... |
|-2.5|-6|b|
|-1.5|-7|b|
| ... | ... | ... | 

</div>

---

## Example: Geometric Object

<div class="left" data-markdown="true">

| v1 | v2 | cat |
|:-|:-|-:-|
|8.5|-9| r |
|10|-8| r |
|11.5|-7| r |
|12.5|-5.5| r |
|13|-4| r |
| ... | ... | ... |
|-2.5|-6|b|
|-1.5|-7|b|
| ... | ... | ... | 

</div>

<!-- .slide: data-background-image="images/mushroom.svg" data-background-size="30% auto" data-background-position="right 20% bottom 50%" -->

---

## Examples: Quantity

We can encode the values associated with a data point by modifying how we
express it.  To do so, we need to be able to identify the different components
of representation, and how we can scale between them.

---

## Dimensions of Representation

Given a single datum on a visualization, we can control several different
components of its representation.

 * Position

<!-- .slide: data-background-image="images/dimensions_1.svg" data-background-size="auto 50%" data-background-position="right 20% bottom 50%"-->

---

## Dimensions of Representation

Given a single datum on a visualization, we can control several different
components of its representation.

 * Position
 * Color

<!-- .slide: data-background-image="images/dimensions_2.svg" data-background-size="auto 50%" data-background-position="right 20% bottom 50%"-->

---

## Dimensions of Representation

Given a single datum on a visualization, we can control several different
components of its representation.

 * Position
 * Color
 * Size

<!-- .slide: data-background-image="images/dimensions_3.svg" data-background-size="auto 50%" data-background-position="right 20% bottom 50%"-->

---

## Dimensions of Representation

Given a single datum on a visualization, we can control several different
components of its representation.

 * Position
 * Color
 * Size
 * Shape

<!-- .slide: data-background-image="images/dimensions_4.svg" data-background-size="auto 50%" data-background-position="right 20% bottom 50%"-->

---

## Dimensions of Representation

Given a single datum on a visualization, we can control several different
components of its representation.

 * Position
 * Color
 * Size
 * Shape
 * Relationship

<!-- .slide: data-background-image="images/dimensions_5.svg" data-background-size="auto 50%" data-background-position="right 20% bottom 50%"-->

---

<iframe width="1024" height="576"
src="https://www.youtube.com/embed/kY-pUxKQMUE" frameborder="0"
allow="autoplay; encrypted-media" allowfullscreen></iframe>

---

## Just to remove any ambiguity

Don't do this!

---

http://adsabs.harvard.edu/abs/2013ApJ...763...38S 

([This
plot](http://iopscience.iop.org/article/10.1088/0004-637X/763/1/38/meta#apj455166f4)
might be a bit too busy.)

<!-- .slide: data-background-image="images/skory_et_al.png" data-background-size="auto 75%" data-background-position="right 20% bottom 50%" -->

---

## Continuous Data

Data organized in a continuous fashion along one or more dimensions can enable
additional operations.

<!-- .slide: data-background-image="images/cube.png" data-background-size="auto 50%" data-background-position="right 20% bottom 50%"-->

---

## Continuous Data

Data organized in a continuous fashion along one or more dimensions can enable
additional operations.

<!-- .slide: data-background-image="images/cube_z_slice.png" data-background-size="auto 50%" data-background-position="right 20% bottom 50%"-->


---

## Distributions

Given a point or set of points, how do we make them into a "continuous"
distribution?

<!-- .slide: data-background-image="images/binning_1.svg" data-background-size="75% auto" data-background-position="bottom 30% center"-->

---

## Distributions

Given a point or set of points, how do we make them into a "continuous"
distribution?

<!-- .slide: data-background-image="images/binning_2.svg" data-background-size="75% auto" data-background-position="bottom 30% center" -->

---

## Distributions

Given a point or set of points, how do we make them into a "continuous"
distribution?

Uniform-width bins allow us to compute:

```python
bin_id = floor( (value - left_edge ) / bin_width)
```

<!-- .slide: data-background-image="images/binning_2.svg" data-background-size="75% auto" data-background-position="bottom 30% center" -->

---
## Distributions

Given a point or set of points, how do we make them into a "continuous"
distribution?

Non-uniform bins require searching.

<!-- .slide: data-background-image="images/binning_3.svg" data-background-size="75% auto" data-background-position="bottom 30% center" -->

---

## Binning and Histograms

<!-- .slide: data-background-image="../week03/images/circles_grid_filled.svg" data-background-size="auto 75%" data-background-position="right 20% bottom 50%"-->

* $\Sigma 1$ (count)
* $\Sigma v_i$ (sum)
* $\frac{\Sigma v_i }{ \Sigma 1}$ (average)
* $\frac{\Sigma v_i w_i}{\Sigma w_i}$ (weighted average)

---

## Summation

Useful for describing total quantity measured.

 * Inches of rain.
 * Total time of recorded UFO sitings in the area.
 * How many votes were cast?

---

## Arithmetic Average

Useful for describing average or mean quantity.

* Average rainfall in the area.
* Average time of UFO sighting.
* Who was the average candidate?

---

## Weighted Average

Useful for describing mean, but not strict arithmetic mean.

* Average rainfall, weighted by how humid it was that day.
* What was the most commonly seen UFO type, as a function of the time it was
  seen?
* What's the mean age of a voter, as a function of the total years of
  experience in the election?

---

## Scales and Scaling

Displaying a quantity requires assigning to it a given representation.
A common mechanism for doing this is to vary the color of a particular region
or set of display units with respect to the quantity expressed in those units.

In mathematical notation, we first "normalize" our data value by assigning to a
range:

$g(v) \rightarrow v' \in [0, 1]$

and then, given a color mapping function, assign to this a given color:

$f(v') \rightarrow (R, G, B)$

---

## Scales and Scaling

Group discussion:

  * How is this similar to or different from our discussions of "binning" and
    histogramming?
  * What are some functions we can use for $g(v)$?
  * What are some considerations we need to take into account for variable
    bins?

---

## Histograms and Binning

Group work:

Write a function -- in plain language at first, and then in python -- that
takes a set of values, a series of bin "edges," and returns to you the integer
IDs of the bins that each belongs to.

---

## Assignment 2

Using one of the tools that we have discussed (matplotlib or vega-lite),
construct a visualization of the Illinois Building Inventory that communicates
the following information:

 * Relationship between the year acquired and the year constructed
 * Total square footage as a function of congressional district
 * Average square footage per floor as a function of congressional district
 * Square footage for the five most common departments as a function of year

Each component will be worth 5 points and *must* be a completely communicative
visualization -- including labels and a one paragraph writeup of successes and
shortcomings in your approach.  Submit a notebook or a set of JSON gists to
Moodle.  All source code must be in these files.
