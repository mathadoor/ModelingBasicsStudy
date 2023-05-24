# Check if the dataconsumption.csv is available in the directory - if not run get_data.sh available in the directory of
# this file

import os
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# DEFINE GLOBAL VARIABLES
SPLIT = 0.8
DATA_FILE = 'dataconsumption.csv'
RANDOM_STATE = 42

# get the directory of this file
dir_path = os.path.dirname(os.path.realpath(__file__))

# check if the dataconsumption.csv is available in the directory
if not os.path.exists(dir_path + '/' + DATA_FILE):
    # if not run get_data.sh
    os.system('bash ' + dir_path + '/get_data.sh')

# load the data
data = np.loadtxt(dir_path + '/' + DATA_FILE, delimiter=',', skiprows=1)

# split the data into training and testing
train, test = train_test_split(data, train_size=SPLIT, random_state=RANDOM_STATE)

# split the training data into features and labels
train_x, test_x = train[:, :-1], test[:, :-1]
train_y, test_y = train[:, -1], test[:, -1]

# train a decision tree classifier
clf = DecisionTreeClassifier(random_state=RANDOM_STATE)
clf.fit(train_x, train_y)

# print the accuracy of the classifier
print('Accuracy of the classifier is: ' + str(clf.score(test_x, test_y)))



#

