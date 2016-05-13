""" dogcat """

import sys
import aima.search as a       # AIMA module for search problems

# file name for list of three and four letter words and their frequency scores
dict_file = "words34.txt"

# dictionary to hold words
dictionary = {}

# load words into dictaionary dict
minfreq3 = minfreq4 = sys.maxint
for line in open(dict_file):
    word, n = line.strip().split('\t')
    n = float(n)
    dictionary[word] = n
    if len(word) == 3 and n < minfreq3:
        minfreq3 = n
    elif len(word) == 4 and n < minfreq4:
        minfreq4 = n

class DC(a.Problem):
    """A state is represented as a string """

    def __init__(self, initial='dog', goal='cat', cost=None):
        self.initial = initial
        self.goal = goal
        if cost not in ['steps', 'scrabble', 'frequency']:
            raise ValueError('Unrecognized cost: ' + cost)
        self.cost = cost

    def actions(self, state):
        for n in range(len(state)):
            for l in  "abcdefghijklmnopqrstuvwxyz":
                word = list(state)
                word[n] = l
                new_word = ''.join(word)
                if new_word in dictionary and new_word != state:
                    yield (n, l)

    def result(self, state, action):
        n, l = action
        new = list(state)
        new[n] = l
        return ''.join(new)

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        n, letter = action
        if self.cost == 'steps':
            return c + 1
        elif self.cost == 'scrabble':
            return c + letter_cost[letter]
        elif self.cost == 'frequency':
            return c + 1 + dictionary[state2]

    def __repr__(self):
        return "dc({},{})".format(self.initial, self.goal)

    def h(self, node):
        """Heuristic: returns an estimate of the cost to get from the
        state of this node to the goal state.  The heuristic's value
        should depnd on the Problem's cost parameter (steps, scrabble
        or frequency) as this will effect the estimate cost to get to
        the nearest goal. """

        word = node.state
        goal = self.goal
        cost = self.cost
        n = 0
        for i in range(len(word)):
            if word[i] != goal[i]:
                n += letter_cost[goal[i]] if cost == 'frequency' else 1
        if cost == 'frequency':
            n +=  dictionary[goal]
        return n

# letter_cost is a dict from a character in a..z to an int
letter_cost = {}

for l in "aeioulnstr":
    letter_cost[l] = 1
for l in "dg":
    letter_cost[l] = 2
for l in "bcmp":
    letter_cost[l] = 3
for l in "fhvwy":
    letter_cost[l] = 4
letter_cost['k'] = 5
letter_cost['j'] = letter_cost['x'] = 8
letter_cost['q'] = letter_cost['z'] = 10

    



