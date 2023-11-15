# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:27:38 2023

@author: ASHOK
"""

import pyttsx3             # convert text to speech
import speech_recognition as sr  # convert speech to text
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def commands():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print('wait for few moments ...')
        query = r.recognize_google(audio, language='en-in')
        print(f'you just said {query}\n')

    except Exception as e:
        print(e)
        speak('please tell me again')
        query = 'none'

    return query


def wishings():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        print('Good Morning Boss...')
        speak('Good Morning Boss')

    elif hour >= 12 and hour < 17:
        print('Good AfterNoon Boss...')
        speak('Good Afternoon Boss')

    elif hour >= 17 and hour < 21:
        print('Good Evening Boss...')
        speak('Good Evening Boss')

    else:
        print('Now sleeping Time Boss...')
        speak('now sleeping time boss')


if __name__ == '__main__':
    wishings()
    query = commands().lower()

    if 'time' in query:
        strtime = datetime.datetime.now().strftime('%H:%M:%S')
        print(strtime)
        speak(f'Boss,The time is {strtime}')

    elif 'open chrome' in query:
        speak('opening Google chrome application Boss')
        os.startfile(
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif 'wikipedia' in query:
        speak('Searching in wikipedia...')
        try:
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=1)
            speak('According to wikipedia,')
            print(results)
            speak(results)

        except:
            speak('No results found')
            print('No results found')

    elif 'play' in query:
        query = query.replace('play', '')
        speak('playing' + query)
        pywhatkit.playonyt(query)

    elif 'type' in query:
        speak('what should i write')
        while True:
            writeInNotepad = commands()
            if writeInNotepad == 'exit typing':
                speak('done sir')
                break
            else:
                pyautogui.write(writeInNotepad)

    elif 'joke' in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif 'exit program' in query:
        speak("I'm leaving sir")
        quit()
