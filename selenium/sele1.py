#在Window上記得下載geckodriver放到python的目錄下
from selenium import webdriver
import time

x=webdriver.Firefox()
time.sleep(3)
x.quit()
