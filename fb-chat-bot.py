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

            elif ("😎" in msg):
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "[ IDH BH9NGII G9NG K9 B!G F9TH3R M9RK  09 FIIR3 <<(( (Y) ))>>IDH 9LL KIDXX   KID))X 09 MY L9ND)) :D 🤍 -: ]  (( (y) ))"
                sendMsg()
                reply = "[[ :) ' #IDH BH9NGI G9NG T9TT0 KII M99 K0 UTH99 K9R P9T9K K3 CH0DN33 W9[L4 :D <3 (Y)??? :D (Y) <(') ❤ 😃[[ #UN5T0PP9BL3_F9DD3B994Z_M9RK 09 FIIR33 ((Y)) [9]____ ^(_=_)^ (Y) :V<(') [[-----------  #F33L UR D9D KIDZ (( M9RK H3R3 :D (Y) (Y)_____}} (Y) :V 😈 🔥^^ ]]"
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = "IDH K3 PILL0 KII G9ND M3 KH9D99 L9ND D3N3 W9L999 M9RKKK 9LW9YSXX 09 FIIR33  (y)"
                sendMsg()
                time.sleep(60)
                reply = "IDH BH9NGII G9NG KI M999 BH3N K0 XH0D K9R P9KI5T99N M3 F3KKN33 W9L9 M99RKK H3R3 :D (y) "
                sendMsg()
                time.sleep(60)
                reply = "😎 😎 (Y) 😈  ❤ IDH K3 XHUD3XXXX KIDX BH9=GN99 M99T 😛 😃  XU'D3'XX K93 NIK=K93 NIK=K93 89'CH'00 K9 B99P  😛 😃 (Y) ❤ 😎 8|[[=M9RK'H'3R'3]]  😎 😎"
                sendMsg()
                time.sleep(60)
                reply = " XHUD33 HU3 IDH K3 PILL0 KI 4MMI K0 B4444R B44444R P4KD K4R UTH4 K4R CH0DN33 W4L44 😎 8|[[=M9RK' 099 FIRR33 ]]  😎 😎"
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
