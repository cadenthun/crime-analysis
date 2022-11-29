import pandas as pd

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
        
    def delRows(self):
        print(data.shape)
        self.df = self.df.loc[self.df["Sex"] != "X"]
        print(data.shape)
        
        
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