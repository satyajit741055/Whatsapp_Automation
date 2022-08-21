import csv
import os,sys

class Extract_data:
    '''
    Creating files which are needed for the operations 
    '''
    def __init__(self,file_name):
        self.file_name = file_name
    
    def extract(self):
        try:
            with open(self.file_name,"r") as data :
                data_csv = csv.reader(data,delimiter = "\n")
                next(data)

                for i,j in enumerate(data_csv):
                    k = j[0].split(',')
                    with open('names_for_message','a') as f:
                        f.write(k[1]+'\n')
                    with open('saved_names','a') as f:
                        f.write(k[0]+'\n')
                    with open('numbers','a') as f:
                        f.write(k[2]+'\n')

        except Exception as e:
            print(str(e))

    
    def read_data(self):
        try:
            receiver_name = []
            with open('saved_names','r') as f:
                receiver_name = [i.strip('\n') for i in f.readlines()]

            names_for_messages = []
            with open('names_for_message','r') as f:
                names_for_messages =  [i.strip('\n') for i in f.readlines()]
            return receiver_name,names_for_messages 
        except Exception as e:
            print(str(e))
    
    def remove_files(self):
        try:
            os.remove('names_for_message')
            os.remove('saved_names')
            os.remove('numbers')
        except Exception as e:
            print(str(e))
            


