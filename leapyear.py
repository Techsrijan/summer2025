from gtts import gTTS
from playsound import playsound
year=int(input("enter Any year"))
print("Year=",year)
if year%100==0:
    if year%400==0:
        print("leap year")
        audio = gTTS("leap year")
        audio.save('a.mp3')
        playsound('a.mp3')
    else:
        print("not leap year")
        audio1 = gTTS(" not leap year")
        audio1.save('a1.mp3')
        playsound('a1.mp3')
elif year%4==0:
    print("leap year")
    audio = gTTS("leap year")
    audio.save('a.mp3')
    playsound('a.mp3')
else:
    print("not leap year")
    audio1 = gTTS(" not leap year")
    audio1.save('a1.mp3')
    playsound('a1.mp3')
