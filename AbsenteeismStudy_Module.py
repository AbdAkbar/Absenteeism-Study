#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import all libraries needed
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

    
# create the class that will be used for predictions with new data
class absenteeism_model():
    
    def __init__(self, model_file):
        # read the 'model' and 'scaler' files which were saved
        with open('logmodel','rb') as model_file:
            self.reg = pickle.load(model_file)
            self.data = None
            
    # take a data file (*.csv) and preprocess it in the same way as in the lectures
    def load_and_clean_data(self, data_file):
            
        # import the data
        df = pd.read_csv(data_file, delimiter=',')
        # store the data in a new variable for later use
        self.df_with_predictions = df.copy()
        # drop the 'ID' column
        df = df.drop(['ID'], axis = 1)
        # the new data is used to predict absenteeism; thus it will not have an 'Absenteeism Time in Hours' column
        # to preserve the preprocessing and model code, add an 'Absenteeism Time in Hours' column of NaN values
        df['Absenteeism Time in Hours'] = 'NaN'
            
        # create a separate dataframe, containing dummy values for ALL available reasons
        reason_columns = pd.get_dummies(df['Reason for Absence'], drop_first = True)
            
        # split reason_columns into 4 types
        reason_type_1 = reason_columns.loc[:,'1':'14'].max(axis=1)
        reason_type_2 = reason_columns.loc[:,'15':'17'].max(axis=1)
        reason_type_3 = reason_columns.loc[:,'18':'21'].max(axis=1)
        reason_type_4 = reason_columns.loc[:,'22':].max(axis=1)
            
        # to avoid multicollinearity, drop the 'Reason for Absence' column from df
        df = df.drop(['Reason for Absence'], axis = 1)
            
        # concatenate df anf the 4 types of reason for absence
        df = pd.concat([df, reason_type_1, reason_type_2, reason_type_3, reason_type_4], axis=1)
            
        # assign names to the 4 reason type columns
        column_names = ['Date', 'Transportation Expense', 'Distance to Work', 'Age',
                       'Daily Work Load Average', 'Body Mass Index', 'Education',
                       'Children', 'Pets', 'Absenteeism Time in Hours', 'Reason 1', 'Reason 2', 'Reason 3', 'Reason 4']
        df.columns = column_names
            
        # re-order the columns in df
        column_names_reordered = ['Reason 1', 'Reason 2', 'Reason 3', 'Reason 4','Date', 'Transportation Expense', 'Distance to Work', 'Age',
                                   'Daily Work Load Average', 'Body Mass Index', 'Education',
                                   'Children', 'Pets', 'Absenteeism Time in Hours']
        df = df[column_names_reordered]
            
        # convert the 'Date' column into datetime
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
            
        # create a list with Month Values retrieved from the 'Date' column
        list_months = []
        for i in range(df.shape[0]):
            list_months.append(df['Date'][i].month)
                
        # insert the values in a new column in df, called 'Month Value'
        df['Month Value'] = list_months
        
        # create a new feature called 'Day of the Week'
        def date_to_weekday(date_value):
            return date_value.weekday()
        
        df['Day of the Week'] = df['Date'].apply(date_to_weekday)

            
        # drop the 'Date' column from df
        df = df.drop(['Date'], axis=1)
            
        # re-order the columns in df
        column_names_upd = ['Reason 1', 'Reason 2', 'Reason 3', 'Reason 4', 'Month Value',
                           'Day of the Week','Transportation Expense', 'Distance to Work', 'Age',
                           'Daily Work Load Average', 'Body Mass Index', 'Education',
                           'Children', 'Pets', 'Absenteeism Time in Hours']
        df = df[column_names_upd]
            
        # map 'Education' variables; the result is a dummy
        df['Education'] = df['Education'].map({1:0, 2:1, 3:1, 4:1})
            
        # replace the NaN values
        df = df.fillna(value=0)
            
        # drop the original absenteeism time 
        df = df.drop(['Absenteeism Time in Hours'],axis=1)
            
        # drop the variables we decide we don't need
        df = df.drop(['Day of the Week', 'Daily Work Load Average', 'Distance to Work'],axis=1)
            
        self.preprocessed_data = df.copy()
            
        # we must implement our feature scaling
        columns_to_omit = ['Reason 1','Reason 2','Reason 3','Reason 4','Education']
        columns_to_scale = [x for x in unscaled_inputs.columns.values if x not in columns_to_omit]
        
        df_to_scale = df[columns_to_scale]
        
        absenteeism_scaler.fit(df_to_scale)
        scaled_data = absenteeism_scaler.transform(df_to_scale)
        scaled_df = pd.DataFrame(scaled_data, columns = columns_to_scale)
        
        self.data = pd.concat([df[columns_to_omit],scaled_df],axis=1)
        inputs_reordered = ['Reason 1', 'Reason 2', 'Reason 3', 'Reason 4','Month Value',
                            'Transportation Expense', 'Age','Body Mass Index', 'Education',
                            'Children', 'Pets']
        self.data = self.data[inputs_reordered]

            
    # a function which outputs the probability of a data point to be 1
    def predicted_probability(self):
        if (self.data is not None):
            pred = self.reg.predict_proba(self.data)[:,1]
            return pred
            
    # a function which outputs 0 or 1 based on our model
    def predicted_output_category(self):
        if (self.data is not None):
            pred_outputs = self.reg.predict(self_data)
            return pred_outputs
                
    # predict the outputs and the probabilites and
    # add columns with these values at the end of the new data
    def predicted_outputs(self):
        if (self.data is not None):
            self.preprocessed_data['Probability'] = self.reg.predict_proba(self.data)[:,1]
            self.preprocessed_data['Prediction'] = self.reg.predict(self.data)
            return self.preprocessed_data
            

