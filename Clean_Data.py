import pandas as pd
import datetime
from sklearn import preprocessing

class data_cleaner:
    '''
    intent is to clean the data (keep what's needed, discard what's not)
    '''
    def __init__(self, file):
        '''
        initializing the data cleaner by reading the data file
        Args:
            file: csv data file.
        Return:
            N/A
        '''
        #do exception handling
        self.df = pd.read_csv(file)

    def keepColumns(self, columns):
        '''
        keep the given columns
        Args:
            columns: a list of strings.
        Return:
            None.
        '''
        self.df = self.df[columns]

    def changeName(self, oldName, newName):
        '''
        change the name of given columns
        Args:
            oldName: a list of strings of current column names.
            newName: a list of strings of new column names.
        Return:
            None
        '''
        if len(oldName)==len(newName):
            for i in range(len(oldName)):
                self.df.rename(columns={oldName[i]: newName[i]}, inplace=True)
        else:
            raise ValueError("Make sure there are the same number of new and old column names.")
            
    def onlyDate(self, date_name):
        '''
        converts date time format to just dates
        Args:
            date_name: String of what the date column is called ("Date")
        Returns"
            None. 
        '''
        
        self.df[date_name] = pd.to_datetime(self.df[date_name])

         
    def delNa(self):
        '''
        delete NA values
        Args:
            None - amends data cleaner. 
        Returns:
            None
        '''
        self.df = self.df.dropna()
        
    def delRows(self):
        '''
        deletes rows with incomplete data.
        Args:
            None - amends data cleaner.   
        Return:
            None. 
        '''
        self.df = self.df[self.df["Sex"] != "X"]
        self.df = self.df[self.df["Sex"] != "H"]
        self.df = self.df[self.df["Descent"] != "X"]
    
    def toNum(self):
        '''
        ensures that there are no unknown data types. 
        converts females and males to 0 and 1 respectively. 
        also converts descent into a number. 
        Args:
            None - amends data cleaner
        Returns:
            None. 
        '''
        if any(self.df["Sex"] == "X"):
            raise TypeError("There are victim's with unknown sex in this dataset.")
        if any(self.df["Sex"] == "H"):
            raise TypeError("There are victim's with unknown sex in this dataset.")
        if any(self.df["Descent"] == "X"):
            raise TypeError("There are victim's with unknown descent in this dataset.")
        else:
            le = preprocessing.LabelEncoder()
            self.df['Sex'] = le.fit_transform(self.df['Sex'])
            self.df['Descent'] = le.fit_transform(self.df['Descent'])
            #change male values that are greater than 0 to 1. 
            #data[data["Vict Sex"] > 0] = 1 this is wrong
    
    def createDF(self):
        '''
        converts data cleaner into a dataframe
        Args:
            None - amends data cleaner.    
        Return:
            None. 
        '''
        return pd.DataFrame(data = self.df)
