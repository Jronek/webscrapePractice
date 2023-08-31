import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def doAThing():
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    assert "No results found." in driver.page_source
    driver.close()


if __name__ == '__main__':
    doAThing()
