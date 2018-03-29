"""
===================   TASK 1   ====================
* Name: Area Of Circle
*
* Write a function `area_of_circle` that will
* return area enclosed by a circle of radius `r`.
* Consider that only float value for radius will
* be passed. Negative values should be considered
* as typo and function should ignore sign of a
* number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here

#Area of Circle
# A = Pi * (r**2)

Pi = 3.14

def area_of_circle(r):

    if (not isinstance(r, int)) and (not isinstance(r, float)):
        return -1
    if r > 0:

        return Pi*(r**2)


def main():

    povrsina = area_of_circle(2)
    print(povrsina)

main()