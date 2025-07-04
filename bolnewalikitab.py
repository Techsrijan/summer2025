import pyttsx3
import PyPDF2
speaker=pyttsx3.init()
speaker.setProperty('rate', 125)
book=open('gk.pdf','rb')
reader=PyPDF2.PdfFileReader(book)
no_of_page=reader.numPages
# print(no_of_page)
# text="Welcome to INDIA"

for i in range(3,no_of_page):
     page=reader.getPage(0)
     text=page.extractText()
     speaker.say(text)
     speaker.runAndWait()