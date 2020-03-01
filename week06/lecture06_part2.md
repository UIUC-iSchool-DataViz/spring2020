---
title: Lecture 6, Part 2
layout: lecture
visible_lec: false
visible_n: true
---

<!-- .slide: class="titleslide" -->

# Data Visualization, continued
<div style="height: 6.0em;"></div>

## Jill P. Naiman
## Spring 2020
## Lecture 6, Part 2

---

<br>
<br>
<br>

# Topic #4: Maps & their projections

---

## Today's Main Topics


#### ~~Part 1:~~
 * ~~Evaluating Visualization Systems - Summary of HW Ideas~~
 * ~~More on dashboards~~
 * ~~Beginning map-dashboards with histogramming & bqplot~~


#### Part 2:
 * Maps - in more detail
   * Projections
   * Coordinate Systems
   * Infoviz/Choropleth maps 
   * Plotting with CartoPy (next week)
   * Plotting with ipyleaflet (next week)

---

## Maps

Thinking about map projections is important for GIS data, and generic global info viz.

Let's start by thinking about the fact that...

---

## Maps

Thinking about map projections is important for GIS data, and generic global info viz.

Let's start by thinking about the fact that...

The Earth is a sphere.

(Fun question: to what degree is it a sphere?)

Have you ever wrapped a piece of paper around a ball?

---

## Projections

To map from one system to another, we must "project" from the original sphere
to the flat object we are observing.

What are some things we could preserve during such a projection?

<img src="images/mapwrap.gif" height="350"/>

notes:
One common conversion from sphere to plane is the squashed cylinder approach


---

## Projections

<img src="images/mapsplode.gif" height="350"/>

notes:
There's always a weird way to do it too. Here we're exploding the sphere into lots of 
mostly planar pieces that we can just lie out side-by-side.

---

## Projections: Common Preservations

Typically, one or more of these will be preserved, or at least, the distortion
will be minimized:

 * Area
 * Shape (Conformal)
 * Distance

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

notes:
conformal = shape preserving (at the expense of accurate size)

---

## Projections: Distortions

We can characterize distortions in a projection by examining how a known shape
appears on them.  The Tissot Ellipse of Distortion is a method of showing this
by drawing circles of a fixed radius and examining their elliptical distortion.

<img src="images/Tissot_indicatrix_world_map_Mercator_proj.svg" height="400">

notes: so here for example, we see that the mercator projection has circles that
stay circles, though they change in relative size depending on where they are on the map

---

What do you notice?

<!-- .slide: data-background-image="images/mercator.png" data-background-size="auto 80%" -->

---

<!-- .slide: data-background-image="images/mercator_tissot.png" data-background-size="auto 80%" -->

notes:
Greenland and Antarctica are HUGE

---

<!-- .slide: data-background-image="images/transversemercator.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/transversemercator_tissot.png" data-background-size="auto 95%" -->

notes:
this projection is most accurate near the vertical center line

---

<!-- .slide: data-background-image="images/lambertcylindrical.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/lambertcylindrical_tissot.png" data-background-size="auto 95%" -->

notes:
Also known as "equirectangular", this is the favorite format of NASA because it's mathematically straightforward.

Note that the very top line of the image represents a single point on the globe.

---

<!-- .slide: data-background-image="images/mollweide.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/mollweide_tissot.png" data-background-size="auto 95%" -->

notes:
this is considered a good compromise between shape-preserving and angle preserving - but it's not perfect at either.

---

<!-- .slide: data-background-image="images/sinusoidal.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/sinusoidal_tissot.png" data-background-size="auto 95%" -->

notes:
this has even less distortion than mollweide, but the pointy ends don't feel very elegant and planet-like

---

<!-- .slide: data-background-image="images/gnomonic.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/gnomonic_tissot.png" data-background-size="auto 95%" -->

notes:
this is another nightmare scenario like Mercator that was initially created for navigation. Straight lines on this map are the shortest route, but area, shape, and size are distorted.

---

## Discussion

What happens when we make a map that minimizes one region and maximizes
another?

---

## Discussion

<iframe width="1024" height="576" src="https://www.youtube.com/embed/vVX-PrBRtTY?rel=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

notes:
after watching this, it's useful to know that the Peters projection is actually flawed as a teaching tool because of how much it distorts the shapes of countries near the poles.

---

## Discussion

[The True Size Of...](https://thetruesize.com)

notes:
Let's go see what Greenland actually looks like

---

## Discussion

Why is Europe at the center of all the maps we've looked at?

---

## Discussion

<img src="images/Azimuthal_equidistant_projection.jpg" width="512"/>

notes: there is nothing specifically wrong with putting a pole at the center of the map

---

## Discussion

<img src="images/Azimuthal_equidistant_tissot.png" width="512"/>

notes: also see here that now the equator is very distorted

---
## Discussion

<img src="images/Waterman_projection.png" width="512"/>

notes: or why bother having a spherical or rectangular shape at all?

---

## Discussion

<img src="images/Waterman_tissot.png" width="512"/>

notes: look how here there is very little distortion of size or shape

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

<!--What does this do?-->

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

notes:
the blue line is Plate Carree, which maintains a straight line on the lat-lon grid

the orange line is Geodetic, which maintains a straight line around the curvature of the Earth

---

<!-- .slide: data-background-image="images/map_plot2.png" data-background-size="auto 95%" -->

notes:
now even the blue line has some curvature because we are picking a best-of-both-worlds Mollweide projection that doesn't perfectly preserve angle or area.

---

## Other Map Viz

 * Google Maps & Earth
 * WorldWide Telescope
 * CesiumJS
 * bqplot
 * Vega & friends

---

