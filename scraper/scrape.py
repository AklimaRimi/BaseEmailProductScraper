from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import time


df = pd.read_csv('links.csv')

links = df['Link'].values.tolist()

driver = webdriver.Chrome()
i =1
data = []
for link in links:
    print(i)
    i += 1
    driver.get(link)
    name = driver.find_element(By.CLASS_NAME,'titre_produit').text
    short_des = driver.find_element(By.CLASS_NAME,'description').find_element(By.TAG_NAME,'p').text
    des= driver.find_element(By.CLASS_NAME,'description').find_element(By.TAG_NAME,'div').text
    price = driver.find_element(By.CLASS_NAME,'prix').find_element(By.TAG_NAME,'span').text
    data.append([name,short_des,des,price])
    time.sleep(2)
   
df = pd.DataFrame(data=data,columns=['Product Name','Short Description','Description','Price']) 
df.to_csv('info.csv',index=False)