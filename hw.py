import statistics as st
import pandas as pd
import plotly.express as pe
import numpy as np
import plotly.figure_factory as pf
import csv
#Loading the variables
data = pd.read_csv("savings_data_final.csv")
savings = data["quant_saved"].tolist()
reminded = data["rem_any"].tolist()
#Getting mean, median, mode of population data
mean = st.mean(savings)
mode=st.mode(savings)
median=st.median(savings)
sd = st.stdev(savings)
#Printing population data and graphing it
print("The mean is", mean, ". The mode is ", mode, ". The median is", median, ", and the standard deviation of the whole data is", sd)
print("Getting graph")
graph = pe.scatter(data, y="quant_saved", color="rem_any")
graph.show()
print("Done plotting population graph")
print("__________________________________")
#Getting correlation of data
highschool = data["highschool_completed"].tolist()
wealthy = data["wealthy"].tolist()
corr= np.corrcoef(highschool,wealthy)
if(corr[0][1]>0.7 or corr[0][1]==1):
    print("The correlation between the two sets is related, as it is greater than 0.7 or equal to 1(",corr[0][1],")")
else:
    print("Hmm...these two things don't seem to be related. The correlation was", corr[0][1])
print("Plotting correlation graph")
newgraph = pf.create_distplot([highschool], ["Amount of people who finished high school"], show_hist=False)
newgraph.show()
print("Done!")
print("__________________________________")
#Finding the relation between two parts of the data and then graphing it.
above80=[]
below39=[]
for i in savings:
    if(i>=80):
        above80.append(i)
    elif(i<=39):
        below39.append(i) 
meanabove80 = st.mean(above80)
modeabove80 = st.mode(above80)
medianabove80 = st.median(above80)
sdabove80 = st.stdev(above80)
print("The mean of the people who saved over $80 is ", meanabove80)
print("The mode of the people who saved over $80 is ", modeabove80)
print("The median of the people who saved over $80 is ", medianabove80)
print("The standard deviation of the people who saved over $80 is ", sdabove80)
print("____________________________________________________________")

meanbelow39 = st.mean(below39)
modebelow39 = st.mode(below39)
medianbelow39 = st.median(below39)
sdbelow39 = st.stdev(below39)
print("The mean of the people who saved below $39 is ", meanbelow39)
print("The mode of the people who saved below $39 is ", modebelow39)
print("The median of the people who saved below $39 is ", medianbelow39)
print("The standard deviation of the people who saved over $39 is ", sdbelow39)
 
    
