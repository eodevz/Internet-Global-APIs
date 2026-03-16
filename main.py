# INTERNET GLOBAL APIs
# Made by @hazzereign & @env

# This CLI project shows how nice is to get along with the
# requests & InquirerPy lib.

# You can create your own CLI with I.G.A. and publish it,
# but you need to credit the original version.

import requests
from colorama import Fore, Style, init
from InquirerPy import inquirer
import os
import random
import time
import html
import sys

#CONFIGURATIONS
shuffle_options = False#toggle this on if you want the inquirerpy list to shuffle everytime   
                      #the code runs
sort_options = True#toggle this off if you don't want the list to be sorted by alphabetic order
                    #this will OVERWRITE shuffle_options.

os.system("cls")
init()




#--core variables--
#thanks @env for the weather codes
weather_codes = {
    0: "Clear sky ☀️",
    1: "Mainly clear 🌤",
    2: "Partly cloudy ⛅",
    3: "Overcast ☁️",
    45: "Fog 🌫",
    48: "Depositing rime fog 🌫",
    51: "Light drizzle 🌦",
    53: "Moderate drizzle 🌦",
    55: "Dense drizzle 🌧",
    61: "Light rain 🌧",
    63: "Moderate rain 🌧",
    65: "Heavy rain 🌧",
    71: "Light snow ❄️",
    73: "Moderate snow ❄️",
    75: "Heavy snow ❄️",
    95: "Thunderstorm ⛈",
}
#--core functions--
#even if u do know what ur doing here, please dont edit
#i took hours to do thiss.. (15min)
def __authorization__(reason):
    print("== WAIT! ==")
    print(
        Fore.CYAN + "[AUTH] "
        + Style.RESET_ALL + f"This command requires your authorization to \"{reason}\"."
    )
    print("Internet Global APIs will never use your data for anything; you can check our entire code on\nhttps://github.com/hazzereign/Internet-Global-APIs.")
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

#--main system--
def __advice__():
    http = "https://api.adviceslip.com/advice"

    r = requests.get(http)
    data = r.json()

    print(
        Fore.CYAN + "[ADVICE] " + Style.RESET_ALL +
        data["slip"]["advice"]
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

    try:
        ip_data = requests.get("http://ip-api.com/json/", timeout=5).json()
    except requests.RequestException: #if website falls etc etc
        print(Fore.RED + "[ERROR]" + Style.RESET_ALL + " Failed to get IP data.")
        return

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
    weather_code = weather["current_weather"]["weathercode"]
    is_day = weather["current_weather"]["is_day"]

    condition = weather_codes.get(weather_code, "Unknown")
    
    #main weather
    os.system("cls")
    
    def time_consolelog():
        if is_day == 1:
            #day
            print(
                Fore.YELLOW + "[TIME] " +
                Style.RESET_ALL + "Day. Time to wake up."
            )
        else:
            #night
            print(
                Fore.CYAN + "[TIME] "
                + Style.RESET_ALL + f"Night. Sweet dreams."
            )
    
    time_consolelog()
    print(
        Fore.GREEN + "[WEATHER]" + Style.RESET_ALL +
        f" Temperature: {temp}°C"
    )

    print(
        Fore.GREEN + "[WIND]" + Style.RESET_ALL +
        f" Wind Speed: {wind} km/h"
    )

    print(
        Fore.YELLOW+ "[CONDITION] "
        + Style.RESET_ALL + condition
    )


def __randomword__():
    http = "https://random-word-api.herokuapp.com/word"

    r = requests.get(http)
    data = r.json()

    print(data[0])


def __trivia__():
    os.system("cls")
    http = "https://opentdb.com/api.php?amount=1"
    r = requests.get(http)
    data = r.json()

    question = html.unescape(data["results"][0]["question"])
    correct = html.unescape(data["results"][0]["correct_answer"])
    wrong = data["results"][0]["incorrect_answers"]

    arr_quest = [correct] + wrong

    random.shuffle(arr_quest)

    letters = ["a", "b", "c", "d"]

    correct_index = arr_quest.index(correct)
    correct_letter = letters[correct_index]

    print(
        Fore.CYAN + "[QUESTION] "
        + Style.RESET_ALL + question
    )

    for i, option in enumerate(arr_quest):
        print(f"{letters[i]}) {html.unescape(option)}")

    answer = input("Type your answer. (a/b/c/d)\nYOU: ").lower()

    print("Your answer is...")
    time.sleep(2)

    if answer == correct_letter:
        print(
            Fore.GREEN + "[RIGHT] "
            + Style.RESET_ALL + f"It is {correct}!"
        )
    else:
        print(
            Fore.RED + "[WRONG] "
            + Style.RESET_ALL + f"The correct answer was\n\"{correct}\"."
        )
    time.sleep(2)
    again = inquirer.select(
        message="Would you like to play again?",
        choices=["Yes.","Head me back to the main menu."]
    ).execute()

    if again == "Yes.":
        __trivia__()

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

def __exit__():
    print(
        Fore.CYAN + "[SYSTEM] "
        + Style.RESET_ALL + "User chose to leave. Attempting to close all threads."
    )
    sys.exit()

commands = {
    "Advice": __advice__,
    "Random Cats Fact": __catsfact__,
    "Random Word": __randomword__,
    "Trivia": __trivia__,
    "Random Fact": __randomfact__,
    "Random Task": __randomtask__,
    "Weather by IP": __weather__,
}

choices_dictionary = list(commands.keys())

#below this comments theres the main system
#do whatever you want!! but only if you know what ur doingg
if shuffle_options: random.shuffle(choices_dictionary)
if sort_options: choices_dictionary.sort()

choices_dictionary += ["== More Options Below ==", "Exit"]
forceExit = False
while True:
    try:
        choice = inquirer.select(
            message="What do you need for today?",
            choices=choices_dictionary
        ).execute()

        if choice in commands:
            commands[choice]()

        if choice == "Exit":
            forceExit = True
            __exit__()
            
        if not forceExit:
            time.sleep(2)
    except KeyboardInterrupt:
        forceExit = True
        os.system("cls")
        print(
            Fore.CYAN + "[SYSTEM] "
            + Style.RESET_ALL + "Attempting to close all current open threads..."
        )
    finally:
        if forceExit:
            print(
                Fore.GREEN + "[SUCCESS] " +
                Style.RESET_ALL + "Closed all threads. See you next time!"
            )
            sys.exit()
