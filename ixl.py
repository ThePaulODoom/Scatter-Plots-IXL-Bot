#!/usr/bin/env python3 
try:
 from selenium.webdriver.common.keys import Keys 
 from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
 from selenium import webdriver 
 import time
 from time import sleep
 import sys

 #cap = DesiredCapabilities().CHROMIUM
 browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

 def login(uname, pword):
  time.sleep(1) 
  browser.find_element_by_class_name("explore-btn").click()
  username = browser.find_element_by_id("qlusername")
  username.clear()
  username.send_keys(uname)
  password = browser.find_element_by_id("qlpassword")
  password.clear()
  password.send_keys(pword)
  #browser.find_element_by_class_name("action-btn").click()
  browser.find_element_by_id("qlsubmit").click()

 def wrong():
  browser.find_element_by_class_name("got-it-top").click()

 def answer():
  sleep(1)
  try:
   browser.find_element_by_class_name("lastInRow").click()
  except:
   browser.find_element_by_class_name("lastInRow").click()
  finally: 
 #  browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   sleep(1)
   try:
    browser.find_elements_by_xpath("//button[text()='Submit']")[1].click()
   except:
    browser.find_elements_by_xpath("//button[text()='Submit']")[0].click()
 #  browser.execute_script("window.scrollTo(0, 0);")
   sleep(1)
  

 browser.get("https://www.ixl.com/math/grade-7/identify-trends-with-scatter-plots")
 login(sys.argv[1],sys.argv[2])
 while True:
  browser.get("https://www.ixl.com/math/grade-7/identify-trends-with-scatter-plots")
  while int(browser.find_element_by_id("currentscore").text) < 90:
   answer()
   if browser.find_element_by_xpath("//div[text()='Incomplete answer']").text == "Incomplete answer":
    browser.find_element_by_xpath("//button[text()='Go Back']").click()
    continue
   if browser.find_element_by_class_name("feedback-header").text == "Sorry, incorrect...":
    wrong()
  sleep(2)
  try:
   while int(browser.find_element_by_id("currentscore").text) < 100:
    answer()
    if browser.find_element_by_class_name("feedback-header").text == "Sorry, incorrect...":
     wrong(1)
    try:
     if browser.find_element_by_class_name("hdr-problems-correct").text == "Questions Correct":
      break
    except:
     pass
  except:
   pass
finally:
 browser.quit()
 print(sys.exc_info()[0])
