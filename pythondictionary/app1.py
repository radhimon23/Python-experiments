#to run this file,copy paste it into radhikamonpara maik both the fil
#u can extend this code to take input froma live webpage ora web application instead of taking inputfrom the command line...

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0 :
        yn = input("Did you mean %s instead ? yes Y or no N ? " %get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return"Word doesnnt exist  sorry"
        else:
            return "We dint understand your query"
    else:
        return "Word doesnt exist"

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
