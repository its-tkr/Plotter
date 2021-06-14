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
        file=input("enter the filename:")
        file_pat=pat+"\\"+file+".csv"
        x=pd.read_csv(file_pat)
        return(pd.DataFrame(x).head())
    else:
        return("Please enter a valid option")
def plotter(option):
    print("sorry enaku theriyathu")

def plotter_col(option):
    print("sorry enaku theriyathu")

def select_plot(option):
    if option=="1":
        print("Select the type of plot in which you want to view the dataframe by selecting 1 to 6")
        print("1.Line Plot")
        print("2.Scatter Plot")
        print("3.Bar Plot")
        print("4.Histogram")
        print("5.Box Plot")
        print("6.Surface Plot")
        plot=input()
        plotter(plot)
    elif option=="2":
        print("Select the type of plot in which you want to view the dataframe by selecting 1 to 7")
        print("1.Line Plot")
        print("2.Scatter Plot")
        print("3.Bar Plot")
        print("4.Histogram")
        print("5.Box Plot")
        print("6.Surface Plot")
        print("7.Bubble Plot")
        plot=input()
        plotter_col(plot)
    else:
        print("Please enter a valid option")






print("Welcome to Plotter")
print("1.Create a Random dataframe with 100 rows and 5 columns")
print("2.Customize your own dataframes")
print("3.Upload your file(csv/json)")
option = int(input("please enter any option between 1 or 2 or 3:"))
df = create_df(option)
print("DataFrame is created and head of the dataframe is given below")
print(df)
print("Enter '1' if you want to plot the entire columns or \nEnter '2' to print specific column")
plot_option=input()
select_plot(plot_option)