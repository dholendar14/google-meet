from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {

    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(options=opt, executable_path=r'C:\Program Files (x86)\chromedriver.exe')


def google_signin():
    driver.get("https://apps.google.com/intl/en/meet/")
    sign_in = driver.find_element_by_xpath('/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a').click()
    email = driver.find_element_by_id("identifierId")
    email.send_keys("cse17jn1a0575@gmail.com")
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
    time.sleep(5)
    password = driver.find_element_by_name("password")
    password.send_keys("svcn575#@!") # replace the password
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
    time.sleep(10)


def mic_off():
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span/span/div/div[1]/div').click()


def camera_off():
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div/div').click()


def meet_join():
    meet_id = driver.find_element_by_xpath('//*[@id="i3"]')
    meet_id.send_keys("amz gmgq ieh")
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[2]/div[2]/button/span').click()
    time.sleep(5)
    mic_off()
    time.sleep(1)
    camera_off()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span').click()


if __name__ == '__main__':
    google_signin()
    meet_join()
    time.sleep(100)
    people = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[2]/div/div')
    while int(people.text) != 0:
        if int(people.text) < 15:
            driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[6]/span/button').click()
            break
        else:
            time.sleep(10)
