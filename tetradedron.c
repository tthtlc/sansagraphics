
Regular Polyhedron Generators


Regular Polyhedron are three dimensional objects that have
one type of regular polygon on the surface. There are only
a few:
       name        faces      face type           vertices  edges
    Tetrahedron       4   equilateral triangles      4        6
    Cube              6   squares                    8       12
    Dodecahedron     12   pentagons                 20       30
    Octahedron        8   equilateral triangles      6       12
    Icosahedron      20   equilateral triangles     12       30
    Sphere          inf   technically not a regular polyhedron

The purpose of this page is to provide the algorithm and pseudocode
to generate the vertices of each regular polyhedron.

For my convenience, all vertices will be inscribed on a sphere
of radius r, and numeric results will use r = 1.

The standard equation for points on a sphere will be used:
  x = r * cos(theta) * cos(phi)
  y = r * sin(theta) * cos(phi)
  z = r * sin(phi)
  x^2 + y^2 + z^2 = 1 for the unit sphere

  The angle theta goes around the equator 0 to 360 degrees, 0 to 2Pi
  The angle phi goes from north pole 90 to -90 degrees, Pi/2 to -Pi/2
  Radians = Pi * (angle_in_degrees) / 180

Pseudocode assumes all variables of type double except for i, j, k
which are obviously integer. The code was extracted from OpenGL
test programs similar to the commonly available "cube.c". This is
original code based on mathematics, not copied, covered by GNU
General Public License. 

Tetrahedron
Cube
Dodecahedron
Octahedron
Icosahedron

Tetrahedron

The "C" pseudo code to generate the vertices is:

*/

generate_tetrahedron(){

  double vertices[4][3]; /* 4 vertices with  x, y, z coordinate */
  double Pi = 3.141592653589793238462643383279502884197;

  double phiaa  = -19.471220333; /* the phi angle needed for generation */

  r = 1.0; /* any radius in which the polyhedron is inscribed */
  phia = Pi*phiaa/180.0; /* 1 set of three points */
  the120 = Pi*120.0/180.0;
  vertices[0][0] = 0.0;
  vertices[0][1] = 0.0;
  vertices[0][2] = r;
  the = 0.0;
  for(i=1; i<4; i++)
  {
    vertices[i][0]=r*cos(the)*cos(phia);
    vertices[i][1]=r*sin(the)*cos(phia);
    vertices[i][2]=r*sin(phia);
    the = the+the120;
  }

  /* map vertices to 4 faces */
  polygon(0,1,2);
  polygon(0,2,3);
  polygon(0,3,1);
  polygon(1,2,3);
}

/*
The tetrahedron coordinates:

 Vertex        coordinate
    0,  x= 0.000, y= 0.000, z= 1.000 
    1,  x= 0.943, y= 0.000, z=-0.333 
    2,  x=-0.471, y= 0.816, z=-0.333 
    3,  x=-0.471, y=-0.816, z=-0.333 

Length of every edge 1.6329932 
*/
