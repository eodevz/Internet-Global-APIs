import requests
from colorama import Fore, Style, init
from InquirerPy import inquirer
import os
import random
import time
import html

#CONFIGURATIONS
shuffle_options = True#toggle this off if you dont want the inquirerpy list to shuffle everytime   
                      #the code runs
sort_options = False#toggle this on if you want the list to sort by alphabetic order
                    #this will OVERWRITE shuffle_options.

os.system("cls")
init()
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
    "Random Task"
]

#below this comments theres the main system
#do whatever you want!! but only if you know what ur doingg
if shuffle_options: random.shuffle(choices_dictionary)
if sort_options: choices_dictionary.sort()

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
except KeyboardInterrupt:
    os.system("cls")
    print(
        Fore.CYAN + "[SYSTEM] "
        + Style.RESET_ALL + "Attempting to close all current open threads..."
    )
finally:
    print(
        Fore.GREEN + "[SUCCESS] " +
        Style.RESET_ALL + "Closed all threads. See you next time!"
    )
