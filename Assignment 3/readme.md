# Shape Transformation Program

This interactive Python program allows you to apply transformations to different shapes and plot them using matplotlib. The program supports two types of shapes: circles and polygons. You can perform various transformations such as translation, rotation, and scaling on these shapes.

## Getting Started

1. Clone the repository or download the source code.
2. Make sure you have Python installed on your system.
3. Open the terminal and navigate to the project directory.
4. Run the `a3.py` file using the following command:

```
python a3.py
```


## Usage

### 1. Circle

To work with a circle, choose option 1 when prompted. Enter the center coordinates (a, b) and the radius (r) of the circle.

### 2. Polygon

To work with a polygon, choose option 0 when prompted. Enter the number of sides (n) of the polygon, followed by the x and y coordinates of each vertex.

### Transformation Queries

For both circles and polygons, you can perform the following transformation queries:

1. **Translate**: T dx (dy)
   - Translates the shape by dx units along the x-axis and dy units along the y-axis.
   - If dy is not given, assume equal translation dy = dx.

2. **Rotate**: R theta (rx) (ry)
   - Rotates the shape by theta degrees clockwise (or anti-clockwise if theta is negative) around the point (rx, ry).
   - If rx and ry are not given, assume rotation from the origin.

3. **Scale**: S sx (sy)
   - Scales the shape by a factor of sx along the x-axis and sy along the y-axis.
   - In case of a polygon, if only one argument is given, assume sy = sx.
   - Scaling is done with respect to the center of the shape.

4. **Plot**: P
   - Plots the shape before and after the transformation using matplotlib.
   - Before plot is shown with a dashed line, and the after plot is shown with a solid line.

### Input Format

The program prompts for the following inputs:

1. **Verbose**: Enter 1 to plot the transformations or 0 to display only the results.
2. **Shape Type**: Enter 0 for a polygon or 1 for a circle.
3. **Polygon**:
   - Number of Sides (n)
   - Coordinates (x, y) of each vertex
4. **Circle**:
   - Center Coordinates (a, b)
   - Radius (r)
5. **Number of Queries (Q)**
6. **Transformation Queries (Q lines)**

### Output Format

For each query, the program outputs the following:

- For a circle, the before transformation (a, b, r) and the after transformation (a, b, r) values.
- For a polygon, the before transformation x and y coordinate lists and the after transformation x and y coordinate lists.
- If verbose is set to 1, the program plots the previous and current state of the shape.
