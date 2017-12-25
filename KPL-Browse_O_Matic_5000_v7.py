# KPL-Browse_0_Matic_5000_v7.py
# Made with Python 2.7.14
# by Evan Nordquist Oct 28, 2017
# Version 7.0
# New for Version 2 - Supresses MicrosoftEdge, Firefox, and old school Internet Explorer.
# New for Version 3 - Output reduced to only show errors, not a status update for every loop.
# New for Version 4 - ASCII graphic KPL logo added purely for laughs.
# New for Version 5 - pyautogui added to simulate keypresses (such as "F11" to toggle full screen mode).
# New for Version 6 - Added "cmd", and "powershell" to the list of banned programs.
# New for Version 7 - Closes any previously open chrome browsers upon startup.

######################################################################################################
# Import modules for: the operating system, the clock, the task manager, and the default web browser #
# Initialize global variables																		 #
######################################################################################################
import os
import time  
import subprocess
import webbrowser
import pyautogui
howOftenToCheck = 2 # measured in seconds
targetPage = "https://studiocentraldisplay.weebly.com/" # Target page. If modified, remember to keep the quotation marks.
currentTasks = []	# Global variable that can be updated by one function, and referenced by another. 

####################
# Helper Functions #
####################
def closeOtherBrowsers():
	# Checks the currentTasks list for any other browsers or off limits programs, and kills those processes in Task Manager.
	global currentTasks
	dangerList = ["iexplore", "MicrosoftEdge", "firefox", "cmd", "powershell"]
	for item in dangerList:
		if any (item in s for s in currentTasks):	# Break down the currenTasks list into word sized chunks and look for a match with any dangerList items. 
			print ("\nAt " + time.strftime("%H:%M:%S")+ ", "+ item+ " was detected.")
			dangerProcess = item +".exe"	# Adds ".exe" to the end of the program name so that it matches the official process name to be stopped.
			time.sleep(.4)
			os.system("taskkill /f /im "+dangerProcess)		# Shuts down the banned program. 
		else:
			None

def init_and_CloseChrome():
	global currentTasks
	# Checks the currentTasks list for chrome as well as dangerList items, closes all that match.
	currentTasks = subprocess.check_output(['tasklist']).split("\r\n") #Checks the Task Manager, outputs everything to a list called "currentTasks"
	dangerList = ["chrome"]	# Checks to see if Chrome is already running.  
	for item in dangerList:
		if any (item in s for s in currentTasks): # Check to see if the word "chrome" appears in the currentTasks list.
			dangerProcess = item +".exe"
			time.sleep(.5)
			print "loading"
			os.system("taskkill /f /im "+dangerProcess)
			webbrowser.open(targetPage, new=1, autoraise=True,) # If 'chrome is NOT found, then open a new browser window to the page you want. 
			time.sleep(2)
			pyautogui.press('space') # If Chrome was open and shutdown abruptly by this program, spacebar deals with the "This browser didn't shut down properly" pop-up.
			time.sleep(2)
			pyautogui.press('f11')	# Simulates a keyboard F11 key, which will toggle Full Screen Mode
			closeOtherBrowsers()
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

######################
# Main Program Logic #
######################
def keepChromeOpen():
	global currentTasks
	loop = True
	graphic()
	print("KPL - Browse-O-Matic 5000")
	print("Version 7.0")
	init_and_CloseChrome()
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
			webbrowser.open(targetPage, new=1, autoraise=True,) # If 'Chrome is NOT found, then open a new browser window to the page you want. 
			time.sleep(2)	# Ensures that the new window has time to open before the next action takes place. 
			pyautogui.press('f11') # F11 toggles full screen (which is off by default for a new window, so it toggles to "On").
			closeOtherBrowsers()
	print ("finished, this should never happen") # This is only a test, if this line ever appears, that means that the forever loop isn't doing its job.

########################
# Run the main program # 
########################
keepChromeOpen()
