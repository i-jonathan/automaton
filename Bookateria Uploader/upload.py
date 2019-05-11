from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd
import os

driver = webdriver.Chrome()
df = pd.read_csv('bookateria-uploader.csv', index_col='Index')
b = [30, 29, 47, 2, 8, 50, 70, 64, 21, 76, 71, 59, 1, 80, 79, 9, 56, 73, 67, 81, 14, 77, 55, 40, 51, 11, 44, 68, 31, 62, 46, 48, 13, 61, 10, 39, 0, 37, 42, 74, 28, 60, 66, 19, 69, 41, 43, 83, 15, 63, 57, 65, 25, 58, 3, 17, 7, 36, 5, 12, 45, 26, 6, 34, 4, 27, 78, 20, 38, 49, 22, 18, 54, 52, 75, 16, 24, 82, 35, 53, 23, 72]

driver.get('https://bookateria.net/documents/add-a-document/')
try:
    for i in range(len(b)):
        x = b[i]
        title = str(df.Title[x])
        author = str(df.Author[x])
        description = str(df.Author[x])
        typology = str(df.Type[x])
        path = str(df.Path[x])

        if driver.find_element_by_tag_name('h2').text == 'Login':
            print('Forging Signatures...')
            driver.find_element_by_id("login_username").send_keys('Uploader_bot')
            driver.find_element_by_id("login_password").send_keys('I Upload Stuff')
            driver.find_element_by_id('submit_login').click()
            driver.get('https://bookateria.net/documents/add-a-document/')
            i -= 1
        else:
            print('Doing ', x)
            driver.find_element_by_id("add_title").send_keys(title)
            print('Dinosaurs or Dragons...')
            driver.find_element_by_id("add_author").send_keys(author)
            print('Eggs or Chicken...')
            category = Select(driver.find_element_by_id('add_cat'))
            category.select_by_visible_text(typology)
            print("Found Nemo...")
            driver.find_element_by_id("add_description").send_keys(description)
            print('Holy Cannoli...')
            driver.find_element_by_id('add_file').send_keys(path)
            print('He he he or She she she...')
            driver.find_element_by_id('add_submit').click()
            print('What have you done???')
            print('Do it again!!!')


finally:
    pass