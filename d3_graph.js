
// Set the dimensions and margins of the graph
const margin = {top: 20, right: 30, bottom: 40, left: 50},
      width = 800 - margin.left - margin.right,
      height = 600 - margin.top - margin.bottom;

// Append the svg object to the body of the page
const svg = d3.select("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

// Sample data
const data = [
  {x: 30, y: 20},
  {x: 50, y: 90},
  {x: 70, y: 50},
  {x: 90, y: 120},
  {x: 110, y: 70},
  {x: 130, y: 200},
  {x: 150, y: 150},
];

// Add X axis
const x = d3.scaleLinear()
  .domain([0, 200])
  .range([ 0, width ]);
svg.append("g")
  .attr("transform", `translate(0,${height})`)
  .call(d3.axisBottom(x));

// Add Y axis
const y = d3.scaleLinear()
  .domain([0, 200])
  .range([ height, 0]);
svg.append("g")
  .call(d3.axisLeft(y));

// Add dots
svg.append('g')
  .selectAll("dot")
  .data(data)
  .enter()
  .append("circle")
    .attr("cx", d => x(d.x))
    .attr("cy", d => y(d.y))
    .attr("r", 5)
    .attr("class", "dot");

