# <b>Titanic Survivor Prediction</b>

<div style="text-align: center;"><img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/Screenshot%20(355).png"
width="1000" ></div>
<br>

### <b>Project Demo:</b>
<hr />
<b>Passenger Form:</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titnic_sc_1.png" width="600" style="float: left;"/>
  
<b>Prediction:</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic_sc2.png" width="600" style="float: left;"/>


### <b>Data Source:</b>
<hr />
The goal of this project is to <b>Predict</b> who will survive and who will not based on given Titanic passenger data (name, age, gender, passenger class, etc). In this project we will use <b>train and test</b> datasets provided by <b>Kaggle</b>.
<br>
1. <a href="https://www.kaggle.com/code/alexisbcook/titanic-tutorial/data?select=train.csv">train.csv</a> - Used for Data Analysis, Feature Engineering and Model Building.
<br> 
2. <a href="https://www.kaggle.com/code/alexisbcook/titanic-tutorial/data?select=test.csv">test.csv</a> - Used for Prediction.



### <b>Technologies Used:</b>
<hr />
<ul>
  <li>python==3.7.6(Kaggle)</li>
  <li>python==3.7.11(pycharm)</li>
  <li>pandas==1.1.3</li>
  <li>numpy==1.18.5</li>
  <li>scikit-learn==0.23.2</li>
  <li>flask==2.0.2</li>
 </ul>

### <b>Overview of the Notebook:</b>
<hr />
<b>Titanic Survivor ML Prediction</b> notebook was created in Kaggle platform to predict who <b>Survived</b> and who did not when <b>RMS Titanic</b> sank in the early morning hours of 15 April 1912 in the North Atlantic Ocean. Please refer this <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic-survivor-ml-prediction.ipynb"> Notebook </a> for the detail implementataion of this project.
<br>

<b>Lets take a peek into the datasets:</b>
<ol>
  <li><b>Train:</b>
    <br>
    <img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic_sc_3.png" />
  </li>
  <li><b>Test:</b>
    <br>
    <img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic_sc_4.png" />
  </li>
 </ol>
 
 <b>Data Analysis:</b>
 <br>
 
 Each <b>feature</b> from the train dataset were analysed throughly to determine its importance in <b>Predicting</b> the Survival rate of the passenger. The screenshot below shows the analysis of the features <b>'Pcalss'</b> stands for Passenger Class and <b>'Sex'</b>.
 <br>
Please refer this <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic-survivor-ml-prediction.ipynb"> Notebook </a> for the detail analysis and implementataion of this project.
 <br>
 
 <img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic_sc_5.png" />
 
 
 <b>Feature Engineering:</b>
 <br>
 
 When there were redundant features present and dose not make sence individually they were combained to form a new feature. This new feature is then analysed to see its importance in predicting the target. The screenshot below shows the Feature Engineering of the features <b>'SibSp'</b> stands for Siblings and Spouse and <b>'Parch'</b>stands for Parents and Children. 
<br>
Please refer this <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic-survivor-ml-prediction.ipynb"> Notebook </a> for the detail implementataion of this project.
<br>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic_sc_6.png" />


<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic_sc_7.png" />


<b>Missing Values:</b>
<br>

The datasets in this project were examined throughly for any missing values. If the feature(s) had more than 80% of the value missing then that feature was removed from analysis. Otherwise, missing values were substituted based on the domain knowledge of the feature. The screenshot below shows how missing values were handled for <b>'Age'</b> feature.
<br>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic_sc_8.png" />
<br>
Please refer this <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic-survivor-ml-prediction.ipynb"> Notebook </a> for the detail implementataion of this project.



<b>Model Selection:</b>
<br>

Here we are at the Heart and Soul of this project where 9 State of the art <b>Classifiers</b> were chosen to select the best <b>One</b> for Prediction based on its <b>Accuracy</b> value. Using <b>StratifiedKFold()</b> the <b>Train</b> dataset was split into <b>Train and Validation</b> sets. The models were trained on Training set and Accuracy was calculated on Validation set. The screenshot below shows the <b>Models and their <b>Accuracy</b> values.
<br>
  
<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic_sc_13.png" />
<br>  
Please refer this <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic-survivor-ml-prediction.ipynb"> Notebook</a> for the detail implementataion of this project.

  
  
<b>Model Tuning:</b>
<br>

Once the Best model was selected, in this case <b>SVC</b>, <b>GridSearchCV</b> was used to find the best parameters for our model.
<br>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic_sc_11.png" />


<b>The Model:</b>
<br>

The screenshot below shows how the <b>SVC</b> model and its tuned parameters were used to fit the <b>Train</b> dataset. Using this model, Prediction was made on the <b>Test</b> dataset and submitted to Kaggle for scoring.

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic_sc_14.png" />


Please refer this <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Titanic%20Survivor%20Prediction/titanic-survivor-ml-prediction.ipynb"> Notebook </a> for the detail implementataion of this project.
<br>
