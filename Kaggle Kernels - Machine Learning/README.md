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


### <b>Data Source:</b>
-------------------------

We will work <a href='https://www.kaggle.com/c/home-data-for-ml-course'>Ames Housing dataset</a> from <b>Kaggle</b> for this project. The dataset has 79 explanatory variables describing (almost) every aspect of residential homes in <b>Ames, Iowa</b>. 


### <a id='First_ML_Model'>Building a Machine Learning Model:</a>
-----------------------------------------------------------------


<a href='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/exercise-your-first-machine-learning-model.ipynb'>This Kernel</a> demonstrates the basics of building a machine learning model and make predictions using it.  We will use <b>DecisionTreeRegressor</b> from the <b>scikit-learn</b> library to create our model. Many machine learning models allow some randomness in model training. Specifying a number for random_state ensures we get the same results in each run. 
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

To build a <b>Random forest</b> model, we will use <b>RandomForestRegressor</b> class from the <b>scikit-learn</b> library. <a href='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/exercise-random-forests.ipynb'>This Kernel</a> demonstrates how a <b>Random forest</b> model even without tuning can lead to better performance.


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

<a href='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/exercise-categorical-variables.ipynb'>This Kernel</a> demonstrates how to handle <b>Categorical Variables</b> using <b>Label encoding</b> and with <b>One-Hot encoding</b>.

<b>Label encoding</b>: Fitting a label encoder to a column in the training data creates a corresponding integer-valued label for each unique value that appears in the training data. In the case that the validation data contains values that don't appear in the training data, the encoder will throw an error, because these values won't have an integer assigned to them. There are many approaches to fixing this issue like writing a custom label encoder to deal with new categories but in this demonstration we will drop the problematic categorical columns.

Identifying the columns that can be safely label encoded:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/cv_1.png' />

Dropping problematic columns and applying label encoding to the rest:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/cv_2.png' />



<b>One-Hot encoding</b>: One-hot encoding creates new columns indicating the presence (or absence) of each possible value in the original column data. In contrast to ordinal encoding, one-hot encoding does not assume an ordering of the categories. One-hot encoding generally does not perform well if the categorical variable takes on a large number of values.

Investigating <b>cardinality</b> in each column with categorical data:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/cv_3.png' />


Selecting <b>low cardinality columns</b> to One-Hot encode:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/cv_4.png' />


Applying <b>one-hot</b> encoding to training and validation data:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/cv_5.png' />





### <a id='Pipelines'>Pipelines</a>
-----------------------------------------------------------------

<b>Pipelines</b> are a simple way to keep data preprocessing and modeling code organized. Specifically, a pipeline bundles preprocessing and modeling steps so we can use the whole bundle as if it were a single step. Pipelines offers some important benefits like Cleaner Code, Fewer Bugs, Easier to Productionize and More Options for Model Validation.

<a href='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/exercise-pipelines.ipynb'>This Kernel</a> demonstrates how to improve the efficiency of our machine learning code using <b>pipelines</b>.

Using <b>ColumnTransformer</b> class to bundle preprocessing for numerical and categorical data :

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/pipeline_1.png' />


Define a <b>Random Forest</b> model:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/pipeline_2.png' />


Train and Evaluate the model using <b>Pipeline</b>:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/pipeline_3.png' />




### <a id='Cross_Validation'>Cross-Validation</a>
-----------------------------------------------------------------

<a href='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/exercise-cross-validation.ipynb'>This Kernel</a> demonstrates how to use cross-validation to select <b>best</b> parameter(s) for a machine learning model. 

In this project, we will create a function that returns the average MAE over 3 CV folds of random forest model corresponding to eight different values of <b>n_estimators</b> parameter: 50, 100, 150, ..., 300, 350, 400. Our goal is to find the value of <b>n_estimators</b> parameter which returns the <b>lowest</b> average MAE.

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/cross_val_1.png' />


Calling the <b>get_score()</b> function for each value of the <b>n_estimators</b>:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/cross_val_2.png' />


Visualizing results using <b>matplotlib</b> library:

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/cross_val_3.png' />

From the above <b>plot</b>, we can clearly see that the value <b>200</b> for <b>n_estimators</b> parameter gets the <b>lowest</b> average MAE.




### <a id='XGBoost'>XGBoost</a>
-----------------------------------------------------------------

<b>XGBoost</b> stands for <b>extreme gradient boosting</b> which is an implementation of <b>gradient boosted decision trees</b> designed for Execution Speed and Model Performance. <a href='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/exercise-xgboost.ipynb'>This Kernel</a> demonstrates how to build and fit a model using XGBoost.

 The <b>XGBRegressor</b> class has many tunable parameters, but the few that dramatically affect accuracy and training speed are :
 
 <ol>
  <li><b>n_estimators</b></li> -  specifies how many times to go through the modeling cycle or in other words, number of models that we include in the ensemble.
  <li><b>learning_rate</b></li> - a small number that will be multiplied to the predictions from each model before adding them in.
  <li><b>n_jobs</b></li> - number of cores on a machine. When runtime is a consideration, we can use parallelism to build our models faster.
 </ol>
In general, a <b>small learning rate and large number of estimators</b> will yield more accurate XGBoost models, though it will also take the model longer to train since it does more iterations through the cycle. As default, XGBoost sets learning_rate=0.1.
<br>
<br>

<b>early_stopping_rounds</b>:


<b>early_stopping_rounds</b> offers a way to automatically find the ideal value for n_estimators. Early stopping causes the model to stop iterating when the validation score stops improving, even if we aren't at the hard stop for n_estimators. Since random chance sometimes causes a single round where validation scores don't improve, we need to specify a number for how many rounds of straight deterioration to allow before stopping.
It's smart to set a high value for n_estimators and then use early_stopping_rounds to find the optimal time to stop iterating. 

<b>eval_set</b>:

When using <b>early_stopping_rounds</b>, we need to set aside some data for calculating the validation scores - this is done by setting the <b>eval_set</b> parameter.


<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/xg.png' />
 


### <a id='Data_Leakage'>Data Leakage</a>
--------------------------------------------

The goal of <b>predictive modeling</b> is to develop a model that makes accurate predictions on new data, unseen during training. This is a hard problem.
It’s hard because we cannot evaluate the model on something we don’t have.
<br>
Therefore, we must estimate the performance of the model on unseen data by training it on only some of the data we have and evaluating it on the rest of the data.
This is the principle that underlies cross validation and more sophisticated techniques that try to reduce the variance in this estimate.

<b>Data leakage (or leakage)</b> happens when our training data contains information about the target, but similar data will not be available when the model is used for prediction. This leads to high performance on the training set (and possibly even the validation data), but the model will perform poorly in production.
<br>
Data leakage can cause us to create overly optimistic if not completely invalid predictive models.

There are two main types of leakage: <b>Target leakage</b> and <b>Train-Test contamination</b>.

<b>Target leakage</b>:

Target leakage occurs when our predictors include data that will not be available at the time we make predictions. It is important to think about target leakage in terms of the timing or chronological order that data becomes available, not merely whether a feature helps make good predictions.

<b>Train-Test Contamination</b>:

Train-Test contamination occurs when we did not distinguish training data from validation data. Validation is meant to be a measure of how a model does on data that it hasn't considered before. But, this process is corrupted if the validation data affects the preprocessing behavior.

<b>How to combat Data Leakage</b>:


<ol>
  <li><b>Temporal Cutoff</b>: Remove all data just prior to the event of interest, focusing on the time we learned about a fact or observation rather than the time the observation occurred.</li>
  <li><b>Add Noise</b>: Add random noise to input data to try and smooth out the effects of possibly leaking variables.</li>
  <li><b>Remove Leaky Variables</b>: If any variable is subject to data leakage, consider removing them. </li>
  <li><b>Use Pipelines</b>: Heavily use pipeline architectures that allow a sequence of data preparation steps to be performed within cross validation folds, such as the caret package in R and Pipelines in scikit-learn.</li>
  <li><b>Use a Holdout Dataset</b>: Hold back an unseen validation dataset as a final sanity check of our model.</li>
</ol>


<a href='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/exercise-data-leakage.ipynb'>This Kernel</a> talks about how to identify and prevent data leakage through a series of real world problems. Data Leakage is a hard and subtle issue. By combining <b>caution, common sense, and data exploration</b>  we can over come data leakage when developing predictive models and aviod multi-million dollar mistake in many data science applications.







