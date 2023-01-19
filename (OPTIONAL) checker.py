try:
    import colorama, getkey, valclient, time, os, random, json, platform
    print("You have all the libraries required!")
    input("\n\nPress ENTER to close")
except ModuleNotFoundError:
    print("You are missing the following libraries:")

try:
    import colorama
except ModuleNotFoundError:
    print("colorama")
try:
    import getkey
except ModuleNotFoundError:
    print("getkey")
try:
    import valclient
except ModuleNotFoundError:
    print("valclient")
try:
    import time
except ModuleNotFoundError:
    print("time")
try:
    import os
except ModuleNotFoundError:
    print("os")
try:
    import random
except ModuleNotFoundError:
    print("random")
try:
    import json
except ModuleNotFoundError:
    print("json")
try:
    import platform
except ModuleNotFoundError:
    print("platform")
