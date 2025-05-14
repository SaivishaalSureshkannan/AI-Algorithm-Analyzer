import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';

const ComplexityGraph = () => {
  const svgRef = useRef();

  useEffect(() => {
    // Replace when you do the backend
    const data = [
      {inputSize: 1, steps: 1}, 
      {inputSize: 2, steps: 2}, 
      {inputSize: 3, steps: 3}, 
      {inputSize: 4, steps: 4}, 
      {inputSize: 5, steps: 5}, 
      {inputSize: 6, steps: 6}, 
      {inputSize: 7, steps: 7}, 
    ]; 

    d3.select(svgRef.current).selectAll("*").remove(); 

    // Sets up the dimesions 
    const width = 600; 
    const height = 400; 
    const margin = {top: 20, right: 30, bottom: 30, left: 40}; 

    // Create the SVG
    const svg = d3.select(svgRef.current)
      .attr("width", width)
      .attr("height", height); 

    // Create the scales(domains and ranges)
    const xScale = d3.scaleLinear()
      .domain([0, d3.max(data, d => d.inputSize)])
      .range([margin.left, width - margin.right]);

    const yScale = d3.scaleLinear()
      .domain([0, d3.max(data, d => d.steps)])
      .range([height - margin.bottom, margin.top]); 

    // Create line generator 
    const line = d3.line()
      .x(d => xScale(d.inputSize))
      .y(d => yScale(d.steps))
      .curve(d3.curveMonotoneX); 

    // Add X axis 
    svg.append('g')
      .attr('transform', `translate(0, ${height - margin.bottom})`)
      .call(d3.axisBottom(xScale))
      .append('text')
      .attr('x', width / 2)
      .attr('y', 40)
      .attr('fill', 'currentColor')
      .text('Input Size (n)'); 

    // Add Y axis 
    svg.append('g')
      .attr('transform', `translate(${margin.left}, 0)`)
      .call(d3.axisLeft(yScale))
      .append('text')
      .attr('x', -height / 2)
      .attr('y', -40)
      .attr('fill', 'currentColor')
      .text('Number of Steps'); 

    // Add the line 
    svg.append('path')
      .datum(data)
      .attr('fill', 'none')
      .attr('stroke', 'blue')
      .attr('stroke-width', 2)
      .attr('d', line); 

    // Add the dots 
    svg.selectAll('circle')
      .data(data)
      .enter()
      .append('circle')
      .attr('cx', d => xScale(d.inputSize))
      .attr('cy', d => yScale(d.steps))
      .attr('r', 5)
      .attr('fill', 'blue'); 

  }, []); 

  return (
    <div className="w-full bg-white border rounded shadow p-4 mb-4">
      <h3 className="text-lg font-semibold mb-2 text-center">Time Complexity Graph:</h3>
      <div className="flex justify-center">
        <svg ref={svgRef}></svg>
      </div>
    </div>
  );
};

export default ComplexityGraph;
