 # Importing Modules
try:
    from time import sleep
    import requests
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.keys import Keys
    import json
except Exception as e:
    print('Error importing: ', e,'\n')

# Import your credentials
with open('creds.json') as json_file:
    data = json.load(json_file)
username = data['username']
password = data['pass']


#Opening Chrome Window
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/')
sleep(0.5)
driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
sleep(2)

# Login in with Password + Email
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
sleep(5)


driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img').click()
sleep(5)

# Click on my logo profile
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div').click()
sleep(5)

# Click on my "following numbers"
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[3]/a').click()
sleep(5)

# touch random person on Instagram
driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/ul/div/li[10]').click()
sleep(5)



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
        sleep(5)
    except Exception as e:
        try:
            sleep(5)
            html_string = "/html/body/div[6]/div/div/div[3]/ul/div/li[" + str(i*12) +"]"
            print('Retrying for link: ', html_string)
            driver.find_element_by_xpath(html_string).click()
        except Exception as e:
            sleep(5)
            driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/a[2]").click()
            sleep(5)
            driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/a[1]").click()
            sleep(5)
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
    sleep(5)
    # confirm
    driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
    sleep(5)
    follower_rank -= 1
