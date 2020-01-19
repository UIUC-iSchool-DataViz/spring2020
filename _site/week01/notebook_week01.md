Our first notebook on [Iodide](https://iodide.io/) is available below, and also may be accessed online as [iodide notebook 3042](https://alpha.iodide.io/notebooks/3042/)

```
%% md
Hello there!

I can also do things like _italicize_ something, or **bold** something, and I can do things like enumerate lists!

 * for instance
 * and things
 * also this

%% js

var myString = "Hello there!";
var myArray = [1, 2, 3, 4, 5];
var myObject = {'hello': 1, 'how': 2,
                'are': {'you': 'me'}
};
%% js

function sayHello(toWhom) {
    return "Hello! " + toWhom;
}

%% js

var sayingHello = sayHello("Matt");

%% js

var sayingHelloTo = sayHello(myObject);

%% js
var newArray = [];
for ( i = 0; i < 10 ; i++) {
    newArray.push(i + 1);
}
%% js
var myStringSubset = sayingHello.slice(3, 6);
%% md
<h1>This is H1!</h1>
<a href="https://google.com/">google</a>

<div id="myDiv">this is the content</div>
%% js
document.getElementById("myDiv").innerText = "I just changed the content!";
%% css
.user-markdown {
    font-style: italic;
}
%% js
var newArray = [];
for ( i = 0; i < 10 ; i++) {
    if (i%2 == 0) {
        newArray.push(i + 1);
    };
}
%% py
import numpy as np
import matplotlib.pyplot as pyplot
%% py
myPythonArray = np.random.random(100)
%% js
pyodide.pyimport("myPythonArray");
%% fetch
js: https://cdn.jsdelivr.net/npm/vega@5.4.0
js: https://cdn.jsdelivr.net/npm/vega-lite@4.0.0-beta.0
js: https://cdn.jsdelivr.net/npm/vega-embed@4.2.1
%% md
<div id="ourFirstViz">
</div>
%% js
var mySpecification = {
    data: {
        values: [
            {name: "Avengers", count: 8},
            {name: "Annihilation", count: 2},
            {name: "La La Land", count: 1},
            {name: "The Secret", count: 1},
            {name: "Rebel of the Rye", count: 1}
        ]
    },
    mark: "bar",
    encoding: {
        x: {field: "name", type: "ordinal"},
        y: {field: "count", type: "quantitative"}
    }
};
var v = vegaEmbed("#ourFirstViz", mySpecification);
```
