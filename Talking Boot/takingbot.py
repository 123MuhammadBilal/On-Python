import pyttsx3
friend = pyttsx3.init()
speech = input("SAY SOME THING")
friend.say(speech)
friend.runAndWait()