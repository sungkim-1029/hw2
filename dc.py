""" CMSC471 02 hw2 spring 2016
    YOUR NAME, YOUR UMBC USERID

    add comments here
"""    

import aima.search as a       # AIMA module for search problems

dict_file = "words34.txt"

dictionary = {}

for line in open(dict_file):
    word, n = line.strip().split('\t')
    dictionary[word] = float(n)

class DC(a.Problem):

    def __init__(self, initial='dog', goal='cat', cost='steps'):
        pass

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def goal_test(self, state):
        pass

    def path_cost(self, c, state1, action, state2):
        pass

    def __repr__(self):
        """ returns a string to represent a dc problem """
        pass

    def h(self, node):
        """Heuristic: returns an estimate of the cost to get from the
        state of this node to the goal state.  The heuristic's value
        should depend on the Problem's cost parameter (steps, scrabble
        or frequency) as this will effect the estimate cost to get to
        the nearest goal. """
        pass

# add more functions here as needed

    



