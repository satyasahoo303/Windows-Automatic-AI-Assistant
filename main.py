import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np
import pyttsx3

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Harry: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def say(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred while saying: {e}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('SOA A.I at your service')
    say("Hello Users.  This is SOA A.I.  How Can i help you?")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ["email", "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"],
                 ["SOA", "https://www.soa.ac.in/iter"], ["Student Portal", "https://soaportals.com/StudentPortalSOA/#/"],
                 ["MAPS", "https://www.google.com/maps/@20.2930529,85.8179029,15z?entry=ttu"],
                 ["Music", "https://music.youtube.com/watch?v=KLBtgOzNAgI&si=dWLg8MwH6BneVxvG"],
                 ["Movie", "https://www.youtube.com/watch?v=jzYxbnHHhY4"],
                 ["Presentation", "https://1drv.ms/p/s!Apl_FOYJ4gsdimkVK4l30tZOD0Vu?e=xtY16b"],
                 ["Amazon", "https://www.amazon.in/"],
                 ["Sex", "https://www.xnxx3.com/video-im76f71/jonnny_sins_audrey_bitoni_xnxx"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = "https://gaana.com/"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            musicPath = "https://gaana.com/"
            hour = datetime.datetime.now().strftime("%H")
            minutes = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {minutes} minutes")

        elif "open facetime".lower() in query.lower():
            os.system(f"open https://gaana.com/https://gaana.com/")

        elif "open pass".lower() in query.lower():
            os.system(f"open /Applications/Passky.app")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
            say(query)
