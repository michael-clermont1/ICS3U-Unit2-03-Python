#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Feb 2022
# This program calculates the circumference of a circle
#    with radius inputted by the user and tau

import constants


def main():
    # this function calculates the circumference

    # input
    radius = int(input("Enter the radius of the circle (mm): "))

    # process
    circumference = radius * constants.TAU

    # output
    print("")
    print("Circumference is {0} mm.".format(circumference))

    print("\nDone.")


if __name__ == "__main__":
    main()
