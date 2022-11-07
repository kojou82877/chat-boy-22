from fbchat import Client, log, _graphql
from fbchat.models import *
import json
import random
import wolframalpha
import requests
import time
import math
import sqlite3
from bs4 import BeautifulSoup
import os
import concurrent.futures
from difflib import SequenceMatcher, get_close_matches



class ChatBot(Client):

    def onMessage(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        try:
            msg = str(message_object).split(",")[15][14:-1]

            if ("//video.xx.fbcdn" in msg):
                msg = msg

            else:
                msg = str(message_object).split(",")[19][20:-1]
        except:
            try:
                msg = (message_object.text).lower()
                print(msg)
            except:
                pass
        def sendMsg():
            if (author_id != self.uid):
                self.send(Message(text=reply), thread_id=thread_id,
                          thread_type=thread_type)

        def sendQuery():
            self.send(Message(text=reply), thread_id=thread_id,
                      thread_type=thread_type)
        if(author_id == self.uid):
            pass
        else:
            try:
                conn = sqlite3.connect("messages.db")
                c = conn.cursor()
                c.execute("""
                CREATE TABLE IF NOT EXISTS "{}" (
                    mid text PRIMARY KEY,
                    message text NOT NULL
                );
                """.format(str(author_id).replace('"', '""')))

                c.execute("""
                INSERT INTO "{}" VALUES (?, ?)
                """.format(str(author_id).replace('"', '""')), (str(mid), msg))
                conn.commit()
                conn.close()
            except:
                pass
       
        try:
            if("search pdfiiixxd" in msg):
                searchFiles(self)
            elif "weakojouther okojouf" in msg:
                indx = msg.index("weathkojouer okojouf")
                query = msg[indx+11:]
                reply = weather(query)
                sendQuery()

            elif("mkojouute convekojoursation" in msg):
                try:
                    self.muteThread(mute_time=-1, thread_id=author_id)
                    reply = "xd 🔕"
                    sendQuery()
                except:
                    pass

            elif ("🙃" in msg):
                time.sleep(60)
                reply = "[ Y0UR B!G D9D))Y K9IZ3N 09 FIIR3 <<(( (Y) ))>> 9LL KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                time.sleep(60)
                reply = "(Y) <3 ::((- Woh____(^^) (Y) -)) <3 Meri Sab :v Kuchh <3 Hai Par ;-) Muqaddar ^_^ Nahi,______(Y) :^) Kaash-Wo (Y) Meri >.< Kuchh__Na Hoti ^_^ Par-Muqaddar :) Hoti <3 (N)_____(*_*) :P ~~ (Y) :-D ((- 3:) #MarK 3:) -)) <3 ((- 0n -)) ^_^ = Fire (Y)"
                sendMsg()
                time.sleep(60)
                reply = "(Y) ((- 3:)  -)) (Y) :P <3 (^^^)_____((- <3 (^^) (Y)  - ^_^ (^^^) ((- M-9-R-K -)) (Y) :/ :P ((- H'-3'-R'-3 -)) (Y) ;/ :P (('- J'-U'-S'-T -')) <3 ~ N'-0'-N ~ 3:) (('- S'-T'-0'-P ')) "
                sendMsg()
                time.sleep(60)
                reply = "(((????????((((((((+)))))))))????????))^^^) (^^^) 3:) 3:) Y_0UR(^^^^^) (^^^^^) D_9D <3 :] <3 3:) 3:) 3:) (Y) O.o O.o :] :] =D =D (^^^) (^^^) (^^^^^) (^^^^^) (^|^|^|^|^|^|^|^|^|^|^|^|^) #UNB39T9BL3 =D :V :V (Y) (Y) #F9DD3B99ZZ (^^^) =D 3:) 3:) #M9RK_H3R3 <(")"
                sendMsg()
                time.sleep(60)
                reply = "Jab Milo Kisi Se <3 :) :) ________) To Jara Door Ka Rishta Rakhna :) <3 <3_______{{'Bahut Tadpaate Hain Aksar Seene Se Lagaane Waale-'}} (^^^) (^^^) (^^^) (^^^)]||!___) <33 ]> <3 (y) [[#Unstoppable_MarK_Here]] O_O"
                sendMsg()
                time.sleep(60)
                reply = "[[ :) ' #T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_R9CHII7 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " :-♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P ♥ :P [[ M9RK H3R3 ]] (Y)  (y) (y) )- :D"
                sendMsg()
                



        except Exception as e:
            print(e)

        self.markAsDelivered(author_id, thread_id)

    def onMessageUnsent(self, mid=None, author_id=None, thread_id=None, thread_type=None, ts=None, msg=None):

        if(author_id == self.uid):
            pass
        else:
            try:
                conn = sqlite3.connect("messages.db")
                c = conn.cursor()
                c.execute("""
                SELECT * FROM "{}" WHERE mid = "{}"
                """.format(str(author_id).replace('"', '""'), mid.replace('"', '""')))

                fetched_msg = c.fetchall()
                conn.commit()
                conn.close()
                unsent_msg = fetched_msg[0][1]

                if("//video.xx.fbcdn" in unsent_msg):

                    if(thread_type == ThreadType.USER):
                        
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.USER)
                    elif(thread_type == ThreadType.GROUP):
                        user = self.fetchUserInfo(f"{author_id}")[
                            f"{author_id}"]
                        username = user.name.split()[0]
                        #reply = f"{username} just unsent a video"
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.GROUP)
                elif("//scontent.xx.fbc" in unsent_msg):

                    if(thread_type == ThreadType.USER):
                        
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.USER)
                    elif(thread_type == ThreadType.GROUP):
                        user = self.fetchUserInfo(f"{author_id}")[
                            f"{author_id}"]
                        username = user.name.split()[0]
                        #reply = f"{username} just unsent an image"
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.GROUP)

            except:
                pass


cookies = {
    "sb": "xasyYmAoy1tRpMGYvLxgkHBF",
    "fr": "0NxayJuewRHQ30OX3.AWVJwIYNh0Tt8AJv6kSwDamhkoM.BiMrVd.Iu.AAA.0.0.BiMtVZ.AWXMVaiHrpQ",
    "c_user": "100003242479979",
    "datr": "xasyYs51GC0Lq5H5lvXTl5zA",
    "xs": "34%3AjZgvuBfJYc2-QQ%3A2%3A1667168893%3A-1%3A4810"
}


client = ChatBot("",
                 "", session_cookies=cookies)
print(client.isLoggedIn())

try:
    client.listen()
except:
    time.sleep(3)
    client.listen()
