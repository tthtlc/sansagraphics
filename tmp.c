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

Dodecahedron

The "C" pseudo code to generate the vertices is:

  double vertices[20][3]; /* 20 vertices with x, y, z coordinate */
  double Pi = 3.141592653589793238462643383279502884197;

  double phiaa = 52.62263590; /* the two phi angles needed for generation */
  double phibb = 10.81231754;

  r = 1.0; /* any radius in which the polyhedron is inscribed */
  phia = Pi*phiaa/180.0; /* 4 sets of five points each */
  phib = Pi*phibb/180.0;
  phic = Pi*(-phibb)/180.0;
  phid = Pi*(-phiaa)/180.0;
  the72 = Pi*72.0/180;
  theb = the72/2.0; /* pairs of layers offset 36 degrees */
  the = 0.0;
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
  polygon(0,1,2,3,4);

  polygon(0,1,6,10,5);
  polygon(1,2,7,11,6);
  polygon(2,3,8,12,7);
  polygon(3,4,9,13,8);
  polygon(4,0,5,14,9);

  polygon(15,16,11,6,10);
  polygon(16,17,12,7,11);
  polygon(17,18,13,8,12);
  polygon(18,19,14,9,13);
  polygon(19,15,10,5,14);
  
  polygon(15,16,17,18,19);

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

Octahedron

The "C" pseudo code to generate the vertices is:

  double vertices[6][3]; /* 6 vertices with x, y, z coordinate */
  double Pi = 3.141592653589793238462643383279502884197;

  double phiaa  = 0.0; /* the phi needed for generation */
  r = 1.0; /* any radius in which the polyhedron is inscribed */
  phia = Pi*phiaa/180.0; /* 1 set of four points */
  the90 = Pi*90.0/180;
  vertices[0][0]=0.0;
  vertices[0][1]=0.0;
  vertices[0][2]=r;

  vertices[5][0]=0.0;
  vertices[5][1]=0.0;
  vertices[5][2]=-r;

  the = 0.0;
  for(i=1; i<5; i++)
  {
    vertices[i][0]=r*cos(the)*cos(phia);
    vertices[i][1]=r*sin(the)*cos(phia);
    vertices[i][2]=r*sin(phia);
    the = the+the90;
  }

  /* map vertices to 8 faces */
  polygon(0,1,2);
  polygon(0,2,3);
  polygon(0,3,4);
  polygon(0,4,1);
  polygon(5,1,2);
  polygon(5,2,3);
  polygon(5,3,4);
  polygon(5,4,1);

The octahedron coordinates:

 Vertex       coordinate
   0,   x= 0.000, y= 0.000, z= 1.000 
   1,   x= 1.000, y= 0.000, z= 0.000 
   2,   x= 0.000, y= 1.000, z= 0.000 
   3,   x=-1.000, y= 0.000, z= 0.000 
   4,   x= 0.000, y=-1.000, z= 0.000 
   5,   x= 0.000, y= 0.000, z=-1.000 

Length of each edge 1.414213562 

Icosahedron

The "C" pseudo code to generate the vertices is:

  double vertices[12][3]; /* 12 vertices with x, y, z coordinates */
  double Pi = 3.141592653589793238462643383279502884197;

  double phiaa  = 26.56505; /* phi needed for generation */
  r = 1.0; /* any radius in which the polyhedron is inscribed */
  phia = Pi*phiaa/180.0; /* 2 sets of four points */
  theb = Pi*36.0/180.0;  /* offset second set 36 degrees */
  the72 = Pi*72.0/180;   /* step 72 degrees */
  vertices[0][0]=0.0;
  vertices[0][1]=0.0;
  vertices[0][2]=r;
  vertices[11][0]=0.0;
  vertices[11][1]=0.0;
  vertices[11][2]=-r;
  the = 0.0;
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


