#import module
import pyttsx3
import os
print("\t\t\t\t\t     -----------------------------------")
print("\t\t\t\t\t*****WELCOME TO WINDOW SOFTWARE LAUNCHER*****")
print("\t\t\t\t\t     -----------------------------------")
pyttsx3.speak("WELCOME TO WINDOW'S SOFTWARE LAUNCHER")

while True:
	#user input
	print("\nEnter program which you want to run:",end="")
	p=input()

	#opens notepad
	if (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("notepad" in p) or ("text editor" in p)):
		pyttsx3.speak("notepad is launching")
		os.system("notepad")

	#opens wondows media player
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("play" in p) or ("launch" in p)) and (("media" in p) or ("player" in p) or ("songs" in p)):
		pyttsx3.speak("windows media player is launching")
		os.system("wmplayer")

	#opens chrome browser
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("chrome" in p) or ("browser" in p) or ("google" in p)):
		pyttsx3.speak("your local brower is launching")
		os.system("chrome")

	#opens control panel
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("control" in p) or ("panel" in p)):
		pyttsx3.speak("cntrol panel is launching")
		os.system("control panel")

	#opens internet explorer
	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("internet" in p) or ("explorer" in p)):
		pyttsx3.speak("internet explorer is launching")
		os.system("iexplore")

	#opens ms word
	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("microsoft word" in p) or ("word" in p)):
		pyttsx3.speak("microsoft word is launching")
		os.system("WINWorD")

	#opens ms power point
	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("microsoft power point" in p) or ("power point" in p)):
		pyttsx3.speak("microsoft power point is launching")
		os.system("POWERPNT")

	#opens ms excel
	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("microsoft excel" in p) or ("excel" in p) or ("ms excel" in p) or ("sheet" in p)):
		pyttsx3.speak("microsoft excel is launching")
		os.system("EXCEL")

	#opens ms onenotes
	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("microsoft onenote" in p) or ("one note" in p) or ("note" in p)):
		pyttsx3.speak("microsoft onenote is launching")
		os.system("ONENOTE")

	#opens settings
	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("settings" in p) or ("tool" in p)):
		pyttsx3.speak("setting is launching")
		os.system("start ms-settings:")

	#opens calculator
	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("calculator" in p) or ("calc" in p)):
		pyttsx3.speak("calculator is launching")
		os.system("start calc")

	#opens whatsapp
	elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("whatsApp" in p) or ("whatsapp" in p) or ("messenger" in p)):
		pyttsx3.speak("whatsapp is launching")
		os.system("WhatsApp")

	#shows current date
	elif (("open" in p) or ("launch" in p) or ("show" in p) or ("what" in p)) and (("today date" in p) or ("today's date" in p) or ("date" in p) or ("month" in p) or ("year" in p)):
		pyttsx3.speak("today is")
		os.system("date /t")

	#shows current time
	elif (("what" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and(("current time" in p) or ("time" in p)):
		pyttsx3.speak("time is")
		os.system("time /t")
		
	#open firefox in browser
	
	elif (("fire" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and(("firefox" in p):
		pyttsx3.speak("firefox is launching")
		os.system("firefox")

	#exit the program
	elif (("exit" in p) or ("quit" in p) or "close" in p):
		break
	else :
		print("SORRY!GIVEN INPUT DOESN'T SUPPORT")
		pyttsx3.speak("SORRY!GIVEN INPUT DOESN'T SUPPORT")
		
print("THANK YOU :)")
pyttsx3.speak("THANK YOU")
