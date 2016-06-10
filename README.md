# Euro2016_TerminalApp_Mac
If you love Soccer/Football and you want to always be up-to-date with the EURO 2016, this program is perfect for you. 

**All you need to do is replace REDDIT_USERNAME AND REDDIT_PASSWORD in line #15 of Streams.py with your own Reddit username and password.** 

#Functionalities
Get live soccer/football streams, highlights and live stats for EURO 2016 directly from your terminal! (MAC)
  1. Find any live soccer/football streams within 3 seconds
  2. Find any EURO2016 highlights within 3 seconds
  3. Browse through live stats about the EURO 2016, fixtures, standings, etc...

![alt text] (/Documentation/live-stream.gif) 
![alt text] (/Documentation/Highlights.gif) 
![alt text] (/Documentation/Fixtures.gif)
![alt text] (/Documentation/Standings.gif)
![alt text](/Documentation/Program%20Directory.png)

#Build from Source:
```
$ git clone https://github.com/jctissier/Euro2016_TerminalApp.git
$ cd Euro2016_TerminalApp
```

#Modules to Install:
Open Mac terminal and write the statements below
  - Pip
```
$sudo easy_install pip
```
  - Praw
```
$pip install praw
```
  - Termcolor
```
$pip install termcolor
```
  - Lxml
```
$pip install lxml
```
  
#For people who havn't run python scripts through terminal before:
  1. Download the folder and move it to your desktop
  2. Before you run the scripts, Open Streams.py, go to line 15 and change 'username' and 'password' to your Reddit Username and Password
  3. Open terminal and type: 

    1. $cd  user/Desktop/Euro2016_TerminalApp
    2. $python3 Main_Menu.py         OR        python Main_Menu.py     
    3. *depends what python version you are running*
      
  4. Once you see a menu with different options, everything is working!

#User Input is not Case Sensitive
Navigating through the different menus within the app, it is not case sensitive:

"What team do you want to see the stats for? 'ALL' 'GROUP' 'TEAM'       
  1. you can search by group, team or see a list of all of the teams
  2. You can type: 'all' or 'ALL', 'group' or 'GROUP' 
![alt text] (/Documentation/User_input.gif)
![alt text] (/Documentation/User_input2.gif)


This is my first time writing a python application, if you have any tips on how I can improve it or have any questions, shoot me a message!
  
