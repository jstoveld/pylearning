import time
import pickle
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# HEADERS = ({'User-Agent':
#             'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
#             'Accept-Language': 'en-US, en;q=0.5'})

# driver = webdriver.Chrome("C:/bin/chromedriver.exe")  # Optional argument, if not specified will search path.
# driver.get("https://my.scheduling.com/selfscheduling/1.3.0/login")
# time.sleep(30) # Let the user actually see something!
# # search_box = driver.find_element_by_name('content ng-star-inserted')
# # search_box.send_keys('ChromeDriver')
# # search_box.submit()
# # time.sleep(30) # Let the user actually see something!
# # driver.quit()


# print(driver)