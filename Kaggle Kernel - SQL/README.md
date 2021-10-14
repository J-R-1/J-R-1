# <b>SQL and BigQuery</b> 


<b>SQL</b> is an important skill for any data scientist. The preceeding <b>Kaggle</b> kernels demonstrats accessing and examining <b>BigQuery</b> datasets using <b>SQL</b> through a series of Question and Answer format.


1. <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/exercise-getting-started-with-sql-and-bigquery%20(2).ipynb">Big query</a> - This kernel explains how to create a <b>client</b> object, accessing a dataset and it's tables using the <b>client</b> object, examining table schema and using Pandas <b>to_dataframe()</b> method to preview first few lines of the table. We will use <b>Chicago_crime</b> dataset for analysis.

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/BQ_1.png" />

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/BQ_2.png" />

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/BQ_3.png" />

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/BQ_4.png" />

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


2. <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/exercise-select-from-where.ipynb">Select-From-Where</a> - This kernel demonstrates using the keywords SELECT, FROM, and WHERE to get data from specific columns based on conditions we specify. we will use the global_air_quality table from the openaq dataset for analysis.

<b>Making a connection to the database:</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/sw_1.png" />


BigQuery datasets can be huge. It is a good practice to estimate the size of any query before running it. To see how much data a query will scan, we create a <b>QueryJobConfig</b> object and set the <b>dry_run</b> parameter to <b>True</b>. Alternatively we can specify a parameter when running the query to limit how much data we are willing to scan. The screenshot below shows that the query will be cancelled if it exceeds 10GB limit.

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/sw_2.png" />

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



3. <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/exercise-group-by-having-count.ipynb">GroupBy-Having-Count</a> - In this kernel we will use <b>comments</b> table from the <b>hacker_news</b> dataset to demonstrate the usage of <b>GROUP BY, HAVING and COUNT()</b> keywords. The queries will be cancelled if it exceeds 10GB limit.

<b>Making a connection to the database and the comments table:</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/GH_3.png" />

<b>Query 1: Selecting prolific commenters and their post counts</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/GH_1.png" />

<b>Query 2: Number of deleted comments</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/GH_2.png" />



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


4. <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/exercise-order-by.ipynb">OrderBy</a> - This kernel demonstrates how to change the order of query results using the <b>ORDER BY</b> clause. We will use <b>international_education</b> table from the <b>world_bank_intl_education</b> dataset.

<b>Making a connection to the database and the international_education table:</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/ob_1.png" />


<b>Query 1: Which country spent the largest fraction of GDP on education between the years 2010-2017</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/ob_2.png" />


<b>Query 2: For the year 2016, select the indicator code and indicator name for all codes with at least 175 rows</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/ob_3.png" />



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/exercise-as-with.ipynb"><b>AS-With:</b></a>

This kernel explains the usage of <b>Common Table Expression</b>.  A <b>Common Table Expression (or CTE)</b> is a temporary table that we return within our query. CTEs are helpful for splitting our queries into readable chunks, and we can write queries against them. We will use <b>taxi_trips</b> table from the <b>chicago_taxi_trips</b> dataset for analysis. As always we will limit our data usage to 10GB.

<b>Making a connection to the database:</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/aw_1.png" />


<b>let's take a peek at taxi_trips table</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/aw_2.png" />


<b>Query 1: Number of trips in each year</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/aw_3.png" />


<b>Query 2: For the year 2017, Number of trips per month</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/aw_4.png" />


<b>Query 3: Number of trips and Average speed for each Hour of the day between 2017-01-01 and 2017-07-01</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/aw_5.png" />

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/exercise-joining-data.ipynb"><b>Joining Data:</b></a>

This kernel demonstrates combining data sources using <b>Join</b> clauses which is critical for almost all real-world data problems. We will use stackoverflow dataset for analysis. 

<b>Making a connection to the database:</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/j_1.png" />


<b>Lets take a look at the relevent tables</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/j_3.png" />

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/j_4.png" />



<b>Query 1: Select the rows from the posts_questions table where the 'tags' column contains other text in addition to the word "bigquery" </b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/j_5.png" />



<b>Query 2: Returns the id, body and owner_user_id columns from the posts_answers table for answers to "bigquery"-related questions </b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/j_6.png" />



<b>Query 3: Returns a single row for each user who answered at least one question with a tag that includes the string "bigquery" </b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/j_7.png" />


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### <a href="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/exercise-joins-and-unions.ipynb"><b>Joins and Unions:</b></a>

This kernel is an extension of the previous kernel. Here, we will explore few more types of <b>JOIN</b>, along with how to use <b>UNIONs</b> to pull information from multiple tables. We will use the same <b>posts_questions</b> and <b>posts_answers</b> tables from the stackoverflow dataset for analysis.


<b>Query 1: How long does it take for questions to receive answers?. For simplicity we restrict the results only to January 2018. </b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/ju_1.png" />



<b>Query 2: Returns all users who created Stack Overflow accounts along with when did they post their first questions and answers. For simplicity we restrict the results only to  January 2019. We'll also need to use the 'users' table from the Stack Overflow dataset to answer this query </b>.

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/ju_2.png" />



<b>Query 3: Returns a single row for each user who answered at least one question with a tag that includes the string "bigquery" </b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Kaggle%20Kernel%20-%20SQL/j_7.png" />




---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


<a href="https://www.kaggle.com/jkuser/exercise-analytic-functions?scriptVersionId=76688181">Analytic functions</a>


<a href="https://www.kaggle.com/jkuser/exercise-nested-and-repeated-data?scriptVersionId=76788370">Nested and Repeated data</a>


<a href="https://www.kaggle.com/jkuser/exercise-writing-efficient-queries?scriptVersionId=76832920">Efficient queries</a>




