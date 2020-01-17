---
title: Lecture 11
layout: lecture
---

<!-- .slide: class="titleslide" -->

# Data Visualization

<div style="height: 6.0em;"></div>

## Matthew Turk
## Fall 2019
## Lecture 11

---

## ipyleaflet

```
conda install -c conda-forge ipyleaflet
jupyter labextension install jupyter-leaflet
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

[Documentation](https://ipyleaflet.readthedocs.io/) and [Github Repo](https://github.com/jupyter-widgets/ipyleaflet)

---

## Creating a Map

```python
import ipyleaflet
m = ipyleaflet.Map()
display(m)
```

Now, zoom waaaaay out.

---

## Layers

We will refer to all of our "data objects" as Layers with ipyleaflet.  These can include:

 * Tiles
 * Markers
 * Image / video overlays
 * Polyline / MultiPolyline / Polygon / MultiPolygon
 * Rectangle / Circle
 * Marker Cluster
 * Heatmap

---

## Add Control

```
m.add_control(ipyleaflet.LayersControl())
```

This will let us choose and manipulate individual layers.

---

## Adding some data

```
import json 
with open("champaign_trees.geojson") as f:
    gd = json.load(f)

layer = ipyleaflet.GeoJSON(data = gd)
m.add_layer(layer)
```

---

## Experiment 1: Champaign Public Transit

Retrieve either the CUMTD data yourself from [developer.cumtd.com](https://developer.cumtd.com/) or on Whole Tale in "Code Along."

Let's visualize the routes.

---

## Experiment 1: Step 1

This data is in the GTFS format.  It has routes, trips, stops, etc.

Step 1: load the stop and route data files

---

## Experiment 1: Step 2

Place markers for stops on the map.

---

## Experiment 1: Step 3

Add a layer for a heatmap of stop locations.

---

## Kepler

First, try out [kepler.gl](https://kepler.gl)

---

## Kepler in Jupyter

We can display the map in a jupyter notebook.

```python
import keplergl
k = keplergl.KeplerGL()
display(k)
```

---

## Kepler: Adding Data in Jupyter

```
gd = pd.read_csv(" ... ")
k.add_data(data = gd, name = "my data")
```

---

## Experiment 2: Step 1

Load the tree data

---

## Experiment 2: Step 2

Display heatmap, with varying values

---

## Voila

```
conda install voila
```

Now, let's take one of our notebooks and make it a dashboard.

---

## Meeting Time

Time for you to meet with your groups.
