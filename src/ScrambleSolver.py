# Given any number of words to unscrable, 
# 

def string_superset(string):
    superset = []
    superset.append("") # add the empty set

    width = 1;

    # size of the superset for string n = 2^n 
    total_len = 2 ** len(string)

    while(len(superset) < total_len):
        left_bound = 0
        right_bound = width

        superset.append()
        # append the string slice at [L..R]

        # step L and R by width

        # increase width when R = width

    return superset




# Sort words by letter, preserving duplicates
# Map of sorted letters to words 
# Sort the given word alphabetically
# Lookup that sorted string in the map

with open("res/words.txt") as allWords:
    print("Constructing map.")
    sortedMap = dict()
    for line in allWords:
        word = line.strip().lower()
        keyAsList = sorted(word)
        key = "".join(keyAsList)

        if key in sortedMap:
            sortedMap[key].append(word)
        else:
            sortedMap[key] = [word]

print("Map constructed.")

with open("Words to Unscramble") as inputFile:
    print("Solving scrambles.")
    for line in inputFile:
        scramble = line.strip()

        if scramble == "":
            continue

        wordAsList = sorted(scramble)
        word = "".join(wordAsList)
        answer = sortedMap.get(word)
        print(scramble + " - " + str(answer))