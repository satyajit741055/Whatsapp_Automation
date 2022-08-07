import pyperclip as pc 
import csv
import os 

with open('data.csv',"r") as data :
    data_csv = csv.reader(data,delimiter = "\n")
    next(data)

    for i,j in enumerate(data_csv):
        k = j[0].split(',')
        with open('names_for_message','a') as f:
            f.write(k[1]+'\n')
            print('file created names_for')
        with open('saved_names','a') as f:
            f.write(k[0]+'\n')
        with open('numbers','a') as f:
            f.write(k[2]+'\n')
            

        
receiver_name = []
with open('names_for_message','r') as f:
    receiver_name = [i.strip('\n') for i in f.readlines()]


for i in receiver_name:
    with open('message.txt','r') as f: 
        message = f.read()
        if 'name' in message:
            message = message.replace("name",i)
            pc.copy(message)
        else:
            message = message 
    print(message)

os.remove('names_for_message')
os.remove('saved_names')
os.remove('numbers')
