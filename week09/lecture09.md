---
title: Lecture 9
layout: lecture
---

<!-- .slide: class="titleslide" -->

# Data Visualization

<div style="height: 6.0em;"></div>

## Matthew Turk
## Fall 2019
## Lecture 9

---

## Warm-Up Activity

 1. What is the visualization trying to show?
 1. What are its methods?
 1. What are the strengths / weaknesses?

https://vimeo.com/187740441

---

## Today - and assignment

<div class="mediumtext" data-markdown>

We will be ending early for the iSchool Research Showcase.

You will have an assignment for this presentation, to be turned in by class
next week.

**This is instead of your usual weekly visualization.**

Your assignment is to identify one of the items presented
(poster, talk, etc) *other than mine* and supply a writeup about
its usage of visualization:

 * How was visualization used in the talk/poster?
 * How was visualization used in the discovery?
 * What were the types of visualization used? What comments did
     you have about them?

This writeup should utilize the vocabulary we use in class, and
the classification of the types of visualization.  It should be
about half a page and include a description of the discovery
presented, its context, and a reasonable discussion of how
visualization was used in the process.

</div>

---

## Final Project

Your final project is due on December 11.

That is over a month from now.

You will have three components:

1. Viz for Self (Due November 20)
1. Viz for Peers (Due December 4)
1. Viz for Others (Due December 11)

---

## Final Project: Part 1

<div class="mediumtext" data-markdown>

This will be graded individually.  Due by class on November 20, submitted via
Moodle.  Submit in a Jupyter notebook.

 * Organize yourselves into groups of 4
 * Identify a dataset to explore.
   * This will be iterative!  You probably won't get one you like on the first
     try.
   * Check out sources like [data.world](https://data.world/),
     [data.illinois.gov](https://data.illinois.gov/),
     [data.gov](https://data.gov/),
     [developer.marvel.com](https://developer.marvel.com/),
     [IDB](https://databank.illinois.edu/), etc.
 * Explore the dataset in a Jupyter notebook.  **Do not delete any cells.**
 * Summarize the characteristics of the dataset in words: what does it
   represent, what are the fields/columns/rows, what data types are they, etc

</div>

---

## Final Project: Part 1 (cont)

<div class="mediumtext" data-markdown>

Your datasets need to be submitted as well.  To do this, include this
information in your Jupyter notebook:

 * What is the "name" of the dataset?
 * Where did you obtain it?
 * Where can we obtain it?  (i.e., URL)
 * What is the license of the dataset?  What are we allowed to do with it?
 * How big is it in file size and in items?

</div>

---

## Final Project: Part 2

<div class="mediumtext" data-markdown>

This will be graded per group.  Submit in a Jupyter notebook or in a series of
vega-lite visualizations.

 * Using your dataset, generate visualizations that explore the data in a
   guided way.
 * Your first component was focused on exploring the data in an unguided way.
   This component is about visualizing the data in a guided way.
 * Construct visualizations that explore each aspect you identified, with
   discussion and descriptions.
 * If you can identify improvements to the visualizations that come from
   interactivity, implement that.
 * The visualizations should utilize visual language relevant for "Viz for
   Peers."
    * Each and every plot should contain all relevant information: appropriate
      units, labeling, etc
    * Annotate and narrate particular pieces of interest (if there are any)
    * Use standard visual representations and augment these if necessary

</div>

---

## Final Project: Part 3

<div class="mediumtext" data-markdown>

You will submit this as your final project and will present it to the class.

You may submit one or more of the following items, but they *must* be in a
repository that is rendered as HTML.  More information will be coming shortly.

This component will include a "for others" visualization that is deeply
narrative with appropriate interactive (or static) content and shared on a
website.

Some possible ways to approach this:

 * Infographic
 * Idyll
 * Jupyter notebook (voila)
 * RShiny
 * Raw HTML / RevealJS / slides.com

</div>

---

## Today's Lab

Today we will expand our visualization of congresspeople to include a map of the United States, along with a table of congresspeople that served in each state.

---

## Geo Data

We will walk through the "airport connections" example on the vega-lite editor, as well as the "brush-table" example.

 * Display a map
 * Display data on that map
 * Look up states
 * Select based on pointer location
 * `"text"` mark
