
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*
   Fractal popcorn
*/

#define width 1000
#define height 1000

int main(int argc,char **argv) 
{
   int i,j,ix,iy,n,N,M;
   double scale = 1;
   double hconst = 0.05;
   double x,y,xnew,ynew;

   if (argc < 5) {
      fprintf(stderr,"Usage: %s scale N M hconst\n",argv[0]);
      exit(-1);
   }
   scale = atof(argv[1]); // Width of image in world coordinates
   N = atoi(argv[2]); // Number of points to draw, eg: 100
   M = atoi(argv[3]); // Density of sampling the image as initial conditions
   hconst = atof(argv[4]);

   for (i=0;i<width;i+=M) {
      for (j=0;j<height;j+=M) {

         // Seed pixel, mapping from pixels to world coordinates
         x = 2 * scale * (i - width / 2) / width;
         y = 2 * scale * (j - height / 2) / height;

         // Iterate for N points
         for (n=0;n<N;n++) {

            // Calculate next point in the series
            xnew = x - hconst * sin(y + tan(3 * y));
            ynew = y - hconst * sin(x + tan(3 * x));

            // Make up some colour mapping
            printf ("color=n %d\n", n);
            //colour = GetColour((double)n,0.0,(double)N,1);
            //bc.r = colour.r*255;
            //bc.g = colour.g*255;
            //bc.b = colour.b*255;

            // Mapping from world coordinates to image pixel cordinates
            ix = 0.5 * xnew * width / scale + width / 2;
            iy = 0.5 * ynew * height / scale + height / 2; 

            // Draw the pixel if it is in bounds
            if (ix >= 0 && iy >= 0 && ix < width && iy < height)
               printf(" %d width=%d ix=%d iy=%d\n", width,height,ix,iy);

            x = xnew;
            y = ynew;
         }
      }
   }

   printf("%g_%d,%d_%g.tga",scale,N,M,hconst);

   exit(0);
}


