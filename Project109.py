import plotly.figure_factory as px
import csv
import pandas as pd
import random
import statistics

df = pd.read_csv("Project109.csv")
Mlist = df["math score"].to_list()
Rlist = df["reading score"].to_list()
Wlist = df["writing score"].to_list()


#maths
mean = sum(Mlist)/len(Mlist)
print ("mean", mean)

median = statistics.median(Mlist)
print("median", median)

mode = statistics.mode(Mlist)
print("mode", mode)

SD = statistics.stdev(Mlist)
print("standard deviation", SD)

#write
mean = sum(Wlist)/len(Wlist)
print ("mean", mean)

median = statistics.median(Wlist)
print("median", median)

mode = statistics.mode(Wlist)
print("mode", mode)

SD = statistics.stdev(Wlist)
print("standard deviation", SD)

#Read
mean = sum(Rlist)/len(Rlist)
print ("mean", mean)

median = statistics.median(Rlist)
print("median", median)

mode = statistics.mode(Rlist)
print("mode", mode)

SD = statistics.stdev(Rlist)
print("standard deviation", SD)

# firstSD_start,firstSD_end = mean - SD , mean + SD
# print("{} % of data lies betw first SD", len(dice_result)*100/)