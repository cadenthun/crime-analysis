# crime-analysis
Crime Analysis Final Project for PIC16A Fall 2022
# Group Members
Anagha Chandrasekharan, Randal Macias, Caden Thun, Vincent Por
# Project Description
In this project, we are looking to discover if there is a correlation between various crime scene tags (crime committed/crime code, victim age, victim descent, district number, and date) and whether a machine learning model can predict the victim’s sex, based on open data from the city of Los Angeles. 
# Package Requirements
We used the following packages:
* numpy (1.21.5)
* sklearn (1.0.2)
* pandas (1.4.2) 
* matplotlib (3.5.1)
# Detailed Description of DEMO
1. Import various packages such as numpy, sklearn, pandas, and matplotlib.
2. Clean dataset using the data_cleaner class from CleanData.py.
3. Use matplotlib to illustrate coorelations between different data variables/crime scene tags and sex. ![image](https://user-images.githubusercontent.com/103856649/206104260-f04b8924-55fe-4bac-971b-bfbdf43a717f.png)
4. Split the data into a training set and a test set to train our machine on the dataset.
5. Use pyplot from matplotlib to graph a comparison between test data and train data to find a best-fit. ![image](https://user-images.githubusercontent.com/103856649/206104412-319efcce-3840-470a-9098-2c03b1e027ba.png)
6. Cross-validate data to improve the machine learning model.
# Conclusion
# Scope Limitations (ethical implications, accessibility concerns, ideas for potential extensions)
# References and Acknowledgements
# Background/Source of Dataset
Crime data from the City of Los Angeles (2020): https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8
