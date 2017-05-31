from math import sqrt # import sqrt(square root) function from math module

# print the following:
print """
                |\\
                | \\
                |  \\
                |   \\
            s1  |    \\ hypotenuse
                |     \\
                |      \\
                |       \\
                |__ __ __\\

                    s2
"""

s1 = float(input("Side 1: ")) # set s1 variable as the input from the user in float form and print message
s2 = float(input("Side 2: ")) # set s2 variable as the input from the user in float form and print message

hypotenuse = sqrt(s1*s1 + s2*s2) # set hypotenuse variable as the square root of the sum of squared s1 and squared s2
print "Hypotenuse = %f" % hypotenuse # print message with the value of hypotenuse
