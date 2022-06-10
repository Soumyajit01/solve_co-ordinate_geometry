"""
This code is for solving the problems related to co-ordinate geometry. The points will take only integers, not any variables.

findDist()- This function is for finding the distance between two points

internalDivision()- This function is for finding the co-ordinates of the point that divides two points in the ratio m:n INTERNALLY

externalDivision()- This function is for finding the co-ordinates of the point that divides two points into the ratio m:n EXTERNALLY

triangleCentroid()- This function is for finding the co-ordinates of the centroid of a triangle

midPoint()- This function is for finding the mid point between two points

areaOfTriangle()- This function is for finding the area of a triangle
"""

import math


def findDist(pt1, pt2):
    """
    pt1 = (x1,y1); 
    pt2 = (x2,y2)
    """
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print(f"The distance between the 2 points is {dist} units.")


findDist((0, 0), (3, 4))


def internalDivision(ratio, pt1, pt2):
    """
    ratio = (m,n);
    pt1 = (x1, y1);
    pt2=(x2, y2);
    """
    m, n = ratio[0], ratio[1]
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    # Now, we will create a point P which divides the line segment into the ratio- m:n internally. The next step is to find the co-ordinates of point 'P'
    P_x = int(((m*x2 + n*x1)/(m+n)))  # (mx2+nx1)/(m+n)
    P_y = int(((m*y2 + n*y1)/(m+n)))  # (my2+ny1)/(m+n)
    print(f"Co-ordinates of the point: ({P_x}, {P_y})")


internalDivision((-3, 2), (4, 6), (3, 5))


def externalDivision(ratio, pt1, pt2):
    """
    ratio = (m,n);
    pt1 = (x1, y1);
    pt2=(x2, y2);
    """
    m, n = ratio[0], ratio[1]
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    # Now, we will create a point P which divides the line segment into the ratio- m:n externally. The next step is to find the co-ordinates of point 'P'
    P_x = int(((m*x2 - n*x1)/(m-n)))  # (mx2-nx1)/(m-n)
    P_y = int(((m*y2 - n*y1)/(m-n)))  # (my2-ny1)/(m-n)
    print(f"Co-ordinates of the point: ({P_x}, {P_y})")


externalDivision((3, 2), (-1, 2), (4, -5))


def triangleCentroid(pt1, pt2, pt3):
    """
    pt1 = (x1,y1); 
    pt2 = (x2,y2); 
    pt3 = (x3, y3);
    """
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    x3, y3 = pt3[0], pt3[1]
    # Let the centroid be the point 'O'
    O_x = int((x1+x2+x3)/3)
    O_y = int((y1+y2+y3)/3)
    print(f"Co-ordinate of the centroid is ({O_x}, {O_y})")


triangleCentroid((4, -3), (-5, 2), (1, 1))

def midPoint(pt1, pt2):
    """
    pt1 = (x1,y1); 
    pt2 = (x2,y2);
    """
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    # Let the mid point be on the point 'O'
    O_x = int((x1+x2)/2)
    O_y = int((y1+y2)/2)
    print(f"Co-ordinates of the mid point is ({O_x}, {O_y})")

midPoint((6,0), (0,7))


def areaOfTriangle(pt1, pt2, pt3):
    """
    pt1 = (x1,y1); 
    pt2 = (x2,y2); 
    pt3 = (x3, y3)
    """
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    x3, y3 = pt3[0], pt3[1]
    area = 1/2* abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
    print(f"Area of triangle is {area} sq. units")

areaOfTriangle((2, -2), (4, 2), (-1, 3))
