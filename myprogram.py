import pyttsx3
import os

print("WELCOME TO WINDOW SOFTWARE LAUNCHER")
pyttsx3.speak("WELCOME TO WINDOW SOFTWARE LAUNCHER")
while True:
	print("Enter program which you want to run:",end="")
	p=input()
	if (("run" in p) OR ("execute" in p) OR ("open" in p) OR ("launch" in p)) AND (("notepad" in p) OR ("text editor" in p)):
		pyttsx3.speak("notepad is launching")
		os.system("notepad")

	elif (("run" in p) OR ("execute" in p) OR ("open" in p) OR ("play" in p) OR ("launch" in p)) AND (("media" in p) OR ("player" in p) OR ("songs" in p)):
		pyttsx3.speak("windows media player is launching")
		os.system("wmplayer")

	elif (("run" in p) OR ("execute" in p) OR ("open" in p) OR ("launch" in p)) AND (("chrome" in p) OR ("browser" in p) OR ("google" in p)):
		pyttsx3.speak("your local brower is launching")
		os.system("chrome")

	elif (("run" in p) OR ("execute" in p) OR ("open" in p) OR ("launch" in p)) AND (("control" in p) OR ("panel" in p)):
		pyttsx3.speak("cntrol panel is launching")
		os.system("control panel")

	elif (("run" in p) OR ("open" in p) OR ("launch" in p)) AND (("internet" in p) OR ("explorer" in p)):
		pyttsx3.speak("internet explorer is launching")
		os.system("iexplore")

	elif (("run" in p) OR ("open" in p) OR ("launch" in p)) AND (("microsoft word" in p) OR ("word" in p)):
		pyttsx3.speak("microsoft word is launching")
		os.system("WINWORD")

	elif (("run" in p) OR ("open" in p) OR ("launch" in p)) AND (("microsoft power point" in p) OR ("power point" in p) OR ("point" in p)):
		pyttsx3.speak("microsoft power point is launching")
		os.system("POWERPNT")

	elif (("run" in p) OR ("open" in p) OR ("launch" in p)) AND (("microsoft excel" in p) OR ("excel" in p) OR ("ms excel" in p) OR ("sheet" in p)):
		pyttsx3.speak("microsoft excel is launching")
		os.system("EXCEL")

	elif (("run" in p) OR ("open" in p) OR ("launch" in p)) AND (("microsoft onenote" in p) OR ("one note" in p) OR ("note" in p)):
		pyttsx3.speak("microsoft onenote is launching")
		os.system("ONENOTE")

	elif (("run" in p) OR ("open" in p) OR ("launch" in p)) AND (("settings" in p) OR ("tool" in p)):
		pyttsx3.speak("setting is launching")
		os.system("start ms-settings:")

	elif (("run" in p) OR ("open" in p) OR ("launch" in p)) AND (("calculator" in p) OR ("calc" in p)):
		pyttsx3.speak("calculator is launching")
		os.system("start calc")

	elif (("run" in p) OR ("open" in p) OR ("launch" in p) ("show" in p)) AND (("today date" in p) OR ("date" in p) OR ("month" in p) ("year" in p):
		pyttsx3.speak("today is")
		os.system("date /t")


	elif (("run" in p) OR ("open" in p) OR ("launch" in p) OR ("show" in p)) AND (("current time" in p) OR ("time" in p)):
		pyttsx3.speak("time is")
		os.system("time /t")

	elif (("exit" in p) OR ("quit" in p) OR "close" in p):
		pyttsx3.speak("THANK YOU")
		break
	else
		print("SOORY!GIVEN INPUT DOESN'T SUPPORT")
		pyttsx3.speak("Try again")
pyttsx3.speak("THANK YOU")
print("THANK YOU :)")