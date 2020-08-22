import pyttsx3 as s
from datetime import date
import os
today = ("Today's date is "+ str(date.today()))
list_of_programs = ['Chrome', 'Notepad', 'Windows Media player', 'TeamViewer', 'Internet Explorer',
                    'Edge', 'MS Word', 'MS Powerpoint', 'MS Excel', 'One Note', 'node', 'Outlook']
print("Welcome User! Mark here.")
print(today)
s.speak("Hello Sir I am mark! Your Personal Assistant.")

while True:

	a = input()
	x = a.lower()

	if(("hi" in x) or ("hello" in x) or ('hey' in x)):
		s.speak("Hi How are you?")

	elif(('introduce' in x) or ('what are you' in x) or ('who are you' in x) or (('something' in x) and ('yourself' in x)) or ('about youself' in x)):
		s.speak('I am Mark. Your Personal Assistant.')
	
	elif((('tell' in x) or ('show' in x) or ('display' in x) or ('how' in x)or('can' in x)or('you' in x)) and (('what' in x) or ('menu' in x) or ('do for me' in x) or ('help' in x))):
		s.speak('I am programmed partially. So as of now, I can do open the following things for you at present')
		for program in list_of_programs:
#			s.speak(program)
			print(program)
		s.speak('Which one do you want me to open for you?')
		break
while True:
        print("Chat With me with your requirements:", end='')
        p = input()

        if((("run" in p) or ('open' in p) or ('launch' in p)) and ("chrome" in p)):
                s.speak('Launching Chrome for you!')
                os.system("chrome")
        elif((("run" in p) or ("open" in p) or ('launch' in p)) and (("media" in p) or ("player" in p) or ("wmplayer" in p))):
                s.speak('Launching windows Media player for you!')
                os.system("wmplayer")
        elif((("run" in p) or ("open" in p) or ('launch' in p)) and (("Team Viewer" in p) or ("team viewer" in p) or ("team viewr" in p)or('team' in p)or('viewer' in p))):
                s.speak('Launching TeamViewer for you!')
                os.system("TeamViewer")
        elif((("run" in p) or ("open" in p) or ('launch' in p)) and (("internet" in p) or ("explorer" in p))):
                s.speak('Launching Internet Explorer for you!')
                os.system("iexplore")
        elif((("run" in p) or ("open" in p) or ('launch' in p)) and (("microsoft edge" in p) or ("ms edge" in p) or ("edge" in p))):
                s.speak('Launching Edge for you!')
                os.system("msedge")
        elif((("run" in p) or ("open" in p) or ('launch' in p)) and (("microsoft word" in p) or ("ms word" in p) or ("word document" in p) or ("ms word" in p))):
                s.speak('Launching a Word Document for you!')
                os.system("WINWORD")
        elif((("run" in p) or ("open" in p)or('launch' in p)) and (("microsoft powerpoint" in p) or ("ms ppt" in p) or ("ms ppt document" in p) or ("ppt" in p) or ("powerpoint maker" in p))):
                s.speak('Launching MS PowerPoint for you!')
                os.system("POWERPNT")
        elif((("run" in p) or ("execute" in p)or('launch' in p)) and (("notepad" in p) or ("editor" in p))):
                s.speak('Launching Notepad for you')
                os.system("notepad")
        elif((("run" in p) or ("open" in p) or ('launch' in p)) and (("microsoft outlook" in p) or ("ms mail" in p) or ("ms outlook mail" in p) or ("microsoft mail" in p))):
                s.speak('Launching Outlook for you!')
                os.system("OUTOOK")
        elif((("run" in p) or ("open" in p) or ('launch' in p)) and (("microsoft excel" in p) or ("ms xls" in p) or ("ms escel document" in p) or ("excel" in p) or ("excel sheets" in p))):
                s.speak('Launching MS Excel for you!')
                os.system("EXCEL")
        elif((("run" in p) or ("open" in p)or ('launch' in p)) and (("microsoft onenote" in p) or ("ms onenote" in p) or ("ms 1note" in p) or ("ms note" in p) or ("ms note maker" in p))):
                s.speak('Launching OneNote for you!')
                os.system("ONENOTEM")
        elif((("run" in p) or ("open" in p) or ('launch' in p)) and (("node js" in p) or ("node" in p) or ("node editor" in p) or ("javascript node" in p) or ("node javascript" in p))):
                s.speak('Launching Node for you!')
                os.system("node")
        elif(("quit" in p) or ("exit" in p) or ("close" in p)or ('offline' in p)or('thankyou in p')):
                s.speak('Alright! Have a nice day bud!')
                break

        else:
                s.speak('Sorry, I dont have anything of that sort mentioned on my menu list. Please try again')
                print("Doesn't support")
