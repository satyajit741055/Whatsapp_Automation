from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 
import os
import pyperclip as pc 
from extract_data import Extract_data



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Will First Try to Open Whatsapp website and Login <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\DELL\\AppData\\Local\\Google\\Chrome\\User Data')
driver = webdriver.Chrome(executable_path='D:\Projects_new\Whatsapp_Automation\chromedriver.exe',chrome_options=options)
web_url = 'https://web.whatsapp.com/'
driver.get(web_url)
driver.maximize_window()

extract_data = Extract_data('data.csv')
extract_data.extract()



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> We are waiting till element is located on the page  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
try:
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))
    )
    
    input_image = int(input('Would you like to send images/video? for yes type 1 otherwise 0'))

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> now we are sending messages   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    receiver_name,names_for_messages = extract_data.read_data()
    
    select_box_path = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
    path = input('image_path')
    image_path = os.path.join(path)

    for i,j in zip(receiver_name,names_for_messages):
        select_box_element = driver.find_element_by_xpath(xpath=select_box_path)
        select_box_element.send_keys(i,Keys.ENTER)

        if input_image == 1:
            
            select_media_icon = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div'
            select_media_element = driver.find_element_by_xpath(xpath=select_media_icon)
            select_media_element.click()
            time.sleep(1)

            select_image_icon = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input'
            select_image_element = driver.find_element_by_xpath(xpath='//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            select_image_element.send_keys(image_path)

            element = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span'))
            )

            send_button_path = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span'
            send_button_element = driver.find_element_by_xpath(xpath=send_button_path)
            send_button_element.click()
            time.sleep(3)
        
            
        send_msg_path  = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        send_msg_element = driver.find_element_by_xpath(xpath=send_msg_path)
        with open('message.txt','r',encoding='utf-8') as f: 
            message = f.read()
            if 'name' in message:
                    message = message.replace("name",j)
                    pc.copy(message)
            else:
                    message = message 

        send_msg_element.send_keys(Keys.CONTROL + "v", Keys.INSERT)
        send_msg_element.send_keys(Keys.ENTER)
        
        time.sleep(3)

    extract_data.remove_files()

except Exception as e:
    print(str(e))
   
finally:
    print('Task Completed ')
    time.sleep(10)
    driver.quit()

