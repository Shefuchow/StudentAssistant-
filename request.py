from bs4 import BeautifulSoup
#from selenium import webdriver
import time
import requests


def checkSeat(url, index):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    info = soup.find_all('td', class_='info')
    # for stuff in info:
    #     print(stuff.get_text().strip())
    seats = info[4+index].get_text().strip()
    return seats


def something( class_num):
    #link = f"http://www.buffalo.edu/class-schedule?switch=showcourses&semester=spring&division=UGRD&dept={dept.upper()}"
    link = "http://www.buffalo.edu/class-schedule?switch=showcourses&semester=spring&division=UGRD&dept=CSE"
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    
    body = soup.contents[16]
    tr = body.find_all("tr")
    for td in tr[4:]:
        try:
            if f"{class_num}" in td.a.get_text():
                data = td.find_all('td', class_='padding')
                if data[len(data)-6].get_text().strip() == "LEC":
                    
                    index = len(data) - 9
                    link = data[index].a['href']
                    days = data[index+4].get_text().strip()
                    time = data[index+5].get_text().strip()
                    print(days)
                    print(time)
                    seat = checkSeat(link, index)
                    print(f"Class has {seat} available")
                    return seat
        except:
            continue

# -- Used to test in command line -------------
# dept = input("Enter the department:")
# num = input("Class level:")
# print('\n' * 3)
# something(dept.upper().strip(),num.strip())



#    browser = webdriver.Chrome(executable_path=r'C:/Users/bcheu/OneDrive/Desktop/webdriver/chromedriver.exe')
#     url = "https://catalog.buffalo.edu/courses/?abbr=CHI&num=102"
#     browser.get(url)
#     resp = browser.page_source
#     browser.quit()
#     soup = BeautifulSoup(resp, "html.parser")