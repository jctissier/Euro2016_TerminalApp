import Stats
import Streams
from termcolor import colored, cprint


def Euro2016():
    input_color = colored("Please choose from the following options:\nStats 'S', Highlights 'H', Live Streams 'L', Exit 'E'\n",'red',attrs=['bold'])
    Choose_menu = input(input_color)

    while (Choose_menu != "s" and Choose_menu != "S" and Choose_menu != "h" and Choose_menu != "H" and Choose_menu != "l"
           and Choose_menu != "L" and Choose_menu != "E" and Choose_menu != "e"):
        Choose_menu = input("Please choose from the following options:\nStats 'S', Highlights 'H', Live Streams 'L'\n")

    if (Choose_menu == "s" or Choose_menu == "S"):
        Stats.Choose_Menu()
        Restart_Menu()

    if (Choose_menu == "H" or Choose_menu == "h"):
        Streams.footballHighlights()
        Restart_Menu()

    if (Choose_menu == "l" or Choose_menu == "L"):
        Streams.sportLinks()
        Restart_Menu()

    if (Choose_menu == "E" or Choose_menu == "e"):
        Stats.Logout()

def Restart_Menu():
    Euro2016()

#Runs entire program
Streams.login()
Euro2016()