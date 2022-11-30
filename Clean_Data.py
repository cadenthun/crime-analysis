import pandas as pd
import datetime
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
        if len(oldName)==len(newName):
            for i in range(len(oldName)):
                self.df.rename(columns={oldName[i]: newName[i]}, inplace=True)
        else:
            raise ValueError("Make sure there are the same number of new and old column names.")
            
    def onlyDate(self, date_name):
        self.df[date_name] = pd.to_datetime(self.df[date_name])

         
    def delNa(self):
        '''
        delete NA values
        '''
        self.df = self.df.dropna()
        
    def delRows(self):
        #once change name works fix the variable name here
        self.df = self.df[self.df["Sex"] != "X"]
        self.df = self.df[self.df["Sex"] != "H"]
        self.df = self.df[self.df["Descent"] != "X"]
    
    def toNum(self):
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
   
            
    #accessor methods
    def showShape(self):
        return self.df.shape
        
    def value_counts(self):
        return self.df.value_counts()
    
    def showHead(self):
        print(self.df.head)
        
    def drop(self, column):
        self.df.drop([column], axis = 1)
        
    def column(self, column_name): #properly returns a panda series.
        return self.df[column_name]
    
    def createDF(self):
        return pd.DataFrame(data = self.df)