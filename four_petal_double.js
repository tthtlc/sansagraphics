
const canvas = document.getElementById('animationCanvas');
const ctx = canvas.getContext('2d');
const nPoints = 60;
const bigA = 200; // Semi-major axis length of the big ellipse
const bigB = 100; // Semi-minor axis length of the big ellipse
const smallA = 100; // Semi-major axis length of the small ellipse
const smallB = 50;  // Semi-minor axis length of the small ellipse
let bigRotationAngle = 0; // Initialize rotation angle for the big ellipse
let smallRotationAngle = 0; // Initialize rotation angle for the small ellipse

function getPoints(a, b, rotationAngle) {
    const points = [];
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const rotationRadians = rotationAngle * Math.PI / 180; // Convert degrees to radians

    for (let i = 0; i < nPoints; i++) {
        const theta = (2 * Math.PI * i) / nPoints;
        const x = centerX + (a * Math.cos(theta) * Math.cos(rotationRadians) - b * Math.sin(theta) * Math.sin(rotationRadians));
        const y = centerY + (a * Math.cos(theta) * Math.sin(rotationRadians) + b * Math.sin(theta) * Math.cos(rotationRadians));
        points.push({ x, y });
    }

    return points;
}

function drawPoints(points, color) {
    ctx.fillStyle = color;

    for (const point of points) {
        ctx.beginPath();
        ctx.arc(point.x, point.y, 3, 0, 2 * Math.PI);
        ctx.fill();
    }
}

function drawLines(points1, points2) {
    ctx.strokeStyle = 'blue';

    for (let i = 0; i < points1.length; i++) {
        ctx.beginPath();
        ctx.moveTo(points1[i].x, points1[i].y);
        ctx.lineTo(points2[i].x, points2[i].y);
        ctx.stroke();
    }
}

function animate() {
    // Get points for both ellipses
    const bigEllipsePoints = getPoints(bigA, bigB, bigRotationAngle);
    const smallEllipsePoints = getPoints(smallA, smallB, smallRotationAngle);

    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw the points on both ellipses
    drawPoints(bigEllipsePoints, 'red');
    drawPoints(smallEllipsePoints, 'green');

    // Draw lines connecting corresponding points of the two ellipses
    drawLines(bigEllipsePoints, smallEllipsePoints);

    // Increment rotation angles for the next frame
    bigRotationAngle += 5;  // Rotate the big ellipse by 5 degrees
    smallRotationAngle += 10; // Rotate the small ellipse by 10 degrees

    // Control animation speed and repeat
    setTimeout(animate, 200);
}

animate();

