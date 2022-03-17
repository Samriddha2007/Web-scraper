from tracemalloc import start
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome('C:/Users/Samriddha Biswas/WhiteHatClass/Python/chromedriver')
browser.get(start_url)
time.sleep(10)

def scrape():
    headers = ['Name','Light_Years_From_Earth','Planet_Mass','Stellar_Magnitude','Discovery_Date']
    planet_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for ul_tag in soup.find_all('ul',attrs={'class','exoplanet'}):
            li_tags = ul_tag.find_all('li')
            temp_list = []
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append('')
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()
    with open('planet.csv','w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerow(planet_data)
    
scrape()
