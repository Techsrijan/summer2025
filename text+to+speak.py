import pyttsx3
engine = pyttsx3.init()
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# f=open("apple.txt","r")
# for data in f:
#     print(data)
#     engine.say(data)


for i in range(1,10):
    print(i)
    engine.say(i)

    engine.runAndWait()

#engine.say("Tkinter is a binding to the Tk GUI toolkit for Python. It is the standard Python interface to the Tk GUI toolkit,[1] and is Python's de facto standard GUI.[2] Tkinter is included with standard Linux, Microsoft Windows and macOS installs of Python.")
