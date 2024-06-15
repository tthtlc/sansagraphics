
// Function to draw a sector of a circle and bisect it perpendicularly to the radial direction
function drawSectorAndBisectPerpendicularly(ctx, x, y, radius, startAngle, endAngle, fillColor) {
    ctx.beginPath(); // Start a new path
    ctx.moveTo(x, y); // Move to the center of the circle
    ctx.arc(x, y, radius, startAngle, endAngle); // Draw the outer arc
    ctx.closePath(); // Create a straight line back to the center of the circle
    ctx.fillStyle = fillColor; // Set the fill color
    ctx.fill(); // Fill the sector with color

    // Calculate points for the bisecting line
    const midAngle = (startAngle + endAngle) / 2;
    const bisectStartAngle = midAngle - (Math.PI / 2 - (endAngle - startAngle) / 2);
    const bisectEndAngle = midAngle + (Math.PI / 2 - (endAngle - startAngle) / 2);

    // Calculate start and end points for the bisecting line
    const startX = x + radius * Math.cos(bisectStartAngle);
    const startY = y + radius * Math.sin(bisectStartAngle);
    const endX = x + radius * Math.cos(bisectEndAngle);
    const endY = y + radius * Math.sin(bisectEndAngle);

    // Draw the bisecting line
    ctx.beginPath(); // Start a new path for the bisecting line
    ctx.moveTo(startX, startY); // Move to the start point of the bisecting line
    ctx.lineTo(endX, endY); // Draw a line to the end point
    ctx.stroke(); // Stroke the line
}

// Get the canvas element and its context
const canvas = document.getElementById('circleSector');
const ctx = canvas.getContext('2d');

// Example usage: Draw a sector of a circle and bisect it perpendicularly
// Parameters: context, centerX, centerY, radius, startAngle, endAngle, fillColor
drawSectorAndBisectPerpendicularly(ctx, 200, 200, 100, 0, Math.PI / 2, 'blue'); // Drawing and bisecting a quarter circle sector

