from selenium import webdriver
from selenium.webdriver.common.keys import Keys

my_links_clicked = input("Enter how much links you wanna open!")
latest = int(my_links_clicked)
my_link_to_be_click = str(input("Enter Link Address!"))
for i in range(1, latest):
    driver = webdriver.Chrome()
    driver.get(my_link_to_be_click)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    driver.get(my_link_to_be_click)
    driver.close()
