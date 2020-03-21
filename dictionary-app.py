import json
import difflib

data_file = open("data.json")
data = json.load(data_file)

def get_definition(_word):
    return data[_word]

def get_matches(_word):
    matches = difflib.get_close_matches(_word, data.keys(), n=3, cutoff=0.6)
    return matches

def main():
    while True:
        word = input("Enter a word: >\n")
        try:
            definitions = get_definition(word)
            for definition in definitions:
                print(definition)
        except KeyError as e:
            print("The word was not found in the dictionary.")
            matches = get_matches(word)
            if matches:
                print("Did you mean one of these?")
                for match in matches:
                    print(match)

if __name__ == '__main__':
    main()
