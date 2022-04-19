#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy

import os
from std_msgs.msg import String, Int16
import numpy as np
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import os
import time
import playsound
import pyttsx3


def mic_setting_check():
    audio = pyaudio.PyAudio()

    for index in range(audio.get_device_count()):
        desc = audio.get_device_info_by_index(index)
        print("DEVICE: {device}, INDEX: {index}, RATE: {rate} ".format(
            device=desc["name"], index=index, rate=int(desc["defaultSampleRate"])))

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

# def Saying(msg):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     volume = engine.getProperty('volume')
#     rate = engine.getProperty('rate')
#     print('rate = ',rate)
#     engine.setProperty('rate', 180)
#     engine.say(msg)
#     engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    class_topic=2
    

    with sr.Microphone(device_index = 13, sample_rate = 44100, chunk_size = 1024 ) as source:
        print("Say something!")
        audio = r.listen(source)
        # audio = r.listen(source, phrase_time_limit=2)
        query = r.recognize_google(audio,language="ko")

    try:
        print("Google Speech Recognition thinks you said : " + query)
        
        (class_topic)=str(query[:1])

        if class_topic =='위':
            class_topic ='up'
        elif class_topic =='아':
            class_topic='down'
        elif class_topic =='지':
            class_topic='B'+str(query[3])
            speak(query[:5]+str("으로 가겠습니다."))
        else:
            speak(query[:2]+str("으로 가겠습니다."))
        button_push = 'rostopic pub /Class_Name std_msgs/String \\"'+str(class_topic)+'\\"'
        print(button_push)
        os.system(button_push)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def start_count(Int16):
    global state_count
    state_count = Int16.data

if __name__ == '__main__':
    rospy.init_node('talk_class',anonymous=True)
    sub = rospy.Subscriber("/talk_class",Int16,start_count)
    mic_setting_check()
    state_count=0

    while not rospy.is_shutdown():
        if state_count ==1:
            
            get_audio()
            state_count = state_count +1