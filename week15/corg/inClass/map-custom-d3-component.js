const React = require('react');
const D3Component = require('idyll-d3-component');
const d3 = require('d3');

// this draws heavily from: http://bl.ocks.org/micahstubbs/8e15870eb432a21f0bc4d3d527b2d14f

// JPN: had to add the following
const topojson = require('topojson-client'); // Need this for map
const d3tip = require('d3-tip');

//const size = 600;
//const width = 600;
//const height= 600;

var margin = {top: 0, right: 0, bottom: 0, left: 0},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;
var format = d3.format(",");


class MapCustomD3Component extends D3Component {
    
    initialize(node, props) {
	const svg = this.svg = d3.select(node).append('svg');
	svg.attr("width", width)
            .attr("height", height)
            .append('g')
            .attr('class', 'map');


	// Set tooltips
	var tip = d3tip() // JPN: had to change here d3.tip -> d3tip
            .attr('class', 'd3-tip')
            .offset([-10, 0])
            .html(function(d) {
		return "<strong>Country: </strong><span class='details'>" + d.properties.name + "<br></span>" + "<strong>Corgis Born: </strong><span class='details'>" + format(d.population) +"</span>";
            })
	
	
	var color = d3.scaleThreshold()
//	    .domain([10000,
//		     100000,
//		     500000,
//		     1000000,
//		     5000000,
//		     10000000,
//		     50000000,
//		     100000000,
//		     500000000,
//		     1500000000])
	    .domain([0,
		     1,
		     5,
		     10,
		     25,
		     50,
		     100,
		     300,
		     750,
		     1000])
	    .range(["rgb(0,0,0)",
		    "rgb(1,1,1)",
		    "rgb(198,219,239)",
		    "rgb(158,202,225)",
		    "rgb(107,174,214)",
		    "rgb(66,146,198)",
		    "rgb(33,113,181)",
		    "rgb(8,81,156)",
		    "rgb(8,48,107)",
		    "rgb(3,19,43)"]);


	var path = d3.geoPath();
		
	//var projection = d3.geoMercator()
	var projection = d3.geoEquirectangular()
            .scale(130)
            .translate( [width / 2, height / 2]);
	
	var path = d3.geoPath().projection(projection);
	
	svg.call(tip);

	d3.queue() // JPN: had to change queue -> d3.queue()
	    .defer(d3.json, "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/spring2020/master/week12/corg/world_countries.json") // data
	    .defer(d3.json, "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/spring2020/master/week12/corg/corgs_per_country_2020.json") // population
	    .await(ready);

	// data = world data
	// population = population/corgPopulation data
	function ready(error, data, population) {
	    if (error) throw error;
	    //var populationById = {};
	    var corgPopulationById = {};

	    // First, fill are countries with zeros
	    data.features.forEach( function(d) { corgPopulationById[d.id] = 0; });
	    
	    // HERE: gotta process into country code
	    // add in population of corgs for each country
	    //population.forEach(function(d) { corgPopulationById[d.country_id] += 1; console.log(d.country_id, corgPopulationById[d.country_id]); }); // This fills populationById from our pop file
	    population.forEach(function(d) { corgPopulationById[d.country_id] += d.totalCorg;  }); // This fills populationById from our pop file
	    //data.features.forEach(function(d) { d.population = populationById[d.id] }); // This places populationById into our data.features
	    data.features.forEach(function(d) { d.population = corgPopulationById[d.id] }); // This places populationById into our data.features
	    
	    svg.append("g")
		.attr("class", "countries")
		.selectAll("path")
		.data(data.features)
		.enter().append("path")
		.attr("d", path)
		.style("fill", function(d) { return color(corgPopulationById[d.id]); })
		.style('stroke', 'white')
		.style('stroke-width', 1.5)
		.style("opacity",0.8)
	    // tooltips
		.style("stroke","white")
		.style('stroke-width', 0.3)
		.on('mouseover',function(d){
		    tip.show(d, this); // JPN: changed tip.show(d) to tip.show(d, this), following: https://github.com/Caged/d3-tip/issues/231#issuecomment-391242702
		    
		    d3.select(this)
			.style("opacity", 1)
			.style("stroke","white")
			.style("stroke-width",3);
		})
		.on('mouseout', function(d){
		    tip.hide(d);
		    
		    d3.select(this)
			.style("opacity", 0.8)
			.style("stroke","white")
			.style("stroke-width",0.3);
		});
	    
	    svg.append("path")
		.datum(topojson.mesh(data.features, function(a, b) { return a.id !== b.id; }))
		.attr("class", "names")
		.attr("d", path);
	}
    
    }
}



module.exports = MapCustomD3Component;
