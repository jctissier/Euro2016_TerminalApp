#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Stats
import Streams
from termcolor import colored, cprint


def euro_2016():
    input_color = colored("Please choose from the following options:\n"
                          "Stats 'S', Highlights 'H', Live Streams 'L', "
                          "Exit 'E'\n", 'red', attrs=['bold'])

    # prompt user for input
    choose_menu = input(input_color).lower()

    if (choose_menu == "s"):
        Stats.choose_menu()
        euro_2016()

    elif (choose_menu == "h"):
        Streams.footballHighlights()
        euro_2016()

    elif (choose_menu == "l"):
        Streams.sportLinks()
        euro_2016()

    elif (choose_menu == "e"):
        Stats.Logout()

    # user must have entered invalid option
    else:
        euro_2016()


if __name__ == "__main__":
    # If this file is program entry point, execute:
    Streams.login()
    euro_2016()
