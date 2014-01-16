

/// g++ dodecahedron.cpp -lglut

// This is a simple introductory program; its main window contains a static
// picture of a dodecahedron, whose top vertex is white and whose bottom
// vertices are red, green and blue.  The program illustrates viewing by
// defining an object at a convenient location, then transforming it so that
// it lies within the view volume.  This is a lousy way to do things (it's
// easier to use gluLookAt()), but it's nice to see how viewing is done at
// a very low level.

#ifdef __APPLE_CC__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

void draw_dodecahedron();

// Clears the window and draws the dodecahedron.  The dodecahedron is  easily
// specified with a triangle strip, though the specification really isn't very
// easy to read.
void draw_pentagon(GLfloat ptr[5][3], int index1, int index2, int index3, int index4, int index5) {

  glColor3f(1.0, 1.0, 1.0);
  glBegin(GL_POLYGON);
    	glVertex3f(ptr[index1][0], ptr[index1][1], ptr[index1][2]);
    	glVertex3f(ptr[index2][0], ptr[index2][1], ptr[index2][2]);
    	glVertex3f(ptr[index3][0], ptr[index3][1], ptr[index3][2]);
    	glVertex3f(ptr[index4][0], ptr[index4][1], ptr[index4][2]);
    	glVertex3f(ptr[index5][0], ptr[index5][1], ptr[index5][2]);
  glEnd();
}

// Sets up global attributes like clear color and drawing color, enables and
// initializes any needed modes (in this case we want backfaces culled), and
// sets up the desired projection and modelview matrices. It is cleaner to
// define these operations in a function separate from main().
void init() {

  // Set the current clear color to sky blue and the current drawing color to
  // white.
  glClearColor(0.1, 0.39, 0.88, 1.0);
  glColor3f(1.0, 1.0, 1.0);
  glColor3ub(23, 23, 25);

  // Tell the rendering engine not to draw backfaces.  Without this code,
  // all four faces of the dodecahedron would be drawn and it is possible
  // that faces farther away could be drawn after nearer to the viewer.
  // Since there is only one closed polyhedron in the whole scene,
  // eliminating the drawing of backfaces gives us the realism we need.
  // THIS DOES NOT WORK IN GENERAL.
  glEnable(GL_CULL_FACE);
  glCullFace(GL_BACK);

  // Set the camera lens so that we have a perspective viewing volume whose
  // horizontal bounds at the near clipping plane are -2..2 and vertical
  // bounds are -1.5..1.5.  The near clipping plane is 1 unit from the camera
  // and the far clipping plane is 40 units away.
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  glFrustum(-2, 2, -1.5, 1.5, 1, 40);

  // Set up transforms so that the dodecahedron which is defined right at
  // the origin will be rotated and moved into the view volume.  First we
  // rotate 70 degrees around y so we can see a lot of the left side.
  // Then we rotate 50 degrees around x to "drop" the top of the pyramid
  // down a bit.  Then we move the object back 3 units "into the screen".
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
  glTranslatef(0, 0, -3);
  glRotatef(50, 1, 0, 0);
  glRotatef(70, 0, 1, 0);
}



/*
Dodecahedron

The "C" pseudo code to generate the vertices is:

*/
#include <math.h>

void draw_dodecahedron(){

  GLfloat vertices[20][3]; /* 20 vertices with x, y, z coordinate */
  double Pi = 3.141592653589793238462643383279502884197;

  double phiaa = 52.62263590; /* the two phi angles needed for generation */
  double phibb = 10.81231754;

  double r = 1.0; /* any radius in which the polyhedron is inscribed */
  double phia = Pi*phiaa/180.0; /* 4 sets of five points each */
  double phib = Pi*phibb/180.0;
  double phic = Pi*(-phibb)/180.0;
  double phid = Pi*(-phiaa)/180.0;
  double the72 = Pi*72.0/180;
  double theb = the72/2.0; /* pairs of layers offset 36 degrees */
  double the = 0.0;
  int i,j,k;
  for(i=0; i<5; i++)
  {
    vertices[i][0]=r*cos(the)*cos(phia);
    vertices[i][1]=r*sin(the)*cos(phia);
    vertices[i][2]=r*sin(phia);
    the = the+the72;
  }
  the=0.0;
  for(i=5; i<10; i++)
  {
    vertices[i][0]=r*cos(the)*cos(phib);
    vertices[i][1]=r*sin(the)*cos(phib);
    vertices[i][2]=r*sin(phib);
    the = the+the72;
  }
  the = theb;
  for(i=10; i<15; i++)
  {
    vertices[i][0]=r*cos(the)*cos(phic);
    vertices[i][1]=r*sin(the)*cos(phic);
    vertices[i][2]=r*sin(phic);
    the = the+the72;
  }
  the=theb;
  for(i=15; i<20; i++)
  {
    vertices[i][0]=r*cos(the)*cos(phid);
    vertices[i][1]=r*sin(the)*cos(phid);
    vertices[i][2]=r*sin(phid);
    the = the+the72;
  }

  /* map vertices to 12 faces */
  glClear(GL_COLOR_BUFFER_BIT);
  draw_pentagon(vertices, 0,1,2,3,4);

  draw_pentagon(vertices, 0,1,6,10,5);
  draw_pentagon(vertices, 1,2,7,11,6);
  draw_pentagon(vertices, 2,3,8,12,7);
  draw_pentagon(vertices, 3,4,9,13,8);
  draw_pentagon(vertices, 4,0,5,14,9);

  draw_pentagon(vertices, 15,16,11,6,10);
  draw_pentagon(vertices, 16,17,12,7,11);
  draw_pentagon(vertices, 17,18,13,8,12);
  draw_pentagon(vertices, 18,19,14,9,13);
  draw_pentagon(vertices, 19,15,10,5,14);
  
  draw_pentagon(vertices, 15,16,17,18,19);
  glFlush();
}


bool fullscreen = false;
bool mouseDown = false;

float xrot = 0.0f;
float yrot = 0.0f;

float xdiff = 0.0f;
float ydiff = 0.0f;


void mouse(int button, int state, int x, int y)
{
	if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
	{
		mouseDown = true;

		xdiff = x - yrot;
		ydiff = -y + xrot;
	}
	else
		mouseDown = false;
}


void mouseMotion(int x, int y)
{
	if (mouseDown)
	{
		yrot = x - xdiff;
		xrot = y + ydiff;

		glutPostRedisplay();
	}
}

void idle()
{
        if (!mouseDown)
        {
                xrot += 0.003f;
                yrot += 0.004f;
        }

        glutPostRedisplay();
}

void display()
{
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        glLoadIdentity();

        gluLookAt(
                0.0f, 0.0f, 3.0f,
                0.0f, 0.0f, 0.0f,
                0.0f, 1.0f, 0.0f);

        glRotatef(xrot, 1.0f, 0.0f, 0.0f);
        glRotatef(yrot, 0.0f, 1.0f, 0.0f);

        draw_dodecahedron();

        glFlush();
        glutSwapBuffers();
}


/*

The dodecahedron coordinates:

 Vertex       coordinate
    0,  x= 0.607, y= 0.000, z= 0.795 
    1,  x= 0.188, y= 0.577, z= 0.795 
    2,  x=-0.491, y= 0.357, z= 0.795 
    3,  x=-0.491, y=-0.357, z= 0.795 
    4,  x= 0.188, y=-0.577, z= 0.795 
    5,  x= 0.982, y= 0.000, z= 0.188 
    6,  x= 0.304, y= 0.934, z= 0.188 
    7,  x=-0.795, y= 0.577, z= 0.188 
    8,  x=-0.795, y=-0.577, z= 0.188 
    9,  x= 0.304, y=-0.934, z= 0.188 
   10,  x= 0.795, y= 0.577, z=-0.188 
   11,  x=-0.304, y= 0.934, z=-0.188 
   12,  x=-0.982, y= 0.000, z=-0.188 
   13,  x=-0.304, y=-0.934, z=-0.188 
   14,  x= 0.795, y=-0.577, z=-0.188 
   15,  x= 0.491, y= 0.357, z=-0.795 
   16,  x=-0.188, y= 0.577, z=-0.795 
   17,  x=-0.607, y= 0.000, z=-0.795 
   18,  x=-0.188, y=-0.577, z=-0.795 
   19,  x= 0.491, y=-0.357, z=-0.795 

Length of every edge is  0.713644 

*/
// Initializes GLUT, the display mode, and main window; registers callbacks;
// does application initialization; enters the main event loop.
int main(int argc, char** argv) {
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
  glutInitWindowPosition(80, 80);
  glutInitWindowSize(800, 600);
  glutCreateWindow("A Simple Dodecahedron");
  glutMouseFunc(mouse);
  glutMotionFunc(mouseMotion);

  glutDisplayFunc(display);
  glutIdleFunc(idle);

  init();
  glutMainLoop();
}
