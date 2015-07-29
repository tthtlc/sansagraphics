###/*                                                                     */
###/*  NAME     : Scott Teresi, www.teresi.us                             */
###/*  DATE     : November 20, 1998                                       */
###/*                                                                     */
###/*  PURPOSE  : Draw and rotate a 3-D Sierpinski tetrahedron and cube.  */
###/*  INPUT    : Real-time rotation by dragging the mouse, and number    */
###/*             keys to specify number of fractal iterations            */
###/*                                                                     */
### origin:
###// http://teresi.us/html/main/programming.html#code


###int CalculateNormal (float x1, float y1, float z1, float x2, float y2, float z2);

import math

TRUE=1
FALSE=0

winWidth = 640;
winHeight = 640;

MAXLEVELS=5   ###    /* max. number of fractal iterations */


#int curX, curY;           /* current mouse pointer pos. (when button pressed */
#int leftButtonDown, rightButtonDown; /* flags indicating button pressed */
#float rotX, rotY, rotZ;   /* amount of rotation accumulated about each axis */
scale = 1.0;          #/* current scale factor */

#float nx, ny, nz;

tetrahedron = TRUE;     #/* is tetrahedron or cube being displayed? */
level = 0;              #/* level of recursion */


#typedef struct pt {         /* 3-D point structure */
#  float x;
#  float y;
#  float z;
#} pt_struct;

#typedef struct ts {         /* tetrahedron structure */
#  pt_struct pt[4];
#} tetra_struct;
#
#typedef struct cs {         /* cube structure */
#  pt_struct pt[8];
#} cube_struct;
#
#
#typedef struct sls {
#  int tetra_shapes;         /* number of shapes in this level */
#  int cube_shapes;
#  int tetra_calculated;     /* TRUE if this shape array has been calculated */
#  int cube_calculated;
#  tetra_struct tetra[1024]; /* the array of shapes in this level */
#  cube_struct cube[8000];
#} shape_struct;
#
#shape_struct shape[MAXLEVELS+1];  /* array of all shapes in all levels */
#
#
#
#
#
# /*
#   Draw all elements involved in the picture
# */

def DrawPicture():

  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
  glRotatef(rotY, 0, 1, 0);
  glRotatef(rotX, 1, 0, 0);
  glScalef(scale, scale, scale);

  glPointSize(1.0);
  glPolygonMode(GL_BACK, GL_POINT);

  ##/* plot tetrahedron */

  if (tetrahedron):
    glColor3f(0.0, 1.0, 1.0);
    if (!shape[level].tetra_calculated):
      CalculateTetrahedron(level);
    for i in range (0, shape[level].tetra_shapes):
      #/* front face */
      DrawTriangle(shape[level].tetra[i].pt[2],
		   shape[level].tetra[i].pt[1],
		   shape[level].tetra[i].pt[0]);
      #/* top back */
      DrawTriangle(shape[level].tetra[i].pt[1],
		   shape[level].tetra[i].pt[3],
		   shape[level].tetra[i].pt[0]);
      #/* bottom right back */
      DrawTriangle(shape[level].tetra[i].pt[2],
		   shape[level].tetra[i].pt[3],
		   shape[level].tetra[i].pt[1]);
      #/* bottom left back */
      DrawTriangle(shape[level].tetra[i].pt[3],
		   shape[level].tetra[i].pt[2],
		   shape[level].tetra[i].pt[0]);


  #/* plot cube */

  else:
    glColor3f(1.0, 0.0, 1.0);
    if (!shape[level].cube_calculated):
      CalculateCube(level);
    for i in range(shape[level].cube_shapes):
      #/* front face */
      DrawSquare(shape[level].cube[i].pt[0],
		 shape[level].cube[i].pt[1],
		 shape[level].cube[i].pt[2],
		 shape[level].cube[i].pt[3]);
      #/* back face */
      DrawSquare(shape[level].cube[i].pt[7],
		 shape[level].cube[i].pt[6],
		 shape[level].cube[i].pt[5],
		 shape[level].cube[i].pt[4]);
      #/* left face */
      DrawSquare(shape[level].cube[i].pt[3],
		 shape[level].cube[i].pt[7],
		 shape[level].cube[i].pt[4],
		 shape[level].cube[i].pt[0]);
      #/* right face */
      DrawSquare(shape[level].cube[i].pt[1],
		 shape[level].cube[i].pt[5],
		 shape[level].cube[i].pt[6],
		 shape[level].cube[i].pt[2]);
      #/* bottom face */
      DrawSquare(shape[level].cube[i].pt[0],
		 shape[level].cube[i].pt[4],
		 shape[level].cube[i].pt[5],
		 shape[level].cube[i].pt[1]);
      #/* top face */
      DrawSquare(shape[level].cube[i].pt[3],
		 shape[level].cube[i].pt[2],
		 shape[level].cube[i].pt[6],
		 shape[level].cube[i].pt[7]);
  #/* double-buffering is easy! */
  glutSwapBuffers();


 #/*
 #  Draw a triangle polygon given three points, specified counterclockwise
 #*/

def DrawTriangle (pt_struct pt1, pt_struct pt2, pt_struct pt3):
 
  CalculateNormal (pt2.x - pt1.x, pt2.y - pt1.y, pt2.z - pt1.z,
		   pt3.x - pt2.x, pt3.y - pt2.y, pt3.z - pt2.z);
  glBegin(GL_POLYGON);
  glNormal3f(nx, ny, nz);
  glVertex3f(pt1.x, pt1.y, pt1.z);
  glVertex3f(pt2.x, pt2.y, pt2.z);
  glVertex3f(pt3.x, pt3.y, pt3.z);
  glEnd();


 #/*
 #  Draw a square given four points, specified clockwise
 #*/

def DrawSquare (pt_struct pt1, pt_struct pt2, pt_struct pt3, pt_struct pt4):
 

  CalculateNormal (pt2.x - pt1.x, pt2.y - pt1.y, pt2.z - pt1.z,
		   pt3.x - pt2.x, pt3.y - pt2.y, pt3.z - pt2.z);
  glBegin(GL_POLYGON);
  glNormal3f(nx, ny, nz);
  glVertex3f(pt1.x, pt1.y, pt1.z);
  glVertex3f(pt2.x, pt2.y, pt2.z);
  glVertex3f(pt3.x, pt3.y, pt3.z);
  glVertex3f(pt4.x, pt4.y, pt4.z);
  glEnd();


 #/*
 #  Specify the normal between two vectors
 #*/

def CalculateNormal (x1, y1, z1, x2, y2, z2):

  nx = y1*z2 - y2*z1;
  ny = x2*z1 - x1*z2;
  nz = x1*y2 - x2*y1;

  length = math.sqrt(pow(nx, 2) + math.pow(ny, 2) + math.pow(nz, 2));
  nx = nx / length;
  ny = ny / length;
  nz = nz / length;

 #/*
 #  Calculate new tetrahedrons for this level
 #*/

def CalculateTetrahedron (lev):
  
  ct = 0;

  if (!shape[lev-1].tetra_calculated):
    CalculateTetrahedron(lev-1);

  for i in range (shape[lev-1].tetra_shapes):

    #/* upper left tetrahedron */
    shape[lev].tetra[ct].pt[0].x = shape[lev-1].tetra[i].pt[0].x;
    shape[lev].tetra[ct].pt[0].y = shape[lev-1].tetra[i].pt[0].y;
    shape[lev].tetra[ct].pt[0].z = shape[lev-1].tetra[i].pt[0].z;
    shape[lev].tetra[ct].pt[1].x = (shape[lev-1].tetra[i].pt[0].x +
				    shape[lev-1].tetra[i].pt[1].x) / 2;
    shape[lev].tetra[ct].pt[1].y = (shape[lev-1].tetra[i].pt[0].y +
				    shape[lev-1].tetra[i].pt[1].y) / 2;
    shape[lev].tetra[ct].pt[1].z = (shape[lev-1].tetra[i].pt[0].z +
				    shape[lev-1].tetra[i].pt[1].z) / 2;
    shape[lev].tetra[ct].pt[2].x = (shape[lev-1].tetra[i].pt[0].x +
				    shape[lev-1].tetra[i].pt[2].x) / 2;
    shape[lev].tetra[ct].pt[2].y = (shape[lev-1].tetra[i].pt[0].y +
				    shape[lev-1].tetra[i].pt[2].y) / 2;
    shape[lev].tetra[ct].pt[2].z = (shape[lev-1].tetra[i].pt[0].z +
				    shape[lev-1].tetra[i].pt[2].z) / 2;
    shape[lev].tetra[ct].pt[3].x = (shape[lev-1].tetra[i].pt[0].x +
				    shape[lev-1].tetra[i].pt[3].x) / 2;
    shape[lev].tetra[ct].pt[3].y = (shape[lev-1].tetra[i].pt[0].y +
				    shape[lev-1].tetra[i].pt[3].y) / 2;
    shape[lev].tetra[ct].pt[3].z = (shape[lev-1].tetra[i].pt[0].z +
				    shape[lev-1].tetra[i].pt[3].z) / 2;
    ct ++;

    #/* upper right tetrahedron */
    shape[lev].tetra[ct].pt[0].x = (shape[lev-1].tetra[i].pt[0].x +
				    shape[lev-1].tetra[i].pt[1].x) / 2;
    shape[lev].tetra[ct].pt[0].y = (shape[lev-1].tetra[i].pt[0].y +
				    shape[lev-1].tetra[i].pt[1].y) / 2;
    shape[lev].tetra[ct].pt[0].z = (shape[lev-1].tetra[i].pt[0].z +
				    shape[lev-1].tetra[i].pt[1].z) / 2;
    shape[lev].tetra[ct].pt[1].x = shape[lev-1].tetra[i].pt[1].x;
    shape[lev].tetra[ct].pt[1].y = shape[lev-1].tetra[i].pt[1].y;
    shape[lev].tetra[ct].pt[1].z = shape[lev-1].tetra[i].pt[1].z;
    shape[lev].tetra[ct].pt[2].x = (shape[lev-1].tetra[i].pt[1].x +
				    shape[lev-1].tetra[i].pt[2].x) / 2;
    shape[lev].tetra[ct].pt[2].y = (shape[lev-1].tetra[i].pt[1].y +
				    shape[lev-1].tetra[i].pt[2].y) / 2;
    shape[lev].tetra[ct].pt[2].z = (shape[lev-1].tetra[i].pt[1].z +
				    shape[lev-1].tetra[i].pt[2].z) / 2;
    shape[lev].tetra[ct].pt[3].x = (shape[lev-1].tetra[i].pt[1].x +
				    shape[lev-1].tetra[i].pt[3].x) / 2;
    shape[lev].tetra[ct].pt[3].y = (shape[lev-1].tetra[i].pt[1].y +
				    shape[lev-1].tetra[i].pt[3].y) / 2;
    shape[lev].tetra[ct].pt[3].z = (shape[lev-1].tetra[i].pt[1].z +
				    shape[lev-1].tetra[i].pt[3].z) / 2;
    ct ++;

    #/* bottom tetrahedron */
    shape[lev].tetra[ct].pt[0].x = (shape[lev-1].tetra[i].pt[0].x +
				    shape[lev-1].tetra[i].pt[2].x) / 2;
    shape[lev].tetra[ct].pt[0].y = (shape[lev-1].tetra[i].pt[0].y +
				    shape[lev-1].tetra[i].pt[2].y) / 2;
    shape[lev].tetra[ct].pt[0].z = (shape[lev-1].tetra[i].pt[0].z +
				    shape[lev-1].tetra[i].pt[2].z) / 2;
    shape[lev].tetra[ct].pt[1].x = (shape[lev-1].tetra[i].pt[1].x +
				    shape[lev-1].tetra[i].pt[2].x) / 2;
    shape[lev].tetra[ct].pt[1].y = (shape[lev-1].tetra[i].pt[1].y +
				    shape[lev-1].tetra[i].pt[2].y) / 2;
    shape[lev].tetra[ct].pt[1].z = (shape[lev-1].tetra[i].pt[1].z +
				    shape[lev-1].tetra[i].pt[2].z) / 2;
    shape[lev].tetra[ct].pt[2].x = shape[lev-1].tetra[i].pt[2].x;
    shape[lev].tetra[ct].pt[2].y = shape[lev-1].tetra[i].pt[2].y;
    shape[lev].tetra[ct].pt[2].z = shape[lev-1].tetra[i].pt[2].z;
    shape[lev].tetra[ct].pt[3].x = (shape[lev-1].tetra[i].pt[2].x +
				    shape[lev-1].tetra[i].pt[3].x) / 2;
    shape[lev].tetra[ct].pt[3].y = (shape[lev-1].tetra[i].pt[2].y +
				    shape[lev-1].tetra[i].pt[3].y) / 2;
    shape[lev].tetra[ct].pt[3].z = (shape[lev-1].tetra[i].pt[2].z +
				    shape[lev-1].tetra[i].pt[3].z) / 2;
    ct ++;

    #/* back tetrahedron */
    shape[lev].tetra[ct].pt[0].x = (shape[lev-1].tetra[i].pt[0].x +
				    shape[lev-1].tetra[i].pt[3].x) / 2;
    shape[lev].tetra[ct].pt[0].y = (shape[lev-1].tetra[i].pt[0].y +
				    shape[lev-1].tetra[i].pt[3].y) / 2;
    shape[lev].tetra[ct].pt[0].z = (shape[lev-1].tetra[i].pt[0].z +
				    shape[lev-1].tetra[i].pt[3].z) / 2;
    shape[lev].tetra[ct].pt[1].x = (shape[lev-1].tetra[i].pt[1].x +
				    shape[lev-1].tetra[i].pt[3].x) / 2;
    shape[lev].tetra[ct].pt[1].y = (shape[lev-1].tetra[i].pt[1].y +
				    shape[lev-1].tetra[i].pt[3].y) / 2;
    shape[lev].tetra[ct].pt[1].z = (shape[lev-1].tetra[i].pt[1].z +
				    shape[lev-1].tetra[i].pt[3].z) / 2;
    shape[lev].tetra[ct].pt[2].x = (shape[lev-1].tetra[i].pt[2].x +
				    shape[lev-1].tetra[i].pt[3].x) / 2;
    shape[lev].tetra[ct].pt[2].y = (shape[lev-1].tetra[i].pt[2].y +
				    shape[lev-1].tetra[i].pt[3].y) / 2;
    shape[lev].tetra[ct].pt[2].z = (shape[lev-1].tetra[i].pt[2].z +
				    shape[lev-1].tetra[i].pt[3].z) / 2;
    shape[lev].tetra[ct].pt[3].x = shape[lev-1].tetra[i].pt[3].x;
    shape[lev].tetra[ct].pt[3].y = shape[lev-1].tetra[i].pt[3].y;
    shape[lev].tetra[ct].pt[3].z = shape[lev-1].tetra[i].pt[3].z;
    ct ++;

  shape[lev].tetra_shapes = ct;
  shape[lev].tetra_calculated = TRUE;



# /*
#   Calculate new cubes for this level
# */

def CalculateCube(lev):

  ct = 0
  offset = 0

  if (!shape[lev-1].cube_calculated):
    CalculateCube(lev-1);

  for i in range(shape[lev-1].cube_shapes):

    for k in range(8):
      #/* order of calculations: */
      #/* k = 0: back upper left cube */
      #/* k = 1: back upper right cube */
      #/* etc.: back lower right cube */
      #/*       back lower left cube */
      #/*       front upper left cube */
      #/*       front upper right cube */
      #/*       front lower right cube */
      #/*       front lower left cube */
      for j in range(8):
	shape[lev].cube[ct].pt[j].x = (shape[lev-1].cube[i].pt[j].x -
				       shape[lev-1].cube[i].pt[k].x) / 3 +
	                               shape[lev-1].cube[i].pt[k].x;
	shape[lev].cube[ct].pt[j].y = (shape[lev-1].cube[i].pt[j].y -
				       shape[lev-1].cube[i].pt[k].y) / 3 +
	                               shape[lev-1].cube[i].pt[k].y;
	shape[lev].cube[ct].pt[j].z = (shape[lev-1].cube[i].pt[j].z -
				       shape[lev-1].cube[i].pt[k].z) / 3 +
	                               shape[lev-1].cube[i].pt[k].z;
        ct+=1

    #/* sandwiched inner-cubes (in x-y plane) */
    for k in range(4):
      for j in range(8):
	shape[lev].cube[ct].pt[j].x = shape[lev].cube[ct-8].pt[j].x;
	shape[lev].cube[ct].pt[j].y = shape[lev].cube[ct-8].pt[j].y;
	shape[lev].cube[ct].pt[j].z = shape[lev].cube[ct-8].pt[j].z - (shape[lev].cube[ct-8].pt[1].x - shape[lev].cube[ct-8].pt[0].x);
        ct+=1

    #/* middle inner-cubes (in y-z plane) */
    offset = 0;
    for k in (1, 7):
      for j in range(8):
	shape[lev].cube[ct].pt[j].x = shape[lev].cube[ct-11+offset].pt[j].x -
	  (shape[lev].cube[ct-11].pt[1].x - shape[lev].cube[ct-11].pt[0].x);
	shape[lev].cube[ct].pt[j].y = shape[lev].cube[ct-11+offset].pt[j].y;
	shape[lev].cube[ct].pt[j].z = shape[lev].cube[ct-11+offset].pt[j].z;
      ct+=1
      if (k == 2):
	k = 4;
	offset = 2;

    #/* planar inner-cubes (in x-z plane) */
    offset = 0;
    for k in range(6):
      for j in range(8):
	shape[lev].cube[ct].pt[j].x = shape[lev].cube[ct-16+offset].pt[j].x;
	shape[lev].cube[ct].pt[j].y = shape[lev].cube[ct-16+offset].pt[j].y +
	  (shape[lev].cube[ct-16].pt[1].x - shape[lev].cube[ct-16].pt[0].x);
	shape[lev].cube[ct].pt[j].z = shape[lev].cube[ct-16+offset].pt[j].z;
      ct+=1
      if (k == 1):
	k = 3;
	offset = 2;
  shape[lev].cube_shapes = ct;
  shape[lev].cube_calculated = TRUE;



# /*
#   Called whenever a mouse button event occurs
# */

def MouseClick(button, state, x, y):

  #/* make sure mouse click or release happened inside the window */
  if ((x >= 0) && (x <= winWidth) && (y >= 0) && (y <= winHeight)):

    #/* if mouse click down, note current x/y values for rotation */
    if (state == GLUT_DOWN):
      #/* left button, rotate left-right and up-down */
      if (button == GLUT_LEFT_BUTTON):
	rightButtonDown = FALSE;
	leftButtonDown = TRUE;
	curX = x;
	curY = y;
      #/* right button, zoom in and out */
      elif (button == GLUT_RIGHT_BUTTON):
	leftButtonDown = FALSE;
	rightButtonDown = TRUE;
	curX = x;
	curY = y;
    /* if mouse click up, stop rotating */
    elif (state == GLUT_UP):
      leftButtonDown = FALSE;
      rightButtonDown = FALSE;

# /*
#   Called whenever a mouse drag occurs
#   (i.e. mouse movement while any button is down)
# */

def MouseDrag(x, y):

  diffX = 0.0 + x - curX;
  diffY = 0.0 + y - curY;
  curX = x;
  curY = y;

  if (leftButtonDown):
    rotY += diffX;
    rotX += diffY;
  elif (rightButtonDown):
    scale += diffY / 250;
    if (scale < 0):
      scale = 0;

  glutPostRedisplay();


# /*
#   Called whenever user presses a key
# */

##def KeyPressed(key, x, y):
##
##  switch (toupper(key)) {
##
##    case 'Q':   /* quit program */
##      QuitProgram();
##      break;
##    case ' ':   /* spacebar: toggle between tetrahedron and cube */
##      if (tetrahedron)
##	tetrahedron = FALSE;
##      else
##	tetrahedron = TRUE;
##      glutPostRedisplay();
##      break;
##    case '0':   /* digits 0-5: set level of recursion */
##      level = 0;
##      glutPostRedisplay();
##      break;
##    case '1':
##      level = 1;
##      glutPostRedisplay();
##      break;
##    case '2':
##      level = 2;
##      glutPostRedisplay();
##      break;
##    case '3':
##      level = 3;
##      glutPostRedisplay();
##      break;
##    case '4':
##      level = 4;
##      glutPostRedisplay();
##      break;
##    case '5':
##      level = 5;
##      glutPostRedisplay();
##      break;
##    default:
##      break;
##  }
##}



def IdleFunction():
	return;


# /*
#   Set up the main window
# */

def Initialize(title):

  light_position[] = { 5, 5, 5, 0 };
  ambient_light[] = { .1, .1, .1, 1.0 };

  #/* Initialize the (double-buffering) window and color mode */
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
  glutInitWindowSize(winWidth, winHeight);
  glutCreateWindow(title);

  glShadeModel(GL_SMOOTH);  ###/* don't need this? */

  glLightfv(GL_LIGHT0, GL_POSITION, light_position);
  glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light);

  glEnable(GL_DEPTH_TEST);
  glEnable(GL_NORMALIZE);
  glEnable(GL_COLOR_MATERIAL);

  glEnable(GL_LIGHT0);
  glEnable(GL_LIGHTING);

  glClearColor(0.2, 0.2, 0.22, 0.0);   /* Background is black */
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

  SetCameraPosition();

  #/* seed the random number generator */
  #srand(time(NULL));



 #/*
 #  Move the camera to the correct viewing position, then set GL_MODELVIEW
 #  to allow drawing of objects on the screen.
 #*/

def SetCameraPosition():
  #/* Set the viewing transformation */
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluPerspective(15, 1.0, .001, 1000);
  gluLookAt(0,0,10, 0,0,0, 0,1,0); ##/* position, direction, up */
  glMatrixMode(GL_MODELVIEW);


 #/*
 #  Refresh the contents of the display (called by the main event loop)
 #*/

def UpdateDisplay():

  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
                       ##/* Clear the main window */

  SetCameraPosition();
  DrawPicture();       ##/* Do the actual drawing of the primitives */

  glFlush();           ##/* Flush all output to the main window */



 ##/*
 ##  Reshape the window if the user resizes it
 ##*/

def ReshapeWindow(width, height):

  winWidth = width;       #/* Update the global winWidth/winHeight variables */
  winHeight = height;
  SetCameraPosition();    #/* Update the camera view to be full screen */
  glViewport(0, 0, winWidth, winHeight);



def PrintUsage():

  print("\n");
  print("________________________________________________________________\n");
  print("\n");
  print("Sierpinksi Sponges\n");
  print("Scott Teresi, Nov. 1998\n");
  print("\n");
  print("Hold down the left mouse button and\n");
  print("   ...move the mouse horizontally to rotate around the Y axis\n");
  print("   ...or move the mouse vertically to rotate around the X axis.\n");
  print("\n");
  print("Hold down the right mouse button and\n");
  print("   ...move the mouse vertically to zoom in or out.\n");
  print("\n");
  print("Use keys 0-5 to set the level of recursion.\n");
  print("Use <spacebar> to toggle between tetrahedron and cube.\n");
  print("Type Q to quit the program.\n");
  print("\n");
  print("WARNING:\n"); 
  print("5 levels of recursion for the cube may take several minutes!\n");
  print("NOTE:\n");
  print("Something about the normals or rotation matrices or OpenGL's\n");
  print("order of drawing things causes some of the component shapes in\n");
  print("the fractal object to show through. Sorry!\n");
  print("________________________________________________________________\n");
  print("\n");


def main():

  glutInit()

  PrintUsage();                       #/* print program usage */

  Initialize("CS318 MP5 Sierpinski Sponges");
                                      #/* set up main window and variables */
  for i in range(MAXLEVELS):
    shape[i].tetra_calculated = FALSE;
    shape[i].cube_calculated = FALSE;

  tetrahedron = TRUE;
  #/* top left */
  shape[0].tetra[0].pt[0].x = -.886;
  shape[0].tetra[0].pt[0].y = .386;
  shape[0].tetra[0].pt[0].z = .35;
  #/* top right */
  shape[0].tetra[0].pt[1].x = .886;
  shape[0].tetra[0].pt[1].y = .386;
  shape[0].tetra[0].pt[1].z = .35;
  #/* bottom */
  shape[0].tetra[0].pt[2].x = 0;
  shape[0].tetra[0].pt[2].y = -1.05;
  shape[0].tetra[0].pt[2].z = .35;
  #/* back */
  shape[0].tetra[0].pt[3].x = 0;
  shape[0].tetra[0].pt[3].y = 0;
  shape[0].tetra[0].pt[3].z = -1;
  shape[0].tetra_calculated = TRUE;
  shape[0].tetra_shapes = 1;

  shape[0].cube[0].pt[0].x = -.6;
  shape[0].cube[0].pt[0].y = -.6;
  shape[0].cube[0].pt[0].z = .6;
  shape[0].cube[0].pt[1].x = .6;
  shape[0].cube[0].pt[1].y = -.6;
  shape[0].cube[0].pt[1].z = .6;
  shape[0].cube[0].pt[2].x = .6;
  shape[0].cube[0].pt[2].y = .6;
  shape[0].cube[0].pt[2].z = .6;
  shape[0].cube[0].pt[3].x = -.6;
  shape[0].cube[0].pt[3].y = .6;
  shape[0].cube[0].pt[3].z = .6;

  shape[0].cube[0].pt[4].x = -.6;
  shape[0].cube[0].pt[4].y = -.6;
  shape[0].cube[0].pt[4].z = -.6;
  shape[0].cube[0].pt[5].x = .6;
  shape[0].cube[0].pt[5].y = -.6;
  shape[0].cube[0].pt[5].z = -.6;
  shape[0].cube[0].pt[6].x = .6;
  shape[0].cube[0].pt[6].y = .6;
  shape[0].cube[0].pt[6].z = -.6;
  shape[0].cube[0].pt[7].x = -.6;
  shape[0].cube[0].pt[7].y = .6;
  shape[0].cube[0].pt[7].z = -.6;
  shape[0].cube_calculated = TRUE;
  shape[0].cube_shapes = 1;

  #/* Set the GLUT Callback Functions */
  ####glutKeyboardFunc(KeyPressed);       /* catch keypresses */
  glutMouseFunc(MouseClick);          #/* catch mouse clicks */
  glutMotionFunc(MouseDrag);          #/* catch mouse drags */
  glutReshapeFunc(ReshapeWindow);     #/* catch window resize events */
  glutDisplayFunc(UpdateDisplay);     #/* set the display updater function */
  glutIdleFunc(IdleFunction);         #/* function called when idle */
  glutMainLoop();  #/* once called, main() is never returned to */

  return 0;        #/* required by ANSI C */
