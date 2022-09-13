#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <cmath>

int main()
{
  //set a filename
  std::string filename = "Prob2.txt";

  // Create and open the output file. 
  std::ofstream ofile;
  ofile.open(filename);

  // Set parameters for computation
  double x_min = 0.0;
  double x_max = 1.0; 
  int n_steps = 100; 
  double h = (x_max - x_min) / n_steps;

  // Width and precission parameters to format output
  int width = 16;
  int prec = 5;

  // x_0, u(x_0)
  double x = x_min;
  double u = 1 - (1-exp(-10))*x - exp(-10*x); 

  // loop over steps
  for (int i = 0; i <= n_steps; i++)
  {
    //write line for x_i, u(x_i)
    ofile << std::setw(width) << std::setprecision(prec) << std::scientific << x
          << std::setw(width) << std::setprecision(prec) << std::scientific << u 
          << std::endl;

    // next x and u value
    x += h; 
    u = 1 - (1-exp(-10))*x - exp(-10*x); 
  }

  // Close output file 
  ofile.close();

  return 0;
}