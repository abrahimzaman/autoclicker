#Author: Abrahim Zaman A.
#Date:   21.02.2021.
#Programming Language: Python.
#Last Updated: 23.02.2021.
#MIT Licensed.
#Version: 1.0.1
#Libraries: Selenium, ChromeWebDrivers

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

my_links_clicked = input("Enter how much links you wanna open! \n")
latest = int(my_links_clicked)
my_link_to_be_click = str(input("Enter Link Address! \n"))
for i in range(1, latest):
	try:
		driver = webdriver.Chrome()
		driver.get(my_link_to_be_click)
		driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
		driver.get(my_link_to_be_click)
		driver.close()
	except Exception:
		print("Error!")
		break
