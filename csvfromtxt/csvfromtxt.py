import pandas as pd 

data = [] #Creatin a list for adding lines from txt.  (This file has four different variables: plate_no,city,district,empty_field)

with open("il_ilce.txt",'r',encoding='utf-8') as data_file:
    for line in data_file: #As using that, can surfing all lines on the txt.
            data.append(line.split()) #Adding lines to the list. (data = [['plate_no','city','district','empty_field'],['plate_no','city','district','empty_field']...])



data = pd.DataFrame(data,columns=['Plate','City','District','empty']) #creating a dataframe with for different column.
data.pop('empty') #deleting empty field
data.to_csv("from_txt.csv") #saving the dataframe as csv.
print(data) #printing dataFrame
