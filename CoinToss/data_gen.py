import numpy as np
class bernoilli_coin:
    '''
    This class is used to generate a random coin toss with probability of heads being p.
    '''
    def __init__(self, p):
        self.p = p

    def toss(self):
        '''
        This function generates a random coin toss.
        '''
        import numpy as np
        if np.random.uniform() < self.p:
            return 1
        else:
            return 0

    def tosses(self, n):
        '''
        This function generates n random coin tosses.
        '''
        return np.random.binomial(1, self.p, n)

    def reset_p(self, p):
        '''
        This function resets the probability of heads to p.
        '''
        self.p = p


class markov_coin:
    '''
    This class is used to generate a random coin toss with probability of heads being p + delta when the coin is facing
    heads up and p - delta when the coin is facing tails up.
    '''
    def __init__(self, p, delta):
        self.p = p
        self.delta = delta
        self.current_state = 0

    def toss(self):
        '''
        This function generates a random coin toss.
        '''
        import numpy as np
        if np.random.uniform() < self.p + self.delta*(2*self.current_state - 1):
            self.current_state = 1
            return 1
        else:
            self.current_state = 0
            return 0

    def tosses(self, n):
        '''
        This function generates n random coin tosses.
        '''
        ret = []
        for i in range(n):
            ret.append(self.toss())
        return ret

    def reset_p(self, p):
        '''
        This function resets the probability of heads to p.
        '''
        self.p = p
        self.current_state = 0

