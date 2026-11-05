import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("students_data.csv")
print(df.isnull().sum())
avg=df.groupby("Department")["Marks"].mean()
depcount=df["Department"].value_counts()
fig,ax=plt.subplots(2,2,figsize=(10,6))
ax[0,0].bar(avg.index, avg.values)
ax[0,0].set_title("Average Marks by Department")
ax[0,0].set_xlabel("Department")
ax[0,0].set_ylabel("Average Marks")
ax[0,1].hist(df["Marks"],bins=7,color="grey")
ax[0,1].set_title("Student Marks Distribution")
ax[0,1].set_xlabel("Marks")
ax[0,1].set_ylabel("Number Of Students")
ax[1,0].scatter(df["Marks"],df["Attendance"],
color="yellow",marker="s")
ax[1,0].set_title("Attendance vs Marks")
ax[1,0].set_xlabel("Attendance")
ax[1,0].set_ylabel("Marks")
ax[1,0].grid("True")
ax[1,1].pie(depcount,labels=depcount.index,
autopct="%1.1f%%",startangle=90)
ax[1,1].set_title("Students Distribution by Department")
plt.tight_layout()
plt.savefig("chart/student_performance_dashboard.png",
dpi=300, bbox_inches="tight")
plt.show()

