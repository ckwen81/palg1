#!/usr/bin/python3

'''Gettysburg Address

This is an exercise in file analysis. Fundamentally it is an exercise in the use of the basic collection objects in
Python such as strings, lists, tuples, dictionaries and sets.request

We are going to use Abraham Lincoln's Gettysburg address of 1863, This is famous for many things, including being a
short speech.

We are going to do some simple analysis on this.
1. Count the number of words in the speech. We will exclude from our analysis a number of 'stop words', in our example
these will be the definite and indefinite articles and some personal pronouns.
2. Count the unique words in the collection produced by 1 above.
3. Count the number of occurrences of each word.

Some hints
1. Import the string module. This gives string.whitespace, a string containing all of the whitespace characters
and string.punctuation, a string containing all of the punctuation characters.

'''

# Import:
# string (gives us whitespace and punctuation lists)
import string, requests
from read_from_file_or_net import get_stuff_from_net as get_url


# Variables to hold file URLs
SPEECH_URL = "http://193.1.33.31:88/pa1/gettysburg.txt"
STOPWORDS_URL = "http://193.1.33.31:88/pa1/stopwords.txt"


def make_word_list(g_file, stop_words):
    """Create a list of words from the file while excluding stop words."""
    speech = []  # list of speech words: initialized to be empty

    for line_string in g_file:
        lineList = line_string.strip(
            string.whitespace).split()  # split each line into a list of words and strip whitespace
        for word in lineList:
            word = word.lower()  # make words lower case (we consider a word in lowercase and uppercase to be equivalent)
            word = word.strip(string.punctuation)  # strip off punctuation
            if (word not in stop_words) and (word not in string.punctuation):
                # if the word is not in the stop word list, add the word to the speech list
                speech.append(word)
    return speech


def count_words(speech):
    """Create a dictionary and count the occurrences of each word.
    If a word already exists in the dictionary, add 1 to its counter
    otherwise set a counter for to to an initial value of 1"""
    counts = {}
    for word in speech:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def main():
    '''Process the speech once you can successfully open both the speech and the stop words files from the net.'''
    try:
        # The requests get method gives us http header information and the content as a bytes object.
        speech_response = requests.get(SPEECH_URL)
        speech_headers = speech_response.headers
        stopwords_response = requests.get(STOPWORDS_URL)
        stopwords_headers = stopwords_response.headers

        # We don't know what we're getting. The content-type header might give us a clue. In this example
        # I'm just going to assume that we can correctly decode utf-8 (the default). I can do this because I know that
        # the file is just a short 'plain text' speech so I know that there won't be any oddities in there. This
        # is often a bit of a gamble for, as we know, there is no such thing as 'plain text'.

        # Make a list of lines by splitting on the newline character.
        speech = speech_response.content.decode().split('\n')

        # Make a tuple of all the stop words while losing the newline character
        stopwords = tuple(stopwords_response.content.decode().strip().split(','))

        # Make word list from speech while excluding stop words
        speech = make_word_list(speech, stopwords)

        # Make a set of words from speech which automatically assures that each entry is unique
        unique = set(word for word in speech)

        # Print the results
        print("Speech Length: {}".format(len(speech)))
        print("Unique words: {}".format(len(unique)))
        print("\nWord count")

        words = count_words(speech)

        print("-" * 50)
        for k,v in words.items():
            print(f"{k}: {v},", end=" ")
        print("\n")

        print("-" * 50)
        print(f"Request for {SPEECH_URL} returned the following response headers")
        for k, v in speech_headers.items():
            print(f"{k}: {v}")
        print("-"*50)
        print(f"Request for {STOPWORDS_URL} returned the following response headers")
        for k, v in stopwords_headers.items():
            print(f"{k}: {v}")

    except Exception as e:
        print(f"{e}")


def main_v2():
    '''Process the speech once you can successfully open both the speech and the stop words files from the net.'''
    try:
        # Make a list of lines by splitting on the newline character.
        speech = get_url(SPEECH_URL)
        speech = speech.split('\n')

        # Make a tuple of all the stop words while losing the newline character
        stopwords = get_url(STOPWORDS_URL)
        stopwords = tuple(stopwords.split(','))

        # Make word list from speech while excluding stop words
        speech = make_word_list(speech, stopwords)

        # Make a set of words from speech which automatically assures that each entry is unique
        unique = set(word for word in speech)

        # Print the results
        print("Speech Length: {}".format(len(speech)))
        print("Unique words: {}".format(len(unique)))
        print("\nWord count")

        words = count_words(speech)

        print("-" * 50)
        for k,v in words.items():
            print(f"{k}: {v},", end=" ")
        print("\n")

    except Exception as e:
        print(f"{e}")


# Run if stand-alone
if __name__ == '__main__':
    # main()
    main_v2()