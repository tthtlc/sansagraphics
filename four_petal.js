
const canvas = document.getElementById('animationCanvas');
const ctx = canvas.getContext('2d');
const nPoints = 240;
let step = 1;

function getPoints() {
    const points = [];
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = Math.min(centerX, centerY) * 0.9;

    for (let i = 0; i < nPoints; i++) {
        const theta = (2 * Math.PI * i) / nPoints;
        const r = Math.cos(4 * theta);
        const x = centerX + radius * r * Math.cos(theta);
        const y = centerY + radius * r * Math.sin(theta);
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

    setTimeout(animate, 200); // Control animation speed
}

animate();
