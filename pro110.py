import statistics
import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go


df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()


population_mean=statistics.mean(data)
population_stdev=statistics.stdev(data)

print(f"Mean of the population is {population_mean}")
print(f"Standard deviation of the population is {population_stdev}")



def random_set_of_mean(counter):
    data_set=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        data_set.append(value)
    mean=statistics.mean(data_set)

    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(mean_list)
    print(f"Mean of sampling distribution is:{mean} ")

    fig=ff.create_distplot([df],["Reading Time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="Mean"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
        
    std_dev=statistics.stdev(mean_list)
    print(f"Standard deviation of sampling distribution: {std_dev}")
    show_fig(mean_list)

setup()



