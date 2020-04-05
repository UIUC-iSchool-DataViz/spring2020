%% md

Starting from last week, we'll continue on with last week's activities.  Just a few reminders!

<!-- I am an HTML/Markdown comment -->


%% py
# I can do stuff in Python using the `%% py` 
import numpy as np

# make a random array:
myPythonArray = np.random.random(100)
myPythonArray

%% md

# Linking data in Javascript with vega-lite

Let's get a quick reminder of some Javascript syntax:

```
var myString = "Hello there!";

var myArray = [1, 2, 3, 4, 5];

var my2dArray = [ [1,2], [3,4], [5, 6] ];

var myObject = {'hello': 1, 'how': 2,
                'are': {'you': 'me'}
};

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

%% md

Recall that to do things with Javascript, we had to make a static HTML element to modify with Javascript:

<div id="myDiv">I am an HTML div.</div>  

Now, let's use some JavaScript to change this `myDiv` element using JavaScript: note this won't run until you do `shift+enter`!

%% js
document.getElementById("myDiv").innerText = "I am so pretty in pink!";
document.getElementById("myDiv").style.color = 'magenta';


%% md

We have to make sure we use `%% fetch` to grab the  `vega/vega-lite` package.  To make use of these functions, we need to `fetch` them from a repository online.  We can check out one useful location for such packages, [the jsdelivr website](https://www.jsdelivr.com) (we can also specifically look for vega stuff with: `https://www.jsdelivr.com/?query=author%3A%20vega`).

Here is the code in a `%% fetch` command:
```
js: https://cdn.jsdelivr.net/npm/vega
js: https://cdn.jsdelivr.net/npm/vega-lite
js: https://cdn.jsdelivr.net/npm/vega-embed
```

Note: this has to do with the asynchronous nature of Javascript. 

%% fetch
js: https://cdn.jsdelivr.net/npm/vega
js: https://cdn.jsdelivr.net/npm/vega-lite
js: https://cdn.jsdelivr.net/npm/vega-embed

%% md

Let's go back to making some visualizations using the police killings we used last week using [examples with vega-lite](https://vega.github.io/vega-lite/examples/).

We are using one of the [FiveThirtyEight](https://fivethirtyeight.com/) datasets about [police killings in the US](https://github.com/fivethirtyeight/data/tree/master/police-killings).

Let's start with a [calculation and transformation using vega-lite](https://vega.github.io/vega-lite/docs/calculate.html) and types of [aggregation in vega-lite](https://vega.github.io/vega-lite/docs/aggregate.html).  We'll plot a histogram of men and women who are killed by police.  We start with creating a new div element like we did last time and using Javascript to update this div.

<div id='firstHist'></div>

%% js
// Recall: I am a comment!

var myHist1 = 
{
  data: {"url": "https://raw.githubusercontent.com/fivethirtyeight/data/master/police-killings/police_killings.csv"
  },
  mark: "bar",
  height: "300",
  width: "600",
  encoding: {
    "x": {"field": "gender", "type": "nominal"},
    // NOTE: this won't work because "sum" assumes numerical data
    //"y": {"aggregate": "sum", "field": "gender", "type": "nominal"} 
    "y": {"aggregate": "count", "field": "gender", "type": "nominal"}
  }
}

var v = vegaEmbed('#firstHist', myHist1)

%% md

What if we want to do this as a percentage instead?  We can do some [more complex data operations](https://vega.github.io/vega-lite/examples/window_percent_of_total.html) using the [window](https://vega.github.io/vega-lite/docs/window.html) and [aggregation](https://vega.github.io/vega-lite/docs/aggregate.html) operations to make this happen.  This can take a bit of trial-and-error to get just right.

%% md 

<div id='secondHist'></div>

%% js

var myHist2 = 
{
  description: "Percentages of Gender in Dataset.",
  data: {"url": "https://raw.githubusercontent.com/fivethirtyeight/data/master/police-killings/police_killings.csv"
  },
  height:"300",
  width:"600",
  "transform": [
    { // think of aggregations much like panda's group bys
      "aggregate": [{"op": "count", "as": "genders"}], // we are creating a new count in each gender 
      "groupby": ["gender"],
    },
    {
     "window":[{ // now we'll calculate the total number of entries in each gender bin
          "op": "sum", // add up the numbers of each gender
          "field": "genders",
          "as":"Total"
          }], 
          "frame":[null,null] // see: https://vega.github.io/vega-lite/docs/window.html
          // basically: null,null means include *all* data
    },
    
   {
    "calculate": "datum.genders/datum.Total*100",
    //"calculate": "datum.genders/sum(datum.genders)",
    "as": "PercentOfTotal"
  }],
  "mark": "bar",
  "encoding": {
    "x": {"field": "gender", "type": "nominal"},
    "y": {
      "field": "PercentOfTotal",
      "type": "quantitative",
      "axis": {
        "title": "% of total"
      }
    }
  }
}


var v = vegaEmbed('#secondHist', myHist2)

%% md

Let's try another grouping, by the `raceethnicity` entry:

<div id='thirdHist'></div>

%% js

var myHist3 = 
{
  description: "Percentages of Race in Dataset.",
  data: {"url": "https://raw.githubusercontent.com/fivethirtyeight/data/master/police-killings/police_killings.csv"
  },
  height:"300",
  width:"600",
  "transform": [
    { // think of aggregations much like panda's group bys
      "aggregate": [{"op": "count", "as": "races"}], // we are creating a new count in each gender 
      "groupby": ["raceethnicity"],
    },
    {
     "window":[{ // now we'll calculate the total number of entries in each gender bin
          "op": "sum",
          "field": "races",
          "as":"Total"
          }], 
          "frame":[null,null]
    },
    
   {
    "calculate": "datum.races/datum.Total*100",
    "as": "PercentOfTotal"
  }],
  "mark": "bar",
  "encoding": {
    "x": {"field": "raceethnicity", "type": "nominal", "title":"Race-Ethnicity"},
    "y": {
      "field": "PercentOfTotal",
      "type": "quantitative",
      "axis": {
        "title": "% of total"
      }
    }
  }
}

var v = vegaEmbed('#thirdHist', myHist3)

%% md

Let's combine these fields and make a stacked bar plot of `raceethnicity` by `gender`:

<div id='stackedBar1'></div>

%% js

var myStack1 = 
{
  description: "Percentages of Race in Dataset, colored by gender.",
  data: {"url": "https://raw.githubusercontent.com/fivethirtyeight/data/master/police-killings/police_killings.csv"
  },
  height:"300",
  width:"600",
  "transform": [
    { // think of aggregations much like panda's group bys
      "aggregate": [{"op": "count", "as": "races"}], // we are creating a new count in each gender 
      "groupby": ["raceethnicity", "gender"],
    },
    {
     "window":[{ // now we'll calculate the total number of entries in each gender bin
          "op": "sum",
          "field": "races",
          "as":"Total"
          }], 
          "frame":[null,null]
    },
    
   {
    "calculate": "datum.races/datum.Total*100",
    "as": "PercentOfTotal"
  }],
  "mark": "bar",
  "encoding": {
    "x": {"field": "raceethnicity", "type": "nominal", "title":"Race-Ethnicity"},
    "y": {
      "field": "PercentOfTotal",
      "type": "quantitative",
      "axis": {
        "title": "% of total"
      }
    },
    "color": {"field":"gender", "type":"nominal"}

  }
}

var v = vegaEmbed('#stackedBar1', myStack1)

%% md

Looking ahead, we will want to plot the distribution of `raceethnicity` and `age` and link these two visualizations.  Selections are not always supported with binning and aggregation (its in development), so we can use the [rect](https://vega.github.io/vega-lite/docs/rect.html) vega-lite plot to help us out.

<div id='rectPlot'></div>

%% js

var myRect = 
{   
    data: {"url": "https://raw.githubusercontent.com/fivethirtyeight/data/master/police-killings/police_killings.csv"},
    description: "Gender and Race/Ethnicity.",
    height:"300",
    width:"300",
    // here we don't need any fancy transforms just yet -- we are going to just bin the data!
    "mark": "rect",
    "encoding": {
        // can also show age. withrect plot
        //"x":{"field":"age", "type":"ordinal"}, // binned: true does not work, qualitative does not work => see vega-lite limitations
        "x":{"field":"gender", "type":"ordinal"}, 
        "y":{"field":"raceethnicity", "type":"nominal"},
        "color": {
                    "aggregate": "count", "type": "quantitative", 
                    "scale":{"type":"log"} // toggle on and off to see how plotting changes
                        // scales info: https://vega.github.io/vega-lite/docs/scale.html
                }
    } // end encoding
}

var v = vegaEmbed('#rectPlot', myRect)

%% md

Now, let's try another binning plot: a distribution of ages in this dataset.  We can do this "in line" by specifying that our x-axis will be binned using [vega-lite's binning capabilities](https://vega.github.io/vega-lite/docs/bin.html).

<div id='agePlot1'></div>

%% js

var myAge1 = 
{
  description: "Distribution of ages.",
  data: {"url": "https://raw.githubusercontent.com/fivethirtyeight/data/master/police-killings/police_killings.csv"
  },
  height:"300",
  width:"600",
  // here we don't need any fancy transforms just yet -- we are going to just bin the data!
  "mark": "bar",
  "encoding": {
      // here we use the key-word "bin" to specify we are doing a histogram
      "x": {"bin": true, "field": "age", "type": "nominal", "title":"Age"},
      "y": {
        "aggregate":"count", // we are specifiying we are aggregating here and y will be this histogram
        "type": "quantitative",
        "axis": {"title": "Histogram"}
    }
  }
}

var v = vegaEmbed('#agePlot1', myAge1)

%% md
Let's put these two plots side by side using [vega-lite's concatenation capabilities](https://vega.github.io/vega-lite/docs/concat.html):

<div id='sidebyside'></div>

%% js

var mySidebySide1 = 
{   // NOTE: we can actually move the data out here!
    data: {"url": "https://raw.githubusercontent.com/fivethirtyeight/data/master/police-killings/police_killings.csv"},

    "hconcat": [
        {// Plot 1: raceethnicity & gender plot
            description: "Gender and Race/Ethnicity.",
            height:"300",
            width:"300",
            "mark": "rect",
            "encoding": {
                // can also show age. withrect plot
                //"x":{"field":"age", "type":"ordinal"}, // binned: true does not work, qualitative does not work => see vega-lite limitations
                "x":{"field":"gender", "type":"ordinal"}, 
                "y":{"field":"raceethnicity", "type":"nominal"},
                "color": {
                    "aggregate": "count", "type": "quantitative", 
                    "scale":{"type":"log"} // toggle on and off to see how plotting changes
                        // scales info: https://vega.github.io/vega-lite/docs/scale.html
                }
            } // end encoding
        }, // end plot 1
        { // Plot 2: the age distribution plot
            description: "Distribution of ages.",
            //data: {"url": "https://raw.githubusercontent.com/fivethirtyeight/data/master/police-killings/police_killings.csv"},
            height:"300",
            width:"300",
            // here we don't need any fancy transforms just yet -- we are going to just bin the data!
            "mark": "bar",
            "encoding": {
                // here we use the key-word "bin" to specify we are doing a histogram
                "x": {"bin": true, "field": "age", "type": "nominal", "title":"Age"},
                "y": {
                    "aggregate":"count", // we are specifiying we are aggregating here and y will be this histogram
                    "type": "quantitative",
                    "axis": {"title": "Histogram"}
                } // end y
            } // end encoding
        } // end plot 2
    ] // end list of plots to concatinate
} // end specification

var v = vegaEmbed('#sidebyside', mySidebySide1)

%% md

Another thing we might want to do is make linked views.  We can do this with [vega-lite's selection properties](https://vega.github.io/vega-lite/docs/selection.html).  There are some caveats, namely that not all plots will work -- in particular [binned and aggreated data has limited selections](https://vega.github.io/vega-lite/docs/project.html#current-limitations).

We can hack this a bit to show the `gender` and `raceethnicity` variables in a [rect](https://vega.github.io/vega-lite/docs/rect.html) plot.

<div id="connectedSidebySide"></div>

%% js

var myConnSidebySide1 = 
{
    data: {"url": "https://raw.githubusercontent.com/fivethirtyeight/data/master/police-killings/police_killings.csv"}, // NOTE: we are using the same data source, so I have moved it up here!

    "hconcat": [
         { // Plot 1: raceethnicity & gender
            "selection": {"brush": {"type": "interval"}},
            //"selection": {"pts": {"type": "multi"}}, // this is not supported!
            description: "Gender and Race/Ethnicity.",
            height:"300",
            width:"300",
            // here we don't need any fancy transforms just yet -- we are going to just bin the data!
            "mark": "rect",
            "encoding": {
                // can also show age. withrect plot
                //"x":{"field":"age", "type":"ordinal"}, // binned: true does not work, qualitative does not work => see vega-lite limitations
                "x":{"field":"gender", "type":"ordinal"}, 
                "y":{"field":"raceethnicity", "type":"nominal"},
                "color": {
                    "condition": {
                        "selection": "brush",
                        "aggregate": "count", "type": "quantitative", 
                        "scale":{"type":"log"} // toggle on and off to see how plotting changes
                        // scales info: https://vega.github.io/vega-lite/docs/scale.html
                    },
                    "value": "grey"
                }
            } // end encoding
        }, // end plot 1
        {// Plot 2: Age distribution plot
            description: "Age distribution.",
            height:"300",
            width:"300",
            "transform": [{"filter":{"selection":"brush"}}], // only use selected data for plot
            "mark": "bar",
            "encoding": {
                "x": {"bin": true, "field": "age", "type": "nominal", "title":"Age"},
                "y": {
                    "aggregate":"count", // we are specifiying we are aggregating here and y will be this histogram
                    "type": "quantitative",
                    "axis": {"title": "Distribution"}
                }//, // end y
                //"color": {"field":"gender", "type":"nominal"} // can also include this if we wanna
            } // end encoding 
        } // end plot 2

    ] // end list of plots to concatinate
} // end specification

var v = vegaEmbed('#connectedSidebySide', myConnSidebySide1)

%% md

Cool stuff with maps & buttons [links on GitHub Issues](https://github.com/vega/vega/issues/1094).