# Given any number of words to unscrable, 
# 

def string_superset(string):
    superset = []
    superset.append("") # add the empty set

    width = 1;

    # size of the superset for string n = 2^n 
    total_len = round((len(string) ** 2) / 2)

    left_bound = 0
    right_bound = width

    while(len(superset) < total_len):
        # increase width when R = len(string)
        if(right_bound == len(string)):
            width += 1
            left_bound = 0
            right_bound = width

        # print(str(left_bound) + ":" + str(right_bound))
        # append the string slice at [L..R]
        superset.append(string[left_bound:right_bound]);

        # step L and R by width
        left_bound += 1
        right_bound += 1

    return sorted(superset, key=len) 


# add a method to extend the sets in the superset to the len of the word to account for repeated letters


print(string_superset("a"))
print(string_superset("abc"))
print(string_superset("abcd"))
print(string_superset("abcdefg"))
print(string_superset("abcdefghijklmnopq"))
# print(string_superset("abcdefghijklmnopqrstuvwxyz"))


string_superset("a")
string_superset("abc")
string_superset("abcd")
string_superset("abcdefg")
string_superset("abcdefghijklmnopq")
string_superset("abcdefghijklmnopqrstuvwxyz")



# Sort words by letter, preserving duplicates
# Map of sorted letters to words 
# Sort the given word alphabetically
# Lookup that sorted string in the map

# with open("res/words.txt") as allWords:
#     print("Constructing map.")
#     sortedMap = dict()
#     for line in allWords:
#         word = line.strip().lower()
#         keyAsList = sorted(word)
#         key = "".join(keyAsList)

#         if key in sortedMap:
#             sortedMap[key].append(word)
#         else:
#             sortedMap[key] = [word]

# print("Map constructed.")

# with open("Words to Unscramble") as inputFile:
#     print("Solving scrambles.")
#     for line in inputFile:
#         scramble = line.strip()

#         if scramble == "":
#             continue

#         wordAsList = sorted(scramble)
#         word = "".join(wordAsList)
#         answer = sortedMap.get(word)
#         print(scramble + " - " + str(answer))