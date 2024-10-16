# Robot Movement Simulation

## Overview

This is a simple Python script that simulates the movement of a robot on a 5x5 grid - part of a challenge from somewhere (I can't remember where!). Very simple, but fairly neat. The robot can be placed on the grid and given commands to move, rotate, and report its current position and direction. The four directions available are North, East, South, and West, and the robot follows basic movement rules within the grid's boundaries.

## Features

- The robot can move in four directions: North, East, South, and West.
- Commands include `PLACE`, `MOVE`, `LEFT`, `RIGHT`, and `REPORT`.
- The robot cannot move outside the 5x5 grid.
- The current position and direction of the robot can be displayed using the `REPORT` command.

## Commands

- `PLACE X,Y,DIRECTION`:
  Places the robot at the specified coordinates `X,Y` (0-5) and facing a specific direction (`NORTH`, `EAST`, `SOUTH`, or `WEST`). Example: `PLACE 1,2,NORTH`.
  
- `MOVE`:
  Moves the robot one unit forward in the current direction. The robot will not move if the move would cause it to fall off the grid.
  
- `LEFT`:
  Rotates the robot 90 degrees to the left (counter-clockwise).

- `RIGHT`:
  Rotates the robot 90 degrees to the right (clockwise).
  
- `REPORT`:
  Outputs the current coordinates and direction of the robot.

## How to Use

1. **Start the Simulation**:
   When the script runs, it initializes a 5x5 grid. At the start, no robot is placed on the grid.
   
2. **Place the Robot**:
   Use the `PLACE X,Y,DIRECTION` command to place the robot on the grid. You must place the robot before issuing any other commands.
   
3. **Move the Robot**:
   After placing the robot, you can issue commands like `MOVE`, `LEFT`, `RIGHT`, and `REPORT` to control its movement.

4. **Grid Layout**:
   The grid consists of 6 rows and 6 columns, indexed from 0 to 5, and the robot moves around in this space. If a move is invalid (e.g., out of bounds), an error message is displayed.

## Example Commands

```
Input Command: PLACE 1,2,EAST
Input Command: MOVE
Input Command: LEFT
Input Command: MOVE
Input Command: REPORT
```
**Output**:

```
Current Position: 0,3,NORTH
```
<br>

```
Input Command: PLACE 1,2,SOUTH
```

**Output**:

```
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⍗🠓⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛
```



## Notes

- Ensure that the robot is placed on the grid before issuing commands. 
- The grid cells are initialized as '⬛', representing an empty space.
- The robot's direction is shown with symbols:
  - North: 🠑⍐
  - East: ➡
  - South: ⍗🠓
  - West: ⬅
