---
title: Lecture 7
layout: lecture
visible_lec: true
visible_n: true
---

<!-- .slide: class="titleslide" -->

# Data Visualization
<div style="height: 6.0em;"></div>

## Jill P. Naiman
## Spring 2020
## Lecture 7

---

## Warm-Up Activity

 1. What is the visualization trying to show?
 1. What are its methods?
 1. What are the strengths / weaknesses?

[Seismic Sound Lab](http://www.seismicsoundlab.org/?page_id=338)

In particular: [Ground Motions for Hait and Tohoku](https://vimeo.com/187740441)

---

## Weekly Viz Report

And the winner is...

notes:
run the random number generator!

---

# Office Hours this week

Tuesday **3:30pm-?**, no office hours on Friday.

<br>
<br>

**FYI:** less internet availability during Spring Break
 * email, Slack, etc should all work if you have questions!

---

# Homework over break

1. Installations & trying some web interfaces out
1. Extra Credit: Map viz

notes:
there will be HW over break, but it will be installing things and trying out some web interfaces.

**go to HW!**

---

## Where we are: Last week

<img src="../week06/images/dataviz_map_thisweek.png">

notes:
last week we started thinking a bit about making maps and their projections

---

## Where we are: This week

<img src="images/this_week_diagram.png">

notes:
this week, we will talk more about maps & their projections and play with a few different mapping options in Python

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
   * Plotting with CartoPy 
   * Plotting with ipyleaflet 
   * Plotting with geopandas
   * Geojson in general

notes:
in more detail: last week we started with maps and how we can use bqplot to do a lot of mapping type stuff

This week we will play with a few different mapping and viz engines and deal with the JSON and geo-json format for storing data

---

<br>
<br>
<br>

# Topic #1: Maps & their projections

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

<img src="../week06/images/mapwrap.gif" height="350"/>

notes:
One common conversion from sphere to plane is the squashed cylinder approach

This can be used to conserve straight lines (distances)


---

## Projections

<img src="../week06/images/mapsplode.gif" height="350"/>

notes:
There's always a weird way to do it too. Here we're exploding the sphere into lots of 
mostly planar pieces that we can just lie out side-by-side.

This may preserve shape well, but it will be hard to use to navigate!

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

<!-- .slide: data-background-image="../week06/images/mercator.png" data-background-size="auto 80%" -->

notes:
conformal = shape preserving (at the expense of accurate size)

---

## Projections: Distortions

We can characterize distortions in a projection by examining how a known shape
appears on them.  The Tissot Ellipse of Distortion is a method of showing this
by drawing circles of a fixed radius and examining their elliptical distortion.

<img src="../week06/images/Tissot_indicatrix_world_map_Mercator_proj.svg" height="400">

notes: so here for example, we see that the mercator projection has circles that
stay circles, though they change in relative size depending on where they are on the map

---

What do you notice?

<!-- .slide: data-background-image="../week06/images/mercator.png" data-background-size="auto 80%" -->

---

<!-- .slide: data-background-image="../week06/images/mercator_tissot.png" data-background-size="auto 80%" -->

notes:
Greenland and Antarctica are HUGE

---

<!-- .slide: data-background-image="../week06/images/transversemercator.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="../week06/images/transversemercator_tissot.png" data-background-size="auto 95%" -->

notes:
this projection is most accurate near the vertical center line

---

<!-- .slide: data-background-image="../week06/images/lambertcylindrical.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="../week06/images/lambertcylindrical_tissot.png" data-background-size="auto 95%" -->

notes:
Also known as "equirectangular", this is the favorite format of NASA because it's mathematically straightforward.

Note that the very top line of the image represents a single point on the globe.

---

<!-- .slide: data-background-image="../week06/images/mollweide.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="../week06/images/mollweide_tissot.png" data-background-size="auto 95%" -->

notes:
this is considered a good compromise between shape-preserving and angle preserving - but it's not perfect at either.

---

<!-- .slide: data-background-image="../week06/images/sinusoidal.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="../week06/images/sinusoidal_tissot.png" data-background-size="auto 95%" -->

notes:
this has even less distortion than mollweide, but the pointy ends don't feel very elegant and planet-like

---

<!-- .slide: data-background-image="../week06/images/gnomonic.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="../week06/images/gnomonic_tissot.png" data-background-size="auto 95%" -->

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
Let's go see what Greenland actually looks like -- this was part of the intro, but I'll point it out again so you can really see it!

---

## Discussion

Why is Europe at the center of all the maps we've looked at?

---

## Discussion

<img src="../week06/images/Azimuthal_equidistant_projection.jpg" width="512"/>

notes: there is nothing specifically wrong with putting a pole at the center of the map

---

## Discussion

<img src="../week06/images/Azimuthal_equidistant_tissot.png" width="512"/>

notes: also see here that now the equator is very distorted

---
## Discussion

<img src="../week06/images/Waterman_projection.png" width="512"/>

notes: or why bother having a spherical or rectangular shape at all?

---

## Discussion

<img src="../week06/images/Waterman_tissot.png" width="512"/>

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

<br>
<br>
<br>

# Topic #2: Formatting for shape data

---

## JSON & GeoJSON

<img src="../week02/images/jsonex.png">

notes:
json is meant to be a way to store data that is "query" based - i.e. it lends itself to searches well

for this reason, it shows up in web development a lot

---

## GeoJSON

<img src="https://www.avenza.com/wp-content/uploads/2017/01/image002-1.png">

notes:
geojson is just a special json formatting for geographical data

it will specify the "shape" of the data file but also things like its default coordinate reference system which tells you something about the "center" and "stretch" of whatever it lists in its coordinates

---

## GeoJSON

<div class="left">

GeoJSON is:
* data format for encoding geographic data structures
* uses "geometries", "features" and "collections of features"
* seven Geometry types/objects
   1. Point
   1. LineString
   1. Polygon
   1. MultiPoint
   1. MultiLineString
   1. MultiPolygon
   1. GeometryCollection

</div>

<div class="right" markdown=1>

<img src="https://www.avenza.com/wp-content/uploads/2017/01/image002-1.png" alt="drawing" width="200"/>

</div>


notes:
cite: https://image.slidesharecdn.com/geojson-170417122110/95/geojson-1-638.jpg?cb=1492431924

We will see a lot of Polygons & MultiPolygons.

---

## GeoJSON

Tips for dealing with GeoJSON:
 * use `.keys()` and progressively drill down to data of interest
 * look for location of `properties` and `features`

We will get practice at this during programming.

notes:
often our issue will be linking the information stored in JSON file formats with that of whatever plotting routine we are using

we'll get some practice with this in the coding portion of class

---

<br>
<br>
<br>

# Topic #3: Data & Viz Engines

---

## Access to geometry files

 1. Cartopy
 1. ipyleaflet
 1. GeoPandas

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

## ipyleaflet

Leaflet is another mechanism of plotting, displaying and interacting with maps.

We will very briefly play with this in Python - could be of use for those that were having issues with cartopy.

---

## Geopandas

<img src="https://geopandas.org/_images/sphx_glr_create_geopandas_from_pandas_001.png">

notes:
the calls for geopandas is going to look very similar to pandas calls!

---

## Geopandas

```python
gdf = geopandas.read_file('mapfile.geojson')
gdf.head()
gdf.plot()
```

---

## Geopandas

```python
gdf = geopandas.read_file('mapfile.geojson')
gdf.head()
gdf.plot()
```

Map information sources:
 * [https://datagateway.nrcs.usda.gov/](https://datagateway.nrcs.usda.gov/)
 * [US Census info](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)
 * [City of Champaign](https://gis-cityofchampaign.opendata.arcgis.com/)

---

## Other Map Viz

 * Google Maps & Earth
 * WorldWide Telescope
 * CesiumJS
 * bqplot
 * Vega & friends

---

# To Python!
