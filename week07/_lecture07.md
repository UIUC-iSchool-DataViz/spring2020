---
title: Lecture 8
layout: lecture
include_vega: true
---

<!-- .slide: class="titleslide" -->

# Data Visualization

<div style="height: 6.0em;"></div>

## Matthew Turk
## Fall 2019
## Lecture 7

---

## Warm-Up Activity

Today I have three!

 1. What is the visualization trying to show?
 1. What are its methods?
 1. What are the strengths / weaknesses?

---

First, a cool visualization I saw last night (with associated ObservableHQ notebook!)

https://twitter.com/karim_douieb/status/1181695687005745153

---

<!-- .slide: data-background-image="https://pbs.twimg.com/media/DY5aB0MVQAIoCPY.jpg" data-background-size="auto 70%" data-background-position="bottom center" -->

https://wapo.st/2HVLqUw

---

And finally, inspired by last week's water bottle:

https://twitter.com/MichaelGalanin/status/1181056943470923777

---

## Today

 * Evaluating Visualization Systems
 * Vega-lite - II
   * Marks
   * Selections
   * Transformations
   * Computations
 * Maps
   * Projections
   * Coordinate Systems
   * Plotting with CartoPy

---

## Evaluating Visualization Engines

 * Costs
 * Functionality
 * Aesthetics


---

## Choices

 * Can I get ahold of this software?
 * Do I install it, or do I use it on a server?
 * What's the user interface like?
 * Is it declarative or is it procedural?

---

## License: Software

 * What can you do with the software?
 * Can you study the software?
 * Who can you share it with?
 * Who can you give your derivative works to?

---

## License: Software

 * Copyleft: share and share-alike
 * Non-copyleft: share, but don't necessarily need to share-alike
 * https://choosealicense.com/

---

## License: Data

 * What can you do with the data?
 * How do you credit that data?
 * Can the data be redistributed, remixed, modified?
 * http://opendefinition.org/guide/data/
 * https://theodi.org/guides/publishers-guide-open-data-licensing

---

## Accessibility

 * Is the software installed locally on your machine?
 * Is it hosted at a local or remote instance?
 * Who owns the visualizations, and how is access to them controlled?

---

## Interface

How do you interact with the software?

 * Declarative: how do you want the plot to look?
 * Procedural: what are the steps to make the plot look that way?

---

## Example Declarative

```python
Chart(df).mark_bar().encode(
    X('precipitation', bin=True),
    Y('count(*):Q')
)
```

(From [Altair Docs](https://altair-viz.github.io/tutorials/exploring-weather.html))

<!-- .slide: data-background-image="images/altair_example01.png" data-background-size="30% auto" data-background-position="right 20% bottom 20%" -->

---

## Evaluation: Costs

The "cost" of software is not exclusively the number of dollars you place on
the counter when you get a big cardboard box with marketing blurbs on the side.

Think about cost in several ways:

 * Monetary cost for *you* to use the software
 * Monetary cost for *someone else* to view your creations
 * Temporal cost of setting up
 * Cognitive cost for learning and using the system (documentation matters!)
 * Transmission cost for sharing your creations

---

## Evaluation: Aesthetics

Visualization is trendy.

When you construct something, think about the different ways it will be
interpreted:

 * How will the viewer understand the story of the data?
 * What will the _message_ of the visualization be?
 * Does the visualization say something about you and your handling of the data
   or utilization of tools?

---

## Assignment 5

Your assignment is to pick four of the following possibilities and write up a
set of comparisons for constructing the *same* visualization.   You must evaluate matplotlib, vega-lite and bqplot, and you can choose one of the following in addition: D3, Bokeh, Plotly, R/RStudio.

These comparisons should be:

 * What is the license for the software?
 * What is the focus of the software?
 * Does it have interactivity, and how easy is it?
 * What are the pros and cons of using it?

These should total roughly half a page per engine.

---

## Vega-Lite - I

Recall that vega-lite is defined in a JSON specification.  This specification will typically take a form similar to this:

```json
{
  "data": .. ,
  "transform": [ .. ],
  "mark": .. ,
  "selection": .. ,
  "encoding": .. ,
  "config": ..
}
```

---

## Vega-Lite - II

Last week we discussed marks and encodings.

This week we will continue with marks, adding on transformations and selections.

---

## Marks - I

vega-lite has numerous different `mark` types.  We can break these down by the type of data they can represent.  We will only consider "primitive" marks today.

 * `area` & `line`
 * `bar` & `rect`
 * `point` & `circle` & `square`
 * `rule` & `text`
 * `tick`
 * `geoshape`

We will demonstrate several of these using our datasets, but first we need to learn how to transform data.

---

## Transformations - I

At the `view`-level of your definition, you can specify transformations that modify, filter, or reshape the data.

At the top level, we specify a transformation.  We can transform data within a given dataset (by specifying a new attribute of each data point) or by reshaping the data.

The types of transformations we will cover today are `filter` and `calculate`.

---

## Transformations - II

We apply a `filter` transform by specifying the field to filter on and the filtering characteristic.  This can be a selection, an expression, or a logical definition.  We will address selection and expression filtering later.

---

## Transformations - III

A logical filtering operation might look like one of these:

```json
"transform": [
  {"filter": {
      "field": "eye_color", "oneOf": ["blue", "brown"]
      }
  },
  {"filter": {"field": "age", "lte": 100 }
  }
]
```

We can use `lt`, `gt`, `lte`, `gte`, `eq`, `oneOf`, `range` and `valid`.

---

## Transformations - IV

We can also compute a new field using the `calculate` transform.  This is an expression that is evaluated on every data point, which is supplied as the variable `datum` to the expression.

```json
"transform": [
  {"calculate": "datum.age / 7", "as": "dog_years"}
]
```

---

## Selections - I

Selections are defined with *names* -- this seems to be the most common stumbling block.  You get to choose the name!

We use selections in one of a few ways.

 * We can conditionally encode data -- for instance, change visibility, or alpha, or color.
 * We can use selections as input for filtering data.  Typically this is done with one plot showing unfiltered data and another using a filter from that selection.
 * Scale a domain based on a selection

---

## Selections - II

There are three types of selections:

 * `single` -- selecting a single point, 
 * `multi` -- multiple points
 * `interval` -- collections of values along encoding axes

We will focus on the `interval` selection.

---

## Selections - III

We can define a box-based selector that operates along the x axis by specifying which encoding it is linked to.  Here, we name it `valrange`, but we can choose whatever name we like.

```json
"selection": {
    "valrange": {"type": "interval",
                 "encodings": ["x"]
                 }
    }
```

Let's try this.

---

## Assignment 6

We will be doing this together, in class, much of this assignment.  Your task will be to do things outside of class and bring them the following week.

We will recreate:

https://pbs.twimg.com/media/DY5aB0MVQAIoCPY.jpg

We will also have a *map* of the United States, wherein we will be displaying the data for a selected region bound to the x axis of this figure.

---

## Assignment 6

To accomplish this, we will need to:

 1. Collect the data (data.world has this dataset)
 2. Transform the data to enable aggregating by decade-of-service.
 3. Encode the x, y and colors based on binning.
 4. Add a selection that colors items on a map (and we need to evaluate the best way to do this on a map)

We will be doing this for the next three weeks.

Based on how we will be approaching this, everyone should get full credit for this.

---

## Maps

The Earth is a sphere.

(Fun question: to what degree is it a sphere?)

Have you ever wrapped a piece of paper around a ball?

---

## Projections

To map from one system to another, we must "project" from the original sphere
to the flat object we are observing.

What are some things we could preserve during such a projection?

---

## Projections: Common Preservations

Typically, one or more of these will be preserved, or at least, the distortion
will be minimized:

 * Area
 * Shape (Conformal)
 * Distance

There are other properties that can be preserved, as well.  Typically, maps
will be a "compromise" between preserving different properties.

What happens when we preserve one property over another?

---

Mercator is a "conformal" projection.  What is wrong with this?

<!-- .slide: data-background-image="images/mercator.png" data-background-size="auto 80%" -->

---

## Projections: Distortions

We can characterize distortions in a projection by examining how a known shape
appears on them.  The Tissot Ellipse of Distortion is a method of showing this
by drawing circles of a fixed radius and examining their elliptical distortion.

---

What do you notice?

<!-- .slide: data-background-image="images/mercator.png" data-background-size="auto 80%" -->

---

<!-- .slide: data-background-image="images/mercator_tissot.png" data-background-size="auto 80%" -->

---

<!-- .slide: data-background-image="images/transversemercator.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/transversemercator_tissot.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/lambertcylindrical.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/lambertcylindrical_tissot.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/mollweide.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/mollweide_tissot.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/sinusoidal.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/sinusoidal_tissot.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/gnomonic.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/gnomonic_tissot.png" data-background-size="auto 95%" -->

---

## Discussion

What happens when we make a map that minimizes one region and maximizes
another?

---

## Maps: Coordinate Systems

Once we have our system of transformation, we need to have a method of
representing positions.

Three common baseline methods:

 * Spherical coordinates
 * Latitude and Longitude
 * Degrees, minutes, seconds

Take care with:

 * Zero points
 * North/South, East/West
 * Ranges

---

## Intro to cartopy

CartoPy is a toolkit that builds on matplotlib to create fast, easy map
representations.

We will be relying on three key concepts:

 * Axes projections (similar to our polar projections)
 * Coordinate representations
 * Shapes

Using these, we will be able to build out many visualizations.

---

## CartoPy: Projections

We start out by constructing an axes in CartoPy that uses a given projection:

```python
import cartopy
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection=cartopy.crs.Mollweide())
ax.coastlines()
```

What does this do?

---

## CartoPy: Coordinate Reference Systems

Transforming from a spherical reference system to a flat reference system is
the job of the projection; transforming from one discretization of a sphere to
another is the job of the coordinate system.

We can utilize Coordinate Reference Systems to describe the *input* coordinate
system and the *rasterization* system are described.

For example, there are several different ways to draw "straight" lines.  We can
do both `PlateCarree` and `Geodetic`.

```python
c_lat, c_lon = 40.1164, -88.2434
a_lat, a_lon = -18.8792, 47.5079
fig = plt.figure()
ax = fig.add_subplot(111, projection = cartopy.crs.PlateCarree())
ax.gridlines()
ax.coastlines()
ax.set_global()
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform = cartopy.crs.PlateCarree())
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform = cartopy.crs.Geodetic())
```

---

<!-- .slide: data-background-image="images/map_plot1.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/map_plot2.png" data-background-size="auto 95%" -->

---

## Other Map Viz

 * Google Maps & Earth
 * WorldWide Telescope
 * CesiumJS
 * bqplot
 * Vega & friends

---

## Lab

Let's get started on developing our recreation of that visualization.
