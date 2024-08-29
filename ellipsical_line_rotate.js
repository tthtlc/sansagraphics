
const canvas = document.getElementById('animationCanvas');
const ctx = canvas.getContext('2d');
const nPoints = 60;
const a = 200; // Semi-major axis length (scaled)
const b = 100; // Semi-minor axis length (scaled)
let step = 1;
let rotationAngle = 0; // Initialize rotation angle

function getPoints() {
    const points = [];
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const rotationRadians = rotationAngle * Math.PI / 180; // Convert degrees to radians

    for (let i = 0; i < nPoints; i++) {
        const theta = (2 * Math.PI * i) / nPoints;
        // Apply rotation to the angle
        const x = centerX + (a * Math.cos(theta) * Math.cos(rotationRadians) - b * Math.sin(theta) * Math.sin(rotationRadians));
        const y = centerY + (a * Math.cos(theta) * Math.sin(rotationRadians) + b * Math.sin(theta) * Math.cos(rotationRadians));
        points.push({ x, y });
    }

    return points;
}

function drawPoints(points) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'blue';

    for (const point of points) {
        ctx.beginPath();
        ctx.arc(point.x, point.y, 3, 0, 2 * Math.PI);
        ctx.fill();
    }
}

function drawLines(points, step) {
    ctx.strokeStyle = 'blue';

    for (let i = 0; i < points.length; i++) {
        const j = (i + step) % points.length;
        ctx.beginPath();
        ctx.moveTo(points[i].x, points[i].y);
        ctx.lineTo(points[j].x, points[j].y);
        ctx.stroke();
    }
}

function animate() {
    const points = getPoints();
    drawPoints(points);
    drawLines(points, step);
    step = (step % (nPoints - 1)) + 1; // Increment step from 1 to 59
    rotationAngle += 5; // Rotate by 5 degrees for the next frame

    setTimeout(animate, 200); // Control animation speed
}

animate();

