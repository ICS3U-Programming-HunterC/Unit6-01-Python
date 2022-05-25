#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: May 19, 2022
# This program generates 10 random numbers between 1 and 100 and
# displays them to the user and then finds the average of all
# the numbers

import random


def main():
    # declare constants
    MAX_SIZE = 10
    MAX_NUM = 100
    MIN_NUM = 0

    # create an empty list
    array_of_num = []

    for counter in range(0, MAX_SIZE):
        # generate random number
        random_number = random.randint(MIN_NUM, MAX_NUM)

        # add the number to the list
        array_of_num.append(random_number)

        # print the random number generated and the position it is in the list
        print(
            "{} added to the list at position {}".format(array_of_num[counter], counter)
        )

    sum = 0

    # find the total of all the numbers
    for counter in range(0, MAX_SIZE):
        sum = sum + array_of_num[counter]

    # calculate the averages
    avg = sum / MAX_SIZE
    print()
    print("The average is: {}".format(avg))


if __name__ == "__main__":
    main()
