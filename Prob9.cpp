#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <chrono>

// Defines the function f(x)
double f(double xi) 
{
    return ( 100*exp(-10*xi) );
}

int main()//int argc, char* argv[]) // Expects number of steps to be specified by user 
{
    // Start measuring time
    auto t1 = std::chrono::high_resolution_clock::now();

    int n_steps = 1000000; // I change n_steps manually (admittedly not the most elegant solution)

    double a = -1.; // Subdiagonal
    double b =  2.; // Diagonal
    double c = -1.; // Superdiagonal
    double ac = a*c;

    std::vector<double> v(n_steps); // v[0] = v0, v[n_steps] = v_n. 
    std::vector<double> g(n_steps-2); // g[0] = g_1, g[n_steps-2] = g(n-1)
    std::vector<double> x(n_steps); // x[0] = x0, x[n_steps] = x_n. 

    std::vector<double> b_(n_steps-2); // b-hat;    b_[0] = b-hat_1, b_(n_steps-2) = b-hat_(n-1)
    std::vector<double> g_(n_steps-2); // g-hat;    g_[0] = g-hat_1, g_(n_steps-2) = g-hat_(n-1)
    
    double x_min = 0.; 
    double x_max = 1.;
    double h = (x_max - x_min) / n_steps; // Step length

    // Fill in x and g
    x[0] = x_min; 
    x[n_steps] = x_max;
    for (int i = 0; i <= n_steps-2; i++)
    {
        x[i+1] = x[i] + h; 
        g[i] = f( x[i+1] )*(h*h); // Generally we must add v0 to g1=g[0] and vN to g(N-1)=g[N-2], but we know that v0=0.
    }

    // Forward substitution 
    b_[0] = b;
    g_[0] = g[0];
    for (int i = 1; i <= n_steps-2; i++)
    {
        b_[i] = b - (ac/b_[i-1]); // ac is one variable
        g_[i] = g[i] - (a/b_[i-1])*g_[i-1];
    }

    // Backward substitution
    v[0] = 0; 
    v[n_steps] = 0;
    v[n_steps-1] = g_[n_steps-2]/b_[n_steps-2];
    for (int i = n_steps-2; i >= 1; i--)
    {
        v[i] = (g_[i-1] - c*v[i+1])/b_[i-1];
    }


    //set a filename
    std::string filename = "Prob7.txt";

    // Create and open the output file. 
    std::ofstream ofile;
    ofile.open(filename);

    // Width and precission parameters to format output
    int width = 16;
    int prec = 5;

    // loop over steps
    for (int i = 0; i <= n_steps; i++)
    {
        //write line for x_i, v(x_i)
        ofile << std::setw(width) << std::setprecision(prec) << std::scientific << x[i]
            << std::setw(width) << std::setprecision(prec) << std::scientific << v[i] 
            << std::endl;
    }

    // Close output file 
    ofile.close();

    // Stop measuring time
    auto t2 = std::chrono::high_resolution_clock::now();

    // Calculate the elapsed time
    double duration_seconds = std::chrono::duration<double>(t2 - t1).count();
    std::cout << duration_seconds;

    return 0;
}