#!/usr/bin/env python3

import argparse
import random

# Set up the command-line arguments
parser = argparse.ArgumentParser(description='Generate secure, memorable passwords using the XKCD method')
parser.add_argument('-w', '--words', type=int, default=4, help='include WORDS words in the password (default=4)')
parser.add_argument('-c', '--caps', type=int, default=0, help='capitalize the first letter of CAPS random words (default=0)')
parser.add_argument('-n', '--numbers', type=int, default=0, help='insert NUMBERS random numbers in the password (default=0)')
parser.add_argument('-s', '--symbols', type=int, default=0, help='insert SYMBOLS random symbols in the password (default=0)')
args = parser.parse_args()

# Load the wordlist
with open('words.txt') as f:
    wordlist = [word.strip() for word in f.readlines()]

# Define a function to generate a password
def generate_password():
    # Choose random words
    words = [random.choice(wordlist) for i in range(args.words)]
    # Capitalize random words
    for i in random.sample(range(args.words), args.caps):
        words[i] = words[i].capitalize()
    # Insert random numbers
    for i in random.sample(range(args.words + args.numbers), args.numbers):
        if i < args.words:
            # Replace a word with a number
            words[i] = str(random.randint(0, 9))
        else:
            # Insert a number at a random position
            words.insert(i, str(random.randint(0, 9)))
    # Insert random symbols
    symbols = '!@#$%^&*'
    for i in random.sample(range(args.words + args.numbers + args.symbols), args.symbols):
        if i < args.words + args.numbers:
            # Replace a character in a word with a symbol
            word_index = i if i < args.words else i - args.numbers
            char_index = random.randint(0, len(words[word_index]) - 1)
            words[word_index] = words[word_index][:char_index] + random.choice(symbols) + words[word_index][char_index+1:]
        else:
            # Insert a symbol at a random position
            words.insert(i, random.choice(symbols))
    # Combine the words into a password
    password = ''.join(words)
    return password

# Generate and print a password
if __name__ == '__main__':
    password = generate_password()
    print(password)
