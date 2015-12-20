from hmm import HMM
import numpy as np

#forward-backward algorithm
def backward(hmm, emissions):
    dist = uniform(hmm.num_states)
    dists = [dist]

    for emission in reversed(emissions):
        dist = backward_step(hmm, dist, emission)
        dists.append(dist)

    dists.reverse()

    return np.row_stack(dists)

def backward_step(hmm, dist, emission):
    return normalize(np.dot(hmm.transition_probs, np.dot(np.diagflat(hmm.emission_dist(emission)), dist.T)).T)

def forward_backward(hmm, initial_dist, emissions):
    forward_dists = forward(hmm, initial_dist, emissions)
    backward_dists = backward(hmm, emissions)

    return normalize(np.multiply(forward_dists, backward_dists))

def forward(hmm, initial_dist, emissions):
    dist = initial_dist
    dists = [dist]

    for emission in emissions:
        dist = forward_step(hmm, dist, emission)
        dists.append(dist)

    return np.row_stack(dists)

def forward_step(hmm, dist, emission):
    return normalize(np.dot(dist, np.dot(hmm.transition_probs, np.diagflat(hmm.emission_dist(emission)))))

#related utilities
def modify_tuple(tuple_, ix, value):
    as_list = list(tuple_)
    as_list[ix] = value

    return tuple(as_list)

def normalize(array, axis=1):
    sum_shape = modify_tuple(array.shape, axis, 1)
    return array / np.reshape(np.sum(array, axis=axis), sum_shape)

def uniform(n):
    return normalize(np.ones((1,n)))

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

if __name__ == "__main__":
    print(forward_backward(hmm, initial_dist, emissions))
