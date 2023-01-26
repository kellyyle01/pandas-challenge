#!/usr/bin/env python
# coding: utf-8

# In[71]:


# dependecies and set up
import pandas as pd

# load files
schools_complete = "schools_complete.csv"
students_complete = "students_complete.csv"

# Read School and Student Data File and store into Pandas DataFrames
school_data= pd.read_csv(schools_complete)
student_data= pd.read_csv(students_complete)

# Combine the data into a single dataset.
school_data_completed = pd.merge(student_data, school_data, on = "school_name", how="outer")
school_data_completed.head()




# In[90]:


# total number of unique schools

school_count= len(school_data["school_name"].unique())
print(school_count)


# In[125]:


# total students
total_students= len(school_data_completed["student_name"].sum())
print(total_students)


# In[96]:


# total budget
total_budget = school_data_completed["budget"].sum()
print(total_budget)


# In[101]:


# average math score
Average_math_score = school_data_completed["math_score"].mean()
print(Average_math_score)


# In[102]:


# average reading score
Average_reading_score = school_data_completed["reading_score"].mean()
print(Average_reading_score)


# In[179]:


# % passing math with 70% (the percentage of students who passed math)
passing_math = school_data_completed[school_data_completed["math_score"] >= 70]
passing_math


# In[181]:


# % passing reading (the percentage of students who passed reading)
passing_reading = school_data_completed[school_data_completed["reading_score"] >= 70]
                                     
school_data_completed


# In[158]:


# % passing math & reading with 70% (the percentage of students who passed math & reading)
passing_math_and_reading = school_data_completed[school_data_completed["reading_score"] >= 70] & [school_data_completed["math_score"] >= 70]
# 

print (passing_math_and_reading)


# In[159]:


School Summary


# In[190]:


# Importing Pandas to create DataFrame
import pandas as pd

# Initialize data to lists.

# Creating Empty DataFrame and Storing it in variable df
new_df = pd.DataFrame()

# Printing Empty DataFrame
new_df


# In[ ]:





# In[ ]:





# In[ ]:




