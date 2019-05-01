from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By

driver_path = r"path"
driver = webdriver.Chrome(executable_path=driver_path)


# html = etree.HTML(driver.page_source)
# text = html.xpath("//input[@type='submit']/@value")
# print(text)


"""ページタグを閉じる"""
#driver.close()

"""ブラウザ全体を閉じる"""
#driver.quit()

"""ソースを見る"""
#print(driver.page_source)

"""idで要素取得"""
#inputTag = driver.find_element_by_id('kw')
#inputTag.send_keys('python')

"""nameで要素を取得"""
# inputname=driver.find_element_by_name('wd')
# inputname.send_keys('python')

"""classで取得"""
# inputclass = driver.find_element_by_class_name('s_ipt')
# inputclass.send_keys('python')

"""xpathで取得"""
# inputxpath = driver.find_element_by_xpath("//input[@class='s_ipt']")
# inputxpath.send_keys('python')

"""cssで取得"""
# inputcss = driver.find_element_by_css_selector(".quickdelete-wrap > input")
# inputcss.send_keys('python')

"""別の書き方"""
# inputcss = driver.find_elements(By.CSS_SELECTOR,".quickdelete-wrap > input")[0]
# inputcss.send_keys('python')

"""click検索練習"""
# driver.get('https://www.baidu.com/')
# inputTag = driver.find_element_by_id('kw')
# inputTag.send_keys('python')
# time.sleep(1)
# inputButton = driver.find_element_by_id('su')
# inputButton.click()

"""ドライブを待たせる"""
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# WebDriverWait(driver, 10).until(
#                                          ここで条件を指定
#     EC.presence_of_all_elements_located((By.ID, 'anony-video'))
# )

"""ipエージェント"""
# options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server=http://182.207.232.135:49166")
# driver_path = r"C:\Users\tian.xiaoyi\Desktop\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
# driver.get('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false')


"""新しいウィンドウを開く"""
# driver.execute_script("window.open('https://www.douban.com/')")

"""現在の開いてるウィンドウオブジェクト全部取得"""
#driver.window_handles

"""ウィンドウ切替"""
# driver.switch_to_window(driver.window_handles[1])

"""現在見てるウィンドウのurlを取得"""
# print(driver.current_url)
"""現在見てるウィンドウを閉じる"""
# driver.close()

"""テスト"""
# driver.get('http://baidu.com')
# driver.execute_script("window.open(https://www.douban.com/)")
# driver.switch_to_window(driver.window_handles[1])
# time.sleep(5)
# driver.switch_to_window(driver.window_handles[0])
# driver.close()

"""画面スクロール(スクロールによるデータ取得用)"""
# for i in range(1, 3):
#     browser.execute_script(
#         "window.scrollTo(0,document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")#
#     time.sleep(3)

#chromedriver画像のロードしない設定
chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_opt.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(executable_path='D:\program\spider\chromedriver_win32\chromedriver.exe',chrome_options=chrome_opt)
browser.get("https://www.taobao.com")

#phantomjs,不可視化のブラウザでクロール(並行処理してると、性能は落ちる)linuxで本領発揮
browser = webdriver.phantomjs(executable_path='phantomjs driverのpath')
browser.get('url')
#ブラウザ表示しないため絶対とじるコードが必要
browser.quit()

driver.get("https://hlo.tohotheater.jp/net/movie/TNPI3090J01.do")
html = driver.page_source
print(html)
