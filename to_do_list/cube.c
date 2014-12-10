/*
Cube


The "C" pseudo code to generate the vertices is:

  double vertices[8][3]; /* 8 vertices with x, y, z coordinate */
  double Pi = 3.141592653589793238462643383279502884197;

  double phiaa = 35.264391; /* the phi needed for generation */

  r = 1.0; /* any radius in which the polyhedron is inscribed */
  phia = Pi*phiaa/180.0; /* 2 sets of four points */
  phib = -phia;
  the90 = Pi*90.0/180.0;
  the = 0.0;
  for(i=0; i<4; i++)
  {
    vertices[i][0]=r*cos(the)*cos(phia);
    vertices[i][1]=r*sin(the)*cos(phia);
    vertices[i][2]=r*sin(phia);
    the = the+the90;
  }
  the=0.0;
  for(i=4; i<8; i++)
  {
    vertices[i][0]=r*cos(the)*cos(phib);
    vertices[i][1]=r*sin(the)*cos(phib);
    vertices[i][2]=r*sin(phib);
    the = the+the90;
  }

  /* map vertices to 6 faces */
  polygon(0,1,2,3);
  polygon(4,5,6,7);
  polygon(0,1,5,4);
  polygon(1,2,6,5);
  polygon(2,3,7,6);
  polygon(3,0,4,7);

The cube coordinates:

 Vertex        coordinate
   0,  x= 0.816, y= 0.000, z= 0.577 
   1,  x= 0.000, y= 0.816, z= 0.577 
   2,  x=-0.816, y= 0.000, z= 0.577 
   3,  x=-0.000, y=-0.816, z= 0.577 
   4,  x= 0.816, y= 0.000, z=-0.577 
   5,  x= 0.000, y= 0.816, z=-0.577 
   6,  x=-0.816, y= 0.000, z=-0.577 
   7,  x=-0.000, y=-0.816, z=-0.577 

Length of every edge 1.1547005 
