# keepChromeOpen3_low_output.py
# Made with Python 2.7.14
# by Evan Nordquist Oct 28, 2017
# Version 5.0
# New for Version 2 - Supresses MicrosoftEdge, Firefox, and old school Internet Explorer.
# New for Version 3 - Output reduced to only show errors, not a status update for every loop
# New for Version 4 - Ascii graphic logo added purely for laughs
# New for Version 5 - pyautogui added to allow keystroke commands (so we can control full screen)

######################################################################################################
# Import modules for: the operating system, the clock, the task manager, and the default web browser #
# Initialize global variables																		 #
######################################################################################################
import os
import time  
import subprocess
import webbrowser
import pyautogui  
howOftenToCheck = 2 #measured in seconds
targetPage = "https://studiocentraldisplay.weebly.com/" # Target page. If modified, remember to keep the quotation marks.
currentTasks = []
throwAway = ""

####################
# Helper Functions #
####################
def closeOtherBrowsers():
	# Checks the currentTasks list for any other browsers, and kills those processes in Task Manager.
	global currentTasks
	dangerList = ["iexplore", "MicrosoftEdge", "firefox"]
	for item in dangerList:
		if any (item in s for s in currentTasks):
			print ("\nAt " + time.strftime("%H:%M:%S")+ ", "+ item+ " was detected.")
			dangerProcess = item +".exe"
			time.sleep(.4)
			os.system("taskkill /f /im "+dangerProcess)
		else:
			None
def graphic():
	print"                                            .....                           "    
	print"                                       .::::;,'...                          "
	print"                    ..                .;::::::::::;,'.                      "
	print"                 .,:cc:.              '::::::::::::::;.                     "
	print"               .,cllllll;.           .;::::::::::::::'                      "
	print"             .;clllllllllc'         .'::::::::::::::,                       "
	print"           .:llllllllllllll;.      .,;:::::::::::::;.                       "
	print"          .cllllllllllllllllc,.    ,c:::::::::::::;.                        "
	print"           ':lllllllllllllllll:.  .;::::::::::::::'                         "
	print"            .':lllllllllllllllll;.,::::::::::::::,                          "
	print"               ':lllllllllllllllll::::::::::::::;.        ......'''.        "
	print"                .'cllllllllllllll:;;;:::::::::::'. .....''''......'.        "
	print"                  .'clllllllllllc:;;;;;:::::::;;'''''..............'.       "
	print"                    .'clllllllollcclllol:::::;,....................'.       "
	print"                   ..';oddxxxkkkkOOOO0kl:::::,'.....................'.      "
	print"       ....';:cclodkkOOO0000000000000Od:::::;'......................'.      "
	print"    .cdxkkOO0000000000000000000OOOkkkdc::::;'.....................'.'.      "
	print"    'k0000000000000000000000Oxoooollllcc::;'...........''''..........       "
	print"    .o0000000000000000000000x:',:clllllcc:,....'';;'......                  "
	print"     :O00000000000000000000kc'..';cllllllc:::ccccll;.                       "
	print"     .d0000000000000000000Oo,''',,;cccllllllllllllllc;.                     "
	print"      cO0000000000OOkdlc:;c:,,,,,,,;;:clllllllllllllllc;.                   "
	print"      'x000OOxdlc;,..    .,;,,,,,,,,,;;:llllllllllllllllc;.                 "
	print"       '::,'..          .,;,;,,;,,,,,,;;;cllllllllllllllllc;.               "
	print"                        ';,,,,,,,,,,;,;'..,cllllllllllllllllc;.             "
	print"                       .;;,,,,,,,,,,;;;.   .;lllllllllllllllllc'            "
	print"                      .,;,,,,,,,,,,,;;'      'clllllllllllllll:.            "
	print"                     .,;,,,,,,,,,,,;;,.       .,clllllllllll:.              "
	print"                     ';,,,,,,,,,,,,;;'          .:lllllllc;.                "
	print"                   .;,,,,,,,,,,,,;;,.            'clllc,.                   "
	print"                    .,;;;;,,,,,,,,;'.              .','.                    "
	print"                      ....',;;;;,;;.                                        "
	print"                            ....''.                                         "

def bar (stringLength, characterToDraw="-"):
	# Return a horizontal bar length n
	return characterToDraw * stringLength

def box(text):
	# put text inside a box
	global throwAway
	print  "+-" + bar(len(text)) + "-+" 
	print  "| " + text + " |" 
	print "+-" + bar(len(text)) + "-+"
	return throwAway

######################
# Main Program Logic #
######################
def keepChromeOpen():
	global currentTasks
	loop = True
	graphic()
	print("KPL - Browse-O-Matic 5000")
	print("Version 5.0")
	while loop: # A forever loop.  Nothing in the loop turns this to false, so it runs over and over until you close this program.
		time.sleep(howOftenToCheck) # Sleeps for the duration "how often to check", measured in seconds
		currentTasks = subprocess.check_output(['tasklist']).split("\r\n") #Checks the Task Manager, outputs everything to a list called "currentTasks"
		if any ("chrome" in s for s in currentTasks): # Check to see if the word "chrome" appears in the currentTasks list.
			#print (currentTasks)  #toggle this row for debugging, to get *.exe names for processes to shutdown
			#loop = False        #toggle this row for debugging.  Allows one pass through the loop to look at the currentTasks printout. 
			closeOtherBrowsers()
		else:
			print ("\nAt " + time.strftime("%H:%M:%S")+ ", Chrome was not found.")
			print ("Restarting a Chrome browser now.")
			webbrowser.open(targetPage, new=1, autoraise=True,) # If 'chrome is NOT found, then open a new browser window to the page you want. 
			time.sleep(.5)
			pyautogui.press('f11')
			closeOtherBrowsers()
	print ("finished, this should never happen") # This is only a test, if this line ever appears, that means that the forever loop isn't doing it's job.

########################
# Run the main program # 
########################
keepChromeOpen()
