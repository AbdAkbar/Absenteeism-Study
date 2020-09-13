# Absenteeism-Study
A study of factors leading to workplace absenteeism.

The dataset was used in academic research at the Universidade Nove de Julho - Postgraduate Program in Informatics and Knowledge Management.
There are 740 total instances; 700 instances are used for model construction and application. The remaining 40 instances are used for data visualization.

Once preprocessing is completed, a logistic regression is fitted on the training data and then tested; an 80/20 train/test split is used. After the initial regression, backwards elimination is utilized to remove inconsequential features. Once the model is finalized, it is exported in a Python module, for use on the visualization dataset. Conclusions from this data are presented in Tableau.
