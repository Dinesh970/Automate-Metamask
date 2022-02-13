import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
import time
import os
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_extension(r"C:\Users\ASUS\Downloads\extension_10_9_0_0.crx")

driver = webdriver.Chrome(executable_path=r"C:\Users\ASUS\Downloads\chromedriver.exe", chrome_options=chrome_options)
#driver = webdriver.Chrome(r"C:\Users\ASUS\Downloads\chromedriver.exe")

driver.get("https://play.pegaxy.io/marketplace")

actions = action_chains.ActionChains(driver)

time.sleep(5)

driver.switch_to.window(driver.window_handles[0])

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Get Started')]")))

element = driver.find_element(By.XPATH, "//*[contains(text(), 'Get Started')]")

element.click()

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Import wallet')]")))

element = driver.find_element(By.XPATH, "//*[contains(text(), 'Import wallet')]")

element.click()

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'I Agree')]")))

element = driver.find_element(By.XPATH, "//*[contains(text(), 'I Agree')]")

element.click()

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//input[@placeholder = 'Paste Secret Recovery Phrase from clipboard']")))

element = driver.find_element(By.XPATH, "//input[@placeholder = 'Paste Secret Recovery Phrase from clipboard']")

element.click()

element.send_keys("Enter Your Secret Key")

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='password']")))

element = driver.find_element(By.XPATH, "//*[@id='password']")

element.click()

element.send_keys("Enter Password")

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="confirm-password"]')))

element = driver.find_element(By.XPATH, '//*[@id="confirm-password"]')

element.click()

element.send_keys("Enter Password")

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@class='first-time-flow__checkbox first-time-flow__terms']")))

element = driver.find_element(By.XPATH, "//*[@class='first-time-flow__checkbox first-time-flow__terms']")

element.click()

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Import')][2]")))

element = driver.find_element(By.XPATH, "//*[contains(text(), 'Import')][2]")

element.click()

time.sleep(10
           )
driver.switch_to.window(driver.window_handles[1])

# WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//span[text()='Connect']")))
#
# element = driver.find_element(By.XPATH, "//span[text()='Connect']")
#
# element.click()

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//span[text()='Connect Metamask']")))

element = driver.find_element(By.XPATH, "//span[text()='Connect Metamask']")

element.click()

WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "(//span[text()='Connect Metamask'])[2]")))

element = driver.find_element(By.XPATH, "(//span[text()='Connect Metamask'])[2]")

element.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
window_before = driver.window_handles[0]
WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "(//span[text()='Connect Metamask'])[2]")))

element = driver.find_element(By.XPATH, "(//span[text()='Connect Metamask'])[2]")

element.click()
# handles = driver.window_handles
# for i in handles:
#     driver.switch_to.window(i)
#
#     # print every open window page title
#     print(driver.title)
# window_after = driver.window_handles[1]
# driver.switch_to.window(window_after)
# WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Approve')]")))
#
# element = driver.find_element(By.XPATH, "//*[contains(text(), 'Approve')]")
#
# element.click()
