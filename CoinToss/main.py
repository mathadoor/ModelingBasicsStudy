# Here, we perform experiments to determine the maximum likelihood estimate of the probability of getting a head
# when tossing a coin.

import numpy as np
import matplotlib.pyplot as plt
import models
from data_gen import bernoilli_coin, markov_coin

P = 0.7  # Probability of getting a head
DELTA = 0.1  # Difference in probability of getting a head when the coin is facing heads up and tails up
NUM_FLIPS_RANGE = np.arange(10, 100, 10)  # Number of coin tosses per experiment
NUM_TRIALS = 100  # Number of experiments
FIG_SIZE = (5, 5)  # Size of the figure


bernoulli_p_bd = np.zeros((len(NUM_FLIPS_RANGE), NUM_TRIALS))
markov_p_bd = np.zeros((len(NUM_FLIPS_RANGE), NUM_TRIALS))
markov_delta_bd = np.zeros((len(NUM_FLIPS_RANGE), NUM_TRIALS))
bernoulli_p_md = np.zeros((len(NUM_FLIPS_RANGE), NUM_TRIALS))
markov_p_md = np.zeros((len(NUM_FLIPS_RANGE), NUM_TRIALS))
markov_delta_md = np.zeros((len(NUM_FLIPS_RANGE), NUM_TRIALS))

# Performing the experiments
for j in range(len(NUM_FLIPS_RANGE)):
    M = NUM_FLIPS_RANGE[j]

    for i in range(NUM_TRIALS):
        # Generating the data
        bernoulli_data = bernoilli_coin(P).tosses(M)
        markov_data = markov_coin(P, DELTA).tosses(M)

        # Fitting the bernoulli model and the markov model to the Bernoulli data
        bernoulli_p_bd[j, i] = models.bernoulli_mle(bernoulli_data)
        t0, t1 = models.markov_chain_mle(bernoulli_data)
        markov_p_bd[j, i], markov_delta_bd[j, i] = t0, t1


        # Fitting the bernoulli model and the markov model to the Markov data
        bernoulli_p_md[j, i] = models.bernoulli_mle(markov_data)
        t0, t1 = models.markov_chain_mle(markov_data)
        markov_p_md[j, i], markov_delta_md[j, i] = t0, t1


# Plotting the results with mean with shaded standard deviation area
fig, ax = plt.subplots(figsize=FIG_SIZE)
ax.plot(NUM_FLIPS_RANGE, bernoulli_p_bd.mean(axis=1), alpha=0.5, color='blue', label='Bernoulli Model', linewidth = 1.0)
ax.fill_between(NUM_FLIPS_RANGE,
                bernoulli_p_bd.mean(axis=1) - bernoulli_p_bd.std(axis=1),
                bernoulli_p_bd.mean(axis=1) + bernoulli_p_bd.std(axis=1),
                color='#0000bb',
                alpha=0.1)
ax.plot(NUM_FLIPS_RANGE, markov_p_bd.mean(axis=1), alpha=0.5, color='red', label='Markov Model', linewidth = 1.0)
ax.fill_between(NUM_FLIPS_RANGE,
                markov_p_bd.mean(axis=1) - markov_p_bd.std(axis=1),
                markov_p_bd.mean(axis=1) + markov_p_bd.std(axis=1),
                color='#bb0000',
                alpha=0.1)
ax.axhline(y=P, color='black', linestyle='--', label='True value')
ax.set_xlabel('Number of tosses/Dataset')
ax.set_ylabel('Probability of getting a head')
ax.set_title('Data Generated with Bernoulli coin')
ax.set_xlim([NUM_FLIPS_RANGE[0], NUM_FLIPS_RANGE[-1]])
ax.set_ylim([0, 1])
ax.legend(loc='best')
plt.savefig('plots/bernoulli_data.png')

fig, ax = plt.subplots(figsize=FIG_SIZE)
ax.plot(NUM_FLIPS_RANGE, bernoulli_p_md.mean(axis=1), alpha=0.5, color='blue', label='Bernoulli Model', linewidth = 1.0)
ax.fill_between(NUM_FLIPS_RANGE,
                bernoulli_p_md.mean(axis=1) - bernoulli_p_md.std(axis=1),
                bernoulli_p_md.mean(axis=1) + bernoulli_p_md.std(axis=1),
                color='#0000bb',
                alpha=0.1)
ax.plot(NUM_FLIPS_RANGE, markov_p_md.mean(axis=1), alpha=0.5, color='red', label='Markov Model', linewidth = 1.0)
ax.fill_between(NUM_FLIPS_RANGE,
                markov_p_md.mean(axis=1) - markov_p_md.std(axis=1),
                markov_p_md.mean(axis=1) + markov_p_md.std(axis=1),
                color='#bb0000',
                alpha=0.1)
ax.axhline(y=P, color='black', linestyle='--', label='True value')
ax.set_xlabel('Number of tosses/Dataset')
ax.set_ylabel('Probability of getting a head')
ax.set_title('Data Generated with Markov coin')
ax.set_xlim([NUM_FLIPS_RANGE[0], NUM_FLIPS_RANGE[-1]])
ax.set_ylim([0, 1])
ax.legend(loc='best')
plt.savefig('plots/markov_data.png')

# Plotting the results of delta
fig, ax = plt.subplots(figsize=FIG_SIZE)
ax.plot(NUM_FLIPS_RANGE, markov_delta_bd.mean(axis=1), alpha=0.5, color='red', label='Bernoulli Coin', linewidth = 1.0)
ax.fill_between(NUM_FLIPS_RANGE,
                markov_delta_bd.mean(axis=1) - markov_delta_bd.std(axis=1),
                markov_delta_bd.mean(axis=1) + markov_delta_bd.std(axis=1),
                color='#bb0000',
                alpha=0.1)
ax.plot(NUM_FLIPS_RANGE, markov_delta_md.mean(axis=1), alpha=0.5, color='blue', label='Markov Coin', linewidth = 1.0)
ax.fill_between(NUM_FLIPS_RANGE,
                markov_delta_md.mean(axis=1) - markov_delta_md.std(axis=1),
                markov_delta_md.mean(axis=1) + markov_delta_md.std(axis=1),
                color='#0000bb',
                alpha=0.1)
ax.axhline(y=0, color='red', linestyle='--', label='True value for Bernoulli coin')
ax.axhline(y=DELTA, color='black', linestyle='--', label='True value for Markov coin')
ax.set_xlabel('Number of tosses/Dataset')
ax.set_ylabel(r'$\delta$')
ax.set_title('$\delta$ for Bernoulli and Markov coins')
ax.set_xlim([NUM_FLIPS_RANGE[0], NUM_FLIPS_RANGE[-1]])
ax.set_ylim([-0.5, 0.5])
ax.legend(loc='best')
plt.savefig('plots/delta.png')