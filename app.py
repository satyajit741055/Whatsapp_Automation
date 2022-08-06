from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 
import pyperclip as pc 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Will First Try to Open Whatsapp website and Login <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\DELL\\AppData\\Local\\Google\\Chrome\\User Data')
driver = webdriver.Chrome(executable_path='D:\Projects_new\Whatsapp_Automation\chromedriver.exe',chrome_options=options)

web_url = 'https://web.whatsapp.com/'

driver.get(web_url)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> We are waiting till element is located on the page  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
try:
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))
    )


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> now we are sending messages   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    receiver_name = []
    with open('names.txt','r') as f:
        receiver_name = [i.strip('\n') for i in f.readlines()]
    

    select_box_path = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
    for i in receiver_name:
        select_box_element = driver.find_element_by_xpath(xpath=select_box_path)
        select_box_element.send_keys(i,Keys.ENTER)

        send_msg_path  = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        send_msg_element = driver.find_element_by_xpath(xpath=send_msg_path)
        send_msg_element.send_keys('Hare Krishna PRabhuji',Keys.ENTER)
        print('Message Sent Prabhu')
        time.sleep(5)



finally:
    print('Hare Krishna ')
    time.sleep(10)

