from selenium import webdriver
import random
import time

browser = webdriver.Chrome()

#url = 'https://eksisozluk.com/mustafa-kemal-ataturk--34712'
#browser.get(url)
#time.sleep(5)
#elements = browser.find_elements_by_css_selector('.content')
#for element in elements:
#print('*****************************************************')
#print(element.text)
#browser.close()

url = 'https://eksisozluk.com/mustafa-kemal-ataturk--34712?p='

pageCount = 1
entries = []
entryCount = 1

while pageCount <= 10:
    randomPage = random.randint(1,2100)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    
    elements = browser.find_elements_by_css_selector('.content')
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pageCount += 1

with open('entries.txt','w', encoding = 'UTF-8') as file:
    for entry in entries:
        file.write(str(entryCount) + '. ------------>\n')
        file.write(entry + '\n\n')
        entryCount += 1
    
browser.close()


