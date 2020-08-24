
import json
import random
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
import pygame
import time

authenticator = IAMAuthenticator('9e2rg8T3by_sBIu3SbyCFWZkQLzCHGBfZUHYx0s4U8E3')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
    )
tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/3806638c-85e1-4670-9013-4e303338e90a')


root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

pygame.mixer.init()  # Initialize the mixer module.

class ToneMusic:

    global tone
    tone = ""
    flag = False


    def __init__(self,text):
        self.text = text


    def run(self,tone):

        if tone == "confident":
            path = os.path.join(root_dir,"AI_game", "music", "normal.wav")
        elif tone == "fear" or tone == "sadness":
            path = os.path.join(root_dir,"AI_game", "music", "fearZombie.wav")
        elif tone == "anger":
            path = os.path.join(root_dir,"AI_game", "music", "angry.wav")
        elif tone == "analytical":
            path = os.path.join(root_dir,"AI_game", "music", "analytical.wav")
        elif tone == "tentative":
            path = os.path.join(root_dir,"AI_game", "music", "tentative.wav")

        if(flag == False):
            pygame.mixer.fadeout(2000)
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(loops=3, start=0.0)



    def playToneMusic(self):
        text = self.text
        tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
        ).get_result()
        hold = tone_analysis['document_tone']['tones']
        toneName = ""
        toneValue = 0
        for post in hold:
            tmp = post['score']
            if(tmp>toneValue):
                toneValue = tmp
                toneName = post['tone_id']

        global tone
        global flag
        if( tone != toneName):
            tone = toneName
            flag = False
        else:
            flag = True
        return toneName
