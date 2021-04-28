from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import loginInfo
import time


browser = webdriver.Chrome()

browser.get("https://twitter.com/")

time.sleep(3)

#giris_yap = browser.find_element_by_xpath(
#    "//*[@id='doc']/div/div[1]/div[1]/div[2]/form/div[3]/div/p/a")

giris_yap = browser.find_element_by_xpath(
    "//*[@id = 'react-root']/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/a[2]")

giris_yap.click()

time.sleep(5)

username = browser.find_element_by_xpath(
    "//*[@id = 'react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")

password = browser.find_element_by_xpath(
    "//*[@id = 'react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

time.sleep(3)


login = browser.find_element_by_xpath(
    "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")

login.click()

time.sleep(5)

explode = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]")
explode.click()
time.sleep(2)
searchArea = browser.find_element_by_xpath(
    "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")
#searchButton = browser.find_element_by_xpath(
#    "//*[@id='global-nav-search']/span/button")

searchArea.send_keys("#yazilimayolver")

#searchButton.click()
searchArea.send_keys(Keys.ENTER)

#browser.find_element_by_name(
#    "//*[@id='typeaheadDropdown-3']/div[2]/div/div").send_keys(Keys.RETURN)

time.sleep(5)

lenOfPage = browser.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match == False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True
time.sleep(5)
tweets = []

#elements = browser.find_elements_by_css_selector("div.css-1dbjc4n")
elements = browser.find_elements_by_css_selector("div.r-1fmj7o5")

for element in elements:
    tweets.append(element.text)

tweetCount = 1

with open("tweets.txt", "w", encoding="UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("**************************\n")
        tweetCount += 1


browser.close()
