// node-module libraries 
const React = require('react');
const D3Component = require('idyll-d3-component');
const d3 = require('d3');


//COPIED:
var margin = {top: 20, right: 20, bottom: 70, left: 40},
    width = 800 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;



// Parse the date / time
var parseDate = d3.isoParse

var x = d3.scaleBand().rangeRound([0, width], .05).padding(0.1);

var y = d3.scaleLinear().range([height, 0]);

var xAxis = d3.axisBottom()
    .scale(x)
    .tickFormat(d3.timeFormat("%Y")); // updated


var yAxis = d3.axisLeft()
    .scale(y)
    .ticks(10);


class HistogramButtonCustomD3Component extends D3Component { // change name

    // needed to first draw the svggraphics
    initialize(node, props) {


	
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


	    // grab length of entries
	    var lengthEntries = 0;
	    data.forEach(function(d) {
		lengthEntries += 1;
	    });

	    // empty array -- make it!
	    data['date'] = Array.apply(null, Array(lengthEntries)).map(function () {});
	    data['value'] = Array.apply(null, Array(lengthEntries)).map(function () {});

	    //var countryName = 'United States';
	    var countryName = props.country;

	    //console.log(Object.keys(props));
	    //console.log(props.country);
	    
	    data.forEach(function(d) {
		d.date = parseDate(d['Years']);
		d.value = d[countryName];
	    });

	    
	    x.domain(data.map(function(d) { return d.date; }));
	    y.domain([0,650]);
	    
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

	    
	}); // end of read in d3.csv data
	

    } // end of initialize props


    // for button updates, we also need to update what happens when things change
    update(props){
	
	const svg = this.svg;
	svg.selectAll("*").remove(); // remove old things

	var countryName = props.country; // grab new country name

	
	// redraw things
	svg.attr("width", width + margin.left + margin.right)
	      .attr("height", height + margin.top + margin.bottom)
	      .append("g")
	      .attr("transform",
		    "translate(" + margin.left + "," + margin.top + ")");


	// redraw stuff based on data
	d3.csv("https://raw.githubusercontent.com/UIUC-iSchool-DataViz/spring2020/master/week12/corg/corgs_per_country_over_time_columns_2020.csv", function(error, data) {


	    // grab length of entries
	    var lengthEntries = 0;
	    data.forEach(function(d) {
		lengthEntries += 1;
	    });

	    // empty array -- make it!
	    data['date'] = Array.apply(null, Array(lengthEntries)).map(function () {});
	    data['value'] = Array.apply(null, Array(lengthEntries)).map(function () {});

	    var countryName = props.country;
	    
	    data.forEach(function(d) {
		d.date = parseDate(d['Years']);
		d.value = d[countryName];
	    });

	    
	    x.domain(data.map(function(d) { return d.date; }));
	    y.domain([0,650]);
	    
	    svg.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(0," + height + ")")
		.call(xAxis.ticks(null).tickSize(0))
		.selectAll("text")
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
	    
	}); // end of read in d3.csv data
	
	
	
  


    } // end of update props


}

module.exports = HistogramButtonCustomD3Component; // add histogram here
