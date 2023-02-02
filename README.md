# BaseEmailProductScrapper

## Introduction
  This repository is just track how I worked for my client. This is one of the basic web scrapping task. 
  
## Get the Output

  This one can be collect data by anyone who is a python practioner with following some steps:
  
  1. Download [BaseEmailProductScraper](https://github.com/AklimaRimi/BaseEmailProductScraper/archive/refs/heads/main.zip). Unzip it.<br>
  2. Create create virtual environment for better experience with the following code on the `terminal` in unzipped file.
  ```
  pip install virtualenv
  
  virtualenv env
  
  env/Scripts/activation
  ```
  3. In the same terminal write
  
  ```
  pip install -r requirements.txt
  ```
  
   to get needed python library.
  
  4. Now, to collect data write
  ```
  
    python run urls.py
    python run scrape.py
    
  ```
  **Wait for about 30min to 1 hour to complete whole task.**
  
## Output
  After completing all of process that you've done above you get 2 `csv` files.
  
  i. One is about collected links in `links.csv` [links.csv](https://github.com/AklimaRimi/BaseEmailProductScraper/blob/main/output/links.csv) </br>
  ii. Another is the main scrapped data `info.csv` [info.csv](https://github.com/AklimaRimi/BaseEmailProductScraper/blob/main/output/info.csv)
  
