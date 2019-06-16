from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

"""スクリーンショットを取る用の関数定義"""
def screenshot(driver, file_path=None):
    # もしpathがなければ
    if file_path == None:
        project_path = os.path.dirname(os.getcwd())
        file_path = project_path + '\image\'
        if not os.path.exists(file_path):
           os.mkdir(file_path)
        image_nmae = time.strftime("%Y%m%d-%H%M%S",time.localtime())
        file_path = file_path + image_name + ".png"
        print(file_path)
    driver.save_screenshot(file_path)

"""cookiesの方式の一つ"""
def save_cookies(driver):
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path+"\cookies\"
    if not os.path.exists(file_path):
       os.mkdir(file_path)
    cookies = driver.get_cookies()
    
    with open(file_path + "jd.cookies", "w") as c:
        # jsonのdump方法を使用
        json.dump(cookies,c)

try:
    driver = webdriver.Chrome("path")
    driver.maximize_window()
    driver.get("url")
    elem = driver.find_element_by_link_text("text")
    
    """マウスの止まる事件"""
    # マウスを指定されたところへ移動
    ActionChains(driver).move_to_element(elem).perform()
    
     """エンターキー事件"""
    search_element = driver.find_element_by_id("key")
    search_element.send_keys("text")
    search_element.send_keys(Keys.RETURN)
    
    """windowの切り替え面白いと思った方法"""
    # 全てのwindos
    handles = driver.window_handles
    # 現在見てるwindow
    current_handle = driver.current_window_handle
    for handle in handles:
        if handle != current_handle:
            driver.switch_to.window(handle)
            # スクリーンショットを取る用の関数にdriverを渡す
            # 関数を定義するのは多少便利さを増すため
            screenshot(driver)
    
finally:
    time.sleep(3)
    driver.quit()
