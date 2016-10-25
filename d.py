"""This exercise will help us increase the abstraction of our code.
Instead of just defininig a function that draws a square, and then a function
that draws a triangle, let's see how they are similar and what parts we can
abstract to make it more useful.

Let's write a function that will creat a regular polygon of N sides.
We also have to have a parameter for the Sidelength(s)
We also have to take into account the angle will change when the number of sides
change."""

# You will need to import turtle and create a turtle

"""
1.   If the total angles must add up to 360 degrees, then how can we use N to
determine what angle it should be?

*Hint:  For 3 sides the angle is 120, for 4 sides the angle is 90.
3 * 120 = 360 ; 4 * 90 = 360
Therefore N * (theta) = 360.  What's (theta)?
"""




"""
2.  Create a function that will take into account 3 parameters: N, anyTurtle, s
and create a regular polygon of sidelength(s) and number of sides N.
"""

def regularPoly(N, anyTurtle, s):



"""
3.  Create a loop that will call your function each time through the loop.
Start with N = 12 and stop with N = 3.  Use a While loop for this:

N = 12
while N >= 3:
    regularPoly(N, anyTurtle, s)  # You need to put in S and anyTurtle here
    N = N - 1

"""

    
