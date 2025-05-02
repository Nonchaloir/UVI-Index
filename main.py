from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4
import chromedriver_autoinstaller
import time

def main():
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.nea.gov.sg/corporate-functions/weather/ultraviolet-index")

    wait = WebDriverWait(driver, 20)  # wait up to 10 seconds
    time.sleep(2)

    UVI = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'circle__container')]")))
    Lastest_hour = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'latest-hour')]")))
    Lastest_time = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'latest-date')]")))

    UVI_Info_Website = UVI.text
    Lastest_hour_Info = Lastest_hour.text
    Lastest_time_Info = Lastest_time.text
    driver.quit()

    if Lastest_hour_Info == "":
        UVI_Info_Website =  "NA"

    print(UVI_Info_Website)
    print(f'{Lastest_time_Info} {Lastest_hour_Info}:')

    # load and update index.html
    with open("index.html") as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt, 'html.parser')

    UVI_Info = soup.find('div', id="UVI Index")
    DateTime_Info = soup.find('div', id="DateTime")

    if UVI_Info:
        UVI_Info.string = UVI_Info_Website
    if DateTime_Info:
        DateTime_Info.string = f'{Lastest_time_Info} {Lastest_hour_Info}:'

    with open("index.html", "w") as outf:
        outf.write(str(soup))

main()
