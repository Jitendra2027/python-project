import pyttsx3
import os

print("WELCOME TO WINDOW SOFTWARE LAUNCHER")
pyttsx3.speak("WELCOME TO WINDOW SOFTWARE LAUNCHER")
while True:
	print("Enter program which you want to run:",end="")
	p=input()
	if (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) AND (("notepad" in p) or ("text editor" in p)):
		pyttsx3.speak("notepad is launching")
		os.system("notepad")

	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("play" in p) or ("launch" in p)) AND (("media" in p) or ("player" in p) or ("songs" in p)):
		pyttsx3.speak("windows media player is launching")
		os.system("wmplayer")

	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) AND (("chrome" in p) or ("browser" in p) or ("google" in p)):
		pyttsx3.speak("your local brower is launching")
		os.system("chrome")

	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) AND (("control" in p) or ("panel" in p)):
		pyttsx3.speak("cntrol panel is launching")
		os.system("control panel")

	elif (("run" in p) or ("open" in p) or ("launch" in p)) AND (("internet" in p) or ("explorer" in p)):
		pyttsx3.speak("internet explorer is launching")
		os.system("iexplore")

	elif (("run" in p) or ("open" in p) or ("launch" in p)) AND (("microsoft word" in p) or ("word" in p)):
		pyttsx3.speak("microsoft word is launching")
		os.system("WINWorD")

	elif (("run" in p) or ("open" in p) or ("launch" in p)) AND (("microsoft power point" in p) or ("power point" in p) or ("point" in p)):
		pyttsx3.speak("microsoft power point is launching")
		os.system("POWERPNT")

	elif (("run" in p) or ("open" in p) or ("launch" in p)) AND (("microsoft excel" in p) or ("excel" in p) or ("ms excel" in p) or ("sheet" in p)):
		pyttsx3.speak("microsoft excel is launching")
		os.system("EXCEL")

	elif (("run" in p) or ("open" in p) or ("launch" in p)) AND (("microsoft onenote" in p) or ("one note" in p) or ("note" in p)):
		pyttsx3.speak("microsoft onenote is launching")
		os.system("ONENOTE")

	elif (("run" in p) or ("open" in p) or ("launch" in p)) AND (("settings" in p) or ("tool" in p)):
		pyttsx3.speak("setting is launching")
		os.system("start ms-settings:")

	elif (("run" in p) or ("open" in p) or ("launch" in p)) AND (("calculator" in p) or ("calc" in p)):
		pyttsx3.speak("calculator is launching")
		os.system("start calc")

	elif (("run" in p) or ("open" in p) or ("launch" in p) ("show" in p)) AND (("today date" in p) or ("date" in p) or ("month" in p) ("year" in p):
		pyttsx3.speak("today is")
		os.system("date /t")


	elif (("run" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) AND (("current time" in p) or ("time" in p)):
		pyttsx3.speak("time is")
		os.system("time /t")

	elif (("exit" in p) or ("quit" in p) or "close" in p):
		pyttsx3.speak("THANK YOU")
		break
	else
		print("SOorY!GIVEN INPUT DOESN'T SUPPorT")
		pyttsx3.speak("Try again")
pyttsx3.speak("THANK YOU")
print("THANK YOU :)")