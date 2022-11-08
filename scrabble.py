from rich.prompt import Prompt
import random
from rich.console import Console

console = Console(record=True)


letter_score = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}

letter_frequency = {'a':9,'b':2,'c':2,'d':4,'e':12,'f':2,'g':3,'h':2,'i':9,'j':1,'k':1,'l':4,'m':2,'n':6,'o':8,'p':2,'q':1,'r':6,'s':4,'t':6,'u':4,'v':2,'w':2,'x':1,'y':2,'z':1}


def word_score(word, is_triple):
    total = 0
    heighest_letter = 0
    for letter in word.lower():
        current_letter = letter_score[letter]
        total += letter_score[letter]

        
        if current_letter > heighest_letter:
            heighest_letter = current_letter
        

    if is_triple == 'y':
        return total + 2*heighest_letter

    return total


def create_bag_of_letters():
    bag = []
    for letter in letter_frequency:
        frequency = letter_frequency.get(letter)
        for i in range(frequency):
            bag.append(letter)
    return bag


def get_players_tiles(bag):
    tiles = []
    for i in range(7):
        random_tile = random.randint(0,len(bag)-1)
        tiles.append(bag.pop(random_tile))
    return tiles


def get_dictionary():
    return open("dictionary.txt", "r")


def find_heighest_scoring_word_with_triples(word, current_word):
    
    if word_score(word, "y") > word_score(current_word, "y"):
        current_word = word
    return current_word


def find_longest_word(word, current_word):
    if len(word) > len(current_word):
        current_word = word
    return current_word


def find_heighest_scoring_word(word, current_word):

    if word_score(word, "n") > word_score(current_word, "n"):
        current_word = word
    return current_word





def find_word(l_h_or_t, tiles, dictionary):
    current_word = ''
    words = list(dictionary)
    not_in_word = 0
    for word in words:
        word = word[:-1]
        removed_letters = []

        if len(word) > 7:
            continue

        for letter in word:
            if tiles.count(letter) > 0:
                removed_letters.append(letter)
                tiles.remove(letter)
            else: 
                not_in_word = 1

        if not_in_word == 0 and l_h_or_t == 'l':
            current_word = find_longest_word(word, current_word)
        elif not_in_word == 0 and l_h_or_t == 'h' :
            current_word = find_heighest_scoring_word(word, current_word)
        elif not_in_word == 0 and l_h_or_t == 't':
            current_word = find_heighest_scoring_word_with_triples(word, current_word)
        for letter in removed_letters:
            tiles.append(letter)
        not_in_word = 0
    return current_word


def main():
    bag_of_letters = create_bag_of_letters()
    players_tiles = get_players_tiles(bag_of_letters)
    dictionary = get_dictionary()
    console.print(players_tiles)
    l_h_or_t = ''
    l_h_or_t = Prompt.ask("Do you want the longest, the heighest scoring or the heighest scoring with a triple letter (l, h, t)?")
    if l_h_or_t == 'l':
        longest_word = find_word(l_h_or_t, players_tiles, dictionary)
        console.print(f"Longest word is {longest_word}: {len(longest_word)}")
    elif l_h_or_t == 'h':
        heighest_scoring_word = find_word(l_h_or_t, players_tiles, dictionary)
        console.print(f"Heighest scoring word is {heighest_scoring_word}: {word_score(heighest_scoring_word, 'n')}")
    elif l_h_or_t == 't':
        heighest_scoring_word_with_triple = find_word(l_h_or_t, players_tiles, dictionary)
        console.print(f"Heighest scoring word with a triple is is {heighest_scoring_word_with_triple}: {word_score(heighest_scoring_word_with_triple, 'y')}")


main()


# print(word_score('Guardian', 'n'))

# dictionary = list(get_dictionary())
# console.print(len(dictionary[0]))


# test_dictionary = ['world', 'it', 'is', 'seb', 'hello']

# test_tiles = ['h', 'l', 'e', 'i', 't', 'l', 'o']

# console.print(find_longest_word(test_tiles, test_dictionary))
