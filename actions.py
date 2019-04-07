from elasticsearch import Elasticsearch
import platform
from subprocess import call
# from elasticsearch import Elasticsearch
p=platform.system()
L="Linux"
W="Windows"
M="Darwin"
es = Elasticsearch()
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
        call(["open","/Applications/Spotify.app"])
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
    result = es.search(index="hacktjfinal", body={"query": {"match": {"message": hashtag}}})
    text = ""
    for tweet in result['hits']['hits']:
        print(tweet['_source']['user'])
        print(tweet['_source']['message'])
        print()
        text += "@" + tweet['_source']['user'] + "\n" + tweet['_source']['message'] + "\n\n"
    call(["curl", "-X", "GET", 'localhost:8004/input?text=' + urllib.parse.quote_plus(text)])
if __name__=="__main__":
    get_tweets("stock market")
#curl -X PUT localhost:9200/test3/_settings -d {\"index\" : {\"mapping\" : {\"total_fields\" : {\"limit\" : \"5000\"}}}}
    #print(platform.system())
    #"Linux","Windows","Darwin"
