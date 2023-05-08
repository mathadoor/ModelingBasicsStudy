# ModelingBasicsStudy
A repository containing code to supplement my blog posts related to bias variance tradeoff.
### General Structure
The general structure of the repository is as follows:  
`ModelingBasicsStudy/`  
&emsp;├── `Coin Toss` contains the code for the coin toss experiment  
&emsp;├&emsp;├── `data_gen.py` code to generate the data   
&emsp;├&emsp;├── `main.py` code to run the experiments  
&emsp;├&emsp;└── `models.py` code to create models  
&emsp;└── `readme.md` - contains general information   

### Setup 
#### Step 1 - Install Conda Environment
If you haven't already, please make sure to download and install anaconda from the [official website](https://www.anaconda.com/products/distribution)
#### Step 2 - Setup Conda Environment
Open a terminal/Command Prompt and create a conda environment by running the following command  
```commandline
conda create --name modeling python=3.8
```
#### Step 3 - Activate the environment
Activate the environment using the following command
```commandline
conda activate modeling
```
#### Step 4 - Install Numpy and Matplotlib
```commandline
conda install numpy
conda install matplotlib
```

