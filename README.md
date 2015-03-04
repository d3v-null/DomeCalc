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
- **DomeCalc.preset_2V** A 2V dome. 
- **DomeCalc.preset_3V3** A 3V dome truncated at 3/8- 
- **DomeCalc.preset_3V5** A 3V dome truncated at 5/8
- **DomeCalc.preset_3VK4** A 3V dome modified using the krushke method truncated at 4/9
- **DomeCalc.preset_3VK5** A 3V dome modified using the krushke method truncated at 5/9
- **DomeCalc.preset_4V** A 4V dome

## Radius
The geometric radius of the dome (as opposed to the floor radius, internal radius, external radius)
## Strut Adjustment
The length that has to added to (positive value) or removed from (negative value) the "geometric" length of each strut to account for the joining method used. The geometric length is the length "bolt to bolt" and the adjustment is the additional length added to the strut so that the bolt holes can be drilled
## Master Length
The length of the pipes that you are cutting the struts from: typically 6000mm, 6100mm, 6500mm

# Examples
## example.py
Example dome: 4.3m radius 4V steel dome (40mm adjustment) cut out of 6100mm lengths gives:

``` python
Number of lengths: 55
solution makeup:
 10 x [3, 4, 4, 4]
 15 x [3, 3, 3, 3]
 30 x [0, 1, 2, 2, 5]
 ```

 Where 0...5 represent A..B lengths

 ## example-plot.py
An example of how to generate csv files that can be used to plot how many lengths it takes to make a dome of a given radius 
