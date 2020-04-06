"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    true_list = [element for element in paragraphs if select(element) == True]

    if k < len(true_list):
        return true_list[k]
    return ''

    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    def select_helper(element):
        for word in split(lower(remove_punctuation(element))):
            if word in topic:
                return True

        return False

    return select_helper


    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3

    "*** YOUR CODE HERE ***"

    num_words = 0
    if len(typed_words) == 0:
            return 0.0

    for index in range((min(len(reference_words), len(typed_words)))):

        if typed_words[index] == reference_words[index]:
            num_words += 1

    return (num_words / len(typed_words) * 100)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    wpm = (len(typed)/5) * (60 / elapsed)
    return wpm

    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"

    if user_word in valid_words:
        return user_word

    difference = [diff_function(user_word, valid_words[element], limit) for element in range(len(valid_words))]

    if min(difference) > limit:
        return user_word

    return valid_words[difference.index(min(difference))]




    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """

    if len(start) == 0 or len(goal) == 0:
        return abs(len(start) - len(goal))

    elif start == goal:
        return 0


    elif limit == 0:
        return 1


    elif start[0] == goal[0]:
        return swap_diff(start[1:], goal[1:], limit)


    return 1 + swap_diff(start[1:], goal[1:], limit - 1)

    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if start == '': # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(goal)
        # END

    elif goal == '': # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(start)
        # END

    elif start[0] == goal[0]:
        return edit_diff(start[1:], goal[1:], limit)

    elif start == goal:
        return 0

    elif limit == 0:
        return 1


    add_diff = 1 + edit_diff(start, goal[1:], limit - 1)  # Fill in these lines
    remove_diff = 1 + edit_diff(start[1:], goal, limit -1)
    substitute_diff = 1 + edit_diff(start[1:], goal[1:], limit -1)

    return min(add_diff, remove_diff, substitute_diff)
    # BEGIN
    "*** YOUR CODE HERE ***"
    # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    correct_count = 0


    for element in range(max(len(prompt), len(typed))):

        if element < min(len(prompt), len(typed)) and typed[element] == prompt[element]:
            correct_count +=1

        else:
            d = {'id': id, 'progress': correct_count/len(prompt)}
            send(d)
            return d['progress']

    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    time_list = []


    def time(player, word, input_lst):
        #works with:
        # return word_times[player][word][1] - word_times[player][word - 1][1]
        return elapsed_time(input_lst[player][word]) - elapsed_time(input_lst[player][word - 1])




    def fastest_word(word):
        lst = [time(player, word, word_times) for player in range(n_players)]
        index = []
        for element in range(len(lst)):
            if lst[element] - min(lst) <= margin:
                index.append(element)

        if len(index):
            return index

        index = lst.index(min(lst))

        return index

    return_list = []

    for player in range(n_players):
        players_list = []

        for index_word in range(n_words):
            if player in fastest_word(index_word + 1) or player == fastest_word(index_word + 1):
                players_list.append(word(word_times[0][index_word + 1]))

        return_list.append(players_list)
    return return_list



        # END PROBLEM 9

def check_for_duplicates(lst):
    """An abstraction for checking if there's a duplicate in a list
    (I MADE IT INTO A FUNCTION BECAUSE IT'S EASIER TO LOOK AT LOL)"""
    for element in lst:
        if lst.count(element) > 1:
            return True
        return False



def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
