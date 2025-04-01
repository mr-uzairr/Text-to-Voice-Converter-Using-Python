from gtts import gTTS
import os

abc = open('sample.txt')  # file you want to read

text = abc.read() # file reading

language = 'en' # en for english language

obj = gTTS(text = text,lang = language, slow = False)
# used slow = false because our converted video have a high speed


obj.save("sample.mp3")


os.system("open sample.mp3")



