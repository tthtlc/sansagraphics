
// Our first 3D example
//
// This program demonstrates various 3D shapes that are
// available in glut.

#include <GL/glut.h>

//
// This is the reshape callback function.  It sets up the
// orthographic projection and the viewport.
void reshape(int width, int height) 
{

	// Set the new viewport size
	glViewport(0, 0, (GLint)width, (GLint)height);

	// Choose the projection matrix to be the matrix 
	// manipulated by the following calls
	glMatrixMode(GL_PROJECTION);

	// Set the projection matrix to be the identity matrix
	glLoadIdentity();

	// Define the dimensions of the Orthographic Viewing Volume
	glOrtho(-8.0, 8.0, -8.0, 8.0, -8.0, 8.0);

	// Choose the modelview matrix to be the matrix
	// manipulated by further calls
	glMatrixMode(GL_MODELVIEW);
}

//
// This is the display callback.  Using glut functions, a cube, 
// teapot, torus, cone, sphere, tetrahedron, octahedron, 
// dodecahedron, and icosahedron are placed on the screen at
// various positions.
void draw(void) 
{

	// Clear the RGB buffer and the depth buffer
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	// Set the modelview matrix to be the identity matrix
	glLoadIdentity();
	glTranslatef(3.5, 0.0, 0.0);
	glRotatef(45, 1.0, 0.0, 0.0);
	glRotatef(45, 0.0, 1.0, 0.0);
	glRotatef(45, 0.0, 0.0, 1.0);

	// Draw a solid cubecube in blue
	glColor3f(0.0, 0.0, 1.0);
	glutSolidCube (3.0);

	//Draw the edges of the cube in yellow
	glColor3f (1.0, 1.0, 0.0);
	glutWireCube(3.0);

	//Translate the teapot
	glLoadIdentity();
	glTranslatef (-3.5, 0.0, 0.0);

	//Draw a solid red teapot
	glColor3f (1.0, 0.0, 0.0);
	glutSolidTeapot(3.0);

	//Draw a wireframe green teapot
	glColor3f (0.0, 1.0, 0.0);
	glutWireTeapot (3.0);

	//Draw a solid magenta Torus
	glColor3f (1.0, 0.0, 1.0);
	glLoadIdentity();
	glTranslatef(0.0, -4.5, 0.0);
	glRotatef (45, 1.0, 0.0, 0.0);
	glutSolidTorus(0.75, 1.5, 10, 10);

	//Draw the wireframe Torus in blue
	glColor3f (0.0, 0.0, 1.0);
	glutWireTorus (0.75, 1.5, 10, 10);

	//Draw a solid Cone in Yellow
	glColor3f (1.0, 1.0, 0.0);
	glLoadIdentity();
	glTranslatef (0.0, 4.5, 0.0);
	glRotatef (45, 1.0, 0.0, 0.0);
	glutSolidCone(2.0, 4.0, 10, 10);

	//Draw the wireframe Cone in Blue
	glColor3f (0.0, 0.0, 1.0);
	glutWireCone (2.0, 4.0, 10, 10);

	//Draw a sphere in cyan and outline in black
	glColor3f (0.0, 1.0, 1.0);
	glLoadIdentity();
	glTranslatef(-4.5, 4.5, 0.0);
	glRotatef (45, 1.0, 0.0, 0.0);
	glutSolidSphere (2.0, 20, 30);
	glColor3f (0.0, 0.0, 1.0);
	glutWireSphere (2.0, 20, 30);

	//Draw a Tetrahedron in Red and outline in white
	glColor3f (1.0, 0.0, 0.0);
	glLoadIdentity ();
	glTranslatef (4.5, 4.5, 0.0);
	glRotatef (45, 1.0, 0.0, 0.0);
	glRotatef (45, 0.0, 1.0, 0.0);
	glRotatef (45, 0.0, 0.0, 1.0);
	glutSolidTetrahedron();
	glColor3f (1.0, 1.0, 1.0);
	glutWireTetrahedron();

	//Draw an Octahedron in red and outline in white
	glColor3f (0.5, 0.0, 0.0);
	glLoadIdentity ();
	glTranslatef (-4.5, -4.5, 0.0);
	glRotatef (30, 1.0, 0.0, 0.0);
	glRotatef (60, 0.0, 1.0, 0.0);
	glutSolidOctahedron();
	glColor3f (1.0, 1.0, 1.0);
	glutWireOctahedron();
	
	//Draw a Dodecahedron in blue and outline in white
	glColor3f (0.0, 0.0, 0.5);
	glLoadIdentity();
	glTranslatef (4.5, -4.5, 0.0);
	glRotatef (30, 1.0, 0.0, 0.0);
	glRotatef (60, 0.0, 1.0, 0.0);
	glutSolidDodecahedron();
	glColor3f (1.0, 1.0, 1.0);
	glutWireDodecahedron();

	//Draw a Icosahedron in green and outline in white
	glColor3f (0.0, 0.5, 0.0);
	glLoadIdentity();
	glTranslatef (6.5, -6.5, 0.0);
	glRotatef (30, 1.0, 0.0, 0.0);
	glRotatef (60, 0.0, 1.0, 0.0);
	glutSolidIcosahedron();
	glColor3f (1.0, 1.0, 1.0);
	glutWireIcosahedron();
	// Flush the buffer to force drawing of all objects thus far
	glFlush();
}



void main(int argc, char **argv) {

	//initialize glut
	glutInit (&argc, argv);
	glutInitDisplayMode (GLUT_RGB|GLUT_SINGLE);

	// Set top left corner of window to be at location (0, 0)
	// Set the window size to be 500x500 pixels
	glutInitWindowSize(500, 500);
	glutInitWindowPosition (0,0);

	glutCreateWindow ("Polygons");

	// Set the clear color to black
	glClearColor(0.0, 0.0, 0.0, 0.0);

	// Set the shading model
	glShadeModel(GL_FLAT);

	// Enable depth testing for hidden line removal
	glEnable(GL_DEPTH_TEST);

	//register callback functions
	glutDisplayFunc (draw);
	glutReshapeFunc (reshape);

	//enter the main loop
	glutMainLoop();

}



