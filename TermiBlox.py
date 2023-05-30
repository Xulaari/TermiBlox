art = """\x1b[36m     s                                                   .          ..          ..                          
    :8                                                  @88>  . uW8"      x .d88"                           
   .88                  .u    .      ..    .     :      %8P   `t888        5888R          u.      uL   ..   
  :888ooo      .u     .d88B :@8c   .888: x888  x888.     .     8888   .    '888R    ...ue888b   .@88b  @88R 
-*8888888   ud8888.  ="8888f8888r ~`8888~'888X`?888f`  .@88u   9888.z88N    888R    888R Y888r '"Y888k/"*P  
  8888    :888'8888.   4888>'88"    X888  888X '888>  ''888E`  9888  888E   888R    888R I888>    Y888L     
  8888    d888 '88%"   4888> '      X888  888X '888>    888E   9888  888E   888R    888R I888>     8888     
  8888    8888.+"      4888>        X888  888X '888>    888E   9888  888E   888R    888R I888>     `888N    
 .8888Lu= 8888L       .d888L .+     X888  888X '888>    888E   9888  888E   888R   u8888cJ888   .u./"888&   
 ^%888*   '8888c. .+  ^"8888*"     "*88%""*88" '888!`   888&  .8888  888"  .888B .  "*888*P"   d888" Y888*" 
   'Y"     "88888%       "Y"         `~    "    `"`     R888"  `%888*%"    ^*888%     'Y"      ` "Y   Y"    
             "YP'                                        ""       "`         "%                             
                                                                                                            \x1b[39m"""

print(art)

import requests, webbrowser, os, pathlib, ctypes, time, json, psutil, glob
from pypresence import Presence

localappdata = os.environ["localappdata"]

client_id = "721829916731113503"
RPC = Presence(client_id)

cwd = os.getcwd()

ctypes.windll.kernel32.SetConsoleTitleW("aw00ga")

version = requests.get("https://setup.rbxcdn.com/version").text
userversion = requests.get("https://setup.rbxcdn.com/version").text.replace(
    "version-", ""
)

if not os.path.exists(f"{localappdata}\\TermiBlox"):
    os.mkdir(f"{localappdata}\\TermiBlox")
    with open(
        f"{localappdata}\\TermiBlox\\settings.json",
        "w",
    ) as jsoncontent:
        jsoncontent.write(
            requests.get(
                "https://raw.githubusercontent.com/Xulaari/TermiBlox/main/settings.json"
            ).text
        )

with open(f"{localappdata}\\TermiBlox\\settings.json", "r") as file:
    data = json.load(file)

    if data["asktoaccesssettings"] == False:
        pass
    elif data["asktoaccesssettings"] == True:
        settings = input(
            "[>] Do you want to access settings? This will not be shown again unless toggled manually: "
        ).lower()
        if settings == "y" or settings == "yes":
            setsy = input("[>] Settings available.\n[>] 1.Enable old oof: ")
            if setsy == "1":
                oofsound = requests.get(
                    "https://github.com/pizzaboxer/bloxstrap/raw/main/Bloxstrap/Resources/Mods/OldDeath.ogg"
                ).content
                with open("OldDeath.ogg", "wb") as ODG:
                    ODG.write(oofsound)
                    ODG.close()
                    os.replace(
                        "OldDeath.ogg",
                        f"{localappdata}\\Roblox\\Versions\\{version}\\content\\sounds\\ouch.ogg",
                    )
            else:
                pass

# actual launcher, settings above ^^

currentpath = str(pathlib.Path(__file__).parent.absolute())

print(f"[>] TermiBlox located at: \x1b[32m{currentpath}\x1b[39m")

print(
    f"[>] Roblox version located as: \x1b[32m{userversion}\x1b[39m. Standby for update check |",
    end=" ",
)

if not os.path.exists(f"{localappdata}\\Roblox"):
    TermiBloxinstall = input(
        "\x1b[31mERR\x1b[39m\n[>] Roblox is not installed on your system, \x1b[36mTermiBlox\x1b[39m can automatically install it for you. Do you want to install Roblox?: "
    ).lower()
    if TermiBloxinstall == "y" or TermiBloxinstall == "yes":
        print("[>] Roblox is being installed, Standby.")
        bootstrapper = requests.get("http://setup.rbxcdn.com/Roblox.exe")
        with open("RobloxPlayerLauncher.exe", "wb") as robloxlauncher:
            robloxlauncher.write(bootstrapper.content)
            robloxlauncher.close()
            os.system(f"{currentpath}\\RobloxPlayerLauncher.exe")
            print(
                "[>] Roblox has successfuly installed. Relaunch \x1b[36mTermiBlox\x1b[39m."
            )
            exit()
    elif TermiBloxinstall == "n" or TermiBloxinstall == "no":
        exit()

elif not os.path.exists(
    f"{localappdata}\\Roblox\\Versions\\{version}"
) and os.path.exists(f"{localappdata}\\Roblox"):
    TermiBloxupdate = input(
        f"\x1b[31mERR\x1b[39m\n[>] The version of the newest roblox version is different to the version you currently have installed.\n[>] Would you like to upgrade your currently installed version?: "
    )
    if TermiBloxupdate == "y" or TermiBloxupdate == "yes":
        robloxplayerlauncher = requests.get(
            f"https://setup.rbxcdn.com/{version}-Roblox.exe"
        ).content
        with open("RobloxPlayerLauncher.exe", "wb") as rpl:
            rpl.write(robloxplayerlauncher)
            rpl.close()
            os.system(f"{currentpath}\\RobloxPlayerLauncher.exe")
            print("[>] Updated. Relaunch TermiBlox.")
            exit()

if data["futureisbright"] == True:
    if not os.path.exists(
        f"{localappdata}\\Roblox\\Versions\\{version}\\ClientSettings"
    ):
        os.mkdir(f"{localappdata}\\Roblox\\Versions\\{version}\\ClientSettings")
    with open(
        f"{localappdata}\\Roblox\\Versions\\{version}\\ClientSettings\\ClientAppSettings.json",
        "w",
    ) as clientsettings:
        clientsettings.write(
            """
{
  "FFlagDebugForceFutureIsBrightPhase3": "True"
}"""
        )
        clientsettings.close()


print("\x1b[32mOK\x1b[39m")

keystroke = input(
    "[>] Welcome to TermiBlox! Enter the PlaceID/Name of the game you want to join: "
).lower()

# gameinfo

if keystroke.isdigit():
    UID = requests.get(
        f"https://apis.roblox.com/universes/v1/places/{keystroke}/universe"
    ).json()["universeId"]
    GAMENAME = requests.get(
        f"https://games.roblox.com/v1/games?universeIds={UID}"
    ).json()["data"][0]["name"]
    GAMETHUMBNAIL = requests.get(
        f"https://thumbnails.roblox.com/v1/games/icons?universeIds={UID}&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false"
    ).json()["data"][0]["imageUrl"]
    GAMECREATOR = requests.get(
        f"https://games.roblox.com/v1/games?universeIds={UID}"
    ).json()["data"][0]["creator"]["name"]
elif keystroke == ":l":
    print(
        "[>] Games available to be joined by their names are: "
        + ", ".join(data["games"])
        + ".",
        end=" ",
    )
    input()
    exit()
else:
    UID = requests.get(
        f"https://apis.roblox.com/universes/v1/places/"
        + str(data["games"][keystroke])
        + "/universe"
    ).json()["universeId"]
    GAMENAME = requests.get(
        f"https://games.roblox.com/v1/games?universeIds={UID}"
    ).json()["data"][0]["name"]
    GAMETHUMBNAIL = requests.get(
        f"https://thumbnails.roblox.com/v1/games/icons?universeIds={UID}&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false"
    ).json()["data"][0]["imageUrl"]
    GAMECREATOR = requests.get(
        f"https://games.roblox.com/v1/games?universeIds={UID}"
    ).json()["data"][0]["creator"]["name"]

# launch

if keystroke.isdigit():
    webbrowser.open(f"roblox://experiences/start?placeId={keystroke}")
else:
    webbrowser.open(
        "roblox://experiences/start?placeId=" + str(data["games"][keystroke])
    )

print(f"[>] Starting roblox. Game: {GAMENAME}")


def checkifrunning(app_name):
    for process in psutil.process_iter():
        if process.name() == app_name:
            return True
    return False


StartTime = time.time()

# let roblox have enough time to launch.

time.sleep(data["waittime"])

# thank you stackoverflow for this
# we just extract the jobid by looking at the most recent file,
# then we will index jobid and status, takeaway from them and boom.

files = os.listdir(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\logs")
paths = [
    os.path.join(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\logs", basename)
    for basename in files
]

newest = max(paths, key=os.path.getctime)

with open(newest, "r") as log:
    logfile = log.read()
    startIndex = logfile.index("jobId")
    endIndex = logfile.index("status")

jobId = logfile[startIndex + 8 : endIndex - 3]

RPC.connect()

if data["letpeoplejoinme"] == False and keystroke.isdigit():
    joinexperience = f"roblox://experiences/start?placeId={keystroke}"
elif data["letpeoplejoinme"] == True and keystroke.isdigit():
    joinexperience = (
        f"roblox://experiences/start?placeId={keystroke}&gameInstanceId={jobId}"
    )
elif data["letpeoplejoinme"] == False and not keystroke.isdigit():
    joinexperience = f"roblox://experiences/start?placeId=" + str(
        data["games"][keystroke]
    )
elif data["letpeoplejoinme"] == True and not keystroke.isdigit():
    joinexperience = (
        f"roblox://experiences/start?placeId="
        + str(data["games"][keystroke])
        + f"&gameInstanceId={jobId}"
    )

if keystroke.isdigit():
    gamepage = f"https://www.roblox.com/games/{keystroke}"
else:
    gamepage = "https://www.roblox.com/games/" + str(data["games"][keystroke])


# this method is probably really bad, but its just what im going to leave in for now, dont fix it if it works ;)

while True:
    if (
        not checkifrunning("RobloxPlayerBeta.exe")
        or time.time() < data["disregardlauncher"]
        and not checkifrunning("RobloxPlayerLauncher.exe")
    ):
        exit()
    else:
        RPC.update(
            details=GAMENAME,
            state=f"by {GAMECREATOR}",
            large_image=GAMETHUMBNAIL,
            large_text="TermiBlox Launcher",
            start=StartTime + 5,
            buttons=[
                {
                    "label": f"Join",
                    "url": joinexperience,
                },
                {
                    "label": "See Details",
                    "url": gamepage,
                },
            ],
        )
    time.sleep(5)
