# ValoLock (Only for Windows!)

The most user friendly way to instalock in Valorant

**NOTE: `This is against Riot's API usage, and could potentialy get you banned. Use with caution! I am not responsible for any bans.`**

## Getkey issue
There is an issue with getkey when installing using pip. As of right now I am unsure how to fix, but I will post a fix when I find it

## Features
- Easy to use interface
- Random agent pools (If you add more agents)
- Instalock delay, if you want to seem more legit
- Frequent updates
- Many more!

## How to use

### Installing

*Final version of ValoLock will come in a .exe file, but early version will be a .py file*

1. Download `main.py`, `data.json`, and `checker.py`
2. Run `checker.py`. This will tell you what libraries you are missing
3. Install any missing libraries (If you have any). I reccomend using `pip install [library]` in your terminal/console
4. Follow the steps bellow on using ValoLock

### Instalocking

1. Launch Valorant
2. Run `main.py`
3. Select your region using the UP, DOWN, and ENTER keys
4. Set your agent pool (**Menu Option 1**)
5. Repeat step 4 for every map
6. Start instalock (**Menu Option 2**)

After every game you will need to repeat step 6 if you want to instalock the next game

## How it works

ValoLock works by sending an API request on behalf of your computer. It does not mess with any files or game configs.

## Libraries

You can use the `checker.py` file to see what libraries you are missing, or you can check individualy bellow:

- valclient
- getkey
- colorama
- time
- os
- random
- json
- platform
