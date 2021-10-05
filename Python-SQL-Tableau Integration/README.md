# <b>Python - SQL - Tableau Integration </b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Integration_logo.png" />

### <b> Introduction: </b>  
--------------------------
  
In a business environment today, problems such as higher competitiveness, unachievable business goals, elevated risk of unemployment can increase an employees stress levels which in time will become detrimental to his/her's health. In this project we will address the Absenteeism at a company during normal working hours. Our goal is to explore whether an Employee presenting certain characteristics is expected to be away from work at some point of time or not. Having such an information in advance can improve an employer's decision making by reorganizing the work process which will increase the quality of work generated in a firm. 

This project focuses on <b>Python, SQL and Tableau Integration</b> as they are indespensible tools for many professionals. We will use Python for Data Preprocessing and Model Building, SQL for Quering and mending data and use Tableau for further analyses.

## <b>Python: </b>

#### <b>Data Preprocessing:</b> 
This <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism_Preprocessing.ipynb">Notebook</a> elaborates the preprocessing of raw <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism-data.csv">Absenteeism</a> file. The steps include removing redundant features, creating dummy variables and grouping them based on their feature similarities, extracting meaning features from the existing feature,etc.. The cleaned data then saved in another <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism_preprocessed_sql.csv">csv</a> file.

#### <b>Model Building:</b>
We will use <b>Logistic Regression</b> to predict the Absenteeism of an employee. This <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism_ML.ipynb">Notebook</a> elaborates the Model building steps and how Backward elimination method is used to simplify the model by removing some of the features(after examining their coefficiants) which have close to No contribution to the model. Finally the simplified Model and the Custom Scalar object which used to scale the features are <b>pickled</b> for later use.

#### <b>Absenteeism Module:</b>
The <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism_Module.py">Absenteeism Module</a> contains all of the above  preprocessing and machine learning steps in one clean <b>.py</b> file for reusability.

#### <b>Integration:</b>
In this section we will explore the <b>Integration</b> part of <b>Python</b> and <b>MySQL Workbench</b>. We will use our <b>Absenteeism Module</b> to make a prediction on a new dataset. Using Python's <b>'pymysql'</b> package we will make a connection to our database in MySQL workbench to store our model's predicted outputs.

Please refer <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism_%20Integration.ipynb">Absenteeism Integration Notebook</a> for implementation.

The new dataset for prediction can be found <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism_new_data.csv">here</a>

Model's predicted output can be found <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism_predictions.csv">here</a>


## <b>SQL</b>

Though there are multiple ways to connect <b>Python</b> to <b>SQL</b>. In this project we will use Python's <b>'pymysql'</b> package to connect our Jupyter notebook to MySQL workbench. By storing our data in a more secure place, makes it easier to manipulate and extract useful information from the data at a later stage.

Creating a database named 'predicted_outputs' and a table (same name as that of database) with column names and datatypes similar to that of our Model's predicted outputs dataset in MySQL workbench

<img src="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/MySQL_1.png" />


Using <b>pymysql</b>, making a connection to our database from Jupyter notebook

<img src="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/conn.jpg" />


Creating an <b>Insert</b> query to populate the 'predicted_outputs' table 

<img src="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/insert.png" />


<b>Execute</b> and <b>Commit</b> methods:

<img src="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/execute.png" />


Querying our 'predicted_outputs' table in MySql workbench

<img src="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/MySQL_2.png" />

Please refer <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism_%20Integration.ipynb">Absenteeism Integration Notebook</a> for elaborate implementation.


## <b>Tableau: </b>

In this section, we will analyse the Predictions made by our model based on 40 new observations using <b>Tableau</b>.

Loading the <b>absenteeism prediction</b> file on <b>Tableau</b>:

<img src="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/absenteeism_csv.png" />







