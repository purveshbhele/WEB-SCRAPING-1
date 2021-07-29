from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Proper name", "Distance (ly)", "Mass (M☉)", "Radius (R☉)"]
    planet_data = []
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        temp_list = []
        for tr in soup.find("table").find_all("tr"):
                td = tr.find_all("td")
                row = [i.text.rstrip() for i in td]
                temp_list.append(row)
        planet_data.append(temp_list)
    with open("star.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()
