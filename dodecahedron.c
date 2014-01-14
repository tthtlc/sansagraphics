/*
Dodecahedron

The "C" pseudo code to generate the vertices is:

*/
#include <math.h>

void polygon(

generate_dodecahedron(){

  double vertices[20][3]; /* 20 vertices with x, y, z coordinate */
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
