import subprocess, platform
def open_google():
    subprocess.call(["open","[location of google]"])
def open_word():
    subprocess.call(["open","[location of Word]"])
def open_spotify():
    subprocess.call(["open","[location of spotify]"])
def computer_volume_0():
    call(["amixer", "-D", "pulse", "sset", "Master", "0%"])
def computer_volume_100():
    call(["amixer", "-D", "pulse", "sset", "Master", "100%"])

if __name__=="__main__":
    print(platform.system())
