import json
import difflib
from difflib import get_close_matches

data=json.load(open('data.json'))
def translate(d):
    d=d.lower()
    if d in data:
        return data[d]
    elif d.upper() in data:
        return data[d.upper()]
    elif d.title() in data:
        return data[d.title()]
   
    elif len(get_close_matches(d,data.keys()))>0:
        word=input("Did you mean %s instead? Type Y if Yes, else N: " %get_close_matches(d,data.keys())[0])
        if word is 'Y':
            return data[get_close_matches(d,data.keys())[0]]
        elif word is 'N':
            return "The word doesn't exist"
        else:
            return "We didn't understand your entry."
    else:    
        return "The word doesn't exist"
		
word=input('Enter a word: ')
output=translate(word)
if type(output) is list:
    for i in output:
        print(i)
else:
    print(output)
