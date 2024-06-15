
// Function to draw a sector of a circle
function drawSector(ctx, x, y, radius, startAngle, endAngle, fillColor) {
    ctx.beginPath(); // Start a new path
    ctx.moveTo(x, y); // Move to the center of the circle
    ctx.arc(x, y, radius, startAngle, endAngle); // Draw the outer arc
    ctx.closePath(); // Create a straight line back to the center of the circle
    ctx.fillStyle = fillColor; // Set the fill color
    ctx.fill(); // Fill the sector with color
}

// Get the canvas element and its context
const canvas = document.getElementById('circleSector');
const ctx = canvas.getContext('2d');

// Example usage: Draw a sector of a circle
// Parameters: context, centerX, centerY, radius, startAngle, endAngle, fillColor
// Note: Angles in radians, where 0 at the 3 o'clock position, and PI/2 at the 6 o'clock position
drawSector(ctx, 200, 200, 100, 0, Math.PI / 2, 'blue'); // Drawing a quarter circle sector

