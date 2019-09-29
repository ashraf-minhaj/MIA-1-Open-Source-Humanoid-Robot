""" Mia-1 Humanoid Robot as
    ** University/College Guide or Receptionist **
    purpose: Educational / Commercial
"""

"""
Mia-1 the advanced open source humanoid robot.

author: Ashraf Minhaj
mail  : ashraf_minhaj@yahoo.com
blog  : ashrafminhajfb.blogspot.com
        http://youtube.com/fusebatti
"""

"""import necessary libraries"""
#import requests             #for making post/get requests
import pyttsx3               #offline text to speech
import speech_recognition as sr   #Speech to text (requires internet to function)
import time
from random import randint   #random integer picking library
import tkinter               #tkinter gui library
from tkinter import Tk, Button, Label, Tk  #gui necessary modules
import serial                #serial library for serial communication over USB
from PIL import Image        #for showing image
import cv2                   #Computer Vision library (open source Computer Vision)


talk = pyttsx3.init()  #initialize pyttsx3
gui = Tk()             #initialize / instantiate TK

#Connect with mia motor driver board over serial communication
try:
    mia = serial.Serial("COM28", 9600)
except:
  pass

#url with NASA API
url = "https://api.nasa.gov/planetary/apod?api_key=YOUR_API_KEY_HERE"

#Voice ID-male/female/language
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

"""possible lists of possible words or sentences with different punctuation
  So that it can detect different ways of Pronunciations of the same word.
"""
call_list = ["Miya", "miya", "mia", "Mia", "mea", "meea", "robot", "Robot"]
r_u_there = ['Are you there', 'are you there', 'Are You There', 'Are you their', 'are you their', 'You there', 'you there', 'You their', 'you their']
hi_List = ['hi', 'Hello', 'Hey', 'yo', 'salam', 'hello', 'yo yo']
bye_List = ['Bye', 'bye', 'Goodbye', 'goodbye', 'Good bye' 'good bye', 'byebye', 'by by', 'By by', 'Tata', 'tata', 'So long', 'so long', 'okay bye', 'ok bye', 'Ok bye', 'Okay bye']
qst1_list = ["Introduce yourself", "Who are you", 'who are you', 'What are you', 'what are you']
res_neg_list = ['Bad Robot', 'bad robot', 'Bad robot', 'bad boy', "Bad boy", 'you are rude', 'You are rude', 'Bad robot' 'bad robot', 'Bad Robot']
slang_list = ['Bal', 'bal', 'Crap', 'crap', 'chutiya', 'Chutiya', 'chootia', 'Chootia']
Love_list = ['i love you', 'I love you', 'Love you', 'love you']
hate_list = ['i hate you', 'I hate you', 'Hate you', 'hate you']
query_time = ["What's the time", "what's the time", "Time", "time"]
query_date = ["Date", "date", "Date please", "date please"]
qstx = ["How do you feel", "what do you feel", "What do you feel", "how do you feel"]
qts_vc = ["Who is the vc of BU"]


#Listen and Process section___________________________________________
def listen():
    """Converts the user voice input into text to be processed."""
    try:
        speech = sr.Recognizer()

        #get input from mic
        with sr.Microphone() as source:
            print("Say 'MIA' followed by command.>>")
            voice = speech.listen(source)
            text = speech.recognize_google(voice)
            print(text)

            text_list = text.split(" ")

            if text_list.pop(0) in call_list:
                command = ' '.join(text_list)
                
                if "abort" in text_list or "quit" in text_list:
                    """Stop listening."""
                    respond("Command granted.", 100)
                    return

                Decide(command)



    except KeyboardInterrupt:  #ctrl+c will break the loop
        return

    else:
        pass             #do nothing

    listen()             #recursion (keep listening forever)

#-----------------------------------------------------------
def Decide(listen):
    """
    Takes decision based on what user says.
    """
    print(f" Command = {listen}.") #just to debug
    
    sent = listen

    word_list = sent.split(" ") #break the sentence

    if "show" in word_list and "astronomy" in word_list: 
        print("It worked")
     
        return

    elif "love" in word_list or "boy friend" in word_list or "boyfriend" in word_list: 
        print("It worked")
        respond("I understand nothing about love. I'm sure I will one day.", 100)
        return

    elif "f***" in word_list or "shona" in word_list or "bal" in word_list: 
        #Show mushti haat
        respond("I Dont have time to dash you..", 100)
        return

    elif "vagina" in word_list or "boobs" in word_list or "breast" in word_list or "boob" in word_list: 
        #Both hand up then down
        respond("Show me your that first.", 100)
        return

    #see what user said is in which list or not
    if listen in hi_List:
        hi()
        return
        
    if listen in qstx:
        respond("I feel, Alive.",100)

    elif listen in bye_List:
        respond("I liked talking with you, okay", 100)
        bye()
        return

    elif listen in Love_list:
        respond("Yuk, I have a robot boy friend, No seat available", 100)
    
    elif listen in hate_list:
        respond("Hate you too.", 100)
     
    elif listen in qst1_list:
        respond("""I am mia, An advanced cyborg or you might say, an intelligent robot
                   Developed by Britannia Dynamics, the Advanced robotics and research lab of Britannia University.
                   I love to learn, and I learn daily. We will meet soon.""", 100)
    
    elif listen in res_neg_list:
        respond("I am very sorry If I ever hurt you", 100)

    elif listen in slang_list:
        respond("You are a bad guy", 100)
    
    elif listen in r_u_there:
        r_u_there_list = ["For you, Always sir", "Yes I am", "No, I am busy right now, don't bother me"]

        rand_r_u_there = r_u_there_list[randint(0, len(r_u_there_list) - 1)]
    
        respond(rand_r_u_there, 100)

    elif listen == "show me an astronomy picture":
        print("apod command1.")
        apod()

    elif "rest" in word_list and  "take" in word_list: #command to take some rest
        respond(" o lala", 90)

    elif "time" in word_list:
        hr = time.localtime().tm_hour
        mins = time.localtime().tm_min
        respond(f"It's {hr} {mins}", 100)

    elif "date" in word_list:
        dte = time.localtime().tm_year
        mon = time.localtime().tm_mon
        day = time.localtime().tm_mday

        if mon == 1:
            mon = 'January'
        if mon == 2:
            mon = 'February'
        if mon == 3:
            mon = 'March'
        if mon == 4:
            mon = 'April'
        if mon == 5:
            mon = 'May'
        if mon == 6:
            mon = 'June'
        if mon == 7:
            mon = 'July'
        if mon == 8:
            mon = 'August'
        if mon == 9:
            mon = 'September'
        if mon == 10:
            mon = 'October'
        if mon == 11:
            mon = 'November'
        if mon == 12:
            mon = 'December'
        
        respond(f"Today is {mon} {day} {dte}", 100)

    else:
        
        clues = listen.split(' ')

        """
        if "show" in clues and "astronomoy" in clues:
            print("It worked")
            apod()
            break
        """

        for clue in clues:
            
            if len(clue) >= 3:
                print(clue)
                respond(f"I am sorry, I have no knowledge about {clue}", 100)
                break
            
            else:
                respond("Sorry I don't understand Please say again.", 100)
                break

  

def respond(words, wordsPerMinute):
    """ words = your text to speak up.
    wordsPerMinute = how many words to say per minute. can be more than 120.
    Respond / Answer to user (Talk). Takes argument from respond and talks."""
    response = words
    wpm = wordsPerMinute

    print(f"Talking the: {words}") #to debug and see if everythings going okay

    talk.setProperty('rate', wordsPerMinute) # words per minute
    talk.setProperty('voice', voice_id)
    talk.say(words)

    talk.runAndWait()



# *** GUI functions / Modules__________________________________________________________________________
def hi():
    """Generate random hi responses"""
    rand_hi = hi_List[randint(0, len(hi_List) - 1)]
    
    mia.write(b'h')
    time.sleep(.700)
    respond(rand_hi, 100)    #speak the random hi text
    
def bye():
    """Generates random Bye response"""
    byes = ["Bye bye", "hasta la vista", "Tata", "Good Bye", "See you", "So long", "Hasta La vista"]
    rand_bye = byes[randint(0, len(byes) - 1)]

    mia.write(b'h')
    time.sleep(.700)
    respond(rand_bye, 100)    #speak the random bye text

def hand_shake():
    """Hand shake for tallers / adults."""

    hsTalk = ["Nice to meet you", "Pleased to meet you", "Honored to meet you human"]
    rand_hsTalk = hsTalk[randint(0, len(hsTalk) - 1)]
    mia.write(b'M')         #handshake or musafaha 'M'
    time.sleep(.700)
    respond(rand_hsTalk, 100)    


def down_hand_shake():
    """Hand shake for kids."""
    hsTalk = ["Nice to meet you", "Pleased to meet you", "Honored to meet you human"]
    rand_hsTalk = hsTalk[randint(0, len(hsTalk) - 1)]
    mia.write(b'm')         #handshake or musafaha  'm'
    time.sleep(.700)
    respond(rand_hsTalk, 100) 


def laser_show():
    """Aim and fire."""
    mia.write(b'l')      
    time.sleep(.700)
    respond("Target Light, ON. Weapon System off line. Can not fire", 120)    #speak the random bye text

def bow():
    """BOW"""
    mia.write(b'b')  #bow command

def demoSpeech():
    """Main speech of Mia"""
    mia.write(b'A') 
    respond("Hellow Everyone", 90)
    #mia.write(b'Salam to all')
    time.sleep(1)
    respond("I am Mia", 90)
    respond("an advanced humanoid robot, developed by Britannia University.", 90)
    respond("I have thirteen degrees of freedom", 90) #two arms open a bit
    
    #claw show
    time.sleep(1)
    respond("I have a Metal hand which is, Cool, isn't it?", 90) #c
    respond("I can also see you, ah, A lot of faces! I can also recognize people.", 90)
    
    time.sleep(2)
    mia.write(b'b') #Thank the audience by saying bye 
    respond("Thank you", 90)
    
def apod():
    """Donwload and show NASA Astronomy Image of the Day (APOD)"""
    respond("Okay", 120)
    r = requests.get(url)

    if r:
        apd = r.json()['hdurl']
        pic = requests.get(apd, allow_redirects = True)

        if 'jpg' in apd:
            respond("Image downloaded", 120)
            open('apod.jpg', 'wb').write(pic.content)
            img = Image.open("apod.jpg")
            img.show()



def motion_detect():
    """detect motion and trigger siren if burgler is detected."""
    
    cap = cv2.VideoCapture(0) #reading from MIA's left eye camera

    respond("Stealth mode activates in", 100)
    for i in range(2, 7):  #runs from 1 to 5
                respond(f"{abs(5 - int(i))}", 100)
    
    

    while True:
        ret, frame1 = cap.read()
        ret, frame2 = cap.read()

        d = cv2.absdiff(frame1, frame2)

        gray = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray, (69, 99), 0)

        #blur = cv2.pyrMeanShiftFiltering(gray, 21, 21)

        ret, th = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    
        #dilated = cv2.dilate(th, np.ones((3,3), np.uint8), iterations = 1)

        #eroded = cv2.erode()

        _, cs, _ = cv2.findContours(th, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        #cv2.drawContours(frame1, cs, -1, (0, 255, 0), 2)

        for c in cs:
            cv2.putText(frame1, "Got IT", (1, 1), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA) 
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x,y), (x + w, y + h), (0, 0, 255), 3)

 
        print(len(cs))

        if len(cs) >= 5:
            respond("Burglar detected. Calling 9 9 9 in", 120)

            for i in range(1, 6):  #runs from 1 to 5
                respond(f"{abs(5 - int(i))}", 100)


        cv2.imshow("Output", frame1)
        cv2.imshow('frmae2', frame2)

        if cv2.waitKey(1) == 27:     #press 'esc' to quit
            break
    
        frame1 = frame2

        ret, frame2 = cap.read()

    cv2.destroyAllWindows()
    cap.release()


#About section
def abt_bu():
    respond("Request confirmed", 120)
    img = Image.open("C:\\Users\\HP\\Desktop\\mia\\floorMap.jpeg") #image path
    img.show()
    respond("Britannia University is the best private university of Cumilla.", 110)

def abt_study_at_bu():
    respond("Request confirmed", 120)

def abt_mission_vision():
    respond("Request confirmed", 120)

def abt_facilities():
    respond("Request confirmed", 120)

def abt_campus_map():
    respond("Request confirmed", 120)
    img = Image.open("C:\\Users\\HP\\Desktop\\mia\\floorMap.jpeg") #image path
    img.show()
    #mia.write(b'B') #point hand to chest (buke haat in bengali)
    respond("Here is BU floor wise map.", 110)

#Academics section
def acad_calender():
    respond("Request confirmed", 120)

def acad_departments():
    respond("Request confirmed", 120)
    img = Image.open("C:\\Users\\HP\\Desktop\\mia\\tutionFee.jpeg") #image path
    img.show()
    #mia.write(b'B') #point hand to chest (buke haat in bengali)
    respond("Here is the list of Tution fee, for more visit our website or consult admission agent.", 110)

def acad_semester_policy():
    respond("Request confirmed", 120)

def acad_grade_sys():
    respond("Request confirmed", 120)

def acad_rules():
    respond("Request confirmed", 120)

#dept of CSE
def cse_faculties():
    respond("Request confirmed", 120)
    img = Image.open("C:\\Users\\HP\\Desktop\\mia\\cseFaculty.png")
    img.show()
    #mia.write(b'B') #point hand to chest (buke haat in bengali)
    respond("Here is the list of our highly qualified Computer Science and Engineering faculty members.", 110)
    

def cse_course_plan():
    respond("Request confirmed", 120)

def cse_credits():
    respond("Request confirmed", 120)

def cse_tution_fee():
    respond("Request confirmed", 120)
    img = Image.open("C:\\Users\\HP\\Desktop\\mia\\tutionFee.jpeg") #image path
    img.show()
    #mia.write(b'B') #point hand to chest (buke haat in bengali)
    respond("Here is the list of Tution fee, for more visit our website or consult admission agent", 110)

def cse_opportunities():
    respond("Request confirmed", 120)

#admission
def addm_notice():
    respond("Request confirmed", 120)

def addm_eligibility():
    respond("Request confirmed", 120)
    

def addm_aid_scholarship():
    respond("Request confirmed", 120)
    

def addm_tution_fee():
    respond("Request confirmed", 120)
    

def addm_credit_tans():
    respond("Request confirmed", 120)
    

#GUI Buttons _________________________________________________________________________________________________________

gui.title("MIA-1: Information Agent of Britannia University.") #title of GUI window
gui.iconbitmap(r"C:\Users\HP\Desktop\mia\bulogo.jpg")          #window icon

#About us Buttons
label1 = tkinter.Label(gui, text="Get to know us (BU)")
label1.grid(row=0, column=2)  #positon = row 1 column 3

button_abtBU = Button(gui, text="About BU", command=abt_bu)                            #button about BU
button_abtBU.config(height=3 , width=18) #set height and width
button_abtBU.grid(row=1, column=0)      #position = row 2 column 1

button_abt_study_bu = Button(gui, text="Why BU?", command=abt_study_at_bu)  
button_abt_study_bu.config(height=3, width=18) #set height and width
button_abt_study_bu.grid(row=1, column=1)      #position = row 2 column 2

button_abt_mission_vision = Button(gui, text="Mission & Vision", command=abt_mission_vision)  
button_abt_mission_vision.config(height=3, width=18) #set height and width
button_abt_mission_vision.grid(row=1, column=2)      #position = row 2 column 3

button_abt_facilities = Button(gui, text="Facilities", command=abt_facilities)  
button_abt_facilities.config(height=3, width=18) #set height and width
button_abt_facilities.grid(row=1, column=3)      #position = row 2 column 4

button_abt_campus_map = Button(gui, text="Campus Map", command=abt_campus_map)  
button_abt_campus_map.config(height=3, width=18) #set height and width
button_abt_campus_map.grid(row=1, column=4)      #position = row 2 column 5

#academics Buttons
"""Comments are omitted as other buttons does the similar job as above."""
label2 = tkinter.Label(gui, text="Academic Information")                            #Academic Information
label2.grid(row=2, column=2)

button_acad_calender = Button(gui, text="Academic Calender", command=acad_calender)  
button_acad_calender.config(height=3, width=18)
button_acad_calender.grid(row=3, column=0)

button_acad_departments = Button(gui, text="Departmens /Schools", command=acad_departments)  
button_acad_departments.config(height=3, width=18)
button_acad_departments.grid(row=3, column=1)

button_acad_semester_policy = Button(gui, text="Semester Policy", command=acad_semester_policy)  
button_acad_semester_policy.config(height=3, width=18)
button_acad_semester_policy.grid(row=3, column=2)

button_acad_grade_sys = Button(gui, text="Grading System", command=acad_grade_sys)
button_acad_grade_sys.config(height=3, width=18)
button_acad_grade_sys.grid(row=3, column=3)

button_acad_rules = Button(gui, text="Regulation", command=acad_rules) 
button_acad_rules.config(height=3, width=18) 
button_acad_rules.grid(row=3, column=4) 

#Dept. of CSE
label3 = tkinter.Label(gui, text="Department of CSE")                            #Dept. of Computer Science & Eng.
label3.grid(row=4, column=2)

button_cse_faculties = Button(gui, text="Faculty Members", command=cse_faculties)
button_cse_faculties.config(height=3, width=18)
button_cse_faculties.grid(row=5, column=0)

button_cse_course_plan = Button(gui, text="Course Plan", command=cse_course_plan)
button_cse_course_plan.config(height=3, width=18)
button_cse_course_plan.grid(row=5, column=1)

button_cse_credit = Button(gui, text="Credits", command=cse_credits) 
button_cse_credit.config(height=3, width=18)
button_cse_credit.grid(row=5, column=2)

button_cse_tution_fee = Button(gui, text="Tution Fee", command=cse_tution_fee)
button_cse_tution_fee.config(height=3, width=18)
button_cse_tution_fee.grid(row=5, column=3)

button_cse_opportunity = Button(gui, text="Facilities", command=cse_opportunities)  
button_cse_opportunity.config(height=3, width=18)
button_cse_opportunity.grid(row=5, column=4)


#Admission
label4 = tkinter.Label(gui, text="Admission Information")                            #Dept. of Computer Science & Eng.
label4.grid(row=6, column=2)

button_addm_notice = Button(gui, text="Admission Notice", command=addm_notice)
button_addm_notice.config(height=3, width=18)
button_addm_notice.grid(row=8, column=0)

button_addm_eligibility = Button(gui, text="Eligibility of Admission", command=addm_eligibility)
button_addm_eligibility.config(height=3, width=18)
button_addm_eligibility.grid(row=8, column=1)

button_addm_finan_scholarship = Button(gui, text="Scholarship", command=addm_aid_scholarship)
button_addm_finan_scholarship.config(height=3, width=18)
button_addm_finan_scholarship.grid(row=8, column=2)

button_addm_tution_fee = Button(gui, text="Tution Fee", command=addm_tution_fee)
button_addm_tution_fee.config(height=3, width=18)
button_addm_tution_fee.grid(row=8, column=3)

#Control panel
"""
label5 = tkinter.Label(gui, text="Control!")                            #Academic Information
label5.grid(row=9, column=2)
"""
button_hi = Button(gui, text="Hi", command=hi)
button_hi.config(height=2, width=18)
button_hi.grid(row=9, column=0)

button_bye = Button(gui, text = "Bye", command=bye)
button_bye.config(height=2, width=18)
button_bye.grid(row=9, column=1)

button_speech = Button(gui, text = "Speech", command=demoSpeech)
button_speech.config(height=2, width=18)
button_speech.grid(row=9, column=2)

button_hs = Button(gui, text = "Hand Shake", command=hand_shake)
button_hs.config(height=2, width=18)
button_hs.grid(row=9, column=3)

button_dhs = Button(gui, text = " down Hand Shake", command=down_hand_shake)
button_dhs.config(height=2, width=18)
button_dhs.grid(row=9, column=4)

button_laser = Button(gui, text = "Target & Fire", command=laser_show)
button_laser.config(height=2, width=18)
button_laser.grid(row=10, column=0)

button_bow = Button(gui, text = "Bow", command=bow)
button_bow.config(height=2, width=18)
button_bow.grid(row=10, column=1)


button_apod = Button(gui, text = "Astronomy Image", command=apod)
button_apod.config(height=2, width=18)
button_apod.grid(row=10, column=2)


button_talk = Button(gui, text = "Talk", command=listen)
button_talk.config(height=2, width=18)
button_talk.grid(row=10, column=3)


button_motion_detect = Button(gui, text = "Motion detect", command=motion_detect)
button_motion_detect.config(height=2, width=18)
button_motion_detect.grid(row=10, column=4)


gui.mainloop()
