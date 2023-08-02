import os
import subprocess
import ctypes
import time
import json

try:
    import pynput
    import numpy
    import fade
    import requests
    from pypresence import Presence
    import playsound # required ver HAS to be 1.2.2
except ImportError:
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("Installing modules... | e621.tech")
    print("You're a bit dumb, aren't ya? Running 'runthisfirst.bat' for you...")
    print("Reopen launch.bat after this window closes")
    time.sleep(2)
    subprocess.call([r'runthisfirst.bat'])

running = False
mode = "LMB"
ver = "0.2"

cfg = {
  "keybind": "x",
  "min": 13,
  "max": 15,
  "switch": "v",
  "panic": "z"
} # example config

cmd = 'mode 60,18'
os.system(cmd)
os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW(f"ParaphiliaRehabClub | v{ver} | e621.tech")

class Config:
    try:
        with open('config.json') as f:
            config = json.load(f)
            keybind = config['keybind']
            min = config['min']
            max = config['max']
            switch = config['switch']
            panic = config['panic']
    except Exception:
        print(fade.pinkred("""    ____  ___    ____  ___    ____  __  ________    _______ 
   / __ \/   |  / __ \/   |  / __ \/ / / /  _/ /   /  _/   |
  / /_/ / /| | / /_/ / /| | / /_/ / /_/ // // /    / // /| |
 / ____/ ___ |/ _, _/ ___ |/ ____/ __  // // /____/ // ___ |
/_/   /_/  |_/_/ |_/_/  |_/_/   /_/ /_/___/_____/___/_/  |_|
                                                            """))
        print(fade.pinkred("config.json is missing or damaged\ncreating one & restarting..."))
        json_obj = json.dumps(cfg, indent=5)
        with open("config.json", "w") as outfile:
            outfile.write(json_obj)
        time.sleep(3)
        os._exit(0)

if Config.min == Config.max:
    Config.min = Config.min - 1 # lazy fix

response = requests.get("https://raw.githubusercontent.com/murrtube/Paraphilia/main/ver.json")
if response.json()["ver"] != ver:
    print(fade.pinkred("""    ____  ___    ____  ___    ____  __  ________    _______ 
   / __ \/   |  / __ \/   |  / __ \/ / / /  _/ /   /  _/   |
  / /_/ / /| | / /_/ / /| | / /_/ / /_/ // // /    / // /| |
 / ____/ ___ |/ _, _/ ___ |/ ____/ __  // // /____/ // ___ |
/_/   /_/  |_/_/ |_/_/  |_/_/   /_/ /_/___/_____/___/_/  |_|
                                                            """))
    print(fade.pinkred("new version available\nget it @ e621.tech"))
    time.sleep(5)
    os._exit(0)

intro = """    ____  ___    ____  ___    ____  __  ________    _______ 
   / __ \/   |  / __ \/   |  / __ \/ / / /  _/ /   /  _/   |
  / /_/ / /| | / /_/ / /| | / /_/ / /_/ // // /    / // /| |
 / ____/ ___ |/ _, _/ ___ |/ ____/ __  // // /____/ // ___ |
/_/   /_/  |_/_/ |_/_/  |_/_/   /_/ /_/___/_____/___/_/  |_|
                                                            
by the one whos name shall not be spoken
everybody wants to be a winner. become one today: e621.tech"""
info = f"Keybind: {Config.keybind}\nMin CPS: {Config.min}\nMax CPS: {Config.max}\nPanic key: {Config.panic}\nMode: {mode} ({Config.switch} to change)"
print(fade.pinkred(intro))
print(fade.pinkred(info))
try:
    playsound.playsound('startup.mp3', True)
except Exception:
    os.system("cls")
    print(fade.pinkred("""    ____  ___    ____  ___    ____  __  ________    _______ 
   / __ \/   |  / __ \/   |  / __ \/ / / /  _/ /   /  _/   |
  / /_/ / /| | / /_/ / /| | / /_/ / /_/ // // /    / // /| |
 / ____/ ___ |/ _, _/ ___ |/ ____/ __  // // /____/ // ___ |
/_/   /_/  |_/_/ |_/_/  |_/_/   /_/ /_/___/_____/___/_/  |_|
                                                            """))
    print(fade.pinkred("startup.mp3 missing or damaged"))
    time.sleep(5)
    os._exit(0)
print("\n")

client_id = "969639445013868615"
RPC = Presence(client_id=client_id)
RPC.connect()
RPC.update(large_image="main", large_text="Paraphilia",details=f"v{response.json()['ver']}",state="ParaphiliaRehabClub",buttons=[{"label": "Start winning", "url": "https://e621.tech/"}])


def on_press(key):
    if key == pynput.keyboard.KeyCode.from_char(Config.switch):
        global mode
        global running
        running = not running

        if mode == "LMB":
            mode = "RMB"
            running = False
            print ("\033[A                             \033[A")
            print ("\033[A                             \033[A")
            print ("\033[A                             \033[A")
            print ("\033[A                             \033[A")
            print(fade.pinkred(f"Mode: {mode} ({Config.switch} to change)"))
            print(fade.fire('[-] Disabled'))
        elif mode == "RMB":
            mode = "LMB"
            running = False
            print ("\033[A                             \033[A")
            print ("\033[A                             \033[A")
            print ("\033[A                             \033[A")
            print ("\033[A                             \033[A")
            print(fade.pinkred(f"Mode: {mode} ({Config.switch} to change)"))
            print(fade.fire('[-] Disabled'))

    if key == pynput.keyboard.KeyCode.from_char(Config.keybind):

        running = not running
        if running:
            print ("\033[A                             \033[A")
            print ("\033[A                             \033[A")
            print(fade.greenblue('[+] Enabled'))
        else:
            print ("\033[A                             \033[A")
            print ("\033[A                             \033[A")
            print(fade.fire('[-] Disabled'))

    if key == pynput.keyboard.KeyCode.from_char(Config.panic):

        os._exit(0)

def main():
    mouse = pynput.mouse.Controller()
    keyboard = pynput.keyboard

    keyboardlistener = keyboard.Listener(on_press=on_press)
    keyboardlistener.start()

    lastTime = time.time()
    delay = 1 / Config.min

    rng = numpy.random.default_rng(seed=420)

    while True:
        if running:
            currentTime = time.time()

            if currentTime - lastTime > delay:
                if mode == "LMB":
                    mouse.click(pynput.mouse.Button.left)
                    lastTime = currentTime

                    delay = 1 / rng.integers(low=Config.min, high=Config.max)
                elif mode == "RMB":
                    mouse.click(pynput.mouse.Button.right)
                    lastTime = currentTime

                    delay = 1 / rng.integers(low=Config.min, high=Config.max)


main()
