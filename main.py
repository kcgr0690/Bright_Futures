# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

# Print out the number of rows and columns
print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

oneCountryBooleanList = lwd["country_name"]=="India"
oneCountryData = lwd.loc[oneCountryBooleanList]

print("Between 1993 and 2006, India experienced major economic growth, but access to electricity remained uneven—especially for women in rural areas. Electricity brings more than light; it supports safety, education, and opportunity. ")

input("~~~~~~~~~~~~~~~~~~~~\nHit enter to continue.\n ")

print("~~~~~~~~~~~~~~~~~~~~\nSita, a teenage girl in a village in 1995, lives without electricity. She studies by kerosene lamp and struggles to concentrate at night. Her days are shaped by limitations she can’t control. In contrast, imagine you live in a nearby town. You have electric lights to study by, a fan to keep you cool, and maybe even a television for learning and entertainment. It’s easier to focus on school and dream bigger. Both Sita and you are equally capable—but your access to electricity shapes the opportunities you have.\n ")

input("~~~~~~~~~~~~~~~~~~~~\nHit enter to see my research question.\n ")

print("~~~~~~~~~~~~~~~~~~~~\nHow did increasing household electricity access from 1993 to 2006 affect women’s education and quality of life in India?\n ")

input("~~~~~~~~~~~~~~~~~~~~\nHit enter to check out my scatterplot and analysis.\n ")

print("~~~~~~~~~~~~~~~~~~~~\nThe scatter plot shows the percent of women in India living in households with electricity, rising from around 55% in 1993 to over 80% by 2006.\n ")

print("The scatterplot should appear in the tab VNC.")

# create a scatter plot
plt.scatter(oneCountryData["year"], oneCountryData["EI_women_elec_p"], color="red")

# add a title to the plot
plt.title("Women living in an household with electricity in India (%)")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("% of Women Living in a Household with Electricity")

# set the range for the y-axis
plt.ylim(0,100)

# show the plot
plt.show()



