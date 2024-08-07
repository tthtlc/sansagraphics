// Initialize WebGL context
const canvas = document.getElementById('webgl-canvas');
const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');

if (!gl) {
  alert('Your browser does not support WebGL');
}

let xrot = 0.2, yrot = 0.0, zrot = 0.0;
let mouseDown = false, fullscreen = false;
let xdiff = 0.0, ydiff = 0.0;

const PI = 3.141592653;
const ngon = 30;
const angle_step = 2 * PI / ngon;
const r1_step = 0.005;
const r2_step = 0.001;
const delta = 0.6;
const theta1 = 2 * PI / ngon;

const ndisc = 20;

function initGL() {
  gl.clearColor(0.0, 0.0, 0.0, 1.0);
  gl.enable(gl.DEPTH_TEST);
  gl.depthFunc(gl.LEQUAL);
  gl.clearDepth(1.0);
}

function drawBilope(uistacks, uislices, radius) {
  const tstep = Math.PI / uislices;
  const sstep = Math.PI / uistacks;
  let cx = 0.1, cy = 0.2, cz = 0.3;
  
  gl.polygonMode(gl.FRONT_AND_BACK, gl.LINE);
  
  for (let i = 0; i < 2 * uislices; i++) {
    const t = tstep * i;
    gl.begin(gl.LINES);
    
    for (let j = 0; j < uistacks; j++) {
      const s = sstep * j;
      gl.vertex3f(0.0, 0.0, 0.0);
      gl.vertex3f(radius * Math.cos(2 * t) * Math.cos(t) * Math.cos(s), 
                  radius * Math.sin(2 * t) * Math.cos(t) * Math.sin(s), 
                  radius * Math.sin(2 * t) * Math.sin(t));
      gl.color3f(cx, cy, cz);
      cx = (cx + 0.1) % 1.0;
      cy = (cy + 0.1) % 1.0;
      cz = (cz + 0.1) % 1.0;
    }
    gl.end();
  }
}

function display() {
  gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
  gl.loadIdentity();
  
  glu.lookAt(0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
  
  gl.rotatef(xrot, 1.0, 0.0, 0.0);
  gl.rotatef(yrot, 0.0, 1.0, 0.0);
  gl.rotatef(zrot, 0.0, 0.0, 1.0);
  
  gl.color3f(0.5, 0.0, 1.0);
  drawBilope(30, 60, 2.0);
  
  gl.flush();
  gl.swapBuffers();
}

function resize() {
  gl.matrixMode(gl.PROJECTION);
  gl.loadIdentity();
  gl.viewport(0, 0, canvas.width, canvas.height);
  glu.perspective(45.0, canvas.width / canvas.height, 1.0, 100.0);
  gl.matrixMode(gl.MODELVIEW);
  gl.loadIdentity();
}

function idle() {
  if (!mouseDown) {
    xrot += 0.3;
    yrot += 0.3;
    zrot += 1.0;
  }
  display();
}

function keydown(event) {
  if (event.keyCode === 27) { // Escape key
    window.close();
  } else if (event.keyCode === 112) { // F1 key
    fullscreen = !fullscreen;
    if (fullscreen) {
      canvas.requestFullscreen();
    } else {
      document.exitFullscreen();
    }
  }
}

function mousedown(event) {
  mouseDown = true;
  xdiff = event.clientX - yrot;
  ydiff = -event.clientY + xrot;
}

function mouseup() {
  mouseDown = false;
}

function mousemove(event) {
  if (mouseDown) {
    yrot = event.clientX - xdiff;
    xrot = event.clientY + ydiff;
  }
  display();
}

function main() {
  initGL();
  
  canvas.addEventListener('mousedown', mousedown, false);
  canvas.addEventListener('mouseup', mouseup, false);
  canvas.addEventListener('mousemove', mousemove, false);
  document.addEventListener('keydown', keydown, false);
  
  resize();
  display();
}

window.onload = main;

