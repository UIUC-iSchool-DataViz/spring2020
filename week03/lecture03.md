---
title: Lecture 3
layout: lecture
visible_lec: true
visible_n: true
---
<!-- .slide: class="titleslide" -->

# Data Visualization
<div style="height: 6.0em;"></div>

## Jill P Naiman
## Spring 2020
## Lecture 3

---

## Warm-Up Activity

1. What is the visualization trying to show?
1. What are its methods?
1. What are the strengths / weaknesses?

http://old.vijayp.ca/blog/2012/06/colours-in-movie-posters-since-1914/

[Movie Poster Hue](images/fullSaturation.png)

[Movie Poster Value](images/modifiedBrightness.png)

notes: go over the blog post - blocky one includes full HSV, without that you
just see Hue (H) and the full set of colors

---

<br>
<br>
<br>

# Bureaucracy, Part 3: The Final Installment

---

## How to get help

Jill P. Naiman - `jnaiman@illinois.edu`
 * Office Hours: Tuesday 3-4pm NCSA 2040 (this OH can go a little longer as needed), Friday 3-4pm in iSchool lounge; other times by request

TA: Diptendra Bagchi, `dbagchi2@illinois.edu`
 * Office Hours: iSchool, Room 56, Wednesday & Friday 1-2pm

TA: Qiuyan Guo, `qqguo2@illinois.edu`
 * Office Hours: iSchool, Room 56, Thursday 8-9am

---

## Where information is located:

 * Moodle: where the grades and assignments will be posted - https://learn.illinois.edu/course/view.php?id=42777

 * Course webpage: where lecture slides, notebooks, data & general course info will live - https://uiuc-ischool-dataviz.github.io/spring2020/ 

 * Slack: the best place to ask questions - https://is590dv-spring2020.slack.com/

---

## Reminder - Python Library List by Week

See: https://uiuc-ischool-dataviz.github.io/spring2020/week01/test_imports_week01.ipynb

**There is an addition!**

notes:
this will occasionally be updated, so be sure to check it out frequently!

---

## Weekly Viz Report

And the winner is...

notes:
run the random number generator!

---

## Today's Main Topics

 * Colors - what are they really?
 * Color mapping - mapping data to colors
 * Visual Encoding in general
 * More on data transformations (Pandas)

---

## Last week

<img src="images/data_viz_diagram_week2.png">

notes:
last week we covered the data management and practical programming aspects of data viz

---

## Today

<img src="images/data_viz_diagram_week3.png">

notes:
this week we will talk about how we can encode information about our data into visual ques

we'll focus mostly on color for this lecture but we'll briefly touch on a few other things.

---

<br />
<br />
<br />

# TOPIC 1: What is color?

---

## How Do Colors Work?

Rods (low-light) and cones (color) mediate vision. Humans have about 20 times
as many rods (120 million) as cones (6 million).

Cones see in the colors red, green and blue.

<img src="images/rodsAndConesDiagram.png" height="400"/>

notes: so here is a little slice of you inner eye and you can see the rods and cones that are
responsible for seeing gray-ish (low light) and in color (cones)

---

## How Do Colors Work?

Rods (low-light) and cones (color) mediate vision. Humans have about 20 times
as many rods (120 million) as cones (6 million).

Cones see in the colors red, green and blue.

<img src="images/rodsAndConesPhoto.png" height="400"/>

notes: here is that image again with an actual bit of the eye shown - the back of the
eye is where the optic nerve is & the front is where the choroid is

---

## Color Matching Function

The R,G, & B cones have different levels of responsiveness to different wavelenghts of light.

Below shows how responsive each type of cone is to a specific wavelength of light.

<img src = "images/cmf.png" height=400>

notes: here, you can think of this as how responsive your eye's cones are to different wavelengths.
You can see that your R cone is a lot more sensitive then there rest, especially at high wavelengths.

---

## Color Matching Function

The R,G, & B cones have different levels of responsiveness to different wavelenghts of light.

Below shows how responsive each type of cone is to a specific wavelength of light.

<img src = "images/cmf_ann.png" height=400>

notes: here, you can think of this as how responsive your eye's cones are to different wavelengths.
You can see that your R cone is a lot more sensitive then there rest, especially at high wavelengths.

---

## Color Matching Function

The R,G, & B cones have different levels of responsiveness to different wavelenghts of light.

Below shows how responsive each type of cone is to a specific wavelength of light.

<img src = "images/cmf_ann.png" height=300>

[Jupyter Notebook of Color Fundamentals](https://uiuc-ischool-dataviz.github.io/spring2019online/nbv.html?notebook_name=%2Fspring2019online%2Fweek05%2Fcolor_fundamentals.ipynb)

notes: there is a lot more of this with links to research in this jupyter notebook

---

## "Naming" Colors

<img src="images/hereIsAColor_nohexnohsvhorgb.png" height="600"/>

notes: so, we talk about how colors are named in different systems, and we'll cover the most basic here

---

## "Naming" Colors

<img src="images/hereIsAColor_nohexnohsv_a.png" height="600"/>

notes: since we have RGB rods and cones, we might think the most natural way to represent this is with RGB colors

This color wheel doesn't give an accurate depiction of all the colors in RGB space
(since the space is actually 3d), but it is often
what you'll see out in the real world, and its pretty easy to see where our example color lies.

---

## "Naming" Colors

<img src="images/hereIsAColor_nohex_a.png" height="600"/>

notes: another representation is Hue, Saturation, and Value

This depiction of HSV is in 3D here, and while its easier to visualize how colors change in the space, its
also hard to accurately mark where our specific one is.

---

## "Naming" Colors

<img src="images/hereIsAColor_allAnn.png" height="600"/>

notes: here is another example - you'll see these codes a lot of you do html programming, but its another way to
specify colors with HEX numbers.  You'll note our color isn't listed here, but in a longer table it would be.

Hexadecimal only shows 16 million colors, RGB as uncompressed floats can theoretically represent quite a bit more (but there's a limitation of what monitors can display)

R = 2^8
G = 2^8
B = 2^8

RGB = 2^24 = 16 million

hexadecimal = 16^6 = 16 million

---

## "Naming" Colors: R,G,B Mapping

<img src="images/mandrillRGB.gif" width="600"/>

notes:
the mandrill image was an early color standardization image established by the Dept of Defense

Here we split it into its R, G, & B components

---

## "Naming" Colors: R,G,B Mapping - Its limitations

<table><tr>
<td><img src="images/sRGB.gif" width="300"/></br>sRGB - graphics RGB</td>
<td><img src="images/CIELAB.gif" width="300"/></br>CIELAB - human RGB perception</td>
</tr></table>

notes:
this unified space of colors that works on most displays and printers is NOT the full range of human perception.

---

## "Naming" Colors: HSV

### HSV Wheel

https://commons.wikimedia.org/wiki/File:HSV_color_solid_cylinder.png

<img src="images/HSVcylinder.png" width="500"/>

notes:
you can see that saturation and value are linear axes while hue is cyclical.


---

## "Naming" Colors: HSV

<img src="images/mandrillHSV.gif" width="500"/>
(Cycle is though (1) H to change color, (2) S to change to grayscale, (3) V black to white)

notes:
This video scans through different hues, which are the part of the rainbow you want

Then different saturations, which is how vibrant or gray the colors are

Then different values, which is how bright or dark the colors are.

Allow to run first and then comment.

---

## "Naming" Colors: HSV

<img src="https://miro.medium.com/max/964/1*B2d44wTBqfygLEZ8ZTJXzg.png">

notes:
You might have actually played around with this system before if you've ever used a "color" picker app.

Here we see we have picked a "H" for Hue as red

We choose 50% saturation - i.e. how much of the color is in there where minimum is none of the color (gray)

We also choose 50% "L" which is sometimes called "V" for Luminiance which controls white-to-black

And here is one more channel = A for opacity.  Note that "A" sort of overlaps with both Saturation and Luminance so its usually not used to encode anything if we are using the others.

---

## "Naming" Colors: Beyond HTML HEX - Specific Names

<table><tr>
<td><img src="images/htmlColors.png" width="350"/></br>HTML</td>
<td><img src="images/matplotlibColors.png" width="350"/></br>matplotlib</td>
</tr></table>

notes:
It's worth noting that "color words" are not consistent across languages or cultures. Color is a product of culture.

---

## "Naming" Colors: Summary

 * Color spaces 
   * HSV (Hue, saturation, value)
   * [CIELAB](https://en.wikipedia.org/wiki/CIELAB_color_space)
   * sRGB, Adobe sRGB
 * RGB triplets, sometimes compressed into hexadecimel ("#00FFAA", etc)
 * List of colors by name
   * [Web](https://www.w3schools.com/colors/colors_names.asp)
   * [matplotlib](https://matplotlib.org/2.0.2/examples/color/named_colors.html)

note: 
coding environments will often provide "named" colors if you're more interested in simplicity than flexible design
 
HSV is typically a color space used by color designers.

sRGB "standard RGB" is a color space that was standardized to unify different monitors and printers. 

CIELAB is the color space that covers the average of human vision.

---

## Importance of Color

Which image has the red dot?

<!-- .slide: class="two-floating-elements" -->

<div class="left">
  <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/colour_P.gif">
</div>

<div class="right">
 <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/colour_A.gif">
</div>

---

## Importance of Color

Which image has the red dot?

<!-- .slide: class="two-floating-elements" -->

<div class="left">
  <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/shape_A.gif">
</div>

<div class="right">
 <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/shape_P.gif">
</div>

---

## Importance of Color

Which image has the red dot?

<!-- .slide: class="two-floating-elements" -->

<div class="left">
  <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/conjoin_A.gif">
</div>

<div class="right">
 <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/conjoin_P.gif">
</div>


---

## Importance of Color

[https://www.csc2.ncsu.edu/faculty/healey/PP/#jscript_search](https://www.csc2.ncsu.edu/faculty/healey/PP/#jscript_search)

Color makes use of our "preattentive" visual cortex processing power -- we are able to detect color *before* our attention focuses.

---

<br />
<br />
<br />

# TOPIC 2: Color Maps


---

## Color maps = Visual Encoding

Color maps encode a data attribute as a color.


---

## Color maps = Visual Encoding

Color maps encode a data attribute as a color.

<img src="images/pbn_pallet_long.png" width="600"/>

<table><tr>
<td><img src="images/pbn_outline.png" width="400"</td>
<td><img src="https://wallpaperplay.com/walls/full/b/d/1/58065.jpg" width="400"/></td>
</tr></table>

notes:
you can think of it like a paint by numbers

Here I give you outlines of sections of the page that have data values, here the numbers 1-13 and I assign them a "palette" of colors.

---

## Color maps = Visual Encoding

Color maps encode a data attribute as a color.

<img src="images/pbn_pallet_long.png" width="600"/>

<table><tr>
<td><img src="images/pbn_outline.png" width="400"/></td>
<td><img src="images/pbn_filled.png" width="400"/></td>
</tr></table>

notes:
Then I "paint" these colors on to make an image from my data

---

## Color maps = Visual Encoding

Color maps encode a data attribute as a color.

<table><tr>
<td>Colormap</br><img src="images/pbn_filled.png" width="400"/></td>
<td>Photo</br><img src="images/lobsterCorgi_orig.png" width="360"/></td>
</tr></table>

notes:
Here I cheated a little bit and used a photo to generate my paint by numbers, so I get something back that looks like its photo

But note that these images are generated in very different ways

The colormap one was generated by a list of color values and instructions

The photo is generated by RGB color combinations at every pixel

---

## Color Palettes

<img src="https://www.personal.psu.edu/cab38/ColorSch/S12-fullstructureClean.gif">

Brewer, 1999

notes:
different kinds of color palettes can be used to describe different types of data

Here is a nice way of mapping out our options.  For example, binary (T/F or Y/N) is pretty easy to encode with 2 colors or luminance.

If we have 3 categories, we can choose different hues for qualatative data.

If we have sequential data, like height maps we can choose differences in Hues or luminance.

When we start combining them though, it can get a little more confusing.

---

## Color Palettes

 * Resources:
  * [colorbrewer](http://colorbrewer2.org)
  * [palettable](www.palettable.io) (package)

notes:
there are a million websites that allow you to create color palettes

---

## Ordered Colormaps

<img src="https://lh3.googleusercontent.com/proxy/Mwkhi008aSx6rEdl2_YqW_yCPvsvO_5tI1taFMN8F7Fwn-LCUR5Zdkg6C5HpgoykG9WPA9Bwz31_sYWs5Ft-YsA-vG_uZWE3YirNE94z6tg">

Historically, rainbows have been very popular.

notes:
which colors jump out at your the most?

---

## Ordered Colormaps

<img src="https://serialmentor.com/dataviz/pitfalls_of_color_use_files/figure-html/rainbow-desaturated-1.png">

Historically, rainbows have been very popular, but they can be misleading.

notes:
Here is that same colormap converted to gray scale, and our intuition is true - our eyes are drawn to the luminacne values here, not only the hues

---

## Ordered Colormaps

<img src="https://1.bp.blogspot.com/-GlAFnAA8cio/XVWpa0KH74I/AAAAAAAAEeg/nK1qDzNGhYYCjaggKCLiNY-J16IzpSunwCLcBGAs/s1600/Screenshot%2B2019-08-15%2Bat%2B9.41.44%2BAM.png">

Historically, rainbows have been very popular, but they can be misleading.

"Fixes" to the rainbow colormap are only so-so.

notes:
even if we try to make a perceptually uniform colormap, the results are underwhelming -- the "better" rainbow colormap looks a little muted and drab

---

## Ordered: Sequential Colormaps

![](images/blues_discrete.png)

![](images/blues_continuous.png)

notes:
one thing we can due is choose a hue and change the saturation or luminance -- here luminance

these are also known as monochromatic and are a subset of ordered colormaps

Here, the hue doesn't change, but the value (luminance) and the saturation do

---

## Diverging Colormaps

![](images/spectral_discrete.png)

![](images/spectral_continuous.png)

notes:
this shows you that different colors in the rainbow have different perceived brightness.

The outsides of this color map get darker while the center is brighter.

---

## Ordered Colormaps

Combinations of color can pick out different features at different scales.

<!-- .slide: class="two-floating-elements" -->

<div class="left">

<img src="images/rainbow_highlight.png" width="400px">

</div>

<div class="right">

<img src="images/diverge_highlight.png" width="400px">

</div>

notes:
The differnet colormaps pick out changes at different scales.  The colormap with more hues heighlights the finer details of this simulation, while the colormap with only 2 hues shows off the larger scale structure.

---

## Qualitative Colormaps

![](images/set1_discrete.png)

![](images/set1_continuous.png)

notes:
The blended areas of the continuous map here are kind of gross looking. This kind of random color map is best for categorical data that is NOT continuous.

---

## Color Meaning

<!--<img src="images/blackBodyColor2.png" width="600"/>-->
![](images/blackbodyColor.png)

notes:
Which end of this is hot and which end is cold? What do red and blue mean?

red in the USA is bravery, but red in China is revolution

green in the western world is Christmas, but green in the eastern world is Islam

You're not always picking colors relative to each other, but relative to culture as well.

---

## Color Meaning

<img src="images/skintones.png" width="600"/>

notes:
Human skin color is a particularly SENSITIVE area of color psychology. Western culture often treats dark colors as "mysterious" or "evil" and this is largely rooted in a history of racial bias.

---

## Just for fun: It's full of colors

https://commons.wikimedia.org/wiki/File:16777216colors.png

<img src="images/16millionColors.png" width="500"/>

notes:
This grid is one way to show all the 16 million colors. They kind of get blurred out when looking at the image in this size, but if you zoom in at the link provided, you can see every pixel from red to green to blue, and from black to white.

---

## Pink: Is it a color?

Or, for that matter, where is brown or cyan in the spectrum?

<img src="images/spectrum.jpg" width="600"/>

https://gizmodo.com/if-the-color-pink-doesnt-scientifically-exist-why-can-1464266788

notes:
just a point of interest, what wavelength would you say magenta (or purple) is?

---

## Palette Mapping

![](images/set1_discrete.png)

Assign each value to a specific color or element.

---

## Palette Mapping

<img src="images/colorByNumber.gif" width="500"/>

---

## Palette Mapping

<img src="images/colorByNumberDone.png" width="500"/>

---

## Color Mapping: Normalizing Our Data

$f(v) \rightarrow (R, G, B)$

We can also re-map:

$f(v') \rightarrow (R, G, B)$

$v' = f(v)$

For instance, with logs or squares.

notes:
We can fit our continuous distribution linearly to a color map - so a low data value is at the beginning of the color map, a high value is at the top, and a middle value is halfway up the map.

Or we can remap it with exponents, or other mathematical operations.

---

## Color Mapping: Linear Normalization of Data

We map from a range of values to (0, 1):

$ v' = (v - v_0)/(v_1 - v_0) $

notes:
in order to get the data values to line up with the color bar - which goes from 0 to 1 - we have to transform our data into a range of 0 to 1. This can be as easy as dividing all value by the largest value, or we can do fancier things.

---

## Color Mapping: RGB Components of Some Colormaps


---

## Color Mapping: RGB Components of Some Colormaps

<!-- .slide: data-background-image="images/gist_stern_colors.png" data-background-size="auto 65%" -->

---

## Color Mapping: RGB Components of Some Colormaps

<!-- .slide: data-background-image="images/gray_colors.png" data-background-size="auto 65%" -->

---

## Color Mapping: RGB Components of Some Colormaps

<!-- .slide: data-background-image="images/jet_colors.png" data-background-size="auto 65%" -->

---

## Color Mapping: RGB Components of Some Colormaps

<!-- .slide: data-background-image="images/magma_colors.png" data-background-size="auto 65%" -->

---

## Color Blindness

<img src="images/colorBlind.png" width="800"/>

notes:
these are not the only types of color blindness, just the types where one of the three types of cone are missing. Sometimes that third cone is just "anomalous", and sometimes more than one cone is missing, but it's much rarer.

You can see that designing for a color blind person can be difficult if you put all the information into one cone. You catch a wider audience by using the colors between the cones, like yellow, cyan, and magenta.

protanopia = no red
deuteranopia = no green
trianopia = no blue

---

## Color Blindness

http://enchroma.com/test/instructions/

---

<br />
<br />
<br />

# TOPIC 3: Other methods of visual encoding


---

## Other methods of visual encoding

<table><tr>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_size.gif"/></br>Size</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_den.gif"/></br>Density</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_curve.gif"/></br>Curvature</td>
</tr></table>

Check out [sc2.ncsu.edu/faculty/healey/PP](sc2.ncsu.edu/faculty/healey/PP) for more examples and research.

---

## Other methods of visual encoding

Motion is another channel, but is *very* attention-grabbing.

<table><tr>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_flick.gif"/></br>Flicker</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_vel.gif"/></br>Velocity</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_dir.gif"/></br>Direction</td>
</tr></table>

Check out [sc2.ncsu.edu/faculty/healey/PP](sc2.ncsu.edu/faculty/healey/PP) for more examples and research.

---

## Colormaps: Loading Data

Colormaps in Python - with the Michigan data and the scan data, we'll evaluate:

 * How to choose a colormap
 * What are some good "bounds" for that colormap
 * How do we set our color normalizations and transformations?

---

# To Python!



