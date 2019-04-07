import platform
from subprocess import call
from elasticsearch import Elasticsearch
p=platform.system()
L="Linux"
W="Windows"
M="Darwin"
def open_google():
    if p==L:
        call(["google-chrome"])
    elif p==M:
        call(["open","[location of google]"])
def open_word():
    if p==M:
        call(["open","[location of Word]"])
def open_spotify():
    if p==M:
        call(["open","[location of spotify]"])
def computer_volume(vol):
    if p==L:
        call(["amixer", "-D", "pulse", "sset", "Master", str(vol)+"%"])
    elif p==M:
        call(["osascript","-e","\"set Volume "+str(vol//10)+"\""])
def computer_mute(bool):
    if p==L:
        if bool:
            call(["amixer", "-D", "pulse", "sset", "Master", "mute"])
        else:
            call(["amixer", "-D", "pulse", "sset", "Master", "unmute"])
    elif p==M:
        call(["osascript","-e","\"set volume output muted "+bool.upper()])
def get_tweets(hashtag):
    
if __name__=="__main__":
    print(platform.system())
    #"Linux","Windows","Darwin"
