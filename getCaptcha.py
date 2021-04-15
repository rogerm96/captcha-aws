import time
import PIL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


x = 1

while x <= 1:

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    browser = webdriver.Chrome(executable_path=r"./driver/chromedriver", options=options)

    browser.get('http://contribuyente.seniat.gob.ve/iseniatlogin/contribuyente.do')

    captcha = browser.find_element_by_id('kaptchaImage')

    screenshot = captcha.screenshot_as_png
    with open('captcha%s.png' % x, 'wb') as f:
        f.write(screenshot)
    
    img = Image.open('captcha%s.png' % x)
    img = img.resize((200, 50), Image.ANTIALIAS)
    img.save('captcha%s.png' % x)

    time.sleep(2)

    #browser.close()

    x+=1