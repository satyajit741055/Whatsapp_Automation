from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 
import pyperclip as pc 
import pyperclip as pc 
import csv
import os 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Will First Try to Open Whatsapp website and Login <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\DELL\\AppData\\Local\\Google\\Chrome\\User Data')
driver = webdriver.Chrome(executable_path='D:\Projects_new\Whatsapp_Automation\chromedriver.exe',chrome_options=options)

web_url = 'https://web.whatsapp.com/'

driver.get(web_url)
driver.maximize_window()

try:
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

except Exception as e:
    print(str(e))


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> We are waiting till element is located on the page  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
try:
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))
    )


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> now we are sending messages   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    receiver_name = []
    with open('saved_names','r') as f:
        receiver_name = [i.strip('\n') for i in f.readlines()]

    names_for_messages = []
    with open('names_for_message','r') as f:
        names_for_messages =  [i.strip('\n') for i in f.readlines()]
    
    print(names_for_messages)


    select_box_path = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
    for i,j in zip(receiver_name,names_for_messages):
        select_box_element = driver.find_element_by_xpath(xpath=select_box_path)
        select_box_element.send_keys(i,Keys.ENTER)

        send_msg_path  = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        send_msg_element = driver.find_element_by_xpath(xpath=send_msg_path)
        with open('message.txt','r',encoding='utf-8') as f: 
            message = f.read()
            if 'name' in message:
                message = message.replace("name",j)
                pc.copy(message)
            else:
                message = message 

                                
        #send_msg_element.send_keys(message,Keys.ENTER)
        send_msg_element.send_keys(Keys.CONTROL + "v", Keys.INSERT)
        send_msg_element.send_keys(Keys.ENTER)

        print('Message Sent Prabhu')
        time.sleep(5)

    os.remove('names_for_message')
    os.remove('saved_names')
    os.remove('numbers')


finally:
    print('Hare Krishna ')
    time.sleep(10)
    driver.quit()

