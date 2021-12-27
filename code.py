import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()

##print("Mean", reading_scores_mean)


def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,100):
    set_of_means= random_set_of_mean(30)
    mean_list.append(set_of_means)

#show_fig(mean_list)

mean = statistics.mean(mean_list)
st_deviation = statistics.stdev(mean_list)

first_std_deviation_start, first_std_deviation_end = mean- st_deviation, mean + st_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*st_deviation), mean + (2*st_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3*st_deviation), mean + (2*st_deviation)

print("std1", first_std_deviation_start, first_std_deviation_end)
print("std2", second_std_deviation_start, second_std_deviation_end)
print("std3", third_std_deviation_start, third_std_deviation_start)

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()
mean_of_sample1=statistics.mean(data)
fig = ff.create_distplot([mean_list], ["claps"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start], y=[0,0.17],mode = "lines",name = "Standard Deviation 1 start"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end], y=[0,0.17],mode = "lines",name = "Standard Deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start], y=[0,0.17],mode = "lines",name = "Standard Deviation 2 start"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end], y=[0,0.17],mode = "lines",name = "Standard Deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17],mode = "lines",name = "Standard Deviation 3 start"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17],mode = "lines",name = "Standard Deviation 3 end"))
fig.show()

fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0,0.17],mode = "lines",name = "Mean of Sample 1"))

zScore = (mean_of_sample1 - mean)/st_deviation
print("Z Score is = ", zScore)
