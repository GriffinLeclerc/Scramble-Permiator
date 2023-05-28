# Given any number of words to unscrable, 
# 

def string_superset(string):
    superset = []
    superset.append("") # add the empty set

    width = 1;

    left_bound = 0
    right_bound = width

    while((right_bound - left_bound < len(string) + 1)):
        # print(str(left_bound) + ":" + str(right_bound))
        # append the string slice at [L..R]
        superset.append(string[left_bound:right_bound]);

        # step L and R by width
        left_bound += 1
        right_bound += 1

        # increase width when R = len(string)
        if(right_bound == len(string) + 1):
            width += 1
            left_bound = 0
            right_bound = width

    return sorted(superset, key=len) 


# add a method to extend the sets in the superset to the len of the word to account for repeated letters

def extend_superset(superset):
    # strip the first elem from the superset
    superset = superset[1:]

    # determine how long the strings need to be
    full_len = len(superset[len(superset) - 1])

    extended_superset = []
    
    for elem in superset:
        padded_elem = elem
        # while the elem is not long enough
        # concatenate it with itself, and truncate any extra bits
        while(len(padded_elem) < full_len):
            padded_elem = (padded_elem + padded_elem)[0:full_len]

        # put it in the new set
        extended_superset.append(padded_elem)

    return extended_superset


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

        sub_scrambles = extend_superset(string_superset(word))

        answers = []

        for elem in sub_scrambles:
            print(elem)
            answer = sortedMap.get(elem)
            if(answer != None):
                answers = answers + sortedMap.get(elem)
            
        print(scramble + " - " + str(answer))