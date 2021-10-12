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



<a href="https://www.kaggle.com/jkuser/exercise-group-by-having-count?scriptVersionId=76418667">GroupBy-Having-Count</a>


<a href="https://www.kaggle.com/jkuser/exercise-order-by?scriptVersionId=76478437">OrderBy</a>


<a href="https://www.kaggle.com/jkuser/exercise-as-with?scriptVersionId=76482980">AS-With</a>

<a href="https://www.kaggle.com/jkuser/exercise-joining-data?scriptVersionId=76576312">Joining Data</a>


<a href="https://www.kaggle.com/jkuser/exercise-joins-and-unions?scriptVersionId=76850549">Joins and Unions</a>


<a href="https://www.kaggle.com/jkuser/exercise-analytic-functions?scriptVersionId=76688181">Analytic functions</a>


<a href="https://www.kaggle.com/jkuser/exercise-nested-and-repeated-data?scriptVersionId=76788370">Nested and Repeated data</a>


<a href="https://www.kaggle.com/jkuser/exercise-writing-efficient-queries?scriptVersionId=76832920">Efficient queries</a>




