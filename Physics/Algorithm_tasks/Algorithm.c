/*
To determine the diameter of a lead sphere, it was weighed on a balance,
obtaining the result 5.2 grmas. Calculate the diameter of the sphere and the
relative errors of the direct measurement of its weight and the measurement
of the composite diameter.

Created by @AdrianSzklarski, 10.2023
*/

#include <stdio.h>
#include <math.h>
#define M_PI 3.14159265358979323846

float calculate(float m, int ro, float e_a, float e_a2)
{
    float x, power, Fi, e_m, e_mp, e_fi, e_fip;

    x = (6*m)/(M_PI*ro);
    power = (float) 1/3;
    Fi = pow(x, power)*1000;

    // Determination of the relative error of mass measurement and diameter measurement
   
    e_m = e_a / m;
    e_mp = e_m * 100;
    e_fi = e_a2 / Fi;
    e_fip = e_fi * 100;

    printf("Diameter Fi [mm]              : %.2lf\n", Fi);
    printf("Relative error                : %.7lf\n", e_m);
    printf("Relative error [P]            : %.2lf\n", e_mp);
    printf("Error diameter measurement    : %.6lf\n", e_fi);
    printf("Error diameter measurement [P]: %.2lf\n", e_fip);
}

int main()
{
    float e_a, e_a2, fi, m, power; 
    int ro;
    // Absolute error as the sensitivity of the measuring instrument [kg]
    e_a = 0.01 * 1e-3;
    e_a2 = 0.1;
    
    // Mass [kg]
    m = 5.2*1e-3;

    // Density of lead [kg/m^3]
    ro =11300;

    calculate(m, ro, e_a, e_a2);

    return 0;
}