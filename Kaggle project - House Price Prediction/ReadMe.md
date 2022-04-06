# <b>House Price Prediction - Advanced Regression</b>
<br>

This Kaggle competition project aims at predicting the <b>Sale Prices</b> of residential homes in Ames, Iowa, US. Please refer this <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/House%20Price%20Prediction%20-%20Kaggle%20Project.ipynb">notebook</a> for complete implementation of this project.

### <b>Data Source:</b>
<br>

The datasets used for this project can be found <a href="https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data">here</a>. 
<br>
<ul>
  <li><b>train.csv</b> - Used for Data analysis and Model training.</li>
  <li><b>test.csv</b> - Used for Prediction.</li>
  <li><b>sample_submission.csv</b> - Used for submission(for scoring).</li>
</ul>


### <b>Technologies Used:</b>
<br>
<ul>
  <li>xgboost==1.3.3</li>
  <li>seaborn==0.11.1</li>
  <li>scikit-learn==0.23.2</li>
  <li>pandas==1.2.0</li>
  <li>numpy==1.19.5</li>
  <li>matplotlib==3.3.3</li>
  </ul>
  
 
 ### <b>The Notebook:</b>
 <br>
 There were 80 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa, US. This project aims to predict the final price of each home. Please refer this <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/House%20Price%20Prediction%20-%20Kaggle%20Project.ipynb">notebook</a> for complete implementation of this project.
<br>

#### <b> lets take a quick look at the datasets:</b>
<br>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/hp_1.png" />

<br>
<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/hp_2.png" />


### <b>Data Analysis:</b>
<br>

After doing some structural investigation on our datasets like exploring the general shape as well as the data types of the features, we focus our attention to the Quality and Content of our datasets with regards to Missing values, Outliers, Feature values and how they relate to the target variable<b>(sale price)</b>.
<br>


Lets take a peek at the <b>Missing values in the train</b> dataset:
<br>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/hp_3.png" />
<br>

<b>Sale price vs Features with missing values (1):</b>
<br>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/hp_4.png" />
<br>
Please refer this <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/House%20Price%20Prediction%20-%20Kaggle%20Project.ipynb">notebook</a> for complete implementation of this project.
<br>


<b>Analysis of Numerical features:</b>
<br>

Numerical variables have 2 categories.. 1. Discrete 2. Continous. Analysis of Numerical features will give us some insights about how many Discrete varibales (Features with unique values range from 3 to ~ 25) and Continous variables (more than 25 unique values) are in the dataset.


<b>Discrete Numerical variables in the train dataset:</b>
<br>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/hp_5.png" />


<b>Visualizing Contiunous variables in the train dataset:</b>
<br>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/hp_6.png" />
<br>

<b>Removing Redundant features:</b>
<br>

Irrelevant or partially relevant features can negatively impact model performance. Models based on highly correlated features need more iterations and therefore take longer to train. <b>Less redundant features means less noise which improves model accuracy and takes less training time</b>. Here in this project, the following steps were taken to remove redundant features.
<br>


1. Features with more than 90% of the data missing were removed from Train and Test datasets.
<br>

2. Using <b>Person Correaltion coefficient</b>, Highly correlated features were removed from the Train and Test datasets. Redundant <b>Categorical features</b> from the Train dataset (which were not present in the Test dataset) were identified and removed.
<br>
<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/hp_7.png" />



<b>Handling Missing Values:</b>
<br>

For Numeric features, if the feature has many outliers then <b>Median</b> value was chosen otherwise <b>mean imputation</b> was used to fillup those missing gaps.
<br>

For Catagorical features, the value was chosen based on the <b>Highest frequency</b> to fillup the missing gaps.
<br>


<b>Skewness:</b>
<br>

Skewness of numerical features from the datasets which showed strong non-gaussian distributions were fixed by taking log-transformation of the feature values. The screenshot below shows how the Skewness of the target variable fixed. 
<br>

Target varible with observed values:
<br>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/hp_9.png" />


Target varible after log-transformation:
<br>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/hp_10.png" />



<b>Feature Selection and Model building:</b>
<br>

<b>mutual_info_regression</b> statistics was used in the <b>SelectKBest()</b> feature selection strategy to select the 'k' best features. <b>GridSearchCV</b> was used to systematically test a range of different numbers of selected features and discover which results in the best performing model. <b>XGBRegressor()</b> was chosen as a perferred model for this task. <b>RepeatedKFold</b> class was used to evaluate model configurations. We used three repeats of 10-fold cross-validation for this project.
<br>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/hp_11.png" />


Please refer this <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20House%20Price%20Prediction/House%20Price%20Prediction%20-%20Kaggle%20Project.ipynb">notebook</a> for complete implementation of this project.

 


