
document.getElementById('startButton').addEventListener('click', drawCircles);

function drawCircles() {
    const radius = document.getElementById('radiusSlider').value;
    const canvas = document.getElementById('circleCanvas');
    const ctx = canvas.getContext('2d');
    const smallerRadius = radius / 2;

    canvas.width = radius * 2 + 20;  // Add some margin
    canvas.height = radius * 2 + 20;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw outer circle
    ctx.beginPath();
    ctx.arc(canvas.width / 2, canvas.height / 2, radius, 0, Math.PI * 2);
    ctx.stroke();

    // Calculate positions for smaller circles
    const innerCircleX = canvas.width / 2;
    const innerCircleY = canvas.height / 2;
    const positions = [
        { x: innerCircleX - smallerRadius, y: innerCircleY },
        { x: innerCircleX + smallerRadius, y: innerCircleY },
        { x: innerCircleX, y: innerCircleY - smallerRadius },
        { x: innerCircleX, y: innerCircleY + smallerRadius }
    ];

    // Draw smaller circles
    positions.forEach(pos => {
        ctx.beginPath();
        ctx.arc(pos.x, pos.y, smallerRadius, 0, Math.PI * 2);
        ctx.stroke();
    });
}

