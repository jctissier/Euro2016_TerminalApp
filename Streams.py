#!/usr/bin/python
import praw
import re
from termcolor import colored, cprint
import sys
import webbrowser


# variables
user_agent = ("Link Getter")
r = praw.Reddit(user_agent=user_agent)


def login():
    r.login('REDDIT_USERNAME', 'REDDIT_PASSWORD', disable_warning=True)
    #Enter REDDIT USERNAME AND REDDIT PASSWORD
    # NEEDED TO SEARCH FOR ALL THE LINKS

    print_login = colored("Logging in...\n", 'yellow')
    print(print_login)

def footballHighlights():
    subreddit = r.get_subreddit("footballhighlights")

    for submission in subreddit.get_hot(limit=15):
        print("Highlight:", submission.title)

    print_input1 = colored("Which game highlights do you want?\n")
    highlight = raw_input(print_input1)
    cprint ("~~~~~~HOLD COMMAND + DOUBLE CLICK = Open link in browser ~~~~~~,'red')

    for submission in subreddit.get_hot(limit=80):
        if re.search(highlight, submission.title, re.IGNORECASE):
            print("\nTitle: ", submission.title)
            comments = submission.comments
            for comment in comments[0:1]:  # first comment is a bot moderator
                print(comment.body)  # prints top comments starting from 2nd top comment
                print("\n")

    restartProgram()

def sportLinks():
    subreddit = r.get_subreddit("soccerstreams")

    test = colored("Live games that you can stream...\n", 'yellow')
    print(test)

    for submission in subreddit.get_hot(limit=12):
        print("Game Name:", submission.title)

    print_input5 = colored("\n\nName of the game you want to watch: \n", 'red', attrs=['bold'])

    user_input = raw_input(print_input5)
    for submission in subreddit.get_hot(limit=12):
        if re.search(user_input, submission.title, re.IGNORECASE):
            print("Title: ", submission.title)
            print("Link: ", submission.url)
            print("Pick your link!")

            comments = submission.comments
            for comment in comments[1:3]:  # first comment is a bot moderator
                print(comment.body)  # prints top comments starting from 2nd top comment
                print("\n")

    restartProgram()

def restartProgram():
    print_restart = colored("Do you need any other links?\nHighlights 'h', Soccer Streams 's', Logout 'L', Main Menu 'MM'\n", 'red',
                            attrs=['bold'])         # restart search if needed
    restart = raw_input(print_restart)

    while (restart != "h" and restart != "H" and restart != "s" and restart != "S" and restart != "l" and restart != "L" and restart != "mm"
           and restart != "MM"):  # testing for wrong user input
        print_restart = colored("Highlights 'h', Soccer Streams 's', Logout 'L', Main Menu 'MM'\n", 'red',
            attrs=['bold'])  # restart search if needed
        restart = raw_input(print_restart)
        restartProgram()

    if (restart == "h" or restart == "H"):
        footballHighlights()
    if (restart == "s" or restart == "S"):
        sportLinks()
    if (restart == "l" or restart == "L"):
        print("Bye")
        sys.exit()



