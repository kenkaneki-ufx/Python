import pandas  as pd
import os
print(pd.__version__)

'''#            PANDA_Series()
marks = pd.Series([70,90,100],index=['x','y','z'])
print(marks['z'])
calories = pd.Series({'day1':420,'day2':380},index = ['day1','day2','day3'])
print(calories)
'''

'''#            PANDA_DataFrame()
data = {'Name':["Spongebob","Patrick","Squidward"], 'Age':[35,40,45]}
df = pd.DataFrame(data)
print(df)
print("-"*20)
#                                           loc = 'locate' either index or "key"
print(df.loc[[0,2]])#               --->    df.loc[0] + df.loc[2]
print("-"*20)

df = pd.DataFrame(data,index = ['Employee 1','Employee 2','Employee 3'])
print(df.iloc[1])#       --->    print(df.loc['Employee 2'])
print("-"*25)

df["job"] = ["cook","N/A","Cashier"]
print(df)
print("-"*30)

#   Adding one Employee details 
new_row = pd.DataFrame({'Name':'Sammy', 'Age':'28', 'job':'Dishwasher' },index = ['Employee 4'])
#   Adding multiple Employee details with their new indexs
new_rows = pd.DataFrame([           
    {'Name':'Sandy', 'Age':'26', 'job':'Cleaner' },
    {'Name':'David', 'Age':'43', 'job':'Manager' }],
    index = ['Employee 5','Employee 6'])
df = pd.concat([df,new_row,new_rows])     
print(df)
'''

#            CSV and json

#            CSV --> Comma-Separated Values
#            JSON --> JavaScript Object Notation 
df = pd.read_csv('pd_data/pokemon.csv') # for Json -->  pd.read_json('pd_data/pokemon.json')
print(df)#      print(df.to_string()) --> prints everything with index
print("-"*30)

print(df[["Name","Height","Weight"]])#      print(df.to_string()) --> prints everything in column [Name]
print("-"*30)