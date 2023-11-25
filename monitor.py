
import speech_recognition as sr
import pyttsx3
from queue import Queue

r = sr.Recognizer()
q = Queue(maxsize = 10)

def SpeakText(command):

    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while (1):

    try:

        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.2)
            init = "Hello there. Speak to activate me."
            print(init)
            SpeakText(init)
            audio2 = r.listen(source2, 4, 7)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say ", MyText, "?")
            MyQuestion = "Did you say " + MyText + "?"
            SpeakText(MyQuestion)
            audio3 = r.listen(source2)
            Response = r.recognize_google(audio3)
            Response = Response.lower()
            if ("yes" in Response):
                myresponse = "Confirmation recieved."
                print(myresponse)
                SpeakText(myresponse)
                welcome = "Welcome to the health clinic. Do you have an appointment?"
                print(welcome)
                SpeakText(welcome)
                audio3 = r.listen(source2)
                Response = r.recognize_google(audio3)
                Response = Response.lower()
                if ("yes" in Response):
                    appcode = "Perfect. What is your appointment number today?"
                    print(appcode)
                    SpeakText(appcode)
                    audio3 = r.listen(source2)
                    Response = r.recognize_google(audio3)
                    Response = Response.lower()
                    print(Response)
                    if (Response in q):
                        q.get(Response)
                    else:
                        error = "Oops. This appointment number doesn't exist."
                        continue
                elif ("no" in Response):
                    bookapp = "That's no issue. Let's book you an appointment now."
                    appnum = q.qsize() + 1
                    q.put(appnum)
                    conf = "Perfect your appointment number is "+appnum
                    print(conf)
                    SpeakText(conf)


            else:
                myresponse = "Confirmation not recieved"
                print(myresponse)
                SpeakText(myresponse)
                

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
