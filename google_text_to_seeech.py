from gtts import gTTS
from playsound import playsound
text=input('enter any text u want to speak')
print(text)
audio=gTTS(text)
audio.save('a.mp3')
playsound('a.mp3')