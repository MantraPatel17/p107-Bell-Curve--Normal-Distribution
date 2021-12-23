import csv
import pandas as pd


import plotly.figure_factory as pf

reader = pd.read_csv("Mobile_ratingData.csv")
reader2  = pd.read_csv("student_marks_presentData.csv")
reader3  = pd.read_csv("data.csv")
reader4  = pd.read_csv("line_chart.csv")


g = pf.create_distplot( [reader["Avg Rating"].tolist()], ["Avg Ratings"],show_hist=False)
g2 = pf.create_distplot( [reader2["Days Present"].tolist()], ["Days Present"],show_hist=False)
g3 = pf.create_distplot( [reader3["InternetUsers"].tolist()], ["Days Present"],show_hist=False)
g4 = pf.create_distplot( [reader4["Per capita income"].tolist()], ["Days Present"],show_hist=False)
g2.show()
#g2.show()