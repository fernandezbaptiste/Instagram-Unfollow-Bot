try:
    print('Importing Modules . . .','\n')
    import time
    import requests
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import requests
    # from requests_html import HTMLSession
    import time
    from selenium.webdriver.common.keys import Keys
    import pandas as pd
    import json
    import re
    import gspread
    from gspread_dataframe import get_as_dataframe, set_with_dataframe
    from oauth2client.service_account import ServiceAccountCredentials
    from selenium.webdriver.common.action_chains import ActionChains
    time.sleep(0.5)
except Exception as e:
    print('Error importing: ', e,'\n')


################## Opening Chrome Window
url = 'https://www.instagram.com/'
driver = webdriver.Chrome('/Users/baptistefernandez/AtomProjects/Scraping Projects/chromedriver')
print('Connecting to Instagram server . . .','\n')
time.sleep(0.5)
print('Accessing website . . .','\n')
time.sleep(0.5)
driver.get(url)
print('Chrome Window Pop Up . . .','\n')
time.sleep(0.5)
print('Accepting Cookies . . .','\n')
driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
time.sleep(2)
# driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').click()
# time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('baptistefernandez1')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('Jorkimien6996!i')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(5)

# driver.find_element_by_xpath('//*[@id="location-typeahead-location-manager-input"]').send_keys(Keys.BACKSPACE)
#
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img').click()
time.sleep(5)
# Click on my logo profile
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div').click()
time.sleep(5)
# Click on my "following numbers"
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[3]/a').click()
time.sleep(5)
# touch random person on Instagram
driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/ul/div/li[10]').click()
time.sleep(5)


# To go down till the end
# for i in range(96):
for i in range(1,30):
    # i = 1 -> li 12
    # i = 2 -> li 24
    # i = 3 -> li 36
    try:
        html_string = "/html/body/div[6]/div/div/div[3]/ul/div/li[" + str(i*12) +"]"
        driver.find_element_by_xpath(html_string).click()
        print('Current link is:', html_string)
        time.sleep(5)
    except Exception as e:
        try:
            time.sleep(5)
            html_string = "/html/body/div[6]/div/div/div[3]/ul/div/li[" + str(i*12) +"]"
            print('Retrying for link: ', html_string)
            driver.find_element_by_xpath(html_string).click()
        except Exception as e:
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/a[2]").click()
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/a[1]").click()
            time.sleep(5)
            html_string = "/html/body/div[6]/div/div/div[3]/ul/div/li[" + str(i*12) +"]"
            print('Retrying for link: ', html_string)
            driver.find_element_by_xpath(html_string).click()



html_string = "/html/body/div[6]/div/div/div[3]/ul/div/li[12]"
print('This is the last html from bottom of list: ', html_string)
numbers_inside_html_link = (re.findall('\d+', html_string ))
follower_rank = int(numbers_inside_html_link[2])

while follower_rank < 340:

    follower_html_to_unfollow =  "/html/body/div[6]/div/div/div[3]/ul/div/li[" + str(html_string[3]) + "]/div/div[2]/button"

    # unfollowing button click
    driver.find_element_by_xpath(follower_html_to_unfollow).click()
    time.sleep(5)
    # confirm
    driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
    time.sleep(5)
    follower_rank -= 1






#################################### DRAFT ####################################


# Test clicking on "Follwing" button to unfollow

# driver.find_element_by_xpath('//*[@id="u_0_g_xQ"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="email"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="email"]').send_keys('fernandez.baptiste1@gmail.com')
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="pass"]').send_keys('Jorkimien6996!f')
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
# time.sleep(5)


# driver.find_element_by_xpath('').click()
# time.sleep(3)
# driver.find_element_by_xpath('').click()

# element = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/ul/div/li[51]")
# actions = ActionChains(driver)
# actions.move_to_element(element).perform()

# Build function that goes until the end - 1118 total followers
    # so make it add 12 for at least 90 times


# Get li number inside strings
# Click on driver xpath to click following
# and delete the that one
# - 1 on the list and do it again


# Same html path
# driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/ul/div/li[259]/div/div[2]/button").click()
# time.sleep(3)
# driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()


# add +12 for every li string
#
# followers_passed = 0
# while followers_passed < 90:
#     for i in range(24, 90):
#         html_string = "/html/body/div[6]/div/div/div[3]/ul/div/li[" + str(i) +"]"
#         followers_passed += 1
#         print(html_string)
#
# # add 12 accounts everytime
# driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/ul/div/li[24]").click()
# driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/ul/div/li[48]").click()
# driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/ul/div/li[60]").click()
#



# element_inside_popup = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/ul/div/li[1]/div')
# element_inside_popup.send_keys(Keys.END)

#
# element=driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/ul/div/li[1]/div")
# element.location_once_scrolled_into_view
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
