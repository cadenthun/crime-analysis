import pandas as pd
from sklearn import preprocessing

class data_cleaner:
    '''
    intent is to clean the data (keep what's needed, discard what's not)
    '''
    def __init__(self, file):
        '''
        initializing the instance by reading the data file
        Args:
            file: a csv data file.
        Return:
            None.
        '''
        #do exception handling
        self.df = pd.read_csv(file)

    def keepColumns(self, columns):
        '''
        keep the given columns
        Args:
            columns: an array of strings.
        Return:
            None.
        '''
        self.df = self.df[columns]

    def changeName(self, oldName, newName):
        '''
        change the name of given columns
        Args:
            oldName: an array of strings.
            newName: an array of strings.
        Return:
            None.
        '''
        for i in range(len(oldName)):
            self.df = self.df.rename(columns={oldName[i]: newName[i]})
            
    def delNa(self):
        '''
        delete NA values
        '''
        self.df = self.df.dropna()
        
    def delRows(self):
        #once change name works fix the variable name here
        self.df = self.df[self.df["Vict Sex"] != "X"]
        
    def sexToNum(self):
        
        if any(self.df["Vict Sex"] == "X"):
            raise TypeError("There are victim's with unknown sex in this dataset.")
        else:
            le = preprocessing.LabelEncoder()
            self.df['Vict Sex'] = le.fit_transform(self.df['Vict Sex'])
            #change male values that are greater than 0 to 1. 
            #data[data["Vict Sex"] > 0] = 1 this is wrong
        
        #lesson 19
        
    def unique(self, column):
        '''
        drop the duplicates in a given column
        Args:
            column: a string.
        Return:
            None.
        '''
        self.df = self.df.drop_duplicates(subset = [column])

    def merge(self, other):
        '''
        merge two Cleaner instances and return a dataframe
        Args:
            other: a Cleaner instance
        Return:
            A dataframe merged by the dataframes of self and other
        '''
        if not (self.df["Player"].is_unique and other.df["Player"].is_unique):
            raise ValueError("The Player column is not unique")
        else:
            return pd.merge(self.df, other.df, on = "Player")
