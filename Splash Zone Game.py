'''
Programmer: Raj Shah
Version: 1.0
Description: The first two arguments specify the x- and y-coordinates of an object. The next two specify the x- and y-coordinates of the
explosion. The final two specify the radii of the inner and outer splash zones. Based on the values given, determine whether the object falls
inside of the inner splash zone, inside of the outer splash zone, or outside of both splash zones. 
Date: July 14, 2022



pre-condition: 6 numbers entered in sets of 2 (a,b)
post-condition: 1 string

Algorithm:
Create function coordinates with parameter, prompt
    Assign x and y to the user's input
    Return x and y
While true
    Assign x_of_object to the first user input
    Assign y_of_object to the second user input
    Assign x_of_explosion to the third user input
    Assign y_of_explosion to the forth user input
    Assign radius_inner to the fifth user input
    Assign radius_outer to the sixth user input

    Assign object_in_circle to (x_of_object - x_of_explosion)^2 + (y_of_object - y_of_explosion)^2

    If object_in_circle is less than or equal to radius_inner^2
        Output that the object falls inside the inner splash zone.
    Otherwise if object_in_circle is less than or equal to radius_outer^2
        Output that object falls inside the outer splash zone.
    Else
        output that object is outside of both splash zones.

'''

def coordinates(prompt):    # create function and return inputs x, y
    x, y = eval(input(prompt))
    return x, y

while True:
    x_of_object, y_of_object = coordinates("Enter the x and y coordinates of the object (x,y): ")     # assign variables to the user's inputs using coordinates()
    x_of_explosion, y_of_explosion = coordinates("Enter the x and y coordinates of the explosion (x,y): ")
    radius_inner, radius_outer = coordinates("Enter the radius of the inner and outer explosion (inner,outer): ")

    object_in_circle = (x_of_object - x_of_explosion)**2 + (y_of_object - y_of_explosion)**2    # use the forumla to determine if the circle is inside the circle

    if object_in_circle <= radius_inner**2:       # output message if it is inside the inner circle, outer circle, or outside of both 
        print("Object falls inside the inner splash zone.\n")
    elif object_in_circle <= radius_outer**2:
        print("Object falls inside the outer splash zone.\n")
    else:
        print("Object is outside of both splash zones.\n")
