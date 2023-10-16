from gtts import gTTS
import os

mytext = "Hello Hacktoberfest 2023"

language = 'en'

output = gTTS(text=mytext, lang=language, slow=False)

output.save("opt.mp3")

os.system("start opt.mp3")
