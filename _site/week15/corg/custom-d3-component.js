// node-module libraries 
const React = require('react');
const D3Component = require('idyll-d3-component');
const d3 = require('d3');

// setting the base size of our svg plot
const size = 600;

class CustomD3Component extends D3Component { // essentially adding in a component to a library that is already there (look in node_modules)

    // needed to first draw the svggraphics
    initialize(node, props) {
	// setting the definition of our svg space
	const svg = this.svg = d3.select(node).append('svg');
	// the size of the base box
	svg.attr('viewBox', `0 0 ${size} ${size}`)
	    .style('width', '100%')
	    .style('height', 'auto');

	// here adds the circle (SVG = a vector representation of a circle!)
	svg.append('circle')
	    .attr('r', 20) // 20 pixels 
	    .attr('cx', Math.random() * size)
	    .attr('cy', Math.random() * size);
    }

    // updates when state updates
    update(props, oldProps) {
	this.svg.selectAll('circle') // do something with the circle
	    .transition() // I want a nice animation
	    .duration(750) // duration of my animation in millisecs
	    .attr('cx', Math.random() * size) // replace randomly in x&y
	    .attr('cy', Math.random() * size);
    }
}

module.exports = CustomD3Component; // make this available to idyll
