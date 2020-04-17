'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

word_check = "th"


def count_th(word):
    if len(word) < 2:
        return 0
    count = 0
    # split word input into strings of length == 2 but make sure the letters are right next to eachother in the string
    if word[:2] == word_check:
        count += 1
    # recursive call will take in the same word input but starting at the next index
    return count_th(word[1:]) + count


print(count_th("Thetheebnasdjfnkthth"))
