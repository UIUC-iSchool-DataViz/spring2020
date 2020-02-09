---
title: Lecture 4
layout: lecture
---
<!-- .slide: class="titleslide" -->

# Data Visualization

<div style="height: 6.0em;"></div>

## Matthew Turk
## Fall 2019
## Lecture 4

---

## Warm-Up Activity

1. What is the visualization trying to show?
1. What are its methods?
1. What are the strengths / weaknesses?

 * https://gizmodo.com/observatories-across-the-world-announce-groundbreaking-1819500578
 * https://gizmodo.com/let-s-break-down-what-that-monumental-neutron-star-coll-1819613829

---

## Last Week

 * Transformations
 * Colors and color mapping
 * HSV/RGB/etc
 * Image visualization

---

## Review: Color Mapping

 * Choose an accessible, appropriate colormap
   * "Am I showing different things?"
   * "Can these things be compared directly?"
   * "Do I want to demonstrate deviation or gradiation?"
 * Mapping between "data space" and "color space" requires normalization and
   color mapping
   * Normalization: $f(v) => v' \in [0, 1]$
   * Color mapping: $g(v) => RGBA$

---

## This Week

 * Comparing Datasets
 * Traitlets in IPython/Jupyter
 * Visualization Engines: bqplot

---

## "function of"

---

## Comparison

 * Among Items
   * One Variable, Few Categories: Column, or  collection of bars
   * Two Variables: Variable Width Column Chart
   * Many variables: Embedded table or charts
 * Changing Over Time
   * Many Periods, non-cyclical: Line chart
   * Few Periods: Column or Line (depending on number of categories)

---

## Pandas

 * [pandas.pydata.org](http://pandas.pydata.org/)
 * Support for indexing, multi-indexing
 * Data structures
   * Series
   * DataFrame
   * Panel
 * Groupby, select, aggregation features
 * IO features
   * Reading/writing CSV, HDF5
   * Loading data from remote sources

---

## Engines

This week we'll be looking at two new visualization engines.

 * `bqplot`
 * `vega-lite`

---

## bqplot

Our first engine, `bqplot`, is a Jupyter-based interactive plotting system.

It presents two principal interfaces:

 * `pyplot`-like interface, for making the transition from matplotlib easier
 * An object-oriented API for constructing interactive visualizations

We will be using the latter far more frequently than the former.

---

## Traits and Data

Before we dig into `bqplot` specifically, we will be examining a handful of
methods by which we can provide interaction _as-is_ in Jupyter.

There are two underlying libraries we utilize for interactivity in Jupyter.
The first, `traitlets`, provides methods for datatype-verification and
"watching" for changes.

```#python
import traitlets

class MyObject(traitlets.HasTraits):
    name = traitlets.Unicode()
    age = traitlets.Int()

my_obj = MyObject(name = "Weezer", age = 26)
```

---

## Watching Traitlets

Once we have an object that has traits, we can watch that object for changes.

```#python

def name_changed(change):
    print(change['new'])

my_obj.observe(name_changed, ['name'])
```

In this case, we are watching the trait `name` for changes.  When a change
occurs, the function `name_changed` is called.  The argument is a dict with
these values:

 * `new`: the new value the trait has
 * `old`: the previous value
 * `type`: the type of change
 * `owner`: the object that owns this trait
 * `name`: the name of the trait

---

## Widgets

We can use the `ipywidgets` library to build out widgets in Jupyter notebooks.
These widgets can be quite extensive with many different operations;
additionally, they can have substantial CSS styling.

We've used simple examples before.  For instance, we can create an interactive
function very easily:

```#python
import ipywidgets

@ipywidgets.interact(name = ['Weezer', 'Nerf Herder', 'Mustard Plug'])
def print_bandname(name):
    print(name)
```

This creates a dropdown that we can select an item from, which is supplied.
What this is doing implicitly is creating a widget with a `value` attribute,
and whenever that `value` is changed, the function is called again.

---

## Widget Types 1

Automatically creating widgets using `@ipywidgets.interact` is very handy and
useful for quick operations, but we can do this more deliberately as well.
There are a number of widgets available in `ipywidgets` already:

 * `IntSlider`, `FloatSlider`, `IntRangeSlider`, `FloatRangeSlider`,
   `IntProgress` and `FloatProgress` all display or allow the user to choose
   values.
 * `IntText`, `FloatText`, `BoundedIntText` and `BoundedFloatText` let the user
   input explicit values to a widget.

---

## Widget Types 2

There are additional widget types that can provide indicators or restricted
selections.

 * `ToggleButton`, `Checkbox` and `Valid` provide boolean indicators; `Valid`
   is read-only.
 * For selection, there are `Dropdown`, `RadioButtons`, `Select`,
   `SelectionSlider` and several others.
 * Strings can be provided using `Text`, `TextArea` and `HTML`.
 * Actions can be enabled through `Button` objects.

Widgets can also be laid out using `HBox`, `VBox`, `Tab`, and `Accordion`.

---

## Events and Linking

In addition to watching for changes, we can watch for events and we can link
two (or more) values between different widgets.  

The special method `on_click` on a `Button` allows for a function to be called
when something is clicked.  We can also link using `ipywidgets.link` and
supplying traits.  For example:

```#python
m = MyObject(name = "Weezer", age=26)
l = ipywidgets.Label()
ipywidgets.link((m, 'name'), (l, 'value'))

display(l)

m.name = 'Nerf Herder'
```

**Exercise:** Add a button and make this change occur when clicked.

---

## bqplot

Now that we've learned a bit about widgets, we can start to dig into `bqplot`.
`bqplot` is based around traitlets and widget objects; every object you work
with will have traits and may be represented as a widget.

When we use `bqplot` we will be constructing `Figure` objects, which will
contain `marks` and `axes`.  To use these, we will build mark objects (`Bars`,
`Lines`, `Scatter`, `Map`, etc) and describe the relationship between points
using `Scale` objects.

We will be building out these objects and their relationships to develop
interactivity.

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

## Assignment 3

 * Using traitlets, widgets and bqplot, build a notebook that:
   1. Uses the UFO datasets
   2. Allows changing the x and y fields on a scatter plot from the UFO dataset
   3. Displays tooltips when hovering over individual items
 * Build a second widget that displays binned, aggregate values where you can change:
   1. The field to "bin"
   2. The method of aggregation (sum, mean, min, max, count)
   3. The number of bins

---

## Today: Let's Try Things

Today we are going to build comparisons with our (virtual) hands.

 * A Bit More Matplotlib
   * Patches and elements
   * "Projections"
   * Polar projections
 * Traitlets

---

## Next Week: Lab all day
