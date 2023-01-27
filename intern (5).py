import pyttsx3
import speech_recognition as sr

#text to speech conversion
def speaktext(text):
 friend=pyttsx3.init()
 friend.say(text)
 friend.runAndWait()

speaktext('Hello ,How are you')

def getaudio():
 r = sr.Recognizer()
 with sr.Microphone() as source:
  print('listening...')
  audio = r.listen(source)
  MyText = r.recognize_google(audio)
 return MyText
  #speaktext(MyText)  
#getaudio()
query=getaudio()

import nltk
nltk.download('punkt')
from nrclex import NRCLex
def emotion(text):
 emotion = NRCLex(text)
 print(emotion.raw_emotion_scores) 
 print(emotion.top_emotions[0])

while True:
 if 'hello'==query:
  speaktext("hello")
  emotion(query)
 if 'bye'==query:
  speaktext("Bye Thank you")
  emotion(query)


