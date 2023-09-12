import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split
import plotly.express as px
import matplotlib.pyplot as plt

class Data :
    def __init__(self,type_of_data,path_of_data):
        self.type_of_data=type_of_data
        self.path=path_of_data
    def read_data(self):
        if self.type_of_data=='csv':
           self.dataframe = pd.read_csv(self.path)
           print(self.dataframe)
        if  self.type_of_data=='excel' :
           self.dataframe = pd.read_excel(self.path)
           print(self.dataframe)
        if self.type_of_data=='sql' :
           self.dataframe = pd.read_sql(self.path)
           print(self.dataframe)
    def type_of_each_column(self):
        print(self.dataframe.dtypes)
    def handle_data(self):
        print(self.dataframe.duplicated())
        answer=input("are you need to know duplicated in column?(yes/no)")
        if answer=='yes':
            name_of_column=input("please enter the name of column")
            print(self.dataframe.duplicated(name_of_column))
        answer1=input("are you wnt to dop duplicated?(yes/no)")
        if answer1=='yes':
            self.dataframe.drop_duplicates(name_of_column)
        if (self.dataframe.isna):
            answer2=input("are you want to remove nulls?(yes/no)")
        if answer2=='yes':
            self.dataframe.isna()
    def encode_Categorical_Data(self):
        data=pd.read_csv('International_Report_Departures.csv')
        x=data.iloc[:,:].values
        lx=LabelEncoder()
        input1=int(input("enter the number of column"))
        x[:,input1]=lx.fit_transform(x[:,input1])
        df=pd.DataFrame(x)
        print(df)
    def scaling_numerical_features(self):
        pd_data = pd.DataFrame(self.dataframe)
        input2=int(input("enter the min range of scaling"))
        input3=int(input("enter the max range of scaling"))
        scaler = MinMaxScaler(feature_range=(input2, input3))
        input4=input("enter the name of column")
        pd_data[[input4]] = scaler.fit_transform(pd_data[[input4]])
        print(pd_data)
    def visualize_data(self):
        input6=input("what kind of chart are you want?(bar,histogram,scatter,pie)")
        if input6=='bar':
            input5=input("enter the name of column")
            cut_counts = self.dataframe[input5].value_counts()
            fig = px.bar(x=cut_counts.index, y=cut_counts.values)
            fig.show()
        if input6=='histogram':
            input7=input("enter the name of column")
            Bin=int(input("enter the number of bins and range you want respectively"))
            MIN=int(input("enter the min of range you want"))
            MAX=int(input("enter the max"))
            EDG=input("enter the edg color")
            values,bins,patches=plt.hist(self.dataframe[input7],bins=Bin,range=[MIN,MAX],edgecolor=EDG,linewidth=3)
        if input6=='scatter':
            x,y,z=input("enter").split()
            plt.scatter(self.dataframe[x],self.dataframe[y],color=z)
        if input6=='pie':
            input8=input("enter the name of column")
            counts=self.dataframe[input8].value_counts()
            input9=int(input("enter the size"))
            input10=int(input("size2"))
            plt.figure(figsize=(input9,input10))
            plt.pie(counts,labels=counts.index.values.tolist())
            plt.show()
my_data=Data('csv','International_Report_Departures.csv')
my_data.read_data()
my_data.type_of_each_column()
my_data.handle_data()
my_data.encode_Categorical_Data()
my_data.scaling_numerical_features()
my_data.visualize_data()
