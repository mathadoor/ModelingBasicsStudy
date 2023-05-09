import numpy as np


def bernoulli_mle(data):
    return np.mean(data)


def markov_chain_mle(data):
    '''
    Divide the data in subsequences of lengths 2 with an overlap of 1. For each subsequence, compute the probability of
    the second element given the first element. If the sequence is 11, the probability of the second element being (p + delta).
    If the sequence is 01, the probability of the second element being (p - delta). If the sequence is 10, the probability of
    the second element being (1 - p - delta). If the sequence is 00, the probability of the second element being (1 - p + delta).
    Count the number of such subsequences as m, n, p, q respectively. The overall probability will be
    (p + delta)^m * (p - delta)^p * (1 - (p + delta))^n (1 - (p - delta))^q
    :param data:
    :return:
    '''
    # TODO: Implement this
    m, n, p, q = 0, 0, 0, 0
    prob = 1
    for i in range(len(data) - 1):
        if data[i] == 1 and data[i + 1] == 1:
            m += 1
        elif data[i] == 0 and data[i + 1] == 1:
            n += 1
        elif data[i] == 1 and data[i + 1] == 0:
            p += 1
        else:
            q += 1

    # Perform Grid Search on the values of pr and delta for which the log probability is maximum
    max_prob = -np.inf
    max_p = 0
    max_delta = 0
    for pr in np.linspace(0.01, 0.99, 100):
        p_s = np.log(pr) if data[0] == 1 else np.log(1 - pr)
        for delta in np.linspace(-0.99, 0.99, 100):
            if pr + delta >= 1 or pr - delta <= 0 or pr + delta <= 0 or pr - delta >= 1:
                continue
            prob = p_s + m * np.log(pr + delta) + p * np.log(pr - delta) + n * np.log(1 - (pr + delta)) + q*np.log(1 - (pr - delta))
            if prob > max_prob:
                max_prob = prob
                max_p = pr
                max_delta = delta

    return max_p, max_delta
