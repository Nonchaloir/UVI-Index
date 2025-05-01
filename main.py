from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import bs4
import re

def main():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    driver.get("https://www.nea.gov.sg/corporate-functions/weather/ultraviolet-index")
    UVI = driver.find_element(By.XPATH, "//div[contains(@class, 'circle__container')]")
    Lastest_hour = driver.find_element(By.XPATH, "//span[contains(@class, 'latest-hour')]")
    Lastest_time = driver.find_element(By.XPATH, "//span[contains(@class, 'latest-date')]")

    UVI_Info_Website = UVI.text
    Lastest_hour_Info = Lastest_hour.text
    Lastest_time_Info = Lastest_time.text
    driver.close()


    # load the file
    with open("main.html") as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt, 'html.parser')

    # create new link
    #new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png")
    # insert it into the document
    #soup.head.append(new_link)

    UVI_Info = soup.find('div', id = "UVI Index")
    DateTime_Info = soup.find('div', id = "DateTime")

    UVI_Info.string = UVI_Info_Website
    DateTime_Info.string = f'{Lastest_time_Info} {Lastest_hour_Info}:'


    # save the file again
    with open("main.html", "w") as outf:
        outf.write(str(soup))

main()
