/*
Icosahedron

The "C" pseudo code to generate the vertices is:
*/

generate_icosahedron(){

  int i, j, k;
  double vertices[12][3]; /* 12 vertices with x, y, z coordinates */
  double Pi = 3.141592653589793238462643383279502884197;

  double phiaa  = 26.56505; /* phi needed for generation */
  double r = 1.0; /* any radius in which the polyhedron is inscribed */
  double phia = Pi*phiaa/180.0; /* 2 sets of four points */
  double theb = Pi*36.0/180.0;  /* offset second set 36 degrees */
  double the72 = Pi*72.0/180;   /* step 72 degrees */

  vertices[0][0]=0.0;
  vertices[0][1]=0.0;
  vertices[0][2]=r;
  vertices[11][0]=0.0;
  vertices[11][1]=0.0;
  vertices[11][2]=-r;
  double the = 0.0;
  for(i=1; i<6; i++)
  {
    vertices[i][0]=r*cos(the)*cos(phia);
    vertices[i][1]=r*sin(the)*cos(phia);
    vertices[i][2]=r*sin(phia);
    the = the+the72;
  }
  the=theb;
  for(i=6; i<11; i++)
  {
    vertices[i][0]=r*cos(the)*cos(-phia);
    vertices[i][1]=r*sin(the)*cos(-phia);
    vertices[i][2]=r*sin(-phia);
    the = the+the72;
  }

  /* map vertices to 20 faces */
  polygon(0,1,2);
  polygon(0,2,3);
  polygon(0,3,4);
  polygon(0,4,5);
  polygon(0,5,1);
  polygon(11,6,7);
  polygon(11,7,8);
  polygon(11,8,9);
  polygon(11,9,10);
  polygon(11,10,6);
  polygon(1,2,6);
  polygon(2,3,7);
  polygon(3,4,8);
  polygon(4,5,9);
  polygon(5,1,10);
  polygon(6,7,2);
  polygon(7,8,3);
  polygon(8,9,4);
  polygon(9,10,5);
  polygon(10,6,1);
}

/*
The icosahedron coordinates:

 Vertex       coordinate
   0,  x= 0.000, y= 0.000, z= 1.000 
   1,  x= 0.894, y= 0.000, z= 0.447 
   2,  x= 0.276, y= 0.851, z= 0.447 
   3,  x=-0.724, y= 0.526, z= 0.447 
   4,  x=-0.724, y=-0.526, z= 0.447 
   5,  x= 0.276, y=-0.851, z= 0.447 
   6,  x= 0.724, y= 0.526, z=-0.447 
   7,  x=-0.276, y= 0.851, z=-0.447 
   8,  x=-0.894, y= 0.000, z=-0.447 
   9,  x=-0.276, y=-0.851, z=-0.447 
  10,  x= 0.724, y=-0.526, z=-0.447 
  11,  x= 0.000, y= 0.000, z=-1.000 

Length of each edge 1.0514622 

Back to Reference Page
Last updated 6/3/05

*/
