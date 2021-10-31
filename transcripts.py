import os
import sys

import datetime
import time

from selenium import webdriver



# USAGE: py transcripts.py NAME
# eg: py transcripts.py tadic
# the generated html file will be stored in the same directory as NAME.html


PATH = "C:\\Users\\nikol\\OneDrive\\Desktop\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

name = sys.argv[1]

url = "https://www.icty.org/en/case/" + name + "/#trans"

driver.get(url)



def extract_date(link):
    code = link.split("/")[-1][:6]
    year = code[:2]
    if year[1] == "0":
        year = 2000 + int(year)
    else:
        year = 1900 + int(year)
    month = int(code[2:4])
    day = int(code[4:6])

    return datetime.datetime(year, month, day)



dates = {}

# extract all links from the main page
table = driver.find_element_by_class_name("transcript")
cells = table.find_elements_by_class_name("transcript-cell")
for cell in cells:
    try: 
        links = cell.find_elements_by_tag_name("a")
        for link in links:
            l = link.get_attribute("href")

            # one link with a different structure comes up
            if "reftab" in l:
                continue

            dates[l] = extract_date(l)
    except:
        pass


# sort transcripts by date
dates = dict(sorted(dates.items(), key=lambda x:x[1]))

# download html page of all transcripts, merge into one html document
for it in dates.items():
    # wait for 10 seconds before requesting another url, as requested in robots.txt
    time.sleep(10)
    os.system("curl " + it[0] + " >> " + name + ".html")

driver.quit()