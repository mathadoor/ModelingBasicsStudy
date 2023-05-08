# Here, we perform experiments to determine the probability of getting a head
# when tossing a coin. We use the maximum likelihood estimator to estimate the
# probability of getting a head. We use two different estimators: the Bernoulli
# estimator and the Markov chain estimator. The Bernoulli estimator is the
# simplest estimator. It assumes that the probability of getting a head is the
# same for all tosses. The Markov chain estimator assumes that the probability
# of getting a head depends on the previous toss. If the previous toss was a
# head, the probability of getting a head is higher. If the previous toss was a
# tail, the probability of getting a head is lower.

import numpy
import matplotlib.pyplot as plt
import models
from data_gen import bernoilli_coin, markov_coin

P = 0.6
DELTA = 0.1
N = 100

bernoulli_data = bernoilli_coin(P).tosses(N)
markov_data = markov_coin(P, DELTA).tosses(N)
