
"""
import datetime
from datetime import timedelta, date, timezone
import time
hoje = (date.today() + timedelta(days=21))
amanha = hoje.strftime('%d/%m/%Y')
print('Depois ', amanha, datetime.time(hour=0, minute=0))

hora = datetime.timedelta(hours=4)
print(hora)



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke #actual browser
driver = webdriver.Edge(executable_path="../bin/msedgedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
#to refresh the browser
#driver.refresh()
# identifying the link with the help of Javascript executor
time.sleep(5)
javaScript = "document.getElementsByClassName('tp-logo')[0].click();"
print(javaScript.__contains__(''))
# driver.execute_script(javaScript)
#to close the browser
#driver.quit()
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ie_options = webdriver.IeOptions()
ie_options.attach_to_edge_chrome = True
ie_options.edge_executable_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

driver = webdriver.Ie(options=ie_options)

driver.get("http://www.bing.com")
elem = driver.find_element(By.ID, 'sb_form_q')
elem.send_keys('WebDriver' + Keys.RETURN)

