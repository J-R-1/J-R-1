
# Movie Recommendation using Spark ALS Recommender system
<img src="https://media.giphy.com/media/2eKtgBTca0l4atcsPI/giphy.gif?cid=790b76111152f32a380d5cd59abdd73471f8a3f78e9ecaaf&rid=giphy.gif&ct=g" />

A common task of recommender systems is to improve customer experience through personalized recommendations based on prior user feedback. This allows Google to show you relevant ads, Amazon to recommend relevant products, and Netflix to recommend movies that you might like. This <b>project</b> will demonstrate how we can use <b>Apache Spark</b> to recommend movies to a user. We will start with somec basic EDA on the datasets and recommendation techniques, and then use the <b>Spark ML</b> library's <b>Alternating Least Squares</b> method to make more sophisticated predictions.

### <b>Collaborative filtering and Alternating Least Squares(ALS) algorithm :</b>
---------------------------------------------------------------------------------
There are different methods for building a recommender system, such as, user-based, content-based, or collaborative filtering. This project employs <b>Collaborative filtering</b> for building a recommender system. <b>Collaborative filtering</b> is a technique that is commonly used for recommender systems. It employs a form of wisdom of the crowd approach to generate recommendations based on the preferences of users. For this reason, 

<b><i>spark.ml</i></b> supports an implementation of matrix factorization for collaborative filtering. Matrix factorization models have consistently shown to perform extremely well for collaborative filtering. The type of matrix factorization we will explore in this project is called explicit matrix factorization. In explicit matrix factorization, preferences provided by users themselves are utilized - as contrasted with implicit matrix factorization, where only implicit feedback (e.g. views, clicks, purchases, likes, shares etc.) is utilized. Collaborative filtering aims to fill in the missing entries of a user-item (in the case of movie recommendations, this consists of user and movie IDs) association matrix in which users (userID) and items (movieID) are described by a small set of latent factors that can be used to predict missing entries. <b><i>spark.ml</i></b> uses the <b>Alternating Least Squares (ALS)</b> algorithm to learn these latent factors for this matix factorization problem. ALS works by iteratively solving a series of least square regression problems to derive a model.

![image](https://user-images.githubusercontent.com/66075772/133675900-3d3e7058-9350-48fe-8f5a-aa5b6d2f774c.png)


### <b>Cold-start strategy:</b>
--------------------------------
When making predictions using an <b>ALSModel</b>, it is common to encounter users and/or items in the test dataset that were not present during training the model. This typically occurs in two scenarios:

1. In production, for new users or items that have no rating history and on which the model has not been trained (this is the “cold start problem”).
2. During cross-validation, the data is split between training and evaluation sets. When using simple random splits as in Spark’s CrossValidator or TrainValidationSplit, it is      actually very common to encounter users and/or items in the evaluation set that are not in the training set.

By default, <b>Spark</b> assigns <b>NaN</b> predictions during <b><i>ALSModel.transform</i></b> when a user and/or item factor is not present in the model. This can be useful in a production system, since it indicates a new user or item, and so the system can make a decision on some fallback to use as the prediction.
However, this is undesirable during <b>cross-validation</b>, since any <b>NaN</b> predicted values will result in <b>NaN</b> results for the evaluation metric (for example when using RegressionEvaluator). This makes model selection impossible.

Spark allows users to set the <b>coldStartStrategy</b> parameter to <b>“drop”</b> in order to drop any rows in the <b>DataFrame of predictions</b> that contain <b>NaN</b> values. The evaluation metric will then be computed over the non-NaN data and will be valid.

### <b> Dataset:</b>

This project uses <b>MovieLens 1M</b> dataset (https://grouplens.org/datasets/movielens/1m/). This dataset consists of more than 1 million ratings of approximately 4000 movies made by 6000 MovieLens users who joined MovieLens in 2000. <b>MovieLens</b> is a recommender system and virtual community website that recommends movies for its users to watch, based on their film preferences using collaborative filtering. This benchmark dataset was released February 2003.
This dataset consists of three files: Movies, Ratings and Users.

<b>Ratings File Description:</b>

All ratings are contained in the file "ratings.dat" and are in the
following format:

UserID::MovieID::Rating::Timestamp

![image](https://user-images.githubusercontent.com/66075772/133790133-8591e896-b412-4e6b-bba9-7524e8edf40d.png)

<b>Movies File Description:</b>

Movie information is in the file "movies.dat" and is in the following
format:

MovieID::Title::Genres

![image](https://user-images.githubusercontent.com/66075772/133790486-41c099c6-240c-407f-ab64-8fc9cf7e06c1.png)

<b>Users File Description:</b>

User information is in the file "users.dat" and is in the following
format:

UserID::Gender::Age::Occupation::Zip-code

![image](https://user-images.githubusercontent.com/66075772/133791342-960aa8ad-f732-4de7-a9ba-2d1b39c27ed3.png)

### <b>EDA on Movielens dataset:</b>
------------------------------------
In this section I tried to ask some questions that would give me more insight into the data at hand, and provide answers to those questions in the most simple and clear way.
Some of the sample questions are:

![image](https://user-images.githubusercontent.com/66075772/133797609-2a66f64c-a711-44fc-996c-956f1e5d34fb.png)

![image](https://user-images.githubusercontent.com/66075772/133797783-82d04c8d-ad23-421e-9699-76361fe045f2.png)

<b>Most Rated genres:</b>
![image](https://user-images.githubusercontent.com/66075772/133797925-d36afcc6-b833-4508-980f-1c640802f2aa.png)

<b>Top 10 Rated movies:</b>
![image](https://user-images.githubusercontent.com/66075772/133798120-d37c67ee-c155-4e90-adc1-b0fa0e7b80e6.png)

For more elaborate <b>EDA</b>, please refer to the notebook provided <a href="https://github.com/J-R-1/J-R-1/blob/main/Movie%20Recommendation%20using%20Spark%20ALS%20Recommender%20system/Movie_Recommendation_ALS.ipynb">here</a>. 

### <b>Basic Recommendation:</b>
--------------------------------

In this section, we recommend 20 movies with Highest Average ratings and has 500 or more reviews using Ratings and Movies dataframe.

![image](https://user-images.githubusercontent.com/66075772/133849374-68b6eea4-7364-4e3d-bab7-34b3c3dd05b0.png)

### <b>Build the recommender system using ALS:</b>
--------------------------------------------------
In this section, we use <b><i>SparkML ALS</i></b> algorithm to provide recommendations. The ratings dataset is split into 3 parts: training data(60%), validation data(20%), test data(20%). The model was trained on training data and the validation data is used to evaluate the performance of the model by using the <b>RegressionEvaluator</b> method. The <b>Spark CrossValidator</b> function was used to tune the performance of the model. The CrossValidator function performs a grid search on various parameters of the ALS model as well as k-fold cross validation. The validation data is again used to evaluate the <b>Best ALS model</b> obtained as a result of the CrossValidator function. Then the prediction was made against the test data.

![image](https://user-images.githubusercontent.com/66075772/133854866-95569936-bf83-44c5-a98b-9d21890d1e3d.png)


please refer to the <a href="https://github.com/J-R-1/J-R-1/blob/main/Movie%20Recommendation%20using%20Spark%20ALS%20Recommender%20system/Movie_Recommendation_ALS.ipynb">notebook</a> for in depth look on Model buliding and performance tuning. 

### <b>Recommendation for a prticular user:</b>
-----------------------------------------------

In order to make a recommendation for a particular user(e.g, UserId = 1500) we will apply our <b>Best ALS model</b> on the list of movies that user has not yet watched or rated.

<b>Recommendation for UserId = 1500:</b>

![image](https://user-images.githubusercontent.com/66075772/133939393-5b27b88c-2080-46a1-a940-ddf282e13626.png)

please refer to the <a href="https://github.com/J-R-1/J-R-1/blob/main/Movie%20Recommendation%20using%20Spark%20ALS%20Recommender%20system/Movie_Recommendation_ALS.ipynb">notebook</a> for elaborate application of the model.

### <b>Predictioin for Myself:</b>
--------------------------------------
This section is used to predict what movies to recommend for Myself. First, I assigned myself Id = 0 and chose 15 familiar movies (the final dataframe from the <b>Basic Recommendation</b> section was used to select the movies for simplicity!.) and gave my own ratings for those movies. I added this list of movies and its ratings to the orginal training data. Then a new <b>ALS</b> model was built using the parameters of the <b>Best ALS</b> model. This new model was used to train the modified training dataset. Finally the prediction was made on the list of movies that I've not watched or rated.

Predicted movies for myself with highest Average ratings and 500 or more reviews:

![image](https://user-images.githubusercontent.com/66075772/133940794-abf2fbf7-5b54-430b-a4bd-2134f9476698.png)

please refer to the <a href="https://github.com/J-R-1/J-R-1/blob/main/Movie%20Recommendation%20using%20Spark%20ALS%20Recommender%20system/Movie_Recommendation_ALS.ipynb">notebook</a> for model building and implementation.










  
