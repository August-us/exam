from selenium import webdriver
import time

from tool.myCSDN import hrefs


def findWord(word='洗杯子问题 csdn'):
    options=webdriver.ChromeOptions()
    # ip=requests.get('http://localhost:5000/get')
    # options.add_argument('--proxy-server=%s'%ip)
    options.add_argument('--headless')
    with webdriver.Chrome(chrome_options=options) as driver:
        driver.get("http://www.baidu.com")
        driver.find_element_by_id("kw").send_keys(word)
        driver.find_element_by_id("su").click()
        # driver.implicitly_wait(3)
        # driver.find_element_by_css_selector(r"#\31  > h3 > a").click()
        # driver.implicitly_wait(3)
        # driver.switch_to.window(driver.window_handles[2])
        # driver.find_element_by_xpath(r'//a[@title="August-us"]').click()

        while True:
            for i in hrefs:
                print(i)
                driver.get(i)
                time.sleep(25)


if __name__ == '__main__':
    findWord()

