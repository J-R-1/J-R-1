# **Machine Learning**


<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/ml_pic.png" align='left' />
<b>Machine Learning</b> is undeniably one of the most influential and powerful technologies in today’s world. It is a tool for turning information into knowledge. Machine learning techniques are used to automatically find the valuable underlying patterns within complex data that we would otherwise struggle to discover. The hidden patterns and knowledge about a problem can be used to predict future events and perform all kinds of complex decision making.

<br>
<br>
<br>
The following is a series of <b>Kaggle Kernels</b> that demonstrates how to apply advanced Data Preprocessing and Model Validation techniques to improve the quality of the Machine learning models to building <b>state-of-the-art</b> models that are widely used to win Kaggle competitions (<b>XGBoost</b>).
<br>
<br>
<ol>
  
  <li><a href='#First_ML_Model'>Building a Machine Learning Model</a></li>
  <li><a href='#Model_validation'>Model Validation</a></li>
  <li><a href='#Underfitting_Overfitting'>Underfitting - Overfitting</a></li>
  <li><a href='#Random_Forests'>Random Forests</a></li>
  <li><a href='#Missing_Values'>Missing Values</a></li>
  <li><a href='#Categorical_Variables'>Categorical Variables</a></li>
  <li><a href='#Pipelines'>Pipelines</a></li>
  <li><a href='#Cross_Validation'>Cross-Validation</a></li>
  <li><a href='#XGBoost'>XGBoost</a></li>
  <li><a href='#Data_Leakage'>Data Leakage</a></li>
  
</ol >

### <a id='First_ML_Model'>Building a Machine Learning Model:</a>
-----------------------------------------------------------------


<a href='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/exercise-your-first-machine-learning-model.ipynb'>This Kernel</a> demonstrates the basics of building a machine learning model and make predictions using it.  We will use <b>DecisionTreeRegressor</b> from the <b>scikit-learn</b> library to create our model. Many machine learning models allow some randomness in model training. Specifying a number for random_state ensures we get the same results in each run. We will work with the dataset which has home prices in <b>Iowa</b>.
<br>
<br>
Read the data using <b>Pandas read_csv()</b> method and store data in dataFrame named <b>'home_data'</b>:
  
<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/mb_3.png' />
  
  
Specifing the model:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/mb_1.png' />        


Making Prediction using our model:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/mb_2.png' />


### <a id='Model_validation'>Model Validation:</a>
---------------------------------------------------

In this <a href='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/exercise-model-validation.ipynb'>Kernel</a>, we use <b>model validation</b> to measure the quality of our model. Measuring model quality is the key to iteratively improving our models.  In most (though not all) applications, the relevant measure of model quality is <b>predictive accuracy</b>.

We will use <b>train_test_split</b> function from the <b>scikit-learn</b> library to break up the data into two pieces. We'll use some of that data as <b>training data</b> to fit the model, and we'll use the other data as <b>validation data</b> to calculate <b>'Mean_Absolute_Error'</b> which is our metric for measuring model quality.


Splitting the dataset into <b>train and validation</b> data:
<br>
<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/mv_1.png' />
<br>

Fitting the model:
<br>
<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/mv_2.png' />
<br>

Prediction using <b>validation</b> data:
<br>
<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/mv_3.png' />
<br>

Calculating <b>'Mean_Absolute_Error'</b> on the validation data:
<br>
<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/mv_4.png' />
<br>


### <a id='Underfitting_Overfitting'>Underfitting - Overfitting</a>
-------------------------------------------------------------------

<b>Overfitting</b> -  Where a model matches the training data almost perfectly, but does poorly in validation and other new data.

<b>Underfitting</b> - When a model fails to capture important distinctions and patterns in the data, so it performs poorly even in training data.
<br>

Since we are using <b>DecisionTreeRegressor</b> to <b>fit</b> our model, <b>max_leaf_nodes</b> argument provides a very sensible way to control Overfitting vs Underfitting by controlling the <b>tree depth</b>. <a href='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/exercise-underfitting-and-overfitting.ipynb'>This Kernel</a> demonstrates how we can compare the accuracy of models (using <b>MAE scores</b>) built with different values for <b>max_leaf_nodes</b>.


Creating a function to compare MAE scores from different values for max_leaf_nodes:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/uo_1.png' />


Selecting the <b>max_leaf_node</b> with the <b>least</b> MAE score:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/uo_2.png' />

Here, the optimal value for the <b>Best tree size is 100</b>.
<br>

Using the Best tree size, fitting the model with all data:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/uo_3.png' />



### <a id='Random_Forests'>Random Forests</a>
----------------------------------------------

The <b>Random forest</b> uses many <b>Decision trees</b>, and it makes a prediction by averaging the predictions of each component tree. It generally has much better predictive accuracy than a single decision tree and it works well with default parameters.

To build a <b>Random forest</b> model, we will use <b>RandomForestRegressor</b> class from the <b>scikit-learn</b> library.


<b>Validation MAE</b> when using <b>Decision Tree</b> model:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/rf_1.png' />


<b>Validation MAE</b> when using <b>Random Forest</b> model:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/rf_2.png' />



### <a id='Missing_Values'>Missing Values</a>
-----------------------------------------------------------------

<a href='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/exercise-missing-values.ipynb'>This Kernel</a> demonstrates how to deal with <b>Missing Values</b> using <b>SimpleImputer</b> class from <b>sklearn</b> library. The <b>SimpleImputer</b> class provides basic strategies for imputing missing values. Missing values can be imputed with a provided <b>constant</b> value, or using the statistics (<b>mean, median or most frequent</b>) of each column in which the missing values are located.


Number of <b>Missing Values</b> in the <b>training</b> dataset:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/miss_val_1.png' />


<b>Imputing</b> missing values with the <b>mean</b> value along each column of training and validation datasets: 

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/miss_val_2.png' />

Train and Evaluate a <b>Random Forest</b> model using Imputed datasets:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/miss_val_3.png' />




### <a id='Categorical_Variables'>Categorical Variables</a>
-----------------------------------------------------------------




### <a id='Pipelines'>Pipelines</a>
-----------------------------------------------------------------




### <a id='Cross_Validation'>Cross-Validation</a>
-----------------------------------------------------------------




### <a id='XGBoost'>XGBoost</a>
-----------------------------------------------------------------



### <a id='Data_Leakage'>Data Leakage</a>
-----------------------------------------------------------------







