import numpy

def bernoulli_mle(data):
    return numpy.mean(data)

def markov_chain_mle(data):
    '''
    Divide the data in subsequences of lengths 2 with an overlap of 1. For each subsequence, compute the probability of
    the second element given the first element. If the sequence is 11, the probability of the second element being (p + delta).
    If the sequence is 01, the probability of the second element being (p - delta). If the sequence is 10, the probability of
    the second element being (1 - p - delta). If the sequence is 00, the probability of the second element being (1 - p + delta).
    :param data:
    :return:
    '''
    # TODO: Implement this

    return numpy.mean(data)