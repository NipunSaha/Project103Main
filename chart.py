import pandas as pd
import plotly.express as px

df = pd.read_csv("covidChart.csv")

fig = px.scatter(df,x = "date",y = "cases",color = "country",size_max = 60,size = "cases")
fig.show()