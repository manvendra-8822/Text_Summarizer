from bs4 import BeautifulSoup
import requests
import re
#Creating a function to scrape data from a specified url
def scrape_con(url):
  res = requests.get(url)
  soup = BeautifulSoup(res.text,'html.parser') 
  content = soup.findAll("p")
  data = ""
  for text in content:
    data +=text.text
  return data

scrape_con('https://www.eyeonasia.gov.sg/india/know/overview-of-india/india-profile/')

#Cleaning the data - lowercase conversion and removing the punctutaion
def clean_data(data):
  text = re.sub(r"\[[0-9]*\]"," ",data)
  text = text.lower()
  text = re.sub(r'\s+'," ",text)
  text = re.sub(r","," ",text)
  return text
cleaned_data = clean_data(raw_data)
