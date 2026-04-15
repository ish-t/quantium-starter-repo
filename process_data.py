import pandas as pd
from os import listdir, path, mkdir

#get data files
data_path = "./data"
files = listdir(data_path)

#array to store final input dataframes
inputdfs = []

#process data files
for file in files:
    #read file, converting date to a datetime type and price to a float, without the $
    df = pd.read_csv(path.abspath(data_path + "/" + file), parse_dates=["date"], converters={"price": lambda price: float(price.replace("$", ""))}, thousands=",")

    #create sales column
    df["sales"] = df["price"] * df["quantity"]

    #only retain rows where product = pink morsel 
    df = df[df["product"].isin(["pink morsel"])]
    
    #drop unneeded columns
    df = df.drop(["price", "quantity", "product"], axis=1)

    #re-order columns
    df = df[["sales", "date", "region"]]

    #add final dataframe to list of dataframes
    inputdfs.append(df)

#concat list of dataframes into output dataframe
#ignore index to stack lines ontop of each other (union datasets)
outputdf = pd.concat(inputdfs, ignore_index=True)

#make output directory if it does not exist
try:
    mkdir("./out")
except:
    pass

#output dataframe to csv
outputdf.to_csv("./out/output.csv", index=False)
