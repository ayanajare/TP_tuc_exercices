from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(options=option)

def title_site(): 
    driver.get("https://www.twitter.com/")
    driver.set_window_size(1600,1200)
    title = driver.title
    driver.close()
    return title

def title_article(): 
    driver.get("https://www.wikiroulette.com/")
    driver.set_window_size(1600,1200)
    title = driver.find_element(by=By.CLASS_NAME,value="mw-page-title-main")
    driver.close()
    print(title)
    return title

title_site()
#title_article()