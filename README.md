# Solving Rubik's Cube with Lego Mindstorms

This is a proof-of-concept research project submitted as part of my dissertation project in partial fulfilment of the requirement for the degree of BSc Computer Science.
 

### Requirements & Installation

This project requires Python 3 and Visual Studio Build Tools for the `kociemba` package.
Third party packages used are:

```
colorama                -   colored printouts
ev3dev                  -   allows the EV3 to be used
ev3dev-lang-python      -   Python 3 on the EV3
kociemba                -   used as a fallback for solving
```

### Run the Cube Solver

This software is in two main parts: the host computer, and the EV3. Technically it can all be run on the EV3, but it will take a ridiculously long time to do anything.

To run the host computer software, either run the `main.py` file in the `Codebase` directory, or use the batchfile. Both methods take the following arguments:

- r - Connect to Robot
- d - Generates the entire Database, unless a method is specified
- c - Clear the entire database
- h - half-turn generation/solve method 
- m - multiphase generation/solve method (will fallback to `kociemba` to guarantee solve if wanted)
- t - tree solve
- v - more verbose outputs

To run the EV3, run the `main.py` file in the `robot` directory with Python 3. The IP address of the Host Computer must be changed for the sockets to properly connect.