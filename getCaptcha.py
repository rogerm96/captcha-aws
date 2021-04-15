import time
import PIL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


x = 1

while x <= 1:

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Chrome(executable_path=r"./driver/chromedriver", chrome_options=chrome_options)

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