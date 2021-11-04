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


<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/uo_1.png' />

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/uo_2.png' />

<img src='https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernels%20-%20Machine%20Learning/uo_3.png' />



</br>
</br>
<a id='Random_Forests'>Random Forests</a>





