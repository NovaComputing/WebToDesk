#Released under the GNU GPL V2
# Written by: Scott Spitler
# CopyLeft Held Under: NovaComputing LLC.
# Version Number: 0.0.1


#The purpose of this script is to open the MSOffice Suite of 
#programs in a firefox enviornment. this is to act as a basic
#shell for the "Popular" office suite for the inept
import webbrowser, optparse
#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#the counter variable is defined as a line counter for the option
counter = 0
#parser is used to take terminal options from the user
parser = optparse.OptionParser()
#adding a option for the parser to listen for allowing you to
#select new options for the program
parser.add_option('-p', '--program', 
                  dest="program_select", 
                  default="word",
                  )
#options and remainder are defined to have comparable objects
#from the options selected.
options, remainder = parser.parse_args()
#the option selected from parser is casted to a string for
#comparison
if str(options.program_select) == "Word":
	counter = 0
elif str(options.program_select) == "Excel":
	counter = 1
elif str(options.program_select) == "PowerPoint":
	counter = 2
else:
	#The nonstandard error code of 5 was selected
	counter = 5
	#If there is an error the user will be alerted of
	#their grave mistake
	print options.program_select
#the config file will be opened and scanned for changes
#file_object = open("/home/scotts/Documents/Programming/Python/config.txt","r")
file_object = open("/etc/WebToDesk.txt", "r")
#array created to put the entire file in at once
lines = file_object.readlines()
#uncomment for line debugging
#print counter

#the url for the browser is selected
url = lines[counter]
#uncomment for debugging the url/uri
#print url

#open the web browser 
webbrowser.open_new(url)
