from selenium import webdriver
import time

path_to_chromedriver = '/Users/xiaoli/Desktop/search/scrape/selenium_test/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=7128761&punumber%3D7128761%26filter%3DAND%28p_IS_Number%3A7138973%29%26pageNumber%3D2&pageNumber=1#'

browser.get(url)

while True:
    try:
        next = browser.find_element_by_xpath('//*[@id="results-blk"]/div[2]/div/a[7]')
        next.click()
        time.sleep(5)
        print browser.current_url
    except:
        break
        