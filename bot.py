##########################
# esse bot usa python3.9 #
##########################

import random
from time import sleep

driver = webdriver.Firefox(executable_path='c://geckodriver.exe') #local cm seu geckodriver.exe
driver.get('') #url da enquete
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
    for x in range(0, tamanho): #colocar a quantidade de enquetes
        ale = random.randint(0, tamanho) # colocar a quantidade de opções
        if x != 0:
            ale = ale + (x * 3)
        print(ale)
        find_xpath[ale].click()
        if x == 5:
            count += 1
