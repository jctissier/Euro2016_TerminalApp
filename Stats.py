#see live scores, schedules and group standings for Euro 2016
from lxml import html
import requests
from termcolor import colored, cprint
import sys

#links
page = requests.get('http://www.livescores.com/euro/fixtures/')
tree = html.fromstring(page.content)

groups = requests.get('http://www.livescore.com/euro/tables/')
groupRankings = html.fromstring(groups.content)

def Choose_Menu():
    menu = colored("Standings 'S', Fixtures 'F', Main Menu 'MM', Logout 'L'\n",'red',attrs=['bold'])
    choose_menu = input(menu)
    while (choose_menu != "S" and choose_menu != "s" and choose_menu != "f" and choose_menu!= "F" and
           choose_menu != "TS" and choose_menu != "ts" and choose_menu != "TA" and choose_menu != "ta"
           and choose_menu != "mm" and choose_menu != "MM" and choose_menu != "l" and choose_menu != "L"):
        choose_menu = input(menu)

    if (choose_menu == "S" or choose_menu == "s"):
        pickStandings()
    if (choose_menu == "F" or choose_menu == "f"):
        pickScheduleGroup()
    if (choose_menu == "l" or choose_menu == "L"):
        Logout()
    if (choose_menu == "MM" or choose_menu == "mm"):
        print ("Back to Main Menu:")
    #TS + TA


def Fixtures():
    # A - green B - blue C - red D - yellow E - cyan F - magenta
    cprint(" G   DATE       TIME       GAME             SCORE       ", 'red', attrs=['underline'])
    gameA = tree.xpath('(//html / body / div[2] / div[5] / div[2]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameA)),'green')
    gameA = tree.xpath('(//html / body / div[2] / div[5] / div[3]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameA)),'green')
    gameB = tree.xpath('(//html / body / div[2] / div[5] / div[4]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameB)),'blue')
    gameB = tree.xpath('(//html / body / div[2] / div[5] / div[5]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameB)),'blue')
    gameD = tree.xpath('(//html / body / div[2] / div[5] / div[6]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameD)),'yellow')
    gameC = tree.xpath('(//html / body / div[2] / div[5] / div[7]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameC)),'red')
    gameC = tree.xpath('(//html / body / div[2] / div[5] / div[8]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameC)),'red')
    gameD = tree.xpath('(//html / body / div[2] / div[5] / div[9]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameD)), 'yellow')
    gameE = tree.xpath('(//html / body / div[2] / div[5] / div[10]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameE)),'cyan')
    gameE = tree.xpath('(//html / body / div[2] / div[5] / div[11]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameE)),'cyan')
    gameF = tree.xpath('(//html / body / div[2] / div[5] / div[12]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameF)),'magenta')
    gameF = tree.xpath('(//html / body / div[2] / div[5] / div[13]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameF)),'magenta')
    gameB = tree.xpath('(//html / body / div[2] / div[5] / div[14]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameB)),'blue')
    gameA = tree.xpath('(//html / body / div[2] / div[5] / div[15]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameA)),'green')
    gameA = tree.xpath('(//html / body / div[2] / div[5] / div[16]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameA)),'green')
    gameB = tree.xpath('(//html / body / div[2] / div[5] / div[17]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameB)),'blue')
    gameC = tree.xpath('(//html / body / div[2] / div[5] / div[18]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameC)),'red')
    gameC = tree.xpath('(//html / body / div[2] / div[5] / div[19]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameC)),'red')
    gameE = tree.xpath('(//html / body / div[2] / div[5] / div[20]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameE)),'cyan')
    gameD = tree.xpath('(//html / body / div[2] / div[5] / div[21]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameD)),'yellow')
    gameD = tree.xpath('(//html / body / div[2] / div[5] / div[22]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameD)),'yellow')
    gameE = tree.xpath('(//html / body / div[2] / div[5] / div[23]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameE)),'cyan')
    gameF = tree.xpath('(//html / body / div[2] / div[5] / div[24]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameF)),'magenta')
    gameF = tree.xpath('(//html / body / div[2] / div[5] / div[25]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameF)),'magenta')
    gameA = tree.xpath('(//html / body / div[2] / div[5] / div[26]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameA)),'green')
    gameA = tree.xpath('(//html / body / div[2] / div[5] / div[27]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameA)),'green')
    gameB = tree.xpath('(//html / body / div[2] / div[5] / div[28]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameB)),'blue')
    gameB = tree.xpath('(//html / body / div[2] / div[5] / div[29]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameB)),'blue')
    gameC = tree.xpath('(//html / body / div[2] / div[5] / div[30]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameC)),'red')
    gameC = tree.xpath('(//html / body / div[2] / div[5] / div[31]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameC)),'red')
    gameD = tree.xpath('(//html / body / div[2] / div[5] / div[32]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameD)),'yellow')
    gameD = tree.xpath('(//html / body / div[2] / div[5] / div[33]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameD)),'yellow')
    gameF = tree.xpath('(//html / body / div[2] / div[5] / div[34]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameF)),'magenta')
    gameF = tree.xpath('(//html / body / div[2] / div[5] / div[35]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameF)),'magenta')
    gameE = tree.xpath('(//html / body / div[2] / div[5] / div[36]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameE)),'cyan')
    gameE = tree.xpath('(//html / body / div[2] / div[5] / div[37]//text())[position()>4 and not(position()=6)]')
    cprint("".join(map(str, gameE)),'cyan')

def FixturesGroup():
    gameA1 = tree.xpath('(//html / body / div[2] / div[5] / div[2]//text())[position()>4 and not(position()=6)]')
    gameA2 = tree.xpath('(//html / body / div[2] / div[5] / div[3]//text())[position()>4 and not(position()=6)]')
    gameB1 = tree.xpath('(//html / body / div[2] / div[5] / div[4]//text())[position()>4 and not(position()=6)]')
    gameB2 = tree.xpath('(//html / body / div[2] / div[5] / div[5]//text())[position()>4 and not(position()=6)]')
    gameD1 = tree.xpath('(//html / body / div[2] / div[5] / div[6]//text())[position()>4 and not(position()=6)]')
    gameC1 = tree.xpath('(//html / body / div[2] / div[5] / div[7]//text())[position()>4 and not(position()=6)]')
    gameC2 = tree.xpath('(//html / body / div[2] / div[5] / div[8]//text())[position()>4 and not(position()=6)]')
    gameD2 = tree.xpath('(//html / body / div[2] / div[5] / div[9]//text())[position()>4 and not(position()=6)]')
    gameE1 = tree.xpath('(//html / body / div[2] / div[5] / div[10]//text())[position()>4 and not(position()=6)]')
    gameE2 = tree.xpath('(//html / body / div[2] / div[5] / div[11]//text())[position()>4 and not(position()=6)]')
    gameF1 = tree.xpath('(//html / body / div[2] / div[5] / div[12]//text())[position()>4 and not(position()=6)]')
    gameF2 = tree.xpath('(//html / body / div[2] / div[5] / div[13]//text())[position()>4 and not(position()=6)]')
    gameB3 = tree.xpath('(//html / body / div[2] / div[5] / div[14]//text())[position()>4 and not(position()=6)]')
    gameA3 = tree.xpath('(//html / body / div[2] / div[5] / div[15]//text())[position()>4 and not(position()=6)]')
    gameA4 = tree.xpath('(//html / body / div[2] / div[5] / div[16]//text())[position()>4 and not(position()=6)]')
    gameB4 = tree.xpath('(//html / body / div[2] / div[5] / div[17]//text())[position()>4 and not(position()=6)]')
    gameC3 = tree.xpath('(//html / body / div[2] / div[5] / div[18]//text())[position()>4 and not(position()=6)]')
    gameC4 = tree.xpath('(//html / body / div[2] / div[5] / div[19]//text())[position()>4 and not(position()=6)]')
    gameE3 = tree.xpath('(//html / body / div[2] / div[5] / div[20]//text())[position()>4 and not(position()=6)]')
    gameD3 = tree.xpath('(//html / body / div[2] / div[5] / div[21]//text())[position()>4 and not(position()=6)]')
    gameD4 = tree.xpath('(//html / body / div[2] / div[5] / div[22]//text())[position()>4 and not(position()=6)]')
    gameE4 = tree.xpath('(//html / body / div[2] / div[5] / div[23]//text())[position()>4 and not(position()=6)]')
    gameF3 = tree.xpath('(//html / body / div[2] / div[5] / div[24]//text())[position()>4 and not(position()=6)]')
    gameF4 = tree.xpath('(//html / body / div[2] / div[5] / div[25]//text())[position()>4 and not(position()=6)]')
    gameA5 = tree.xpath('(//html / body / div[2] / div[5] / div[26]//text())[position()>4 and not(position()=6)]')
    gameA6 = tree.xpath('(//html / body / div[2] / div[5] / div[27]//text())[position()>4 and not(position()=6)]')
    gameB5 = tree.xpath('(//html / body / div[2] / div[5] / div[28]//text())[position()>4 and not(position()=6)]')
    gameB6 = tree.xpath('(//html / body / div[2] / div[5] / div[29]//text())[position()>4 and not(position()=6)]')
    gameC5 = tree.xpath('(//html / body / div[2] / div[5] / div[30]//text())[position()>4 and not(position()=6)]')
    gameC6 = tree.xpath('(//html / body / div[2] / div[5] / div[31]//text())[position()>4 and not(position()=6)]')
    gameD5 = tree.xpath('(//html / body / div[2] / div[5] / div[32]//text())[position()>4 and not(position()=6)]')
    gameD6 = tree.xpath('(//html / body / div[2] / div[5] / div[33]//text())[position()>4 and not(position()=6)]')
    gameF5 = tree.xpath('(//html / body / div[2] / div[5] / div[34]//text())[position()>4 and not(position()=6)]')
    gameF6 = tree.xpath('(//html / body / div[2] / div[5] / div[35]//text())[position()>4 and not(position()=6)]')
    gameE5 = tree.xpath('(//html / body / div[2] / div[5] / div[36]//text())[position()>4 and not(position()=6)]')
    gameE6 = tree.xpath('(//html / body / div[2] / div[5] / div[37]//text())[position()>4 and not(position()=6)]')

    choose = colored ("Fixtures by GROUP [Stats Menu 'SM', Main Menu 'MM', Logout 'L']\n'A' 'B' 'C' 'D' 'E' 'F' or All Groups 'ALL'\n", 'red', attrs=['bold'])
    chooseGroup = input(choose)
    while (chooseGroup != "A" and chooseGroup != "B" and chooseGroup != "C" and chooseGroup != "D" and chooseGroup != "E"
        and chooseGroup != "F" and chooseGroup != "a" and chooseGroup != "b" and chooseGroup != "c" and chooseGroup != "d"
           and chooseGroup != "e" and chooseGroup != "f" and chooseGroup != "ALL" and chooseGroup != "all" and
               chooseGroup != "l" and chooseGroup != "L" and chooseGroup != "team" and chooseGroup != "Team" and
                   chooseGroup != "TEAM" and chooseGroup != "sm" and chooseGroup != "SM" and chooseGroup != "MM" and
           chooseGroup != "mm"):
        chooseGroup = input(choose)

    if chooseGroup == "l" or chooseGroup == "L":
        Logout()

    if chooseGroup == "team" or chooseGroup == "Team" or chooseGroup == "TEAM":
        FixturesTeam()

    if chooseGroup == "sm" or chooseGroup == "SM":
        Choose_Menu()

    if chooseGroup == "MM" or chooseGroup == "mm":
        print("Back to Main Menu:")

    if chooseGroup == "A" or chooseGroup == "a":
        cprint(" G   DATE       TIME       GAME             SCORE       ", 'red', attrs=['underline'])
        print("".join(map(str, gameA1)))
        print("".join(map(str, gameA2)))
        print("".join(map(str, gameA3)))
        print("".join(map(str, gameA4)))
        print("".join(map(str, gameA5)))
        print("".join(map(str, gameA6)))
        print('\n')
        pickScheduleGroup()

    if chooseGroup == "B" or chooseGroup == "b":
        cprint(" G   DATE       TIME       GAME             SCORE       ", 'red', attrs=['underline'])
        print("".join(map(str, gameB1)))
        print("".join(map(str, gameB2)))
        print("".join(map(str, gameB3)))
        print("".join(map(str, gameB4)))
        print("".join(map(str, gameB5)))
        print("".join(map(str, gameB6)))
        print('\n')
        pickScheduleGroup()

    if chooseGroup == "C" or chooseGroup == "c":
        cprint(" G   DATE       TIME       GAME             SCORE       ", 'red', attrs=['underline'])
        print("".join(map(str, gameC1)))
        print("".join(map(str, gameC2)))
        print("".join(map(str, gameC3)))
        print("".join(map(str, gameC4)))
        print("".join(map(str, gameC5)))
        print("".join(map(str, gameC6)))
        print('\n')
        pickScheduleGroup()

    if chooseGroup == "D" or chooseGroup == "d":
        cprint(" G   DATE       TIME       GAME             SCORE       ", 'red', attrs=['underline'])
        print("".join(map(str, gameD1)))
        print("".join(map(str, gameD2)))
        print("".join(map(str, gameD3)))
        print("".join(map(str, gameD4)))
        print("".join(map(str, gameD5)))
        print("".join(map(str, gameD6)))
        print('\n')
        pickScheduleGroup()

    if chooseGroup == "E" or chooseGroup == "e":
        cprint(" G   DATE       TIME       GAME             SCORE       ", 'red', attrs=['underline'])
        print("".join(map(str, gameE1)))
        print("".join(map(str, gameE2)))
        print("".join(map(str, gameE3)))
        print("".join(map(str, gameE4)))
        print("".join(map(str, gameE5)))
        print("".join(map(str, gameE6)))
        print('\n')
        pickScheduleGroup()

    if chooseGroup == "F" or chooseGroup == "f":
        cprint(" G   DATE       TIME       GAME             SCORE       ", 'red', attrs=['underline'])
        print("".join(map(str, gameF1)))
        print("".join(map(str, gameF2)))
        print("".join(map(str, gameF3)))
        print("".join(map(str, gameF4)))
        print("".join(map(str, gameF5)))
        print("".join(map(str, gameF6)))
        print('\n')
        pickScheduleGroup()

    if chooseGroup == "ALL" or chooseGroup == "all":
        cprint(" G   DATE       TIME       GAME             SCORE       ", 'red', attrs=['underline'])
        print("".join(map(str, gameA1)))
        print("".join(map(str, gameA2)))
        print("".join(map(str, gameA3)))
        print("".join(map(str, gameA4)))
        print("".join(map(str, gameA5)))
        print("".join(map(str, gameA6)))
        print('\n')
        print("".join(map(str, gameB1)))
        print("".join(map(str, gameB2)))
        print("".join(map(str, gameB3)))
        print("".join(map(str, gameB4)))
        print("".join(map(str, gameB5)))
        print("".join(map(str, gameB6)))
        print('\n')
        print("".join(map(str, gameC1)))
        print("".join(map(str, gameC2)))
        print("".join(map(str, gameC3)))
        print("".join(map(str, gameC4)))
        print("".join(map(str, gameC5)))
        print("".join(map(str, gameC6)))
        print('\n')
        print("".join(map(str, gameD1)))
        print("".join(map(str, gameD2)))
        print("".join(map(str, gameD3)))
        print("".join(map(str, gameD4)))
        print("".join(map(str, gameD5)))
        print("".join(map(str, gameD6)))
        print('\n')
        print("".join(map(str, gameE1)))
        print("".join(map(str, gameE2)))
        print("".join(map(str, gameE3)))
        print("".join(map(str, gameE4)))
        print("".join(map(str, gameE5)))
        print("".join(map(str, gameE6)))
        print('\n')
        print("".join(map(str, gameF1)))
        print("".join(map(str, gameF2)))
        print("".join(map(str, gameF3)))
        print("".join(map(str, gameF4)))
        print("".join(map(str, gameF5)))
        print("".join(map(str, gameF6)))
        print('\n')
        pickScheduleGroup()

def pickScheduleGroup():
    FixturesGroup()

def FixturesTeam():
    gameA1 = tree.xpath('(//html / body / div[2] / div[5] / div[2]//text())[position()>4 and not(position()=6)]')
    gameA2 = tree.xpath('(//html / body / div[2] / div[5] / div[3]//text())[position()>4 and not(position()=6)]')
    gameB1 = tree.xpath('(//html / body / div[2] / div[5] / div[4]//text())[position()>4 and not(position()=6)]')
    gameB2 = tree.xpath('(//html / body / div[2] / div[5] / div[5]//text())[position()>4 and not(position()=6)]')
    gameD1 = tree.xpath('(//html / body / div[2] / div[5] / div[6]//text())[position()>4 and not(position()=6)]')
    gameC1 = tree.xpath('(//html / body / div[2] / div[5] / div[7]//text())[position()>4 and not(position()=6)]')
    gameC2 = tree.xpath('(//html / body / div[2] / div[5] / div[8]//text())[position()>4 and not(position()=6)]')
    gameD2 = tree.xpath('(//html / body / div[2] / div[5] / div[9]//text())[position()>4 and not(position()=6)]')
    gameE1 = tree.xpath('(//html / body / div[2] / div[5] / div[10]//text())[position()>4 and not(position()=6)]')
    gameE2 = tree.xpath('(//html / body / div[2] / div[5] / div[11]//text())[position()>4 and not(position()=6)]')
    gameF1 = tree.xpath('(//html / body / div[2] / div[5] / div[12]//text())[position()>4 and not(position()=6)]')
    gameF2 = tree.xpath('(//html / body / div[2] / div[5] / div[13]//text())[position()>4 and not(position()=6)]')
    gameB3 = tree.xpath('(//html / body / div[2] / div[5] / div[14]//text())[position()>4 and not(position()=6)]')
    gameA3 = tree.xpath('(//html / body / div[2] / div[5] / div[15]//text())[position()>4 and not(position()=6)]')
    gameA4 = tree.xpath('(//html / body / div[2] / div[5] / div[16]//text())[position()>4 and not(position()=6)]')
    gameB4 = tree.xpath('(//html / body / div[2] / div[5] / div[17]//text())[position()>4 and not(position()=6)]')
    gameC3 = tree.xpath('(//html / body / div[2] / div[5] / div[18]//text())[position()>4 and not(position()=6)]')
    gameC4 = tree.xpath('(//html / body / div[2] / div[5] / div[19]//text())[position()>4 and not(position()=6)]')
    gameE3 = tree.xpath('(//html / body / div[2] / div[5] / div[20]//text())[position()>4 and not(position()=6)]')
    gameD3 = tree.xpath('(//html / body / div[2] / div[5] / div[21]//text())[position()>4 and not(position()=6)]')
    gameD4 = tree.xpath('(//html / body / div[2] / div[5] / div[22]//text())[position()>4 and not(position()=6)]')
    gameE4 = tree.xpath('(//html / body / div[2] / div[5] / div[23]//text())[position()>4 and not(position()=6)]')
    gameF3 = tree.xpath('(//html / body / div[2] / div[5] / div[24]//text())[position()>4 and not(position()=6)]')
    gameF4 = tree.xpath('(//html / body / div[2] / div[5] / div[25]//text())[position()>4 and not(position()=6)]')
    gameA5 = tree.xpath('(//html / body / div[2] / div[5] / div[26]//text())[position()>4 and not(position()=6)]')
    gameA6 = tree.xpath('(//html / body / div[2] / div[5] / div[27]//text())[position()>4 and not(position()=6)]')
    gameB5 = tree.xpath('(//html / body / div[2] / div[5] / div[28]//text())[position()>4 and not(position()=6)]')
    gameB6 = tree.xpath('(//html / body / div[2] / div[5] / div[29]//text())[position()>4 and not(position()=6)]')
    gameC5 = tree.xpath('(//html / body / div[2] / div[5] / div[30]//text())[position()>4 and not(position()=6)]')
    gameC6 = tree.xpath('(//html / body / div[2] / div[5] / div[31]//text())[position()>4 and not(position()=6)]')
    gameD5 = tree.xpath('(//html / body / div[2] / div[5] / div[32]//text())[position()>4 and not(position()=6)]')
    gameD6 = tree.xpath('(//html / body / div[2] / div[5] / div[33]//text())[position()>4 and not(position()=6)]')
    gameF5 = tree.xpath('(//html / body / div[2] / div[5] / div[34]//text())[position()>4 and not(position()=6)]')
    gameF6 = tree.xpath('(//html / body / div[2] / div[5] / div[35]//text())[position()>4 and not(position()=6)]')
    gameE5 = tree.xpath('(//html / body / div[2] / div[5] / div[36]//text())[position()>4 and not(position()=6)]')
    gameE6 = tree.xpath('(//html / body / div[2] / div[5] / div[37]//text())[position()>4 and not(position()=6)]')

    fixtures = colored("What team fixtures do you need? List of teams 'list', Stats Menu 'SM', Main Menu 'MM', Logout 'L' \n",'red',attrs=['bold'])
    fixtures_team = input(fixtures) ## add these

    while(fixtures_team != "france" and fixtures_team != "France" and fixtures_team != "Albania" and
                  fixtures_team != "albania" and fixtures_team != "Switzerland" and fixtures_team != "switzerland"
        and fixtures_team != "Romania" and fixtures_team != "romania" and fixtures_team != "england"
        and fixtures_team != "England" and fixtures_team != "russia" and
                  fixtures_team != "Russia" and fixtures_team != "slovakia" and fixtures_team != "Slovakia"
        and fixtures_team != "wales" and fixtures_team != "Wales" and fixtures_team != "germany"
        and fixtures_team != "Germany" and fixtures_team != "poland" and
                  fixtures_team != "Poland" and fixtures_team != "ukraine" and fixtures_team != "Ukraine"
        and fixtures_team != "Nothern Ireland" and fixtures_team != "nothern ireland"
        and  fixtures_team != "Croatia" and fixtures_team != "croatia" and fixtures_team != "Czech" and
                  fixtures_team != "czech" and fixtures_team != "Czech Replublic"
        and fixtures_team != "czech republic" and fixtures_team != "spain" and fixtures_team != "Spain" and fixtures_team != "turkey"
        and fixtures_team != "Turkey" and fixtures_team != "belgium" and fixtures_team != "Belgium"
        and fixtures_team != "Ireland" and fixtures_team != "ireland" and fixtures_team != "Italy"
        and fixtures_team != "italy" and fixtures_team != "Sweden" and fixtures_team != "sweden"
        and fixtures_team != "austria" and fixtures_team != "Austria" and fixtures_team != "Hungary" and
                  fixtures_team != "hungary" and fixtures_team != "Iceland" and fixtures_team != "iceland"
        and fixtures_team != "portugal" and fixtures_team != "Portugal" and fixtures_team != "list"
          and fixtures_team != "List" and fixtures_team != "MM" and fixtures_team != "mm" and fixtures_team != "sm"
          and fixtures_team != "SM"):

        fixtures_team = input(fixtures)

    if (fixtures_team == "sm" or fixtures_team == "SM"):
        Choose_Menu()

    if (fixtures_team == "list" or fixtures_team == "List"):
        teamList()
        FixturesTeam()

    if (fixtures_team == "MM" or fixtures_team == "mm"):
        print ("Back to Main Menu:")

    if (fixtures_team == "L" or fixtures_team == "l"):
        Logout()

    if (fixtures_team == "france" or fixtures_team == "France"):
        print("".join(map(str, gameA1)))
        print("".join(map(str, gameA4)))
        print("".join(map(str, gameA6)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "albania" or fixtures_team == "Albania"):
        print("".join(map(str, gameA2)))
        print("".join(map(str, gameA4)))
        print("".join(map(str, gameA5)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "romania" or fixtures_team == "Romania"):
        print("".join(map(str, gameA1)))
        print("".join(map(str, gameA3)))
        print("".join(map(str, gameA5)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "switzerland" or fixtures_team == "Switzerland"):
        print("".join(map(str, gameA2)))
        print("".join(map(str, gameA3)))
        print("".join(map(str, gameA6)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "England" or fixtures_team == "england"):
        print("".join(map(str, gameB2)))
        print("".join(map(str, gameB4)))
        print("".join(map(str, gameB6)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Russia" or fixtures_team == "russia"):
        print("".join(map(str, gameB2)))
        print("".join(map(str, gameB3)))
        print("".join(map(str, gameB5)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Slovakia" or fixtures_team == "slovakia"):
        print("".join(map(str, gameB1)))
        print("".join(map(str, gameB3)))
        print("".join(map(str, gameB6)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Wales" or fixtures_team == "wales"):
        print("".join(map(str, gameB1)))
        print("".join(map(str, gameB4)))
        print("".join(map(str, gameB5)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Germany" or fixtures_team == "germany"):
        print("".join(map(str, gameC2)))
        print("".join(map(str, gameC4)))
        print("".join(map(str, gameC5)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Northern Ireland" or fixtures_team == "northern ireland"):
        print("".join(map(str, gameC1)))
        print("".join(map(str, gameC3)))
        print("".join(map(str, gameC4)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Poland" or fixtures_team == "poland"):
        print("".join(map(str, gameC1)))
        print("".join(map(str, gameC4)))
        print("".join(map(str, gameC6)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "ukraine" or fixtures_team == "Ukraine"):
        print("".join(map(str, gameC2)))
        print("".join(map(str, gameC3)))
        print("".join(map(str, gameC6)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Croatia" or fixtures_team == "croatia"):
        print("".join(map(str, gameD1)))
        print("".join(map(str, gameD3)))
        print("".join(map(str, gameD5)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Czech Republic" or fixtures_team == "czech republic" or fixtures_team == "czech" or
    fixtures_team == "Czech"):
        print("".join(map(str, gameD2)))
        print("".join(map(str, gameD3)))
        print("".join(map(str, gameD6)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Spain" or fixtures_team == "spain"):
        print("".join(map(str, gameD2)))
        print("".join(map(str, gameD4)))
        print("".join(map(str, gameD5)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Turkey" or fixtures_team == "turkey"):
        print("".join(map(str, gameD1)))
        print("".join(map(str, gameD4)))
        print("".join(map(str, gameD6)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Belgium" or fixtures_team == "belgium"):
        print("".join(map(str, gameE2)))
        print("".join(map(str, gameE4)))
        print("".join(map(str, gameE6)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Italy" or fixtures_team == "italy"):
        print("".join(map(str, gameE2)))
        print("".join(map(str, gameE3)))
        print("".join(map(str, gameE5)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Ireland" or fixtures_team == "ireland"):
        print("".join(map(str, gameE1)))
        print("".join(map(str, gameE4)))
        print("".join(map(str, gameE5)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Sweden" or fixtures_team == "sweden"):
        print("".join(map(str, gameE1)))
        print("".join(map(str, gameE3)))
        print("".join(map(str, gameE6)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Austria" or fixtures_team == "austria"):
        print("".join(map(str, gameF1)))
        print("".join(map(str, gameF4)))
        print("".join(map(str, gameF6)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Hungary" or fixtures_team == "hungary"):
        print("".join(map(str, gameF1)))
        print("".join(map(str, gameF3)))
        print("".join(map(str, gameF5)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Iceland" or fixtures_team == "iceland"):
        print("".join(map(str, gameF2)))
        print("".join(map(str, gameF3)))
        print("".join(map(str, gameF6)))
        print('\n')
        FixturesTeam()

    if (fixtures_team == "Portugal" or fixtures_team == "portugal"):
        print("".join(map(str, gameF2)))
        print("".join(map(str, gameF4)))
        print("".join(map(str, gameF5)))
        print('\n')
        FixturesTeam()


def pickStandings():
    pick = colored("Pick standings by: 'ALL' 'GROUP' 'TEAM' , or Stats Menu 'SM', Logout 'L'\n", 'red',attrs=['bold'])
    pickStandings = input(pick)
    while (pickStandings != "All" and pickStandings != "all" and pickStandings != "Group" and pickStandings != "group"
           and pickStandings != "GROUP" and pickStandings != "TEAM" and pickStandings != "team" and pickStandings != "Team"
           and pickStandings != "SM" and pickStandings != "l" and pickStandings != "L"and pickStandings != "All"
           and pickStandings != "sm"):
        pickStandings = input(pick)

    if (pickStandings == "ALL" or pickStandings == "all" or pickStandings == "All"):
        GroupAllStandings()
        restartStandings()
    if (pickStandings == "GROUP" or pickStandings == "group" or pickStandings == "Group"):
        GroupStandings()
        restartStandings()
    if (pickStandings == "TEAM" or pickStandings == "team" or pickStandings == "Team"):
        TeamStandings()
        restartStandings()
    if (pickStandings == "SM" or pickStandings == "sm"):
        Choose_Menu()
    if (pickStandings == "l" or pickStandings == "L"):
        print("Back to Main Menu")

def Logout():
    print("Bye")
    sys.exit()


def restartStandings():
    pickStandings()

def GroupStandings():
    pick = colored("Which Group? [Stats Menu 'SM', Logout 'L']\n 'A' 'B' 'C' 'D' 'E' 'F'\n",'red', attrs=['bold'])
    pickGroup = input(pick)
    while (pickGroup != "A" and pickGroup != "a" and pickGroup != "B" and pickGroup != "b" and pickGroup != "C" and
                   pickGroup != "c" and pickGroup != "D" and pickGroup != "d" and pickGroup != "E" and pickGroup != "e" and
                   pickGroup != "F" and pickGroup != "f" and pickGroup != "sm" and pickGroup != "SM" and pickGroup != "L" and pickGroup != "l"):
        pickGroup = input(pick)

    if pickGroup == "l" or pickGroup == "L":
        Logout()

    if pickGroup == "SM" or pickGroup == "sm":
        Choose_Menu()

    if pickGroup == "A" or pickGroup == "a":
        GroupAStandings()
        pickStandings()
    if pickGroup == "B" or pickGroup == "b":
        GroupBStandings()
        pickStandings()
    if pickGroup == "C" or pickGroup == "c":
        GroupCStandings()
        pickStandings()
    if pickGroup == "D" or pickGroup == "D":
        GroupDStandings()
        pickStandings()
    if pickGroup == "E" or pickGroup == "E":
        GroupEStandings()
        pickStandings()
    if pickGroup == "F" or pickGroup == "f":
        GroupFStandings()
        pickStandings()


def GroupAStandings():
    GroupA1 =groupRankings.xpath('//html/body/div[2]/div[5]/div[2]/div[2]//text()')
    GroupA2 =groupRankings.xpath('//html/body/div[2]/div[5]/div[2]/div[3]//text()')
    GroupA3 =groupRankings.xpath('//html/body/div[2]/div[5]/div[2]/div[4]//text()')
    GroupA4 =groupRankings.xpath('//html/body/div[2]/div[5]/div[2]/div[5]//text()')

    cprint("GroupA   Pts  P   GD   TEAM       ",'red',attrs=['underline'])
    print('  ' +GroupA1[3]+'.     ' + GroupA1[24] + '    ' + GroupA1[10] + '   ' + GroupA1[22]+ '    ' + GroupA1[7])
    print('  ' +GroupA2[3]+'.     ' + GroupA2[24] + '    ' + GroupA2[10] + '   ' + GroupA2[22]+ '    ' + GroupA2[7])
    print('  ' +GroupA3[3]+'.     ' + GroupA3[24] + '    ' + GroupA3[10] + '   ' + GroupA3[22]+ '    ' + GroupA3[7])
    print('  ' +GroupA4[3]+'.     ' + GroupA4[24] + '    ' + GroupA4[10] + '   ' + GroupA4[22]+ '    ' + GroupA4[7])
    print("\n")


def GroupBStandings():
    GroupB1 =groupRankings.xpath('//html/body/div[2]/div[5]/div[3]/div[2]//text()')
    GroupB2 =groupRankings.xpath('//html/body/div[2]/div[5]/div[3]/div[3]//text()')
    GroupB3 =groupRankings.xpath('//html/body/div[2]/div[5]/div[3]/div[4]//text()')
    GroupB4 =groupRankings.xpath('//html/body/div[2]/div[5]/div[3]/div[5]//text()')

    cprint("GroupB   Pts  P   GD   TEAM       ",'red',attrs=['underline'])
    print('  ' +GroupB1[3]+'.     ' + GroupB1[24] + '    ' + GroupB1[10] + '   ' + GroupB1[22]+ '    ' + GroupB1[7])
    print('  ' +GroupB2[3]+'.     ' + GroupB2[24] + '    ' + GroupB2[10] + '   ' + GroupB2[22]+ '    ' + GroupB2[7])
    print('  ' +GroupB3[3]+'.     ' + GroupB3[24] + '    ' + GroupB3[10] + '   ' + GroupB3[22]+ '    ' + GroupB3[7])
    print('  ' +GroupB4[3]+'.     ' + GroupB4[24] + '    ' + GroupB4[10] + '   ' + GroupB4[22]+ '    ' + GroupB4[7])
    print("\n")

def GroupCStandings():
    GroupC1 =groupRankings.xpath('//html/body/div[2]/div[5]/div[4]/div[2]//text()')
    GroupC2 =groupRankings.xpath('//html/body/div[2]/div[5]/div[4]/div[3]//text()')
    GroupC3 =groupRankings.xpath('//html/body/div[2]/div[5]/div[4]/div[4]//text()')
    GroupC4 =groupRankings.xpath('//html/body/div[2]/div[5]/div[4]/div[5]//text()')

    cprint("GroupC   Pts  P   GD   TEAM       ",'red',attrs=['underline'])
    print('  ' +GroupC1[3]+'.     ' + GroupC1[24] + '    ' + GroupC1[10] + '   ' + GroupC1[22]+ '    ' + GroupC1[7])
    print('  ' +GroupC2[3]+'.     ' + GroupC2[24] + '    ' + GroupC2[10] + '   ' + GroupC2[22]+ '    ' + GroupC2[7])
    print('  ' +GroupC3[3]+'.     ' + GroupC3[24] + '    ' + GroupC3[10] + '   ' + GroupC3[22]+ '    ' + GroupC3[7])
    print('  ' +GroupC4[3]+'.     ' + GroupC4[24] + '    ' + GroupC4[10] + '   ' + GroupC4[22]+ '    ' + GroupC4[7])
    print("\n")

def GroupDStandings():
    GroupD1 =groupRankings.xpath('//html/body/div[2]/div[5]/div[5]/div[2]//text()')
    GroupD2 =groupRankings.xpath('//html/body/div[2]/div[5]/div[5]/div[3]//text()')
    GroupD3 =groupRankings.xpath('//html/body/div[2]/div[5]/div[5]/div[4]//text()')
    GroupD4 =groupRankings.xpath('//html/body/div[2]/div[5]/div[5]/div[5]//text()')

    cprint("GroupD   Pts  P   GD   TEAM       ",'red',attrs=['underline'])
    print('  ' +GroupD1[3]+'.     ' + GroupD1[24] + '    ' + GroupD1[10] + '   ' + GroupD1[22]+ '    ' + GroupD1[7])
    print('  ' +GroupD2[3]+'.     ' + GroupD2[24] + '    ' + GroupD2[10] + '   ' + GroupD2[22]+ '    ' + GroupD2[7])
    print('  ' +GroupD3[3]+'.     ' + GroupD3[24] + '    ' + GroupD3[10] + '   ' + GroupD3[22]+ '    ' + GroupD3[7])
    print('  ' +GroupD4[3]+'.     ' + GroupD4[24] + '    ' + GroupD4[10] + '   ' + GroupD4[22]+ '    ' + GroupD4[7])
    print("\n")

def GroupEStandings():
    GroupE1 =groupRankings.xpath('//html/body/div[2]/div[5]/div[5]/div[2]//text()')
    GroupE2 =groupRankings.xpath('//html/body/div[2]/div[5]/div[5]/div[3]//text()')
    GroupE3 =groupRankings.xpath('//html/body/div[2]/div[5]/div[5]/div[4]//text()')
    GroupE4 =groupRankings.xpath('//html/body/div[2]/div[5]/div[5]/div[5]//text()')

    cprint("GroupE   Pts  P   GD   TEAM       ",'red',attrs=['underline'])
    print('  ' +GroupE1[3]+'.     ' + GroupE1[24] + '    ' + GroupE1[10] + '   ' + GroupE1[22]+ '    ' + GroupE1[7])
    print('  ' +GroupE2[3]+'.     ' + GroupE2[24] + '    ' + GroupE2[10] + '   ' + GroupE2[22]+ '    ' + GroupE2[7])
    print('  ' +GroupE3[3]+'.     ' + GroupE3[24] + '    ' + GroupE3[10] + '   ' + GroupE3[22]+ '    ' + GroupE3[7])
    print('  ' +GroupE4[3]+'.     ' + GroupE4[24] + '    ' + GroupE4[10] + '   ' + GroupE4[22]+ '    ' + GroupE4[7])
    print("\n")

def GroupFStandings():
    GroupF1 =groupRankings.xpath('//html/body/div[2]/div[5]/div[5]/div[2]//text()')
    GroupF2 =groupRankings.xpath('//html/body/div[2]/div[5]/div[5]/div[3]//text()')
    GroupF3 =groupRankings.xpath('//html/body/div[2]/div[5]/div[5]/div[4]//text()')
    GroupF4 =groupRankings.xpath('//html/body/div[2]/div[5]/div[5]/div[5]//text()')

    cprint("GroupF   Pts  P   GD   TEAM       ",'red',attrs=['underline'])
    print('  ' +GroupF1[3]+'.     ' + GroupF1[24] + '    ' + GroupF1[10] + '   ' + GroupF1[22]+ '    ' + GroupF1[7])
    print('  ' +GroupF2[3]+'.     ' + GroupF2[24] + '    ' + GroupF2[10] + '   ' + GroupF2[22]+ '    ' + GroupF2[7])
    print('  ' +GroupF3[3]+'.     ' + GroupF3[24] + '    ' + GroupF3[10] + '   ' + GroupF3[22]+ '    ' + GroupF3[7])
    print('  ' +GroupF4[3]+'.     ' + GroupF4[24] + '    ' + GroupF4[10] + '   ' + GroupF4[22]+ '    ' + GroupF4[7])

def GroupAllStandings():
    GroupAStandings()
    GroupBStandings()
    GroupCStandings()
    GroupDStandings()
    GroupEStandings()
    GroupFStandings()
    print ("\n")

def TeamStandings():
    search = colored("What team are you looking for? Type 'list' for a list of all the countries, Stats Menu 'SM', Logout 'L'\n",'red', attrs=['bold'])
    Search_TeamName = input(search)

    while(Search_TeamName != "france" and Search_TeamName != "France" and Search_TeamName != "Albania" and
        Search_TeamName != "albania" and Search_TeamName != "Switzerland" and Search_TeamName != "switzerland"
        and Search_TeamName != "Romania" and Search_TeamName != "romania" and Search_TeamName != "england"
        and Search_TeamName != "England" and Search_TeamName != "russia" and
        Search_TeamName != "Russia" and Search_TeamName != "slovakia" and Search_TeamName != "Slovakia"
        and Search_TeamName != "wales" and Search_TeamName != "Wales" and Search_TeamName != "germany"
        and Search_TeamName != "Germany" and Search_TeamName != "poland" and
        Search_TeamName != "Poland" and Search_TeamName != "ukraine" and Search_TeamName != "Ukraine"
        and Search_TeamName != "Nothern Ireland" and Search_TeamName != "nothern ireland"
        and  Search_TeamName != "Croatia" and Search_TeamName != "croatia" and Search_TeamName != "Czech" and
        Search_TeamName != "czech" and Search_TeamName != "Czech Replublic"
        and Search_TeamName != "czech republic" and Search_TeamName != "spain" and Search_TeamName != "Spain" and Search_TeamName != "turkey"
        and Search_TeamName != "Turkey" and Search_TeamName != "belgium" and Search_TeamName != "Belgium"
        and Search_TeamName != "Ireland" and Search_TeamName != "ireland" and Search_TeamName != "Italy"
        and Search_TeamName != "italy" and Search_TeamName != "Sweden" and Search_TeamName != "sweden"
        and Search_TeamName != "austria" and Search_TeamName != "Austria" and Search_TeamName != "Hungary" and
        Search_TeamName != "hungary" and Search_TeamName != "Iceland" and Search_TeamName != "iceland"
        and Search_TeamName != "portugal" and Search_TeamName != "Portugal" and Search_TeamName != "list"
          and Search_TeamName != "List" and Search_TeamName != "sm" and Search_TeamName != "SM" and Search_TeamName != "L" and Search_TeamName != "l"):

        Search_TeamName = input("Please be more specific\nex: 'France' 'Germany' 'Czech' 'Northern Ireland' etc..[Stats Menu 'SM', Logout 'L']\n")

    if (Search_TeamName == "l" or Search_TeamName == "L"):
        Logout()

    if (Search_TeamName == "SM" or Search_TeamName == "sm"):
        Choose_Menu()

    if (Search_TeamName == "list" or Search_TeamName == "List"):
        print('\n')
        teamList()
        TeamStandings()

    if (Search_TeamName == "france" or Search_TeamName == "France" or Search_TeamName == "Albania" or
                Search_TeamName == "albania" or Search_TeamName == "Switzerland" or Search_TeamName == "switzerland"
        or Search_TeamName == "Romania" or Search_TeamName == "romania"):
        GroupAStandings()

    if (Search_TeamName == "england" or Search_TeamName == "England" or Search_TeamName == "russia" or
               Search_TeamName == "Russia" or Search_TeamName == "slovakia" or Search_TeamName == "Slovakia"
        or Search_TeamName == "wales" or Search_TeamName == "Wales"):
        GroupBStandings()

    if (Search_TeamName == "germany" or Search_TeamName == "Germany" or Search_TeamName == "poland" or
                Search_TeamName == "Poland" or Search_TeamName == "ukraine" or Search_TeamName == "Ukraine"
        or Search_TeamName == "Nothern Ireland" or Search_TeamName == "nothern ireland"):
        GroupCStandings()

    if (Search_TeamName == "Croatia" or Search_TeamName == "croatia" or Search_TeamName == "Czech" or
                Search_TeamName == "czech" or Search_TeamName == "Czech Replublic" or Search_TeamName == "czech republic"
        or Search_TeamName == "spain" or Search_TeamName == "Spain"or Search_TeamName == "turkey" or Search_TeamName == "Turkey"):
        GroupDStandings()

    if (Search_TeamName == "belgium" or Search_TeamName == "Belgium" or Search_TeamName == "Ireland" or
                Search_TeamName == "ireland" or Search_TeamName == "Italy" or Search_TeamName == "italy"
        or Search_TeamName == "Sweden" or Search_TeamName == "sweden"):
        GroupEStandings()

    if (Search_TeamName == "austria" or Search_TeamName == "Austria" or Search_TeamName == "Hungary" or
                Search_TeamName == "hungary" or Search_TeamName == "Iceland" or Search_TeamName == "iceland"
        or Search_TeamName == "portugal" or Search_TeamName == "Portugal"):
        GroupFStandings()

def teamList():
    print(
    'Albania              Poland\n'
    'Austria              Portugal\n'
    'Beligum              Ireland\n'
    'Croatia              Romania\n'
    'Czech Republic       Russia\n'
    'England              Slovakia\n'
    'France               Spain\n'
    'Germany              Sweden\n'
    'Hungary              Switzerland\n'
    'Iceland              Turkey\n'
    'Italy                Ukraine\n'
    'Northern Ireland     Wales\n'
    )

#Fix Fixtures by Group