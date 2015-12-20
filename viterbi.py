from hmm import HMM
import numpy as np
import sys

#the Viterbi algorithm
def viterbi(hmm, initial_dist, emissions):
    probs = hmm.emission_dist(emissions[0]) * initial_dist
    stack = []

    for emission in emissions[1:]:
        trans_probs = hmm.transition_probs * np.row_stack(probs)
        max_col_ixs = np.argmax(trans_probs, axis=0)
        probs = hmm.emission_dist(emission) * trans_probs[max_col_ixs, np.arange(hmm.num_states)]

        stack.append(max_col_ixs)

    state_seq = [np.argmax(probs)]

    while stack:
        max_col_ixs = stack.pop()
        state_seq.append(max_col_ixs[state_seq[-1]])

    state_seq.reverse()

    return state_seq

# file
lines = open('data', 'r').readlines()

# emissions
emission_probs_d1 = np.array(map(lambda x: float(x), lines[0].split(' ')))
temp = reduce(lambda x, y: x + y, emission_probs_d1)
emission_probs_d1 = map(lambda x: x / temp, emission_probs_d1)

emission_probs_d2 = np.array(map(lambda x: float(x), lines[1].split(' ')))
temp = reduce(lambda x, y: x + y, emission_probs_d2)
emission_probs_d2 = map(lambda x: x / temp, emission_probs_d2)

emission_probs = np.array([[0.0] + emission_probs_d1, [0.0] + emission_probs_d2])

# transitions probs
transition_probs_1 = np.array(map(lambda x: float(x), lines[2].split(' ')))
temp = reduce(lambda x, y: x + y, transition_probs_1)
transition_probs_1 = map(lambda x: x / temp, transition_probs_1)

transition_probs_2 = np.array(map(lambda x: float(x), lines[3].split(' ')))
temp = reduce(lambda x, y: x + y, transition_probs_2)
transition_probs_2 = map(lambda x: x / temp, transition_probs_2)

transition_probs = np.array([transition_probs_1, transition_probs_2])

# trans
emissions = map(lambda x: int(x), filter(lambda s: len(s) > 0, lines[4].split(' ')))

initial_dist = np.array([[0.5, 0.5]])#np.array([transition_probs[0]])

hmm = HMM(transition_probs, emission_probs)
'''
if __name__ == "__main__":
    result = viterbi(hmm, initial_dist, emissions)
    #result = viterbi(wiki_hmm, wiki_initial_dist, wiki_emissions)
    for n in result:
        print(n),

###################

#examples
#from Wikipedia

'''

wiki_transition_probs = np.array([[0.9, 0.1], [0.1, 0.9]]) #0=dice1, 1=dice2
wiki_emissions = [5, 4, 2, 1, 1, 1, 6, 5, 4, 2, 1, 1, 2, 4, 3, 1, 1, 1, 2, 1, 1, 1, 1, 3, 6, 6, 4, 6, 5, 5, 1, 3, 3, 6, 6, 5, 2, 1, 4, 4, 6, 3, 6, 1, 1, 1, 1, 1, 5, 1, 1, 1, 2, 1, 1, 1, 6, 1, 1, 1, 1, 3, 1, 4, 4, 6, 6, 6, 1, 1, 2, 1, 1, 3, 3, 4, 1, 1, 1, 4, 3, 2, 2, 1, 1, 1, 1, 4, 5, 5, 1, 1, 1, 3, 1, 1, 6, 4, 2, 1, 5, 4, 6, 6, 6, 6, 4, 1, 4, 6, 6, 6, 2, 6, 3, 6, 6, 4, 5, 6, 6, 3, 3, 6, 3, 6, 5, 1, 3, 1, 1, 4, 4, 1, 3, 6, 2, 6, 6, 5, 4, 6, 6, 2, 3, 1, 1, 2, 1, 3, 4, 1, 2, 1, 5, 6, 6, 4, 6, 1, 2, 6, 6, 1, 6, 1, 2, 5, 1, 6, 6, 5, 6, 6, 6, 1, 6, 6, 6, 6, 4, 6, 4, 1, 2, 3, 6, 2, 6, 4, 6, 5, 6, 6, 6, 6, 6, 3, 1, 1]
wiki_emission_probs = np.array([[0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5], [0.0, 0.5, 0.1, 0.1, 0.1, 0.1, 0.1]])
wiki_initial_dist = np.array([[0.5, 0.5]])
wiki_hmm = HMM(wiki_transition_probs, wiki_emission_probs)

if __name__ == "__main__":
    result = viterbi(wiki_hmm, wiki_initial_dist, wiki_emissions)
    for n in result:
        print(n),

print ''
print '---'
print emission_probs
print wiki_emission_probs
print '---'
print transition_probs
print wiki_transition_probs
print '---'
print emissions
print wiki_emissions
print '---'
print initial_dist
print wiki_initial_dist
print '---'

