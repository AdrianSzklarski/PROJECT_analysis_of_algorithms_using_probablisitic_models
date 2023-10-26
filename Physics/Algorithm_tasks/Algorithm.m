% To determine the diameter of a lead sphere, it was weighed on a balance, 
% obtaining the result 5.2 grmas. Calculate the diameter of the sphere and the 
% relative errors of the direct measurement of its weight and the measurement 
% of the composite diameter. 

% Created by @AdrianSzklarski, 10.2023

% clc;
% clear all;
% close all; 

% Absolute error as the sensitivity of the measuring instrument [kg]
e_a = 0.01 * 1e-3;
e_a2 = 0.1;

% Mass [kg]
m = 5.2 * 1e-3;

% Density of lead [kg/m^3]
ro =11300;

% Calculation

x = (6*m)/(pi*ro);
Fi = round(nthroot(x,3)*1000*100)/100;

% Results:
res_Fi = ['Diameter Fi [mm]              : ', num2str(Fi)];

% Determination of the relative error of mass measurement and 
%diameter measurement

e_m = ['Relative error                : ', num2str(e_a / m)];
e_m100 = round((e_a / m)*100*100)/100;
e_mp = ['Relative error [%]            : ', num2str(e_m100)];


e_fi = ['Error diameter measurement    : ', num2str(e_a2 / (Fi))]; 
e_fi100 = round((e_a2/(Fi))*100*100)/100;
e_fip = ['Error diameter measurement [%]: ', num2str(e_fi100)]; 

% Results
disp(res_Fi)
disp(e_m)
disp(e_mp)
disp(e_fi)
disp(e_fip)