
from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3, datetime, sys, wikipedia, wolframalpha, os, smtplib, random, webbrowser, pygame, subprocess

client = wolframalpha.Client('Your_App_ID')

folder = 'C:\\Users\\skt\\Music\\YouTube\\'

engine = pyttsx3.init()
voices = engine.getProperty('voices')

#b_music = ['Edison', 'Micro', 'Lucid_Dreamer']
#pygame.mixer.init()
#pygame.mixer.music.load(folder + random.choice(b_music) + '.mp3')
#pygame.mixer.music.set_volume(0.05)
#pygame.mixer.music.play(-1)

def speak(audio):
    print('FOVER:', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Try again')
        print('Try again')
        pass

    return query


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

class Widget:
    def __init__(self):
       root = Tk()
       root.title('FOVER')
       root.config(background='black')
       root.geometry('350x600')
       root.resizable(0, 0)
       #root.iconbitmap(r'C:\Users\skt\Documents\Karen Mark I\Untitled-1.ico')
       #img = ImageTk.PhotoImage(Image.open(r"C:\Users\skt\Documents\Karen Mark I\karen image 2.png"))
       #panel = Label(root, image = img)
       #panel.pack(side = "bottom", fill = "both", expand = "no")

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click \'Start Listening\' to Give commands')

       userFrame = LabelFrame(root, text="USER", font=('Black ops one', 10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='black', fg='green')
       left2.config(font=("Comic Sans MS", 10, 'bold'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="FOVER", font=('Black ops one', 10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='black',fg='white')
       left1.config(font=("Comic Sans MS", 10, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='deepSkyBlue', fg='white', command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white', command=root.destroy).pack(fill='x', expand='no')

       speak('Hello, I am FOVER! What should I do for You?')
       self.compText.set('Hello, I am FOVER! What should I do for You?')

       root.bind("<Return>", self.clicked) # handle the enter key event of your keyboard
       root.mainloop()
    
    def clicked(self):
        print('Working')
        query = myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        if 'open ccleaner' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\CCleaner\CCleaner.exe')

        elif 'open google chrome' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

        elif 'open powerpoint' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\Microsoft Office\Office14\POWERPOINT.EXE')

        elif 'open youtube' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'shutdown' in query:
            self.compText.set('okay')
            speak('okay')
            os.system('shutdown -s')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            self.compText.set(random.choice(stMsgs))
            speak(random.choice(stMsgs))

        elif 'email' in query:
            self.compText.set('Who is the recipient? ')
            speak('Who is the recipient? ')
            recipient = myCommand()
            self.userText.set(recipient)
            recipient = recipient.lower()
            
    
            if 'me' in recipient:
                try:
                    self.compText.set('What should I say? ')
                    speak('What should I say? ')
                    content = myCommand()
                    self.userText.set(content)
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Username')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    self.compText.set('Email sent!')
                    speak('Email sent!')

                except:
                    self.compText.set('Email sent!')
                    speak('Sorry ' + 'Sir' + '!, I am unable to send your message at this moment!')



        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            self.compText.set('Okay')
            speak('okay')
            self.compText.set('Bye Sir, have a good day.')
            speak('Bye Sir, have a good day.')
           
        elif 'hello' in query:
            self.compText.set('Hello Sir')
            speak('Hello Sir')


        elif 'bye' in query:
            self.compText.set('Bye ' + 'Sir' + ', have a good day.')
            speak('Bye ' + 'Sir' + ', have a good day.')
                                    
        elif 'play music' in query:
            music_folder = 'F:\\music'
            music = ['Edison', 'bensound-actionable', 'bensound-buddy', 'Micro', 'Lucid_Dreamer']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            
            
            self.compText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')
           
        elif 'i like you' in query or 'love you' in query:
            self.compText.set('thanks ' )
            speak('thanks ' )
            self.compText.set('you just made my day')
            speak(' you just made my day' )

        elif 'can you detect the face' in query or 'detect face' in query:
            self.compText.set('just wait a second ' )
            import fac
            speak('yes, sir ' )
            speak('please, keep focus on camera ' )
            #print(ex.facerecognition())

        elif 'fover recognise the face' in query or 'recognise face' in query:
            self.compText.set('just wait a second ' )
            speak('yes, sir ' )
            import recog
            #speak('please, keep focus on camera ' )
            #print(exrec.facerecognition())


        elif 'your best friend' in query or 'your friend' in query:
           self.compText.set('i think all my friends are best ')
           speak('i think all my friends are best ')
           self.compText.set('i am very lucky assistance')
           speak('i am very lucky assistance') 
           
        # Compare
        elif 'better than alexa' in query:
            self.compText.set('a like alexa')
            speak('a like alexa')
            self.compText.set(' she is a greate assistance!')
            speak(' she is a greate assistance!')
        elif 'better than google' in query:
            self.compText.set('a like google')
            speak('a like google')
            self.compText.set(' she is a greate assistance!')
            speak(' she is a greate assistance!')
        elif 'better than siri' in query:
            self.compText.set('a like siri')
            speak('a like siri')
            self.compText.set(' she is a greate assistance!')
            speak(' she is a greate assistance!')
            
          # How are you FOVER
        elif query == 'how are you' or query == 'how are you FOVER':
            self.compText.set('i am fine.......')
            speak('i am fine')

        elif query == 'what are you doing':
            self.compText.set('waiting for you.......')
            speak(' just waiting for your next commond') 

        elif query == 'who are you' in query:
            self.compText.set('i am not really a person, i am digital assistant')
            speak('i am not really a person, i am digital assistant')
            self.compText.set('i had prefer to think of myself as your friend')
            speak('i had prefer to think of myself as your friend')

        elif query == 'what is your name':
            self.compText.set('my name is FOVER')
            speak('my name is FOVER')

        
        else:
            self.compText.set('i can not understand it')
            speak('i can not understand it')


                  
if __name__ == '__main__':
    greetMe()
    widget = Widget()       
