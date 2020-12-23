from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path='/Users/glebsvarcer/Downloads/chromedriver',options=chrome_options)
driver.get('file:///Users/glebsvarcer/Downloads/Reflection-2020-Dec-22_12-38-01/index.html#!/modules')
for i in range(1,16):
    xpath = '/html/body/div/div/div[2]/div[8]/table/tbody/tr['+str(i)+']/td/div/div[2]/span/span/a'
    driver.find_element_by_xpath(xpath).click()
    ele = driver.find_element_by_id('app')
    total_height = ele.size["height"]
    if total_height > 2700:
        for d in range(total_height//2700+1):
            driver.execute_script("window.scrollTo(0, "+str(2700*d)+")") 
            driver.set_window_size(1920, 2700)
            driver.save_screenshot('screen'+str(i)+'-'+str(d)+'.png')
    else:
        driver.set_window_size(1920, total_height)  
        driver.save_screenshot('screen'+str(i)+'.png')
    driver.back()