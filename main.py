import os
import numpy as np
import pandas as pd
import plotly as pl
import plotly.offline as po
import cufflinks as cf

po.init_notebook_mode(connected=True)
cf.go_offline()

def create_df(value):
    if value == 1:
        return(pd.DataFrame(np.random.rand(100,5),columns=["a","b","c","d","e"]).head())
    elif value==2:
        nc=int(input("Enter the no of columns:"))
        col=["" for i in range (nc)]
        for i in range (nc):
            col[i]=input("Enter the  column name: ")
        nr=int(input("Enter the no of rows:"))
        rows=[["" for k in range (nc)] for i in range (nr)]
        for i in range (nr):
            print("enter the ",i," row values:")
            for j in range (nc):
                v=input("")
                rows[i][j]=v
        return (pd.DataFrame(rows,columns=col).head())
    elif value==3:
        pat=os.getcwd()
        file=input("Enter your file name")
        file_path=pat+'\\'+file+".csv"
        print(file_path)
        return(pd.DataFrame(pd.read_csv(file_path).head()))


print("Welcome to Plotter")
print("1.Create a Random dataframe with 100 rows and 5 columns")
print("2.Customize your own dataframes")
print("3.Upload your file(csv/json)")
option = int(input("please enter any option between 1 or 2 or 3:"))
df = create_df(option)
print(df)