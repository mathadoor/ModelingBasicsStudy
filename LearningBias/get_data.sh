# check if data_consumption.* file already exists. If it does, ask the user if they would like to clean and redownload the data
if [ -f "$(dirname "$0")/drug_consumption.csv" ]; then
    read -p "Data file already exists. Would you like to clean and redownload the data? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm "$(dirname "$0")/drug_consumption.csv"
    else
      wget -P "$(dirname "$0")" https://archive.ics.uci.edu/ml/machine-learning-databases/00373/drug_consumption.data
      mv "$(dirname "$0")/drug_consumption.data" "$(dirname "$0")/drug_consumption.csv"
    fi
fi
wget -P "$(dirname "$0")" https://archive.ics.uci.edu/ml/machine-learning-databases/00373/drug_consumption.data
mv "$(dirname "$0")/drug_consumption.data" "$(dirname "$0")/drug_consumption.csv"