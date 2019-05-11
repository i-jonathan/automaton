from selenium import webdriver
import pandas as pd

option = webdriver.ChromeOptions()
option.add_extension('integration.crx')
driver = webdriver.Chrome(options=option)
df = pd.read_csv('getcomics.csv', index_col='Index')

try:
    for i in range(len(df)):
        error = 0
        title = str(df.Title[i]).lower().replace(' ', '-')
        link = 'https://getcomics.info/' + str(df.Category[i]) + '/' + title + '-' + str(df.Issue[i]) + '-' + \
               str(df.Year[i]) + '/'
        success_issue = df.Issue[i]
        success_year = df.Year[i]

        while error < 3:
            if error == 2:
                error = 0
                df.Issue[i] = success_issue
                df.Year[i] = success_year
                break

            else:
                driver.get(link)

                if driver.find_elements_by_class_name('error404'):
                    error += 1
                    print(
                        str(df.Title[i]) + ' ' + str(df.Issue[i]) + ' with year ' + str(df.Year[i]) + ' doesn\'t exist')
                    df.Year[i] += 1
                    link = 'https://getcomics.info/' + str(df.Category[i]) + '/' + title + '-' + str(
                        df.Issue[i]) + '-' + str(df.Year[i]) + '/'

                else:
                    driver.find_element_by_link_text('Download Now').click()
                    print('Downloading ' + str(df.Title[i]) + ' Issue ' + str(df.Issue[i]))
                    success_issue = df.Issue[i] + 1
                    success_year = df.Year[i]
                    df.Issue[i] += 1
                    error = 0
                    link = 'https://getcomics.info/' + str(df.Category[i]) + '/' + title + '-' + str(
                        df.Issue[i]) + '-' + str(df.Year[i]) + '/'

finally:
    driver.quit()
    df.to_csv('getcomics.csv')
