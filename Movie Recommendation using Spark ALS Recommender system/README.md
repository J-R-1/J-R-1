
# Movie Recommendation using Spark ALS Recommender system
<img src="https://media.giphy.com/media/2eKtgBTca0l4atcsPI/giphy.gif?cid=790b76111152f32a380d5cd59abdd73471f8a3f78e9ecaaf&rid=giphy.gif&ct=g" />

One of the most common uses of big data is to predict what users want. This allows Google to show you relevant ads, Amazon to recommend relevant products, and Netflix to recommend movies that you might like. This <b>project</b> will demonstrate how we can use <b>Apache Spark</b> to recommend movies to a user. We will start with somec basic EDA on the  datasets and recommendation techniques, and then use the <b>Spark ML</b> library's <b>Alternating Least Squares</b> method to make more sophisticated predictions.

The two widely used approaches for building a Recommender system are the <b>content-based filtering (CBF)</b> and <b>collaborative filtering (CF)</b>.

To understand the concept of recommender systems, let us look at an example. The below table shows the user-item utility matrix Y where the value Rui denotes how item i has been rated by user u on a scale of 1–5. The missing entries (shown by ? in Table) are the items that have not been rated by the respective user.

![image](https://user-images.githubusercontent.com/66075772/133624553-0e0825e0-aed0-440c-bafc-83a0118e3648.png)


The objective of the recommender system is to predict the ratings for these items. Then the highest rated items can be recommended to the respective users. 

![image](https://user-images.githubusercontent.com/66075772/133628564-6f3792cd-6e17-47d7-bd33-2c55bbb80ffb.png)

### <b>Collaborative filtering (CF):</b>
----------------------------------------
<b>Collaborative filtering</b> is commonly used for recommender systems. These techniques aim to fill in the missing entries of a user-item association matrix. <b><i>spark.ml</i></b> currently supports model-based collaborative filtering, in which users and products are described by a small set of latent factors that can be used to predict missing entries. <b>spark.ml</b> uses the <b>Alternating Least Squares (ALS)</b> algorithm to learn these latent factors.

### <b>Recommendation using Alternating Least Squares (ALS):</b>
----------------------------------------------------------------
<b>Alternating Least Squares (ALS)</b> matrix factorisation attempts to estimate the ratings matrix R as the product of two lower-rank matrices, X and Y, i.e. X * Yt = R. Typically these approximations are called ‘factor’ matrices. The general approach is iterative. During each iteration, one of the factor matrices is held constant, while the other is solved for using least squares. The newly-solved factor matrix is then held constant while solving for the other factor matrix.

### <b>Explicit v.s. Implicit ratings:</b>
----------------------------------------

The standard approach to matrix factorization based collaborative filtering treats the entries in the user-item matrix as explicit preferences given by the user to the item, for example, users giving ratings to movies.
It is common in many real-world use cases to only have access to implicit feedback (e.g. views, clicks, purchases, likes, shares etc.). Essentially, instead of trying to model the matrix of ratings directly, this approach treats the data as numbers representing the strength in observations of user actions (such as the number of clicks, or the cumulative duration someone spent viewing a movie). Those numbers are then related to the level of confidence in observed user preferences, rather than explicit ratings given to items. The model then tries to find latent factors that can be used to predict the expected preference of a user for an item.

### <b>Cold-start strategy:</b>
--------------------------------
When making predictions using an <b>ALSModel</b>, it is common to encounter users and/or items in the test dataset that were not present during training the model. This typically occurs in two scenarios:

1. In production, for new users or items that have no rating history and on which the model has not been trained (this is the “cold start problem”).
2. During cross-validation, the data is split between training and evaluation sets. When using simple random splits as in Spark’s CrossValidator or TrainValidationSplit, it is      actually very common to encounter users and/or items in the evaluation set that are not in the training set.

By default, <b>Spark</b> assigns <b>NaN</b> predictions during <b><i>ALSModel.transform</i></b> when a user and/or item factor is not present in the model. This can be useful in a production system, since it indicates a new user or item, and so the system can make a decision on some fallback to use as the prediction.
However, this is undesirable during <b>cross-validation</b>, since any <b>NaN</b> predicted values will result in <b>NaN</b> results for the evaluation metric (for example when using RegressionEvaluator). This makes model selection impossible.

Spark allows users to set the <b>coldStartStrategy</b> parameter to <b>“drop”</b> in order to drop any rows in the <b>DataFrame of predictions</b> that contain <b>NaN</b> values. The evaluation metric will then be computed over the non-NaN data and will be valid.
