#https://www.youtube.com/watch?v=C6qjpR4WlV8
#https://www.youtube.com/watch?v=Rdd_xEMwCGk
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


x = 1

while x <= 1000:

    browser = webdriver.Chrome(executable_path=r"/home/rhino/opt/chromedriver")

    browser.get('http://contribuyente.seniat.gob.ve/iseniatlogin/contribuyente.do')

    captcha = browser.find_element_by_id('kaptchaImage')

    screenshot = captcha.screenshot_as_png
    with open('captcha%s.png' % x, 'wb') as f:
        f.write(screenshot)
    
    img = Image.open('captcha%s.png' % x)
    img = img.resize((200, 50), Image.ANTIALIAS)
    img.save('captcha%s.png' % x)

    time.sleep(2)

    browser.close()

    x+=1