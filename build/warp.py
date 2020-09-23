from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

start = 15
end = 17

driver = webdriver.Chrome()
driver.get('https://subaccount.shopee.com/login/')
sleep(1)

_input = driver.find_elements_by_css_selector(
    'input.shopee-input__input')

usernameInput = _input[0]
usernamePassword = _input[1]
usernameInput.send_keys("maybelline:nhat.duy")
usernamePassword.send_keys("Onpoint@20")
loginButton = driver.find_element_by_css_selector('button[type="button"]')
loginButton.click()
sleep(3)

sellerCenter = driver.find_elements_by_xpath(
    '/html/body/div/div[2]/div/div/div[1]/div/span')
sellerCenter[0].click()
sleep(1)

driver.switch_to.window(driver.window_handles[1])

stores = driver.find_elements_by_xpath(
    '/html/body/div[1]/div[2]/div/div/div[4]/div[2]/div[1]')

stores[0].click()
sleep(2)
driver.find_element_by_xpath(
    "/html/body/div[1]/div[2]/div[1]/div[2]/ul/li[5]/ul/li/a/span[1]").click()

sleep(6)
popupPassword = driver.find_elements_by_xpath(
    '/html/body/div[1]/div[2]/div/div/div/div/div/div/div[1]/form/div[2]/div/div/div/div/input')
if (popupPassword != []):
    popupPassword[0].send_keys("Onpoint@20")
    verify = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div/div/div/div/div/div/div[1]/form/div[3]/button[2]')
    verify.click()
# open wait
openCal = WebDriverWait(driver, 25).until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[2]")))
driver.execute_script("arguments[0].click();", openCal)

# day
action = ActionChains(driver)
byDay = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[2]/ul/li[6]')
action.move_to_element(byDay).perform()

dayPick = driver.find_element_by_xpath(
    f'/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]//*[contains(text(),\'{start}\')]')
driver.execute_script(
    "console.log(arguments);arguments[0].click();", dayPick)
downButton = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/button')

for i in range(start+1, end+1):
    driver.execute_script("arguments[0].click();", downButton)
    driver.execute_script("arguments[0].click();", openCal)
    action.move_to_element(byDay).perform()
    dayPick = driver.find_element_by_xpath(
        f'/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]//*[contains(text(),\'{i}\')]')
    driver.execute_script(
        "console.log(arguments);arguments[0].click();", dayPick)
    sleep(61)
else:
    driver.execute_script("arguments[0].click();", downButton)
