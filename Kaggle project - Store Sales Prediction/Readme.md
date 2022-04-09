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

  ### <b>The Notebook:</b>
  <br>
  
  The goal of this project is to apply modern machine learning methods to time series data to produce accurate predictions. The Key elements to note in this project are:
  <br>
  
  <ul>
    <li><b>Fourier features</b>were used to model the major time series components like trends, seasons in the train and test data. Cyclic behavior of a feature was captured by using <b>Lagged</b> values of that feature.</li>
  
