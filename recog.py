import speech_recognition as sr
import time as t
import webbrowser as wb
import wp
import os
import smtplib
from email.message import EmailMessage as em
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
msg=em()
email_add='20cs42@cit.edu.in'
msg['From']=email_add
email_pass='yyhqnjdpgvnoghcp'
pas='yyhqnjdpgvnoghcp'
sq='https://www.google.com/search?q='
yous='https://www.youtube.com/results?search_query='
you='https://www.youtube.com'
mail='https://mail.google.com/mail/u/1/#inbox'
r = sr.Recognizer()
rd={"Balamurugan":"20cs03@cit.edu.in","Sanjay":"20cs41@cit.edu.in","Sanju":"sanjaypotter3523@gmail.com","Manoj":"20cs31@cit.edu.in","Harshini":"20cs18@cit.edu.in","Asif":"20cs32@cit.edu.in","Gopika":"20cs13@cit.edu.in","Madhu":"20cs30@cit.edu.in"}
def rec():
    with sr.Microphone() as src:
        print("Please wait. Calibrating microphone...")
        speak("Please wait. Calibrating microphone...")
        # listen for 5 seconds and calculate the ambient noise energy level
        r.adjust_for_ambient_noise(src, duration=5)
        print("what do you want me to do ? ")
        speak("what do you want me to do ? ")
        audio = r.listen(src)
        try:
            txt = r.recognize_google(audio)
            if "inbox" in txt:
                print("opening gmail")
                speak("opening gmail")
                t.sleep(3)
                wb.get().open_new(mail)
            if("write" in txt or "compose" in txt):
                print("enter your subject")
                speak("enter your subject")
                a1 = r.listen(src)
                sub = r.recognize_google(a1)
                print("your sub is : ", sub)
                speak("your sub is : "+sub)
                msg['Subject'] = sub
                print("enter your body")
                speak("enter your body")
                a2 = r.listen(src)
                body = r.recognize_google(a2)
                print("your body is : ", body)
                speak("your body is : "+body)
                msg.set_content(body)
                '''print("do you want to attach any documents ?")
                a3 = r.listen(src)
                y_n = r.recognize_google(a3)
                if("yes"in y_n):
                    print("attaching")
                if("no" in y_n):
                    print("sending mail")'''
                print("who you want to send the mail?")
                speak("who you want to send the mail?")
                a4 = r.listen(src)
                rec = r.recognize_google(a4)
                l=rec.split(" ")
                if(l[-1] in rd):
                    print("sending mail to: ",rd[l[-1]])
                    speak("sending mail to: "+str( rd[l[-1]]))
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(email_add, email_pass)
                        msg['To']=rd[l[-1]]
                        smtp.send_message(msg)
                        print("message sent")
                        speak("message sent")
                else:
                    print("reciver not in your list")
                    speak("reciver not in your list")
                    inp=input("do you want to add new user ?")
                    if(inp=="yes"):
                        rd[input("enter your name")]=input("enter your email id :")
            if("search" in txt):
                print( "say your query")
                speak("say your query")
                a6 = r.listen(src)
                tx = r.recognize_google(a6)
                wb.get().open_new(sq+tx)
            if("YouTube" in txt):
                print("do you want to search anything ?")
                speak("do you want to search anything ?")
                a5 = r.listen(src)
                tx = r.recognize_google(a5)
                if("yes" in tx):
                    print("what do you want to search :")
                    speak("what do you want to search :")
                    a1 = r.listen(src)
                    tx = r.recognize_google(a1)
                    wb.get().open_new(yous + tx)
                if("no" in tx or "No" in tx):
                    wb.get().open_new (you)
            if("Whatsapp" in txt or "message" in txt):
                print("enter your message:")
                speak("enter your message:")
                a7 = r.listen(src)
                tx = r.recognize_google(a7)
                print("who is the sender")
                speak("who is the sender")
                a8 = r.listen(src)
                tx1 = r.recognize_google(a8)
                b1 = tx1.split(" ")
                wp.send(b1[-1],tx)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)