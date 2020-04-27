// importing JS libraries
const React = require('react');
const D3Component = require('idyll-d3-component');
const d3 = require('d3');

var margin = {top: 20, right: 20, bottom: 70, left: 40},
    width = 800 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;



class HistogramCustomD3Component extends D3Component { // creates custom comp.
    // extending D3 class a bit to add our thing
    
    // initializing the drawing 
    initialize(node, props) {

	// Parse the date / time
	var parseDate = d3.isoParse
	
	var x = d3.scaleBand().rangeRound([0, width], .05).padding(0.1);
	
	var y = d3.scaleLinear().range([height, 0]);
	
	var xAxis = d3.axisBottom()
	    .scale(x)
	//.tickFormat(d3.timeFormat("%b"));
	    .tickFormat(d3.timeFormat("%Y"));
	
	var yAxis = d3.axisLeft()
	    .scale(y)
	    .ticks(10);

	// creating a vector drawing and
	//  attaching with JS to an html node
	const svg = this.svg = d3.select(node).append('svg') 
	      .attr("width", width + margin.left + margin.right)
	      .attr("height", height + margin.top + margin.bottom)
	      .append("g")
	      .attr("transform",
		    "translate(" + margin.left + "," + margin.top + ")");

	// linking to the bar-data -> reading in the data
	//d3.csv("https://raw.githubusercontent.com/UIUC-iSchool-DataViz/spring2020/master/week14/bar-data.csv", function(error, data) {
	d3.csv("https://raw.githubusercontent.com/UIUC-iSchool-DataViz/spring2020/master/week12/corg/corgs_per_country_over_time_columns_2020.csv", function(error, data) {

	    // checking out whats in our dataset
	    console.log("Printing out data info");
	    console.log(Object.keys(data));
	    console.log(data.columns);
	    console.log(data[0]);

	    // to our dataset we want to add an array of Years &
	    //  our chosen country
	    var lengthEntries = 0;
	    data.forEach(function(d) {
		lengthEntries += 1;
	    });
	    // make a new entry for "date" and "value"
	    data['date'] = Array.apply(null, Array(lengthEntries)).map(function () {});
	    data['value'] = Array.apply(null, Array(lengthEntries)).map(function () {});
	    
	    // formatting the data
	    data.forEach(function(d) {
		//d.date = parseDate(d.date);
		//d.value = +d.value;
		d.value = d['United States'];
		d.date = parseDate(d['Years']);
	    });

	    // choosing our domain
	    x.domain(data.map(function(d) { return d.date; }));
	    //y.domain([0, d3.max(data, function(d) { return d.value; })]);
	    y.domain([0,1000]);
	    
	    // drawing the x-axis
	    svg.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(0," + height + ")")
		.call(xAxis.ticks(null).tickSize(0))
		.selectAll("text")
		//.style("text-anchor", "middle")
		.style("text-anchor", "end")
	        .style("font-size", "6px")
	        .attr("transform", "rotate(-65)");

	    // drawing the y-axis
	    svg.append("g")
		.attr("class", "y axis")
		.call(yAxis.ticks(null).tickSize(0))
		.append("text")
		.attr("y", 6)
		.style("text-anchor", "middle")
		.text("Value");

	    // drawing the bars
	    svg.selectAll("bar")
		.data(data)
		.enter().append("rect")
		.style("fill", '#EF5F67')
		.attr("x", function(d) { return x(d.date); })
		.attr("width", x.bandwidth())
		.attr("y", function(d) { return y(d.value); })
		.attr("height", function(d) { return height - y(d.value); });


	    
	}); // end of d3.csv

	
    } // end initialization
    
    // updating our drawing whenever the "state" is updated
    //update(props, oldProps) {
    //} // end updating
    
    
} // closing the defintion of our custom component

module.exports = HistogramCustomD3Component;
