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




def word_score(word):
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
        random_tile = random.randint(0,len(bag))
        tiles.append(bag.pop(random_tile))
    return tiles


def get_dictionary():
    return open("dictionary.txt", "r")


def find_longest_word(tiles, dictionary):
    current_longest = ''
    dictionary = list(dictionary)
    for word in dictionary:
        # console.print(current_longest)
        word = str(word)
        not_in_tiles = False
        if len(word) > 7:
            continue
        for letter in word:
            if letter not in tiles:
                not_in_tiles = True
                # console.print('break')
                break
        if not_in_tiles == False:
            console.print(f'no break: {word}')
        if len(word) > len(current_longest) and not_in_tiles == False:
            current_longest = word
    return current_longest
                    



def main():
    bag_of_letters = create_bag_of_letters()
    players_tiles = get_players_tiles(bag_of_letters)
    dictionary = get_dictionary()
    longest_word = find_longest_word(players_tiles, dictionary)
    console.print(players_tiles)
    console.print(longest_word)


# main()

test_dictionary = ['world', 'it', 'is', 'seb', 'hello']

test_tiles = ['h', 'l', 'e', 'i', 't', 'l', 'o']

console.print(find_longest_word(test_tiles, test_dictionary))

