import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------------------------------------------------------------
df=pd.read_csv('Students.csv')
print("-----------------------------------------------------------------------")
print(df.head())
#----------------------------------------------------------------------------------------------------------------------------------


df['Total Marks']=df[['Math','Science','English','History','Computer']].sum(axis=1)
df['Average']=df[['Math','Science','English','History','Computer']].mean(axis=1)
print("----------------------------------Updated-------------------------------")
print(df.head(11))
#----------------------------------------------------------------------------------------------------------------------------------

print("-----------------------------------------------------------------------")
print("Min marks : ",np.min(df[['Math','Science','English','History','Computer']].sum(axis=1)))
print("Max marks : ",np.max(df[['Math','Science','English','History','Computer']].sum(axis=1)))
print("Average marks : ",np.mean(df[['Math','Science','English','History','Computer']].sum(axis=1)))
print("Standard Deviation marks : ",np.std(df[['Math','Science','English','History','Computer']].sum(axis=1)))
print("-----------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------------------

top_3=df.sort_values(by='Average',ascending=False).head(3)
print(top_3)
print("-----------------------------------------------------------------------")
high_avg=df[['Math','Science','English','History','Computer']].mean()
high_avg_sub=high_avg.idxmax()
print("HIgh AVerage in Subject : " ,high_avg_sub)
print("-----------------------------------------------------------------------")
print("Average in all Subjects  ")
print(high_avg)
print("-----------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------------------


students=df['Name'].to_numpy()
total_marks=df['Total Marks'].to_numpy()
subjects = ['Math', 'Science', 'English', 'History', 'Computer']
subject_avgs = df[subjects].mean()
marks=df['Math'].to_numpy()
#--------------------------
# 
# --------------------------------------------------------------------------------------------------------


fig, ax = plt.subplots(2, 2, figsize=(12,8))
#----------------------------------------------------------------------------------------------------------------------------------


ax[0,0].bar(students,total_marks,color='orange',label='Students Marks')
ax[0,0].set_title("Total Marks")
ax[0,0].legend()
ax[0,0].grid()
#----------------------------------------------------------------------------------------------------------------------------------


for i, row in top_3.iterrows():
    ax[0,1].plot(subjects, row[subjects], marker='o', label=row['Name'])
ax[0,1].set_title("Scores of Top 3 Students")
ax[0,1].legend()
ax[0,1].grid()
#----------------------------------------------------------------------------------------------------------------------------------


ax[1,0].pie(subject_avgs, labels=subjects, autopct='%1.1f%%',colors=['red','yellow','skyblue','orange','green'])
ax[1,0].set_title("Average per Subject")
#----------------------------------------------------------------------------------------------------------------------------------


ax[1,1].hist(marks, bins=5, color='pink', edgecolor='black')
ax[1,1].set_xlabel('Scores Range')
ax[1,1].set_ylabel('Number of Students')
ax[1,1].set_title('Math Score Distribution')
#----------------------------------------------------------------------------------------------------------------------------------
plt.tight_layout()
plt.show()
#----------------------------------------------------------------------------------------------------------------------------------

df.to_csv('Output.csv')





















