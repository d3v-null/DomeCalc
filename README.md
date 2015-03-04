# DomeCalc
This script is essential for anyone building a custom geodesic dome. It helps you determine the optimal geodesic dome for your purposes by calculating the strut wastage considering the strut lengths and joiner size / strut extensions

# Status
This is just some code that I thought I would share because it could be useful to geodesic dome builders, it's by no means good code, but if there is enough interest in this repository I'll update the instructions and make it a bit nicer :P

If you have any questions just shoot me an email and I'll be happy to help

# Installation
## Prerequisites
### PVSolver
Domecalc requires a genius bit of code called PVSolver, you can get that here: https://github.com/fdabrandao/vpsolver
Just download the repository, run the compile shell script then run the setup.py python script (as root) to install the python module
### GLPK
GLPK can be found here: https://www.gnu.org/software/glpk/

If you are running OSX you will need to use the glpk macport
## Python Module
All the code you need is contained in the domecalc.py file. If you just drop that in to your usual python path, you can import domecalc file as a python module

# Usage
To use the dome calculator simply import the DomeCalc class from the domecalc module with `from domecalc import DomeCalc`
Then you can create an instance of the DomeCalc class by specifying the preset function, radius, strut adjustment and master length in the constructor. Here's what those things mean:
## Preset Function
A Preset function is a callback passed into the constructor that takes the other parameters and generates the presets for PSolver. You can provide your own but DomeCalc comes with preset functions for all the most common dome frequencies as static class functions:
DomeCalc.preset_2V
DomeCalc.preset_3V4
