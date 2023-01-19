import time,os,random, json, sys, platform
from colorama import Fore, Back, Style, init
from valclient.client import Client
from getkey import getkey, keys

init(autoreset=True)

version = 0
title = Fore.RED+"Valo"+Fore.WHITE+"Lock | Version: "+Fore.RED+str(version)

regions = ['BR','EU','KR','LATAM','NA','AP']
regionnames = {
    "BR":"Brazil",
    "EU":"Europe",
    "KR":"Korea",
    "LATAM":"Latin America",
    "NA":"North America",
    "AP":"Southeast Asia / Asia-Pacific",
}

agents = {}
with open('data.json','r') as f:
    agents = json.load(f)

maps = ['Lotus','Pearl','Fracture','Breeze','Icebox','Bind','Haven','Split','Ascent']


def region_select():
    """
    Select a users region
    """
    selecting = True
    selected = 0
    while selecting:
        os.system("clear")
        print(title)
        print(Fore.CYAN+"Select a region using UP, DOWN, and ENTER keys\n")
        for i in range(len(regions)):
            if i == selected:
                print(Back.WHITE+regionnames[regions[i]])
            else:
                print(regions[i])
        print("")
        key = getkey()
        if key == keys.UP:
            if selected < 1:
                pass
            else:
                selected-=1
        elif key == keys.DOWN:
            if selected>len(regions)-2:
                pass
            else:
                selected+=1
        elif key == keys.ENTER:
            selecting = False
    os.system("clear")
    print(title)
    print("You selected "+regions[selected]+" ("+regionnames[regions[selected]]+")")
    input(Fore.CYAN+"\nPress ENTER to continue"+Fore.RESET)
    return regions[selected].lower()
def agent_select():
    """
    Select an agent
    """
    selecting = True
    while selecting:
        os.system("clear")
        print(title)
        agent = input("Enter an angent name (like KAYO or Jett)"+Fore.RED+"\nLeave blank to cancle"+Fore.RESET+"\n\n> ").lower()
        if agent.lower() in agents['agents'].keys():
            selecting = False
        elif agent == "":
            selecting = False
    if agent == "":
        pass
    else:
        os.system("clear")
        print(title)
        print("You selected "+agent)
        input(Fore.CYAN+"\nPress ENTER to continue"+Fore.RESET)
        return agent.lower()
def map_select():
    """
    Select a map
    """
    selecting = True
    selected = 0
    while selecting:
        os.system("clear")
        print(title)
        print(Fore.CYAN+"Select a map using UP, DOWN, and ENTER keys\n")
        for i in range(len(maps)):
            if i == selected:
                print(Back.WHITE+maps[i])
            else:
                print(maps[i])
        print("")
        key = getkey()
        if key == keys.UP:
            if selected < 1:
                pass
            else:
                selected-=1
        elif key == keys.DOWN:
            if selected>len(maps)-2:
                pass
            else:
                selected+=1
        elif key == keys.ENTER:
            selecting = False
    os.system("clear")
    print(title)
    print("You selected "+maps[selected])
    input(Fore.CYAN+"\nPress ENTER to continue"+Fore.RESET)
    return maps[selected].lower()

if platform.system() == 'Windows':
    os.system('cls & title ValoLock')
#Uncomment this to lock to windows
elif platform.system() != 'Windows':
    os.system("clear")
    print(title)
    print(Fore.CYAN+"It looks like you are on "+platform.system()+". ValoLock works best on Windows.")
    input(Fore.BLACK+"\nPress ENTER to exit")
    exit()

client = Client(region=region_select())
client.activate()

#maps
lotus = []
pearl = []
fracture = []
breeze = []
icebox = []
bind = []
haven = []
split = []
ascent = []

valolock_history = []

while True:
    os.system("clear")
    print(title)
    print(Back.RED+"\n  Menu  ")
    print("[1] - Set Agent Pool\n[2] - Start Instalock")
    key = getkey()
    if key == "1":
        location = map_select()
        selecting = True
        pool = []
        while selecting:
            agent = agent_select()
            if agent in pool:
                pass
            elif agent == None:
                pass
            else:
                pool.append(agent)
            if input("Would you like to add another agent? (Y/n)").lower() != "y":
                selecting = False
        if location == "lotus":
            lotus = []
            for i in range(len(pool)):
                lotus.append(pool[i])
        elif location == "pearl":
            pearl = []
            for i in range(len(pool)):
                pearl.append(pool[i])
        elif location == "fracture":
            fracture = []
            for i in range(len(pool)):
                fracture.append(pool[i])
        elif location == "breeze":
            breeze = []
            for i in range(len(pool)):
                breeze.append(pool[i])
        elif location == "icebox":
            icebox = []
            for i in range(len(pool)):
                icebox.append(pool[i])
        elif location == "bind":
            bind = []
            for i in range(len(pool)):
                bind.append(pool[i])
        elif location == "haven":
            haven = []
            for i in range(len(pool)):
                haven.append(pool[i])
        elif location == "split":
            split = []
            for i in range(len(split)):
                split.append(pool[i])
        elif location == "ascent":
            ascent = []
            for i in range(len(pool)):
                ascent.append(pool[i])
        else:
            print("Error: No location")
    elif key == "2":
        locking = True
        status = "Waiting for match"
        while locking:
            try:
                os.system("clear")
                print(title)
                sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                matchID = client.pregame_fetch_match()['ID']
                if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in valolock_history)):
                    status = "Locking Agent"
                    matchInfo = client.pregame_fetch_match(matchID)
                    mapName = matchInfo["MapID"].split('/')[-1].lower()
                    if mapName == "Lotus":
                        agent = random.choice(lotus)
                    elif mapName == "Pearl":
                        agent = random.choice(pearl)
                    elif mapName == "Fracture":
                        agent = random.choice(fracture)
                    elif mapName == "Breeze":
                        agent = random.choice(breeze)
                    elif mapName == "Icebox":
                        agent = random.choice(icebox)
                    elif mapName == "Bind":
                        agent = random.choice(bind)
                    elif mapName == "Haven":
                        agent = random.choice(haven)
                    elif mapName == "Split":
                        agent = random.choice(split)
                    elif mapName == "Ascent":
                        agent = random.choice(ascent)
                    print("Selecting agent: "+Fore.GREEN+agent)
                    client.pregame_select_character(agents['agents'][agent])
                    client.pregame_lock_character(agents['agents'][agent])
                    print("Agent Locked!")
                    locking = False
            except Exception as e:
                print("", end="")
