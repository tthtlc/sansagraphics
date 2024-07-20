
document.getElementById('startButton').addEventListener('click', drawCircles);

function drawCircles() {
    const radius = parseInt(document.getElementById('radiusSlider').value);
    const innerCircleCount = parseInt(document.getElementById('innerCircleCount').value);
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
    const angleStep = (2 * Math.PI) / innerCircleCount;

    for (let i = 0; i < innerCircleCount; i++) {
        const angle = i * angleStep;
        const x = innerCircleX + smallerRadius * Math.cos(angle); //### - smallerRadius;
        const y = innerCircleY + smallerRadius * Math.sin(angle); // #### - smallerRadius;

        ctx.beginPath();
        ctx.arc(x, y, smallerRadius, 0, Math.PI * 2);
        ctx.stroke();
    }
}

