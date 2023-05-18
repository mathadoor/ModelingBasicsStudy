# Check if the dataconsumption.csv is available in the directory - if not run get_data.sh available in the directory of
# this file

import os

# get the directory of this file
dir_path = os.path.dirname(os.path.realpath(__file__))

# check if the dataconsumption.csv is available in the directory
if not os.path.exists(dir_path + '/dataconsumption.csv'):
    # if not run get_data.sh
    os.system('bash ' + dir_path + '/get_data.sh')

