import random
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox(executable_path='') #Adress with your geckodriver.exe
driver.get('') #Url
find_xpath = driver.find_elements_by_xpath("//div[@class='appsMaterialWizToggleRadiogroupOffRadio exportOuterCircle']")

count = 0

while True:
    if count != 0:
        driver.find_element_by_xpath('//div[@jsname="M2UYVd"]').click()
        sleep(1)
        driver.back()
        sleep(1)
        find_xpath = driver.find_elements_by_xpath(
            "//div[@class='appsMaterialWizToggleRadiogroupOffRadio exportOuterCircle']")
    sleep(2)
    for x in range(0, len(driver.find_elements_by_xpath("//div[@class='freebirdFormviewerComponentsQuestionBaseRoot']"))):
        choice = random.randint(0, )# Add alternatives number 
        choice = choice + (x * 3)
        find_xpath[choice].click()
        if x == 5:
            count += 1
