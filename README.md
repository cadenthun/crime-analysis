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
* Utilize the member function keepColumns() to determine the information from the data set that is kept.
* Utilize the other member functions to modify the data for ease of readability and computation.
3. Use matplotlib to illustrate coorelations between different data variables/crime scene tags and sex. ![image](https://user-images.githubusercontent.com/103856649/206104260-f04b8924-55fe-4bac-971b-bfbdf43a717f.png)
4. Split the data into a training set and a test set to train our machine on the dataset.
5. Use pyplot from matplotlib to graph a comparison between test data and train data to find a best-fit. ![image](https://user-images.githubusercontent.com/103856649/206104412-319efcce-3840-470a-9098-2c03b1e027ba.png)
6. Cross-validate data to improve the machine learning model.
<img width="788" alt="Screen Shot 2022-12-08 at 3 05 51 PM" src="https://user-images.githubusercontent.com/43144162/206585804-81cd26e5-e882-40e2-9cb1-17580d391570.png">

# Conclusion
Predicting victim sex based off of the crime scene tags our model considered is a difficult task. Athough our model was able to achieve ~63% accuracy, which is undoubtedly an improvement over the 50% accuracy yielded by a random guess, we would have liked our model to have been a bit more predictive. It is possible that fitting a decision tree was not the optimal approach, though we had to test it out in order to realize that might be the case.  
# Scope Limitations (ethical implications, accessibility concerns, ideas for potential extensions)
* Ethical Implications: It is possible that if a victim's sex is missing from the dataset, the victim did not want to have their sex revealed. Determining sex without the victim's consent in such a case could potentially be problematic.
* Accessibility concerns: Using our model requires an elementary understanding of Python and scikit-learn, which many people have not had the opportunity to develop.
* Ideas for potential extensions: Instead of predicting sex, we could adapt our model to predict various other crime-scene tags using the same dataset. Additionally, we could try applying our model to datasets from cities other than Los Angeles.
# References and Acknowledgements
* https://github.com/joanneqiu07/NBA-Salary-Prediction
* Harlin Lee's PIC 16A lectures at UCLA, Fall Quarter 2022
# Background/Source of Dataset
Crime data from the City of Los Angeles (2020 - Present): 

This dataset contains an exhaustive list with details and information pertaining to incidents of crime in Los Angeles from 2020 and is regularly updated. This data consolidates information from the paper reports originating from the departments that responded to the incidents in question. Note that some of the parameters of the data may be redacted, not recorded, or otherwise missing. 

You may access the entire database at the following link: https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8
