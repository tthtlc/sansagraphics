
// Function to draw a sector of a circle and radially cut it into half
function drawSector(ctx, x, y, radius, startAngle, endAngle, fillColor) {
    ctx.beginPath(); // Start a new path
    ctx.moveTo(x, y); // Move to the center of the circle
    ctx.arc(x, y, radius, startAngle, endAngle); // Draw the outer arc
    ctx.closePath(); // Create a straight line back to the center of the circle
    ctx.fillStyle = fillColor; // Set the fill color
    ctx.fill(); // Fill the sector with color
    ctx.strokeStyle = 'white'; // Fill the sector with color

    ctx.stroke(); // Draw the line
}
// Function to draw a sector of a circle and radially cut it into half
function drawSectorAndCut(ctx, x, y, radius, startAngle, endAngle, fillColor) {
    ctx.beginPath(); // Start a new path
    ctx.moveTo(x, y); // Move to the center of the circle
    ctx.arc(x, y, radius, startAngle, endAngle); // Draw the outer arc
    ctx.closePath(); // Create a straight line back to the center of the circle
    ctx.fillStyle = fillColor; // Set the fill color
    ctx.fill(); // Fill the sector with color

    // Calculate the midpoint angle
    const midAngle = (startAngle + endAngle) / 2;

    // Draw a line to radially cut the sector into half
    ctx.beginPath(); // Start a new path for the line
    ctx.moveTo(x, y); // Start from the center of the circle
    // Calculate the end point of the line on the circle's edge
    ctx.lineTo(x + radius * Math.cos(midAngle), y + radius * Math.sin(midAngle));
    ctx.stroke(); // Draw the line
}

// Get the canvas element and its context
const canvas = document.getElementById('circleSector');
const ctx = canvas.getContext('2d');

// Example usage: Draw a sector of a circle and radially cut it into half
// Parameters: context, centerX, centerY, radius, startAngle, endAngle, fillColor
var ngon = 6;
var mysize = Math.PI * 2/ngon;
var mysize_diff = mysize/10;


for (let angle = 0.0; angle < 2*Math.PI; angle += mysize) {
drawSector(ctx, 200, 200, 100, angle, angle+mysize-mysize_diff, 'blue'); // Drawing and cutting a quarter circle sector
drawSector(ctx, 200, 200, 100/2, angle, angle+mysize-mysize_diff, 'white'); // Drawing and cutting a quarter circle sector
}
