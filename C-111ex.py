import csv
import pandas as pd
import random
import statistics 
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
fig=ff.create_distplot([data],["Math_score"],show_hist=False)
fig.show()

mean=statistics.mean(data)
sd=statistics.stdev(data)
print("mean=",mean)
print("sd=",sd)

def random_setofmean(counter):
    dataset=[]
    for i in range(0,counter) :
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
mean_list=[]
for i in range(0,1000) : 
    setofmean=random_setofmean(100)
    mean_list.append(setofmean)
sd=statistics.mean(mean_list)
print("mean of sample distribution",mean)
fig=ff.create_distplot([mean_list],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,.20],mode="lines",name="mean"))
fig.show()
mean=statistics.mean(mean_list)
sd=statistics.stdev(mean_list)
print("mean=",mean)
print("sd=",sd)

first_st_deviation_start,first_st_deviation_end=mean-sd,mean+sd
second_st_deviation_start,second_st_deviation_end=mean-(2*sd),mean+(2*sd)
third_st_deviation_start,third_st_deviation_end=mean-(3*sd),mean+(3*sd)

print("std1",first_st_deviation_start,first_st_deviation_end)
print("std2",second_st_deviation_start,second_st_deviation_end)
print("std3",third_st_deviation_start,third_st_deviation_end)