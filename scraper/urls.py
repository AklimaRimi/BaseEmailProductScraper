from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains


lists = [
    'https://www.base-emails.com/achat/cat-administrations-4.html',
    'https://www.base-emails.com/achat/cat-agriculture-alimentation-5.html',
    'https://www.base-emails.com/achat/cat-agriculture-alimentation-5.html?page=2',  
    'https://www.base-emails.com/achat/cat-automobiles-transport-6.html',
    'https://www.base-emails.com/achat/cat-banque-assurance-finance-7.html',
    'https://www.base-emails.com/achat/cat-batiment-et-construction-8.html',
    'https://www.base-emails.com/achat/cat-batiment-et-construction-8.html?page=2',
    'https://www.base-emails.com/achat/cat-batiment-et-construction-8.html?page=3',
    'https://www.base-emails.com/achat/cat-culture-loisirs-9.html',
    'https://www.base-emails.com/achat/cat-enseignement-10.html',
    'https://www.base-emails.com/achat/cat-habillement-11.html',
    'https://www.base-emails.com/achat/cat-industrie-12.html',
    'https://www.base-emails.com/achat/cat-industrie-12.html?page=2',
    'https://www.base-emails.com/achat/cat-industrie-12.html?page=3',
    'https://www.base-emails.com/achat/cat-medias-13.html',
    'https://www.base-emails.com/achat/cat-sante-medecine-14.html',
    'https://www.base-emails.com/achat/cat-sante-medecine-14.html?page=2',
    'https://www.base-emails.com/achat/cat-services-divers-17.html',
    'https://www.base-emails.com/achat/cat-services-divers-17.html?page=2',
    'https://www.base-emails.com/achat/cat-services-divers-17.html?page=3',
    'https://www.base-emails.com/achat/cat-services-divers-17.html?page=4',
    'https://www.base-emails.com/achat/cat-sports-15.html',
    'https://www.base-emails.com/achat/cat-sports-15.html?page=2',
    'https://www.base-emails.com/achat/cat-tourisme-restauration-16.html',
    'https://www.base-emails.com/achat/cat-e-mails-par-departement-3.html',
    'https://www.base-emails.com/achat/cat-e-mails-par-departement-3.html?page=2',
    'https://www.base-emails.com/achat/cat-e-mails-par-region-2.html',
]

data = []
driver = webdriver.Chrome()

for i in lists:
    driver.get(i)

    links = driver.find_elements(By.CLASS_NAME,'image_zoom')
    for link in links:
        ln = link.find_element(By.TAG_NAME,'a').get_attribute('href')
        data.append(ln)
        

df = pd.DataFrame(data=data,columns=['Link'])
df.to_csv('links.csv',index=False)
    