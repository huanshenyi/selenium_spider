"""マウスの止まる事件"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

try:
    driver = webdriver.Chrome("path")
    driver.maximize_window()
    driver.get("url")
    elem = driver.find_element_by_link_text("text")
    # マウスを指定されたところへ移動
    ActionChains(driver).move_to_element(elem).perform()
    
    
     """エンターキー事件"""
    search_element = driver.find_element_by_id("key")
    search_element.send_keys("text")
    search_element.send_keys(Keys.RETURN)
    
finally:
    time.sleep(3)
    driver.quit()
