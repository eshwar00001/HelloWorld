import threading
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import pandas as pd
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient()
db=client.test
# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

p1=r"C:\Users\eshwar07\Documents\testing2.csv"
p2=r"C:\Users\eshwar07\Downloads\MOCK_DATA.csv"
# for df in pd.read_csv(p1,sep=",",dtype=object,chunksize=100000):
#     k=df.to_dict(orient='records')
#     db.test3.insert_many(k)
#     print(k)
# k=df.to_dict(orient='records')0
# db.test.insert_many(k)
# print(k)
import datetime
print(datetime.datetime.now())

def test1(df,f):
    client = MongoClient()
    db = client.test
    val = df.to_dict()
    # k=db.test1.find(val).count()
    k = db.test3.find(val)
    for v in k:
        f.write(str(v))

#
#
#         #print(k[0])
# i=0
# j=100
#
# print(datetime.datetime.now())
# # for df in pd.read_csv(p1,sep=",",dtype=object,chunksize=1000000):
# #     print(type(df.iloc[1:100]))
# #     for i,df1 in df.iloc[i:j].iterrows():
# #         print(df1)
# #         test1(df1)
#
#
i=0
j=100
f=open(r"C:\Users\eshwar07\test.csv","w")
for df in pd.read_csv(p1,sep=",",dtype=object,chunksize=100):

    if(j<100000):
        processes = [threading.Thread(target=test1, args=(df1,f)) for i,df1 in df.iloc[i:j].iterrows()]
        for process in processes:
            process.start()

        for process in processes:
            process.join()
        # i=j
        # j=i+100




