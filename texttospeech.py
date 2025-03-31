from gtts import gTTS

text = "Hello guys, How are you, All Fine??" #text that you want to convert

language = 'en' # en for english language

obj = gTTS(text = text,lang = language, slow = False)

# used slow = false because our converted video have a high speed

obj.save("sample.mp3")




