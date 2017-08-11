from gtts import gTTS #import gtts api
import os

#if y is the file containing the name, the extension is not necessary
#import y
#id = y.id
#id = 'Joel'
id = input(">>>")

#reading from a file
#with open(filename) as f
#	id = f.readlines()

#not sure if this works
#file = open("filename","r")
#id = file.read()

def speak():
		head = gTTS(text='the person in front of you is ', lang='en')
		head.save("head.mp3") #intro
		#os.system("sudo mpg321 head.mp3") ...this is slower
		tts = gTTS(text=id, lang='en')
		tts.save("audio.mp3") #name
		os.system("sudo mpg321 head.mp3 audio.mp3") #doesn't work without sudo
		os.system("rm audio.mp3")
		#os.system("rm head.mp3")

speak()