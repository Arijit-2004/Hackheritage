# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EgEykpC5u1aIHOAIU4SY89anpXl2I39N
"""

from google.colab import drive
drive.mount("content/drive")

from google.colab import drive
drive.mount("/content/drive",force_remount=True)

import pandas as pd
df = pd.read_csv("/content/draft1.csv")
median_values = df.median()
df_filled = df.fillna(median_values)

from pandas.io.formats.excel import ExcelFormatter
df1=df_filled.to_excel('output_file.xlsx', index=False)

df1

print(df1)

import scipy.stats as stats

# Sample data for two groups (replace with your actual data)
group1 = [0.21,  0.5, 0, 0.7,0.6,0,1.9,0.9,0,0]
group2 = [1.35, 1.06, 0,0,0,2.6,1,0,0]

# Perform an independent samples t-test
t_stat, p_value = stats.ttest_ind(group1, group2)

# Print the results
print("t-statistic:", t_stat)
print("p-value:", p_value)

# Determine significance
alpha = 0.00  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the groups.")

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Sample data for two groups (replace with your data)
group1 = [0.21,  0.5, 0, 0.7,0.6,0,1.9,0.9,0,0]
group2 = [1.35, 1.06, 0,0,0,2.6,1,0,0]

# Calculate the means and standard errors of the means
mean1 = np.mean(group1)
sem1 = stats.sem(group1)
mean2 = np.mean(group2)
sem2 = stats.sem(group2)

# Calculate the 95% confidence intervals
ci1 = stats.t.interval(0.95, len(group1) - 1, loc=mean1, scale=sem1)
ci2 = stats.t.interval(0.95, len(group2) - 1, loc=mean2, scale=sem2)

# Create a bar chart with confidence intervals
labels = ['Group 1', 'Group 2']
means = [mean1, mean2]
cis = [ci1, ci2]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x, means, width, label='Mean')
ax.errorbar(x, means, yerr=np.array(cis).T, fmt='none', color='black', capsize=5)

ax.set_ylabel('Values')
ax.set_title('Comparison of Means with 95% Confidence Intervals')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()

import matplotlib.pyplot as plt

# Sample data for two groups (replace with your data)
group1 = [0.21,  0.5, 0, 0.7,0.6,0,1.9,0.9,0,0]
group2 = [1.35, 1.06, 0,0,0,2.6,1,0,0]

# Create histograms for each group
plt.hist(group1, alpha=0.5, label='Group 1', bins=10)
plt.hist(group2, alpha=0.5, label='Group 2', bins=10)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histograms of Two Groups')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

group1 = [0.21,
0.5,
0,
0.7,
0.6,
0,
1.9,
0.9,
0,
0]
group2 = [1.35,
1.06,
0,
0.7,
0.9,
0,
2.6,
1,
0,
0,]

# Calculate the means and standard errors of the means
mean1 = np.mean(group1)
sem1 = stats.sem(group1)
mean2 = np.mean(group2)
sem2 = stats.sem(group2)

# Calculate the 95% confidence intervals
ci1 = stats.t.interval(0.05, len(group1) - 1, loc=mean1, scale=sem1)
ci2 = stats.t.interval(0.05, len(group2) - 1, loc=mean2, scale=sem2)

# Create time points (e.g., assuming measurements were taken at different time periods)
time_points = ['01-01-2012',
'01-01-2013',
'01-01-2014',
'01-01-2015',
'01-01-2016',
'01-01-2017',
'01-01-2018',
'01-01-2019',
'01-01-2020',
'01-01-2021']

# Create a line graph with confidence intervals
plt.figure(figsize=(8, 6))
plt.errorbar(time_points, group1, yerr=[sem1], fmt='-o', label='Means with 95% CI for Boys')
plt.xlabel('Time Period')
plt.ylabel('Values')
plt.title('Line Graph of Means with 95% Confidence Intervals')
plt.legend()
plt.grid(True)
plt.show()

print(len(group1))
print(len(group2))

len(time_points)

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

group1 = [0.21,
0.5,
0,
0.7,
0.6,
0,
1.9,
0.9,
0,
0]
group2 = [1.35,
1.06,
0,
0.7,
0.9,
0,
2.6,
1,
0,
0,]

# Calculate the means and standard errors of the means
mean1 = np.mean(group1)
sem1 = stats.sem(group1)
mean2 = np.mean(group2)
sem2 = stats.sem(group2)

# Calculate the 95% confidence intervals
ci1 = stats.t.interval(0.05, len(group1) - 1, loc=mean1, scale=sem1)
ci2 = stats.t.interval(0.05, len(group2) - 1, loc=mean2, scale=sem2)

# Create time points (e.g., assuming measurements were taken at different time periods)
time_points = ['01-01-2012',
'01-01-2013',
'01-01-2014',
'01-01-2015',
'01-01-2016',
'01-01-2017',
'01-01-2018',
'01-01-2019',
'01-01-2020',
'01-01-2021']

# Create a line graph with confidence intervals
plt.figure(figsize=(8, 6))
plt.errorbar(time_points, [group1, group2], yerr=[sem1, sem2], fmt='-o', label='Means with 95% CI')
plt.xlabel('Time Period')
plt.ylabel('Values')
plt.title('Line Graph of Means with 95% Confidence Intervals')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

group1 = [0.21,
0.5,
0,
0.7,
0.6,
0,
1.9,
0.9,
0,
0]
group2 = [1.35,
1.06,
0,
0.7,
0.9,
0,
2.6,
1,
0,
0,]

# Calculate the means and standard errors of the means
mean1 = np.mean(group1)
sem1 = stats.sem(group1)
mean2 = np.mean(group2)
sem2 = stats.sem(group2)

# Calculate the 95% confidence intervals
ci1 = stats.t.interval(0.05, len(group1) - 1, loc=mean1, scale=sem1)
ci2 = stats.t.interval(0.05, len(group2) - 1, loc=mean2, scale=sem2)

# Create time points (e.g., assuming measurements were taken at different time periods)
time_points = ['01-01-2012',
'01-01-2013',
'01-01-2014',
'01-01-2015',
'01-01-2016',
'01-01-2017',
'01-01-2018',
'01-01-2019',
'01-01-2020',
'01-01-2021']

# Create a line graph with confidence intervals
plt.figure(figsize=(8, 6))
plt.errorbar(time_points, group2, yerr=[sem1], fmt='-o', label='Means with 95% CI for girls',color ="green" )
plt.xlabel('Time Period')
plt.ylabel('Values')
plt.title('Line Graph of Means with 95% Confidence Intervals')
plt.legend()
plt.grid(True)
plt.show()

pip install Pillow

from PIL import Image

# Load the two images
image1 = Image.open('/content/guj-boys1.png')
image2 = Image.open('/content/guj-girls1.png')

# Get the dimensions of the first image
width1, height1 = image1.size

# Get the dimensions of the second image
width2, height2 = image2.size

# Determine the dimensions of the combined image
new_width = max(width1, width2)
new_height = height1 + height2

# Create a new blank image with the determined dimensions
combined_image = Image.new('RGB', (new_width, new_height))

# Paste the first image at the top
combined_image.paste(image1, (0, 0))

# Paste the second image below the first one
combined_image.paste(image2, (0, height1))

# Save the combined image
combined_image.save('combined_image.png')

# Optionally, display the combined image
combined_image.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

group1 = [2.75,
3.52,
0,
0.1,
0,
0,
9.1,
7.2,
0,
4.2]
group2 = [8.19,
8.04,
3.1,
0,
0,
0,
5.9,
3.5,
3.1,
5.8,]

# Calculate the means and standard errors of the means
mean1 = np.mean(group1)
sem1 = stats.sem(group1)
mean2 = np.mean(group2)
sem2 = stats.sem(group2)

# Calculate the 95% confidence intervals
ci1 = stats.t.interval(0.05, len(group1) - 1, loc=mean1, scale=sem1)
ci2 = stats.t.interval(0.05, len(group2) - 1, loc=mean2, scale=sem2)

# Create time points (e.g., assuming measurements were taken at different time periods)
time_points = ['01-01-2012',
'01-01-2013',
'01-01-2014',
'01-01-2015',
'01-01-2016',
'01-01-2017',
'01-01-2018',
'01-01-2019',
'01-01-2020',
'01-01-2021']

# Create a line graph with confidence intervals
plt.figure(figsize=(8, 6))
plt.errorbar(time_points, group2, yerr=[sem1], fmt='-o', label='Means with 95% CI for girls',color ="green" )
plt.xlabel('Time Period')
plt.ylabel('Values')
plt.title('Line Graph of Means with 95% Confidence Intervals')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

group1 = [2.75,
3.52,
0,
0.1,
0,
0,
9.1,
7.2,
0,
4.2]
group2 = [8.19,
8.04,
3.1,
0,
0,
0,
5.9,
3.5,
3.1,
5.8,]

# Calculate the means and standard errors of the means
mean1 = np.mean(group1)
sem1 = stats.sem(group1)
mean2 = np.mean(group2)
sem2 = stats.sem(group2)

# Calculate the 95% confidence intervals
ci1 = stats.t.interval(0.05, len(group1) - 1, loc=mean1, scale=sem1)
ci2 = stats.t.interval(0.05, len(group2) - 1, loc=mean2, scale=sem2)

# Create time points (e.g., assuming measurements were taken at different time periods)
time_points = ['01-01-2012',
'01-01-2013',
'01-01-2014',
'01-01-2015',
'01-01-2016',
'01-01-2017',
'01-01-2018',
'01-01-2019',
'01-01-2020',
'01-01-2021']

# Create a line graph with confidence intervals
plt.figure(figsize=(8, 6))
plt.errorbar(time_points, group1, yerr=[sem1], fmt='-o', label='Means with 95% CI for Boys',color ="blue" )
plt.xlabel('Time Period')
plt.ylabel('Values')
plt.title('Line Graph of Means with 95% Confidence Intervals')
plt.legend()
plt.grid(True)
plt.show()

from PIL import Image

# Load the two images
image1 = Image.open('/content/guj-boys2.png')
image2 = Image.open('/content/guj-girls2.png')

# Get the dimensions of the first image
width1, height1 = image1.size

# Get the dimensions of the second image
width2, height2 = image2.size

# Determine the dimensions of the combined image
new_width = max(width1, width2)
new_height = height1 + height2

# Create a new blank image with the determined dimensions
combined_image = Image.new('RGB', (new_width, new_height))

# Paste the first image at the top
combined_image.paste(image1, (0, 0))

# Paste the second image below the first one
combined_image.paste(image2, (0, height1))

# Save the combined image
combined_image.save('upper_primary.png')

# Optionally, display the combined image
combined_image.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

group1 = [13.96,
22.85,
13.7,
8.6,
8.1,
4,
21.2,
20.7,
13.7,
19.4]
group2 = [12.95,
19.81,
9,
11.4,
15.4,
10.2,
25.8,
26,
9,
15.9]

# Calculate the means and standard errors of the means
mean1 = np.mean(group1)
sem1 = stats.sem(group1)
mean2 = np.mean(group2)
sem2 = stats.sem(group2)

# Calculate the 95% confidence intervals
ci1 = stats.t.interval(0.05, len(group1) - 1, loc=mean1, scale=sem1)
ci2 = stats.t.interval(0.05, len(group2) - 1, loc=mean2, scale=sem2)

# Create time points (e.g., assuming measurements were taken at different time periods)
time_points = ['01-01-2012',
'01-01-2013',
'01-01-2014',
'01-01-2015',
'01-01-2016',
'01-01-2017',
'01-01-2018',
'01-01-2019',
'01-01-2020',
'01-01-2021']

# Create a line graph with confidence intervals
plt.figure(figsize=(8, 6))
plt.errorbar(time_points, group1, yerr=[sem1], fmt='-o', label='Means with 95% CI for Boys',color ="blue" )
plt.xlabel('Time Period')
plt.ylabel('Values')
plt.title('Line Graph of Means with 95% Confidence Intervals')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

group1 = [13.96,
22.85,
13.7,
8.6,
8.1,
4,
21.2,
20.7,
13.7,
19.4]
group2 = [12.95,
19.81,
9,
11.4,
15.4,
10.2,
25.8,
26,
9,
15.9]

# Calculate the means and standard errors of the means
mean1 = np.mean(group1)
sem1 = stats.sem(group1)
mean2 = np.mean(group2)
sem2 = stats.sem(group2)

# Calculate the 95% confidence intervals
ci1 = stats.t.interval(0.05, len(group1) - 1, loc=mean1, scale=sem1)
ci2 = stats.t.interval(0.05, len(group2) - 1, loc=mean2, scale=sem2)

# Create time points (e.g., assuming measurements were taken at different time periods)
time_points = ['01-01-2012',
'01-01-2013',
'01-01-2014',
'01-01-2015',
'01-01-2016',
'01-01-2017',
'01-01-2018',
'01-01-2019',
'01-01-2020',
'01-01-2021']

# Create a line graph with confidence intervals
plt.figure(figsize=(8, 6))
plt.errorbar(time_points, group2, yerr=[sem1], fmt='-o', label='Means with 95% CI for Girls',color ="green" )
plt.xlabel('Time Period')
plt.ylabel('Values')
plt.title('Line Graph of Means with 95% Confidence Intervals')
plt.legend()
plt.grid(True)
plt.show()

from PIL import Image

# Load the two images
image1 = Image.open('/content/guj-boys3.png')
image2 = Image.open('/content/guj-girls3.png')

# Get the dimensions of the first image
width1, height1 = image1.size

# Get the dimensions of the second image
width2, height2 = image2.size

# Determine the dimensions of the combined image
new_width = max(width1, width2)
new_height = height1 + height2

# Create a new blank image with the determined dimensions
combined_image = Image.new('RGB', (new_width, new_height))

# Paste the first image at the top
combined_image.paste(image1, (0, 0))

# Paste the second image below the first one
combined_image.paste(image2, (0, height1))

# Save the combined image
combined_image.save('secondary.png')

# Optionally, display the combined image
combined_image.show()

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load your dataset from a CSV file
data = pd.read_csv('/content/m_f.csv')  # Replace 'your_dataset.csv' with your CSV file

# Assuming your dataset columns are named 'CLASS', 'Male', 'Female', and 'TotalDropouts'
X = data[['CLASS', 'Male', 'Female']]
y = data['Total']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model to a pickle file
with open('dropout_prediction_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

# Load the trained model from the pickle file
with open('dropout_prediction_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Take user input for new data
user_class = int(input("Enter Class (1-12): "))
user_male = int(input("Enter the number of Male students: "))
user_female = int(input("Enter the number of Female students: "))

# Create a DataFrame with user input
new_data = pd.DataFrame({'CLASS': [user_class], 'Male': [user_male], 'Female': [user_female]})
predicted_dropouts = model.predict(new_data)

print("Predicted Total Dropouts:", predicted_dropouts[0])

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt

# Specify the Matplotlib backend (use 'inline' for Jupyter Notebook)
# %matplotlib inline
# Create a bar chart to visualize predicted dropout rates
plt.figure(figsize=(10, 6))
plt.bar(new_data['CLASS'], predicted_dropouts, color='skyblue')
plt.xlabel('Class')
plt.ylabel('Predicted Total Dropouts')
plt.title('Predicted Total Dropouts by Class')
plt.xticks(new_data['CLASS'])
plt.show()
# Create a scatter plot for Male students
plt.figure(figsize=(8, 6))
plt.scatter(X_test['Male'], y_test, color='blue', label='Actual')
plt.scatter(X_test['Male'], model.predict(X_test), color='red', label='Predicted')
plt.xlabel('Number of Male Students')
plt.ylabel('Total Dropouts')
plt.title('Actual vs. Predicted Total Dropouts for Male Students')
plt.legend()
plt.show()

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = pd.read_csv('/content/m_f.csv')


X = data[['CLASS', 'Male', 'Female']]
y = data['Total']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


user_class = int(input("Enter Class (1-12): "))
user_male = int(input("Enter the number of Male students: "))
user_female = int(input("Enter the number of Female students: "))


new_data = pd.DataFrame({'CLASS': [user_class], 'Male': [user_male], 'Female': [user_female]})
predicted_dropouts = model.predict(new_data)

print("Predicted Total Dropouts:", predicted_dropouts[0])


plt.figure(figsize=(8, 6))
plt.bar(new_data['CLASS'], predicted_dropouts[0], color='skyblue')
plt.xlabel('Class')
plt.ylabel('Predicted Total Dropouts')
plt.title('Predicted Total Dropouts by Class')
plt.xticks(new_data['CLASS'])
plt.show()

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = pd.read_csv('/content/m_f.csv')


X = data[['CLASS', 'Male', 'Female']]
y = data['Total']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

user_class = int(input("Enter Class (1-12): "))
if user_class < 1 or user_class > 12:
    print("Error: Class should be between 1 and 12.")

else:
    user_male = int(input("Enter the number of Male students: "))
    user_female = int(input("Enter the number of Female students: "))


    new_data = pd.DataFrame({'CLASS': [user_class], 'Male': [user_male], 'Female': [user_female]})
    predicted_dropouts = model.predict(new_data)

    print("Predicted Total Dropouts:", predicted_dropouts[0])


    # plt.figure(figsize=(8, 6))
    # plt.bar(new_data['CLASS'], predicted_dropouts[0], color='skyblue')
    # plt.xlabel('Class')
    # plt.ylabel('Predicted Total Dropouts')
    # plt.title('Predicted Total Dropouts by Class')
    # plt.xticks(new_data['CLASS'])
    # plt.show()

