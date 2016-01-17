import numpy as np
from parse import parse_data

DELTA = 0.001

class HMM:
    def __init__(self, pi, A, B):
        self.pi = pi
        self.A = A
        self.B = B
        self.M = B.shape[1]
        self.N = A.shape[0]

    def forward_with_scale(self, obs):
        T = len(obs)
        N = self.N
        alpha = np.zeros([N,T])
        scale = np.zeros(T)

        alpha[:,0] = self.pi[:] * self.B[:,obs[0]-1]
        scale[0] = np.sum(alpha[:,0])
        alpha[:,0] /= scale[0]

        for t in xrange(1,T):
            for n in xrange(0,N):
                alpha[n,t] = np.sum(alpha[:,t-1] * self.A[:,n]) * self.B[n,obs[t]-1]
            scale[t] = np.sum(alpha[:,t])
            alpha[:,t] /= scale[t]

        logprob = np.sum(np.log(scale[:]))
        return logprob, alpha, scale	

    def backward_with_scale(self, obs, scale):
        T = len(obs)
        N = self.N
        beta = np.zeros([N,T])

        beta[:,T-1] = 1 / scale[T-1]
        for t in reversed(xrange(0,T-1)):
            for n in xrange(0,N):
                beta[n,t] = np.sum(self.B[:,obs[t+1]-1] * self.A[n,:] * beta[:,t+1])
                beta[n,t] /= scale[t]
		
        return beta

    def baum_welch(self, obs):
        T = len(obs)
        M = self.M
        N = self.N		
        alpha = np.zeros([N,T])
        beta = np.zeros([N,T])
        scale = np.zeros(T)
        gamma = np.zeros([N,T])
        xi = np.zeros([N,N,T-1])
    
        # caculate initial parameters
        logprobprev, alpha, scale = self.forward_with_scale(obs)
        beta = self.backward_with_scale(obs, scale)			
        gamma = self.compute_gamma(alpha, beta)	
        xi = self.compute_xi(obs, alpha, beta)	
        logprobinit = logprobprev		
		
        # start interative 
        while True:
            # E
            self.pi = 0.001 + 0.999*gamma[:,0]
            for i in xrange(N):
                denominator = np.sum(gamma[i,0:T-1])
                for j in xrange(N): 
                    numerator = np.sum(xi[i,j,0:T-1])
                    self.A[i,j] = numerator / denominator
                   				
            self.A = 0.001 + 0.999*self.A
            for j in xrange(0,N):
                denominator = np.sum(gamma[j,:])
                for k in xrange(0,M):
                    numerator = 0.0
                    for t in xrange(0,T):
                        if obs[t]-1 == k:
                            numerator += gamma[j,t]
                    self.B[j,k] = numerator / denominator
            self.B = 0.001 + 0.999*self.B

            # M
            logprobcur, alpha, scale = self.forward_with_scale(obs)
            beta = self.backward_with_scale(obs, scale)			
            gamma = self.compute_gamma(alpha, beta)	
            xi = self.compute_xi(obs, alpha, beta)	

            delta = logprobcur - logprobprev
            logprobprev = logprobcur

            if delta <= DELTA:
                break 	
				
        logprobfinal = logprobcur
        return logprobinit, logprobfinal				
			
    def compute_gamma(self, alpha, beta):
        gamma = np.zeros(alpha.shape)
        gamma = alpha[:,:] * beta[:,:]
        gamma = gamma / np.sum(gamma,0)
        return gamma
			
    def compute_xi(self, obs, alpha, beta):
        T = len(obs)
        N = self.N
        xi = np.zeros((N, N, T-1))
			
        for t in xrange(0,T-1):        
            for i in xrange(0,N):
                for j in xrange(0,N):
                    xi[i,j,t] = alpha[i,t] * self.A[i,j] * \
                                self.B[j,obs[t+1]-1] * beta[j,t+1]
            xi[:,:,t] /= np.sum(np.sum(xi[:,:,t],1),0)	
        return xi

# running baum-welch algorithm
def main():
    hmm, pi, emissions = parse_data()
    pi = pi[0]
    A = hmm._transition_probs
    B = hmm._emission_probs
    emissions = np.array(emissions)

    B = np.array([
        np.delete(B[0], 0),
        np.delete(B[1], 0)
    ])

    print "pi:", pi
    print "A:", A
    print "B:", B
    print "Emissions:", emissions

    # test

    # A = np.array([
    #     [0.333, 0.333, 0.333],
    #     [0.333, 0.333, 0.333],
    #     [0.333, 0.333, 0.333],
    # ])
    #
    # B = np.array([
    #     [0.5, 0.5],
    #     [0.75, 0.25],
    #     [0.25, 0.75]
    # ])
    #
    # pi = np.array([0.333, 0.333, 0.333])
    #
    # emissions = np.array([1, 1, 1, 2, 2, 2, 1, 2, 1, 2])
    #
    # print "pi:", pi
    # print "A:", A
    # print "B:", B
    # print "Emissions:", emissions

    hmm = HMM(pi, A, B)
    logprobinit, logprobfinal = hmm.baum_welch(emissions)

    print "initial log probability:", logprobinit
    print "final log probability:", logprobfinal

if __name__ == '__main__': main()
