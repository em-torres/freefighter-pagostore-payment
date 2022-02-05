import os, requests, sys, time, unittest
from bs4 import BeautifulSoup
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# CONSTANTS
WAIT_TIME = 15
WAIT_INLINE_TIME = 5

# VARIABLES
user_id = 2803902007

# FUNCTIONS
def open_website(drv, url):
    return drv.get(url)

def wait_for_element(drv, qtype, query):
    element = None
    try:
        element = WebDriverWait(drv, WAIT_TIME).until(
            EC.presence_of_element_located((qtype, query))
        )
    except:
        return false
    return element

def check_if_element_exist(drv, qtype, query):
    time.sleep(3)
    try:
        element = drv.find_element(qtype, query)
    except NoSuchElementException:
        element = None
    return element

def click_if_exists(drv, element):
    if element:
        element.click()
        return
    print("-----" + element + " not found -----")
    drv.quit()

def fill_if_exists(drv, element, content):
    if element:
        element.send_keys(content)
        return
    print("-----" + element + " not found -----")
    drv.quit()

def bypass_captcha(drv, element):
    click_if_exists(driver, el_captcha_box)
    time.sleep(WAIT_INLINE_TIME)
    
    

# INIT
options=ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(
    ChromeDriverManager(os_type="windows").install(),
    options=options
)

# RUNTIME
open_website(driver, "https://pagostore.com")
el_free_fire_first_button = wait_for_element(driver, By.CSS_SELECTOR, '[alt="Recarga Free Fire"]')
click_if_exists(driver, el_free_fire_first_button)
el_free_fire_second_button = wait_for_element(driver, By.XPATH, '//*[contains(text(), "ID de jugador")]')
click_if_exists(driver, el_free_fire_second_button)

loop = True

while loop:    
    el_user_id_field = wait_for_element(driver, By.XPATH, '//input[@placeholder="ID de jugador"]')
    el_user_id_field.clear()
    fill_if_exists(driver, el_user_id_field, user_id)
    time.sleep(WAIT_INLINE_TIME)
    el_captcha_box = check_if_element_exist(driver, By.XPATH, '//*[contains(@title, "reCAPTCHA")]')
    el_btn_submit_freefire_userid = wait_for_element(driver, By.XPATH, '//input[@value="Ingresar"]')

    if el_captcha_box:
        bypass_captcha(driver, el_captcha_box)
        time.sleep(WAIT_INLINE_TIME)
        click_if_exists(driver, el_btn_submit_freefire_userid)
    else:
        click_if_exists(driver, el_btn_submit_freefire_userid)
    
    time.sleep(WAIT_INLINE_TIME)
    el_box_user_id = check_if_element_exist(driver, By.XPATH, '//*[contains(text(), "Inicia sesión con tu ID de jugador")]')
    
    if not el_box_user_id:
        loop=False


time.sleep(WAIT_TIME)
print("estamos dentro")

# CLOSING
driver.quit()



# class SeleniumCBT(unittest.TestCase):
#     def setUp(self):
#         self.username = "YOUR_USERNAME"
#         self.authkey = "YOUR_AUTHKEY"

#         self.api_session = requests.Session()
#         self.api_session.auth = (self.username,self.authkey)
#         self.test_result = None

#         caps = {}
#         caps['name'] = 'React App Example'
#         caps['browserName'] = 'Chrome'
#         caps['version'] = '75'
#         caps['platform'] = 'Windows'
#         caps['record_video'] = 'true'

#         try:
#             self.driver = webdriver.Remote(
#             desired_capabilities=caps,

#             command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username, self.authkey))

#         except Exception as e:
#             raise e
#     def test_CBT(self):
#         try:
#             self.driver.implicitly_wait(10)

#             self.driver.get('https://alik0211.github.io/pokedex/')

#             search_box = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/input')
#             search_box.send_keys('vaporeon')

#             result = self.driver.find_element_by_css_selector('#root > div > ul > li > div > p')

#             self.assertEqual(result.text, 'vaporeon')

#             self.test_result = 'pass'

#         except AssertionError as e:
#             # log the error message, and set the score to "during tearDown()"
#             self.api_session.put('https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id + '/snapshots/' + snapshot_hash,
#                 data={'description':"AssertionError: " + str(e)})
#             self.test_result = 'fail'
#             raise

#         self.driver.quit()
#         # Here we make the api call to set the test's score
#         # Pass if it passes, fail if an assertion fails, unset if the test didn't finish
#         if self.test_result is not None:
#             self.api_session.put('https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id,
#                 data={'action':'set_score', 'score':self.test_result})

# if __name__ == '__main__':
#     unittest.main()
