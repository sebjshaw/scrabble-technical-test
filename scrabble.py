from rich.prompt import Prompt
import random
from rich.console import Console

console = Console(record=True)

ONE_POINT_LETTERS = ['e', 'a', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u']
TWO_POINT_LETTERS = ['d', 'g']
THREE_POINT_LETTERS = ['b', 'c', 'm', 'p']
FOUR_POINT_LETTERS = ['f', 'h', 'v', 'w', 'y']
FIVE_POINT_LETTER = 'k'
EIGHT_POINT_LETTERS = ['j', 'x']
TEN_POINT_LETTERS = ['q', 'z']

SIX_TILES = ['n', 'r', 't']
FOUR_TILES =['l', 's', 'u', 'd']
TWO_TILES = ['b', 'c', 'm', 'p', 'f', 'h', 'v', 'w', 'y']
ONE_TILE = ['k', 'j', 'x', 'q', 'z']




def word_score(word, is_triple):
    total = 0
    for letter in word:

        if letter in ONE_POINT_LETTERS:
            total += 1
        elif letter in TWO_POINT_LETTERS:
            total += 2
        elif letter in THREE_POINT_LETTERS:
            total += 3
        elif letter in FOUR_POINT_LETTERS:
            total += 4
        elif letter == FIVE_POINT_LETTER:
            total += 5
        elif letter in EIGHT_POINT_LETTERS:
            total += 8
        elif letter in TEN_POINT_LETTERS:
            total += 10
        else:
            console.print("Word must only contain letters")
        

    return total 


def create_bag_of_letters():
    bag = []
    for i in range(12):
        bag.append('e')
    for i in range(9):
        bag.append('a')
        bag.append('i')
    for i in range(8):
        bag.append('o')
    for letter in SIX_TILES:
        for i in range(6):
            bag.append(letter)
    for letter in FOUR_TILES:
        for i in range(4):
            bag.append(letter)
    for i in range(3):
        bag.append('g')
    for letter in TWO_TILES:
        for i in range(2):
            bag.append(letter)
    for letter in ONE_TILE:
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


def find_longest_word(word, current_word):
    if len(word) > len(current_word):
        current_word = word
    return current_word


def find_heighest_scoring_word(word, current_word):

    if word_score(word) > word_score(current_word):
        current_word = word
    return current_word





def find_word(l_or_h, tiles, dictionary):
    current_word = ''
    dictionary = list(dictionary)
    not_in_word = 0
    for word in dictionary:
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

        if not_in_word == 0 and l_or_h == 'l':
            current_word = find_longest_word(word, current_word)
        elif not_in_word == 0 and l_or_h == 'h':
            current_word = find_heighest_scoring_word(word, current_word)
        for letter in removed_letters:
            tiles.append(letter)
        not_in_word = 0
    return current_word


def main():
    bag_of_letters = create_bag_of_letters()
    players_tiles = get_players_tiles(bag_of_letters)
    dictionary = get_dictionary()
    console.print(players_tiles)
    l_or_h = Prompt.ask("Do you want the longest or the heighest scoring (l or h)?")
    if l_or_h == 'l':
        longest_word = find_word(l_or_h, players_tiles, dictionary)
    
        console.print(f"Longest word is {longest_word}: {len(longest_word)}")
    elif l_or_h == 'h':
        heighest_scoring_word = find_word(l_or_h, players_tiles, dictionary)
        console.print(f"Heighest scoring word is {heighest_scoring_word}: {word_score(heighest_scoring_word)}")


main()

# dictionary = list(get_dictionary())
# console.print(len(dictionary[0]))


# test_dictionary = ['world', 'it', 'is', 'seb', 'hello']

# test_tiles = ['h', 'l', 'e', 'i', 't', 'l', 'o']

# console.print(find_longest_word(test_tiles, test_dictionary))
