# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: November 2022
# ICS3U-Unit5-02.py File, learning functions with parameters in python.


def area_of_triangle(base_as_float, height_as_float):

    area = base_as_float * height_as_float / 2
    print("The area of the triangle is {0:,.2f} cm²".format(area))


def main():

    base = input("Enter the base length of a triangle(cm): ")
    height = input("Enter the height of a triangle(cm): ")
    print("")
    try:
        base_as_float = float(base)
        height_as_float = float(height)
        if base_as_float <= 0 or height_as_float <= 0:
            print("A triangle cannot have a height or a base with a value that's equal or less than 0.")
        else:
            area_of_triangle(base_as_float, height_as_float)

    except ValueError:
        print("Invalid input, please try again.")
    print("\n\nDone.")


if __name__ == "__main__":
    main()
