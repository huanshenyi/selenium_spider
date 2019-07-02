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

"""cookies保存の方式の一つ"""
def save_cookies(driver):
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path+"\cookies\"
    if not os.path.exists(file_path):
       os.mkdir(file_path)
    cookies = driver.get_cookies()
    
    with open(file_path + "jd.cookies", "w") as c:
        # jsonのdump方法を使用
        json.dump(cookies,c)
        
"""cookiesの使用""" 
def get_url_with_cookies():
    # cookiesファイル読み込む
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    cookies_file = file_path + "jd.cookies"
    jd_cookies_file = open(cookies_file,"r")
    jd_cookies_str = jd_cookies_file.readline()
    # cookiesを取得
    jd_cookies_dict = json.loads(jd_cookies_str)
    # 一回アクセスしてウェブサイトにある旧のcookiesを削除
    time.sleep(2)
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    # cookiesをdriverに挿入
    for cookie in jd_cookies_dict:
        driver.add_cookie(cookie)
    # ログイン成功してるかどうか確認
    driver.get(url)
    

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
   
    """readonly属性を削除"""
    js = "$('input[id=train_date]').removeAttr('readonly')"
    driver.execute_script(js)
    
    """要らない要素を排除(xpath)"""
    $x("//div[@class='ptable-item']//dd[not(@class='Ptable-tips')]")
    
    """elementのクラスなどがスペース入ってる場合class=" class-name " """
    $x("//div[normalize-space(@class)='class-name']")
    
    """xpath函数->子要素が一定の数のものを特定"""
    """dl_elementを特定、その下に三つのdlが存在する"""
    $x("//dl[count(dl)=3]")
    
    """elementの名前が特定のもので始まるの物を特定"""
    $x("//*[starts-with(name(),'dl')]")
    
    """elementの長さで特定"""
    $x("//*[string-length(name())=2]")
    
    """某elementの親要素を特定"""
    $x("//input[@id='loginname']/parent::div")
    
    """某elementの弟elementを特定(同じ親element下の該当elementの後ろにあるelementのこと)"""
    $x("//input[@id='loginname']/following-sibling::div")
    
    """某elementの兄elementを特定(同じ親element下の該当elementの先頭にあるelementを特定)"""
    $x("//input[@id='loginname']/preceding-sibling::*")
    
    """css select"""
    $$("div[class=p-price]")
    """css select一部含む"""
    $$("DIV[id*fitt]")
    """css 某detaで始まる"""
    $$("div[id^=fi]")
    
   
finally:
    time.sleep(3)
    driver.quit()
