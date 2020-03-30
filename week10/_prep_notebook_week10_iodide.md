---
title: prep_notebook_week11_iodide
---

# Access the most up-to-date version of this notebook online at: [https://alpha.iodide.io/notebooks/4351/](https://alpha.iodide.io/notebooks/4351/)

```
%% md
Hello there!  I am writing things in Markdown, using similar syntax to how you'd do things in a jupyter notebook.

<!-- I can use HTML comment style to make comments here -->

In general, I can use HTML tags: <font color="magenta">For example, I can change font colors!</font>

<!-- I can also use HTML styles to do things like headers -->
<h3>This is a Header.</h3>
<!-- And make links: -->
<a href="https://google.com/">google</a>
<!-- Note that in your report, this will show up w/o the Markdown formatting -->

But you can also do this in markdown like so:
### This is also a Header
[google](https://google.com/)

I can also do things like _italicize_ something, or **bold** something, and I can do things like  lists!

 * for instance
 * and things
 * also this

 I can also make enumerated lists:
  1. My first thing
  1. My 2nd thing
  1. My 3rd thing

Markdown also supports `LaTex` formatting for equations: $x = \frac{5}{3}$, $y = \cos (5)$, $\lambda = 5 \times y$.

You'll note that you get a preview of what you're doing on the right.  You can also click "VIEW AS REPORT" button to see the full page.  Click "EXPLORE" in the top right to get back to this view.
<!-- actually do this & come back -->

<!-- Let's actually get into some coding with Python here!-->

# Python in Iodide

We need to specify the _environment_ as Python before actually being able to use Python.  We do this with in Iodide with a `%% py` as mentioned in the [Iodide IOMD Docs](https://iodide-project.github.io/docs/iomd/):


%% py
# load numpy and pyplot per usual
import numpy as np
import matplotlib.pyplot as plt

# make a random plot:
myPythonArray = np.random.random(100)
myPythonInds = np.arange(100)
plt.figure()
plt.plot(myPythonInds, myPythonArray)
plt.title('Random test data')
plt.show()
# now: hit shift-return: note if you keep doing this, more plots will show up - include the "clear statement" to help with this
#. Now: say we are done with Python and want to be back in Markdown!

%% md
Now, I'm back in Markdown.  Note in your figure that you have access to a lot of useful `widget` type stuff like zoom & pan, and also the ability to save your images.

Also of note is that if you re-run this notebook with this Python cell you will get double figures!  To fix this we would need to make this into its own HTML tag and "wrap" our Python code with some JS.  We'll do a few more Python things now and then just move onto directly plotting with JS and ignoring this oddity for the sake of time.

%% py
# Right now, printing happens to the console by default
"Hi there"

%% md

Python is run via [PyIodide](https://github.com/iodide-project/pyodide) which compiles Python commands into web-assembly (i.e. a basic programming language of webpages).  Note that not all Python libraries are supported -- if we check out the [list of supported packages](https://github.com/iodide-project/pyodide/tree/master/packages) we see that for example, `bqplot` is not supported here (yet), but many analysis tools are like `Pandas` and `SciPy` are.

## Pandas in Iodide

Let's give Pandas a shot!

%% py

import pandas as pd
#df = pd.read_csv('https://uiuc-ischool-dataviz.github.io/spring2020/week01/data/GDP.csv')
# The above will give us errors.  This is because we need to deal with the fact that we are actually dealing with JS and Python is being, essentially, translated to JS for us.

# We can instead use pyiodide to help us do this translation for us:
import pyodide
URL = 'https://uiuc-ischool-dataviz.github.io/spring2020/week01/data/GDP.csv'
df = pd.read_csv(pyodide.open_url(URL))

# This will show the dataframe in the console:
df

# we can also make a quick plot 
df.plot(kind='line',x='DATE',y='GDP',color='red')
plt.show()

%% md
Sweet!  Note that we can also "re-write" our code in Markdown which can be useful if we want to talk about our code in our document:

```#python
import pandas as pd
import pyodide
URL = 'https://uiuc-ischool-dataviz.github.io/spring2020/week01/data/GDP.csv'
df = pd.read_csv(pyodide.open_url(URL))
```

## More about JS

So, we've seen how to use Python to make shareable figures, but what about Javascript?  What's neet about the Iodide engine is that we can communicate between Python and Javascript and pass data between the two.  Before getting into that, it will be worth while to go over some basic Javascript programming.

If you really like Javascript, you can look into learning how to use it in more detail on sites like the [codeacademy JavaScript site](https://www.codecademy.com/learn/introduction-to-javascript).

We'll start with some basics and then get into more fancy stuff with plotting and cross-communication between Python and Javascript.

Code:
```
// This is very important - a comment! Note they are highlighted the same color, but start with a different
//  set of characters

var myString = "Hello there!";

var myArray = [1, 2, 3, 4, 5];

var myObject = {'hello': 1, 'how': 2,
                'are': {'you': 'me'}
};

// Let's try making a function!
function sayHello(toWhom) {
    return "Hello! " + toWhom;
}

var sayingHello = sayHello("Jill");

// In Iodide, the "console printing" is sort of the default, so this works:
sayingHello
```

%% js
// This is very important - a comment! Note they are highlighted the same color, but start with a different
//.  set of characters

// Variables are declared differently than in Python:
var myString = "Hello there!";
// Note the "var" in front, as opposed to a "const" which would be something that doesn't change.
// Also note the ";" at the end of the declaration.

// Arrays are somewhat similar to python, but again called differently:
var myArray = [1, 2, 3, 4, 5];

var my2dArray = [ [1,2], [3,4], [5, 6] ];

// Dictionaries look much the same as in Python as well, but with the JS calling structure:
var myObject = {'hello': 1, 'how': 2,
                'are': {'you': 'me'}
};

// Let's try making a function!
function sayHello(toWhom) {
    return "Hello! " + toWhom;
}

var sayingHello = sayHello("Jill");

// How can we print out this new variable?
// This doesn't work now we expect?
//print(sayingHello);

// In general, we'll have to use JS console:
// console.log(sayingHello);
// In Iodide, the "console printing" is sort of the default, so this works:
sayingHello

%% js
// we can also print out elements from previous JS cells:
my2dArray[1]
%% md

Before getting into Python-JS cross talk, let's look at a few more objects in JS. 
 1. For loops
 1. Conditionals

```
var newArray = [];
for ( i = 0; i < 10 ; i++) {
    if (i%2 == 0) {
        newArray.push(i + 1);
    };
}
```
%% js
var newArray = []; // start with an empty array
for ( i = 0; i < 10 ; i++) { // for loop, here we specify the iteration of i increasing by 1 each time as i++
    if (i%2 == 0) { // if-statement -> look for only even #'s'
        newArray.push(i + 1); // add to this array
    };
}
newArray // show in console
%% md

At this point, you might be asking: How can we get something to print to the report instead of the console?  This is a little bit tricky, because this "Report" webpage is HTML, so we need to have our code in HTML.  To have *variable* text that will change based on variables, we use Javascript -- JS can update HTML "on the fly".  But if we want to print out something from Python, we have to first turn it *into* JavaScript!  So you can see, there is a lot to do here. 

We won't be going into much detail here, but you can check out how to do this [in this post right here](https://stackoverflow.com/questions/56583696/how-to-redirect-render-pyodide-output-in-browser).

## Plotting using vega-lite

Because we will want to make more plots than printing out variables to our reports, let's focus now on making plot's with `vega-lite`.  First, we need to understand a bit about how JS is used to modify static HTML tags, and then use `vega-lite` in JS to modify an HTML tag to add a plot.

Let's break this down bit by bit.  First, let's make a *static* HTML element:

<div id="myDiv">I am some content.</div>  

Now, let's use some JavaScript to change this `myDiv` element using JavaScript: note this won't run until you do `shift+enter`!

%% js
document.getElementById("myDiv").innerText = "I just changed the content!";
document.getElementById("myDiv").style.color = 'magenta';

%% md

Note, this won't run the JS update by default if we hit the "View As Report" button, so we have to make sure we run everything beforehand!

Now that we've done some stuff with changing HTML with JS, let's pass data from Python into JS to do JS things with, we'll start with our simple `myArray` variable:

%% js

myJSArray = pyodide.pyimport("myPythonArray");
myJSInds = pyodide.pyimport("myPythonInds");

myJSArray

%% md

Now that we have this array in a place that JS can use it, we'll import a few functions to make a plot, specifically using the `Vega/Vega-lite` package.  To make use of these functions, we need to `fetch` them from a repository online.  We can check out one useful location for such packages, [the jsdelivr website](https://www.jsdelivr.com) (we can also specifically look for vega stuff with: `https://www.jsdelivr.com/?query=author%3A%20vega`).

Here is the code in a `%% fetch` command:
```
js: https://cdn.jsdelivr.net/npm/vega
js: https://cdn.jsdelivr.net/npm/vega-lite
js: https://cdn.jsdelivr.net/npm/vega-embed
```

%% fetch
js: https://cdn.jsdelivr.net/npm/vega
js: https://cdn.jsdelivr.net/npm/vega-lite
js: https://cdn.jsdelivr.net/npm/vega-embed

%% md

Now, we need to make a HTML `div` element to store our plot in, and we'll use JS to update this `div` element by putting a vega-lite plot in there:
<div id="ourFirstViz">
</div>

Let's make a simple plot.

%% js
// vega lite has a familiar excuction to bqplot in that it is declaritive
// We will see "data", "marks" and "encodings"/scales

// Let's make a plot of how many hours we're spending in PJs over the week:
var mySpecificationFirst = { // we're gonna write a function that "specifies" our plot
    data: { // first, we lay out our data
       values: [
            {day: "Monday", hoursInPjs: 8},
            {day: "Tuesday", hoursInPjs: 10},
            {day: "Wednesday", hoursInPjs: 11.5},
            {day: "Thursday", hoursInPjs: 12},
            {day: "Friday", hoursInPjs: 15},
            {day: "Saturday", hoursInPjs: 20},
            {day: "Sunday", hoursInPjs: 22}
        ]
    },
    mark: "bar", // we want to make a bar plot
    encoding: {
        x: {field: "day", type: "ordinal"}, // this is a categorical data type
        y: {field: "hoursInPjs", type: "quantitative"} // numerical data
    }
};
var v = vegaEmbed("#ourFirstViz", mySpecificationFirst); // embed a vega lite plot

%% js
// Since we made a "toy" plot, we can replace our plot by tagging JS on our div element here again.
// In this case, let's use our data converted from Python:
var mySpecification = {
    data: {
        values: [
            {"x": myJSInds, "y": myJSArray} // replace data with x/y values
        ]
    },
    transform:[{"flatten": ["x", "y"]}], // here we need to get our data into a "vega"-data-formate - see: https://vega.github.io/vega-lite/docs/flatten.html
    mark: {"type": "line", "point": true}, // try w/o "point" first
    encoding: {
        x: {field: "x", type: "quantitative"}, // note: both are numerical data now
        y: {field: "y", type: "quantitative"}
    }
};
var v = vegaEmbed("#ourFirstViz", mySpecification);

%% md

We probably want to change the size of this plot:
<div id="biggerPlot">
</div>

%% js
var mySpecificationBig = {
    data: {
        values: [
            {"x": myJSInds, "y": myJSArray}
        ]
    },
    transform:[{"flatten": ["x", "y"]}],
    width:"600", // specify width and hight
    height:"300",
    mark: {"type": "line", "point": true},
    encoding: {
        x: {field: "x", type: "quantitative"},
        y: {field: "y", type: "quantitative"}
    }
};
var v = vegaEmbed("#biggerPlot", mySpecificationBig);

%% md

Note that vega-lite is nice because we can actually grab data directly off the internets:

<div id="gdpWithVega"> </div>

%% js

var myGDPPlot = {
  data: {"url": "https://uiuc-ischool-dataviz.github.io/spring2020/week01/data/GDP.csv"},
  mark: "line",
  width:"600", // specify width and hight
  height:"300",
  encoding: {
    "x": {"field": "DATE", "type": "temporal"},
    "y": {"field": "GDP", "type": "quantitative"}
  }
}

var v = vegaEmbed('#gdpWithVega', myGDPPlot)
// Note: this also gives you an option to open things up with the Vega editor -> way to mess around with data online

%% md
Let's make our GDP plot a bit more interesting:

<div id='gdpWithVega2'> </div>

%% js
var myGDPPlot2 = {
  data: {"url": "https://uiuc-ischool-dataviz.github.io/spring2020/week01/data/GDP.csv"},
  selection: {
    "brush": {
      "type": "interval"
    }
  },
  mark: {"type": "line", "tooltip":true},
  width:"600", 
  height:"300",
  encoding: {
    "x": {"field": "DATE", "type": "temporal"},
    "y": {"field": "GDP", "type": "quantitative"}, 
    "color": {"value": "red"}
  }
}

var v = vegaEmbed('#gdpWithVega2', myGDPPlot2)

%% js

var myGDPPlot2 = {
  data: {"url": "https://uiuc-ischool-dataviz.github.io/spring2020/week01/data/GDP.csv"},
  selection: {
    "brush": {
      "type": "interval"
    }
  },
  mark: {"type": "line", "tooltip":true},
  width:"600", 
  height:"300",
  encoding: {
    "x": {"field": "DATE", "type": "temporal"},
    "y": {"field": "GDP", "type": "quantitative"}, 
    "color": {"condition": {"selection":"brush"}, "value":"red" }
  }
}

var v = vegaEmbed('#gdpWithVega2', myGDPPlot2)


%% md
We'd probably like to actually select and highlight regions of the graph, but we'll get into more detail about that next week.  For now, we can just see that we can highlight things with interactions!

Right now, let's focus on making a map viz here following some of the examples from [the vega lite docs](https://vega.github.io/vega-lite/examples/geo_text.html).  First, a basic map with `vega-lite`:

<div id="mySimpleMap"></div>

%% js 

var myMapPlot = {
  "width": 800,
  "height": 500,
  "projection": {
    "type": "albersUsa"
  },
  "layer": [
    {
      "data": {
        "url": "https://raw.githubusercontent.com/vega/vega-datasets/master/data/us-10m.json",
        "format": {
          "type": "topojson",
          "feature": "states"
        }
      },
      "mark": {
        "type": "geoshape",
        "fill": "lightgray",
        "stroke": "white"
      }
    },
    {
      "data": {
        "url": "https://raw.githubusercontent.com/vega/vega-datasets/master/data/us-state-capitals.json"
      },
      "encoding": {
        "longitude": {
          "field": "lon",
          "type": "quantitative"
        },
        "latitude": {
          "field": "lat",
          "type": "quantitative"
        }
      },
      "layer": [{
        "mark": {
          "type": "circle",
          "color": "orange"
        }
      }, {
        "mark": {
          "type": "text",
          "dy": -10
        },
        "encoding": {
          "text": {"field": "city", "type": "nominal"}
        }
      }]
    }
  ]
}


var v = vegaEmbed('#mySimpleMap', myMapPlot)

%% md

We can modify this bit of code to point to a new dataset.  In this case, one of the [FiveThirtyEight](https://fivethirtyeight.com/) datasets about [police killings in the US](https://github.com/fivethirtyeight/data/tree/master/police-killings).

<div id='testMap'></div>

%% js

var myMapPlot2 = {
  "width": 800,
  "height": 500,
  "projection": {
    "type": "albersUsa"
  },
  "layer": [
    {
      "data": {
        "url": "https://raw.githubusercontent.com/vega/vega-datasets/master/data/us-10m.json",
        "format": {
          "type": "topojson",
          "feature": "states"
        }
      },
      "mark": {
        "type": "geoshape",
        "fill": "lightgray",
        "stroke": "white"
      }
    },
    {
      "data": { // change our datasource here
        "url": "https://raw.githubusercontent.com/fivethirtyeight/data/master/police-killings/police_killings.csv"
      },
      "encoding": {
        "longitude": {
          "field": "longitude",
          "type": "quantitative"
        },
        "latitude": {
          "field": "latitude",
          "type": "quantitative"
        }
      },
      "layer": [{
        "mark": {
          "type": "circle",
          "color": "orange"
        }
      }, {
        "mark": {
          "type": "text",
          "dy": -10
        },
        "encoding": {
          //"text": {"field": "city", "type": "nominal"}
        "text": {"field": "age", "type": "nominal"} // can change different fields here

        }
      }]
    }
  ]
}

var v = vegaEmbed('#testMap', myMapPlot2)

```