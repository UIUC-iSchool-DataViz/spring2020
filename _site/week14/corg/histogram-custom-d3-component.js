// node-module libraries 
const React = require('react');
const D3Component = require('idyll-d3-component');
const d3 = require('d3');

// setting the base size of our svg plot
//const size = 600;

//COPIED:
var margin = {top: 20, right: 20, bottom: 70, left: 40},
    width = 800 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// to pring out things:
//console.log(margin);



class HistogramCustomD3Component extends D3Component { // change name

    // needed to first draw the svggraphics
    initialize(node, props) {

	// Parse the date / time
	var parseDate = d3.isoParse

	var x = d3.scaleBand().rangeRound([0, width], .05).padding(0.1);

	var y = d3.scaleLinear().range([height, 0]);

	var xAxis = d3.axisBottom()
	    .scale(x)
	//.tickFormat(d3.timeFormat("%b"));
	    //.ticks(20) // updated
	    .tickFormat(d3.timeFormat("%Y")); // updated

	
	var yAxis = d3.axisLeft()
	    .scale(y)
	    .ticks(10);

	
	// setting the definition of our svg space -- this is the attachement to the node done for us!
	const svg = this.svg = d3.select(node).append('svg') //; // take this out!
	      .attr("width", width + margin.left + margin.right)
	      .attr("height", height + margin.top + margin.bottom)
	      .append("g")
	      .attr("transform",
		    "translate(" + margin.left + "," + margin.top + ")");

	// get the data -> we can find the link by googling!
	//d3.csv("https://raw.githubusercontent.com/UIUC-iSchool-DataViz/spring2020/master/week14/bar-data.csv", function(error, data) {
	d3.csv("https://raw.githubusercontent.com/UIUC-iSchool-DataViz/spring2020/master/week12/corg/corgs_per_country_over_time_columns_2020.csv", function(error, data) {

	    // how do we see things in our data?
	    console.log(Object.keys(data)); // what are the attributes in this data set?
	    console.log(data.columns);
	    console.log(data[0]);
	    //console.log(data[0]['date']); // old data
	    console.log(data[0]['Years']);

	    // NOT THIS: formatting
	    //var dataOld = { ...data };
	    //console.log(dataOld);
	    //var data = Array.apply(null, Array(5)).map(function () {});

	    // grab length of entries
	    var lengthEntries = 0;
	    data.forEach(function(d) {
		lengthEntries += 1;
	    });

	    // empty array -- make it!
	    data['date'] = Array.apply(null, Array(lengthEntries)).map(function () {});
	    data['value'] = Array.apply(null, Array(lengthEntries)).map(function () {});
	    //console.log(data);

	    var countryName = 'United States';
	    
	    data.forEach(function(d) {
		d.date = parseDate(d['Years']);
		d.value = d[countryName];
		//console.log(d['Years']);
		//console.log(d.date);
		console.log(d.value);
		//d.value = +d.value;
	    });

	    //console.log(data['date']);
	    //console.log(data.value);
	    
	    x.domain(data.map(function(d) { return d.date; }));
	    //y.domain([0, d3.max(data, function(d) { return d.value; })]);
	    //console.log(d3.max(data, function(d) { return d.value; })]));
	    y.domain([0,1000]);
	    //////////x.domain([parseDate('1940'), parseDate('2020')]);
	    
	    svg.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(0," + height + ")")
		.call(xAxis.ticks(null).tickSize(0))
		.selectAll("text")
		//.style("text-anchor", "middle")
	        .style("text-anchor", "end") // updated
	        .style("font-size", "6px") // updated
		.attr("transform", "rotate(-65)"); // updated
	    
	    svg.append("g")
		.attr("class", "y axis")
		.call(yAxis.ticks(null).tickSize(0))
		.append("text")
		.attr("y", 6)
		.style("text-anchor", "middle")
		.text("Value");
	    
	    svg.selectAll("bar")
		.data(data)
		.enter().append("rect")
	        // coloring --> take off!
	    //.style("fill", function(d){ return d.value < d.target ? '#EF5F67': '#3FC974'})
	        .style("fill", 'EF5F67')
		.attr("x", function(d) { return x(d.date); })
		.attr("width", x.bandwidth())
		.attr("y", function(d) { return y(d.value); })
		.attr("height", function(d) { return height - y(d.value); });

	    // title text - http://www.d3noob.org/2013/01/adding-title-to-your-d3js-graph.html
	    svg.append("text")
		.attr("x", (width / 2))             
		.attr("y", 10 - (margin.top / 2))
		.attr("text-anchor", "middle")  
		.style("font-size", "16px") 
		.style("text-decoration", "underline")  
		.text(countryName);

	    // taking out stuff:
	    //svg.selectAll("lines")
	//	.data(data)
	//	.enter().append("line")
	//	.style("fill", 'none')
  	//	.attr("x1", function(d) { return x(d.date) + x.bandwidth()+5; })
	//	.attr("x2", function(d) { return x(d.date)-5; })
	//	.attr("y1", function(d) { return y(d.target); })
	//	.attr("y2", function(d) { return y(d.target); })
  	//	.style("stroke-dasharray", [2,2])
  	//	.style("stroke", "#000000")
	//	.style("stroke-width", 2)
	    
	});
	

    }


}

module.exports = HistogramCustomD3Component; // add histogram here
