import numpy as np
from hmm import HMM

def parse_data():
    # data input file
    lines = open('data.txt', 'r').readlines()

    # emissions
    emissions = map(lambda x: int(x), filter(lambda s: len(s) > 0, lines[4].split(' ')))

    # emission probabilities
    emission_probs_d1 = np.array(map(lambda x: float(x), lines[0].split(' ')))
    temp = reduce(lambda x, y: x + y, emission_probs_d1)
    emission_probs_d1 = map(lambda x: x / temp, emission_probs_d1)

    emission_probs_d2 = np.array(map(lambda x: float(x), lines[1].split(' ')))
    temp = reduce(lambda x, y: x + y, emission_probs_d2)
    emission_probs_d2 = map(lambda x: x / temp, emission_probs_d2)

    emission_probs = np.array([[0.0] + emission_probs_d1, [0.0] + emission_probs_d2])

    # transitions probabilities
    transition_probs_1 = np.array(map(lambda x: float(x), lines[2].split(' ')))
    temp = reduce(lambda x, y: x + y, transition_probs_1)
    transition_probs_1 = map(lambda x: x / temp, transition_probs_1)

    transition_probs_2 = np.array(map(lambda x: float(x), lines[3].split(' ')))
    temp = reduce(lambda x, y: x + y, transition_probs_2)
    transition_probs_2 = map(lambda x: x / temp, transition_probs_2)

    transition_probs = np.array([transition_probs_1, transition_probs_2])

    # initial probability
    initial_dist = np.array([[0.5, 0.5]])

    # hmm
    hmm = HMM(transition_probs, emission_probs)

    return hmm, initial_dist, emissions
