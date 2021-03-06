# Absenteeism-Study
A study of factors leading to workplace absenteeism.

The dataset was used in academic research at the Universidade Nove de Julho - Postgraduate Program in Informatics and Knowledge Management.
There are 740 total instances; 700 instances are used for model construction and application, stored in 'Absenteeism_data.csv.' The remaining 40 instances are used for data visualization, stored in 'Absenteeism_new_data.csv'.

Once preprocessing is completed, a logistic regression is fitted on the training data and then tested; an 80/20 train/test split is used. After the initial regression, backwards elimination is utilized to remove inconsequential features. Once the model is finalized, it is exported in a Python module, for use on the visualization dataset. Predictions were exported directly from Python as a .csv file. An infographic with conclusions from this data is presented in Tableau.

The predicted data was also inserted into a MySQL database, to allow for easier manipulations in the future.

The infographic is attached both as a Tableau Workbook and a PDF, and can also be viewed here: https://public.tableau.com/profile/abdullah.akbar#!/vizhome/ExcessiveAbsenteeism_16001236764150/Dashboard1?publish=yes
