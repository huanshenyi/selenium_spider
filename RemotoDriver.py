from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread

# テスト
def to_baidu(name, server_address):
    driver = webdriver.Remote(
        command_executor=server_address,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    driver.get("url")

my_address = {
    "docker_1": "http://0,0,0,0:4444/wd/hub",
    "docker_2": "http://0,0,0,0:4444/wd/hub"
}

threads = []
for name, url in my_address.items():
    t = Thread(target=to_baidu, args=(name, url))
    threads.append(t)
    
for t in threads:
    t.start()  
