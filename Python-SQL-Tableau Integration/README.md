# <b>Python - SQL - Tableau Integration</b>

<img src="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Integration_logo.png" />

### <b> Introduction: </b>  
--------------------------
  
In a business environment today, problems such as higher competitiveness, unachievable business goals, elevated risk of unemployment can increase an employees stress levels which in time will become detrimental to his/her's health. In this project we will address the Absenteeism at a company during normal working hours. Our goal is to explore whether an Employee presenting certain characteristics is expected to be away from work at some point of time or not. Having such an information in advance can improve an employer's decision making by reorganizing the work process which will increase the quality of work generated in a firm. 

This project focuses on <b>Python, SQL and Tableau Integration</b> as they are indespensible tools for many professionals. We will use Python for Data Preprocessing and Model Building, SQL for Quering and mending data and use Tableau for further analyses.

### <b>Python:</b>
------------------

#### <b>Data Preprocessing:</b> 
This <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism_Preprocessing.ipynb">Notebook</a> elaborates the preprocessing of raw <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism-data.csv">Absenteeism</a> file. The steps include removing redundant features, creating dummy variables and grouping them based on their feature similarities, extracting meaning features from the existing feature,etc.. The cleaned data then saved in another <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism_preprocessed_sql.csv">csv</a> file.

#### <b>Model Building:</b>
We will use <b>Logistic Regression</b> to predict the Absenteeism of an employee. This <a href="https://github.com/J-R-1/J-R-1/blob/main/Python-SQL-Tableau%20Integration/Absenteeism_ML.ipynb">Notebook</a> elaborates the Model building steps and how Backward elimination method is used to simplify the model by removing some of the features(after examining their coefficiants) which have close to No contribution to the model. Finally the simplified Model and the Custom Scalar object which used to scale the features are <b>pickled</b> for later use.

#### <b>Absenteeism Module:</b>
Here, the 




