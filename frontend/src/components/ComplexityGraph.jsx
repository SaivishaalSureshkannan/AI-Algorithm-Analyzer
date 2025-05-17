import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';

const ComplexityGraph = ({ complexity }) => {
  const svgRef = useRef();

  const generateDataPoints = (complexity) => {
    const maxInputSize = 10;
    const data = [];
    
    switch(complexity) {
      case 'O(1)':
        for (let i = 1; i <= maxInputSize; i++) {
          data.push({ inputSize: i, steps: 1 });
        }
        break;
      case 'O(n)':
        for (let i = 1; i <= maxInputSize; i++) {
          data.push({ inputSize: i, steps: i });
        }
        break;
      case 'O(n^2)':
        for (let i = 1; i <= maxInputSize; i++) {
          data.push({ inputSize: i, steps: i * i });
        }
        break;
      case 'O(2^n)':
        for (let i = 1; i <= maxInputSize; i++) {
          data.push({ inputSize: i, steps: Math.pow(2, i) });
        }
        break;
      default:
        return null;
    }
    return data;
  };

  useEffect(() => {
    const data = generateDataPoints(complexity);
    
    if (!data) {
      // Clear any existing graph
      d3.select(svgRef.current).selectAll("*").remove();
      return;
    }

    d3.select(svgRef.current).selectAll("*").remove();

    // Set up dimensions
    const width = 600;
    const height = 400;
    const margin = { top: 20, right: 30, bottom: 30, left: 60 };

    // Create the SVG
    const svg = d3.select(svgRef.current)
      .attr("width", width)
      .attr("height", height);

    // Create the scales
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
      .attr('y', -50)
      .attr('fill', 'currentColor')
      .text('Number of Steps');

    // Add the line
    svg.append('path')
      .datum(data)
      .attr('fill', 'none')
      .attr('stroke', '#3B82F6')
      .attr('stroke-width', 2)
      .attr('d', line);

    // Add the dots
    svg.selectAll('circle')
      .data(data)
      .enter()
      .append('circle')
      .attr('cx', d => xScale(d.inputSize))
      .attr('cy', d => yScale(d.steps))
      .attr('r', 4)
      .attr('fill', '#3B82F6');

    // Add complexity label
    svg.append('text')
      .attr('x', width - margin.right)
      .attr('y', margin.top)
      .attr('text-anchor', 'end')
      .attr('font-size', '14px')
      .attr('font-weight', 'bold')
      .text(complexity);

  }, [complexity]);

  return (
    <div className="w-full bg-white border rounded shadow p-4 mb-4">
      <h3 className="text-lg font-semibold mb-2 text-center">Time Complexity Graph</h3>
      <div className="flex justify-center">
        {complexity ? (
          <svg ref={svgRef}></svg>
        ) : (
          <div className="text-center text-gray-500 py-8">
            No graph available for unknown complexity
          </div>
        )}
      </div>
    </div>
  );
};

export default ComplexityGraph;
