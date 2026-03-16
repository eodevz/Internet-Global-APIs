import requests
from colorama import Fore, Style, init
from InquirerPy import inquirer
import os
import random
import time
import html
import sys

#CONFIGURATIONS
shuffle_options = True#toggle this off if you dont want the inquirerpy list to shuffle everytime   
                      #the code runs
sort_options = False#toggle this on if you want the list to sort by alphabetic order
                    #this will OVERWRITE shuffle_options.

os.system("cls")
init()
#core functions
def __authorization__(reason):
    print("== WAIT! ==")
    print(
        Fore.CYAN + "[AUTH] "
        + Style.RESET_ALL + f"This command requires your authorization to \"{reason}\"."
    )
    print("Internet Global APIs will never use your data for anything; you can check our entire code on\nhttps://github.com/eodevz/Internet-Global-APIs/edit/main/main.py.")
    auth = inquirer.select(
        message="Do you authorize?",
        choices=["Yes", "No"]
    ).execute()
    if auth == "Yes":
        return True
    return False

def __onauth__(reason, auth):
    if not auth:
        print(
            Fore.RED + "[NOT AUTHORIZED] "
            + Style.RESET_ALL + f"You marked \"{reason}\" as "
            + Fore.RED + "NOT AUTHORIZED"
            + Style.RESET_ALL + ".\n If you want to mark it as authorized, restart the program."
        )
        sys.exit()

#main system
def __advice__():
    http = "https://api.adviceslip.com/advice"

    r = requests.get(http)
    data = r.json()

    print(
        Fore.CYAN + "[ADVICE]" + Style.RESET_ALL +
        f" {data["slip"]["advice"]}"
    )

def __catsfact__():
    http = "https://catfact.ninja/fact"

    r = requests.get(http)
    data = r.json()

    print(
        Fore.CYAN + "[CAT FACT] " +
        Style.RESET_ALL + data["fact"]
    )

def __weather__():
    auth_data = "See your current IP address"
    auth = __authorization__(auth_data)
    __onauth__(auth_data, auth)
    print(Fore.CYAN + "[INFO]" + Style.RESET_ALL + " Getting your IP info...")

    ip_data = requests.get("http://ip-api.com/json/").json()

    city = ip_data["city"]
    country = ip_data["country"]
    lat = ip_data["lat"]
    lon = ip_data["lon"]

    print(
        Fore.CYAN + "[LOCATION]" + Style.RESET_ALL +
        f" {city}, {country}"
    )

    print(Fore.CYAN + "[INFO]" + Style.RESET_ALL + " Getting weather...")

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    weather = requests.get(weather_url).json()

    temp = weather["current_weather"]["temperature"]
    wind = weather["current_weather"]["windspeed"]

    print(
        Fore.GREEN + "[WEATHER]" + Style.RESET_ALL +
        f" Temperature: {temp}°C"
    )

    print(
        Fore.GREEN + "[WIND]" + Style.RESET_ALL +
        f" Wind Speed: {wind} km/h"
    )


def __randomword__():
    http = "https://random-word-api.herokuapp.com/word"

    r = requests.get(http)
    data = r.json()

    print(data[0])

def __trivia__():
    http = "https://opentdb.com/api.php?amount=1"
    r = requests.get(http)
    data = r.json()

    arr_quest = []
    correct = data["results"][0]["correct_answer"]
    wrong = data["results"][0]["incorrect_answers"]
    arr_quest.append(correct)
    for i in wrong:
        arr_quest.append(i)

    random.shuffle(arr_quest)

    print(
        Fore.CYAN + "[QUESTION] "
        + Style.RESET_ALL + html.unescape(data["results"][0]["question"])
    )

    for i in arr_quest:
        print(i)

    time.sleep(10)
    print(
        Fore.GREEN + "[RIGHT ANSWER] "
        + Style.RESET_ALL + correct
    )

def __randomfact__():
    http = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    r = requests.get(http)
    data = r.json()
    print(
        Fore.CYAN + "[RANDOM FACT] "
        + Style.RESET_ALL + data["text"]
    )

def __randomtask__():
    http = "https://bored-api.appbrewery.com/random"
    r = requests.get(http)
    data = r.json()

    print(
        Fore.CYAN + "[RANDOM TASK] " +
        Style.RESET_ALL + data["activity"]
    )


choices_dictionary = [
    "Advice",
    "Random Cats Fact",
    "Random Word",
    "Trivia",
    "Random Fact",
    "Random Task",
    "Weather by IP"
]

#below this comments theres the main system
#do whatever you want!! but only if you know what ur doingg
if shuffle_options: random.shuffle(choices_dictionary)
if sort_options: choices_dictionary.sort()

keyboardInt = False
try:
    choice = inquirer.select(
        message="What do you need for today?",
        choices=choices_dictionary
    ).execute()

    if choice == "Advice":
        __advice__()
    elif choice == "Random Cats Fact":
        __catsfact__()
    elif choice == "Random Word":
        __randomword__()
    elif choice == "Trivia":
        __trivia__()
    elif choice == "Random Fact":
        __randomfact__()
    elif choice == "Random Task":
        __randomtask__()
    elif choice == "Weather by IP":
        __weather__()
except KeyboardInterrupt:
    keyboardInt = True
    os.system("cls")
    print(
        Fore.CYAN + "[SYSTEM] "
        + Style.RESET_ALL + "Attempting to close all current open threads..."
    )
finally:
    if keyboardInt:
        print(
            Fore.GREEN + "[SUCCESS] " +
            Style.RESET_ALL + "Closed all threads. See you next time!"
        )
