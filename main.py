path_to_file = "/home/bee/workspace/github.com/rwhrtuje5/bookbot/books/frankenstein.txt"

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{countWords(file_contents)} words found in the document")
        print()
        fdict = frequency(file_contents)
        for x in sorted(fdict):
            print(f"The '{x}' character was found {fdict[x]} times")
        print("--- End report ---")

def frequency(s):
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    duct = dict()
    for x in alphabet:
        duct[x] = 0
    for x in s:
        if x in duct:
            duct[x] += 1
    return duct

def countWords(string):
    return len(string.split())

main()

