import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Liff:

    def __init__(self, url, login_name, login_pw):
        self.url = url
        self.login_name = login_name
        self.login_pw = login_pw
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument("--log-level=1")
        self.driver = webdriver.Chrome(
                                options=self.options,
                                service_args=["--log-path=mylog.log"]
                                )

    def login(self):
        self.driver.get(self.url)
        time.sleep(3)

        # ログイン
        id_box = self.driver.find_element_by_name('tid')
        pw_box = self.driver.find_element_by_name('tpasswd')
        id_box.send_keys(self.login_name)
        pw_box.send_keys(self.login_pw)
        pw_box.submit()
        print('LIFF Login done')


    def quit(self):
        # input() # ローカルで実施する場合
        print('All done')
        self.driver.quit()