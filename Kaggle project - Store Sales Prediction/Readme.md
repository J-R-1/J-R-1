# <b>Time Series - Store Sales Prediction</b>
<br>

This <b>Kaggle</b> competition project is about <b>time-series</b> forecasting to forecast store sales on data from Corporación Favorita, a large Ecuadorian-based grocery retailer.


### <b>Data Source:</b>
<br>
The datasets used for this project can be found <a href="https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data">here</a>.
<br>
<ul>
  <li><b>train.csv:</b> The training data, comprising time series of features store_nbr, family, and onpromotion as well as the target sales.</li>
  <li><b>test.csv:</b> The test data, having the same features as the training data, we need to predict the target sales for the dates in this file.</li>
  <li><b>sample_submission.csv:</b> used for scoring submission.</li>
  <li><b>oil.csv:</b> Daily oil price. Includes values during both the train and test data timeframes.</li>
  <li><b>holidays_events.csv:</b> Holidays and Events, with metadata.</li>
 </ul>
 

### <b>The Notebook:</b>
<br>

This project focuses on the application of modern machine learning methods to time series data (2013/01/01 - 2017/08/15) with the goal of producing the most accurate predictions over a period of 16 days starting from '2017/08/16' using store sales data from Corporación Favorita, a large Ecuadorian-based grocery retailer. Please refer <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20project%20-%20Store%20Sales%20Prediction/time-series-store-sales-prediction.ipynb">this notebook</a> for a complete implementation of this project.
<br>

The Key elements to note in this Notebook are:
<br>

<ul>
  <li>Additional files like <b>oil.csv</b> and <b>holidays_events.csv</b>, provided valuable information like Daily oil price, 'National' and 'Regional' hoildays, etc.. which held some predictive power over store sales data provided in the training dataset.</li>
  <li><b>Fourier features</b> were used to model the major time series components like trends, seasons in the train and test data.  Cyclic behavior of a feature was captured by using <b>Lagged</b> values of that feature.</li>
  <li>A <b>Hybrid Model</b> which combined the strengths of two forecasters - <b>ElasticNet and RandomForestRegressor</b> was chosen for this project. ElasticNet (which is a popular type of regularized linear regression) was used to extrapolate the trend, transform the target to remove the trend, and RandomForestRegressor (one of few inherently Multioutput Regressior) was trained on the detrended residuals along with remaining features of the training data.</li> 
</ul>


### <b>Project Demo:</b>
<br>

<b>Detrended Sales after applying ElasticNet (Model_1):</b>
<br>

<img src="" />
<br>


<b>RandomForestRegressor (Model_2) Prediction on training data:</b>
<br>

<img src="" />


<b>Forecasting sales of a specific store and family:</b>
<br>

<img src="" />






