import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# CAT3_XPATH    ="/html/body/div/div/div[1]/div/div[1]/div[1]/div/div/form/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[3]/div/div[1]/div[1]/input[1]"
# CAT3_XPATH    ="/html/body/div/div/div[1]/div/div[1]/div[1]/div/div/form/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/following-sibling::div/input"
CAT3_XPATH      ="/html/body/div/div/div[1]/div/div[1]/div[1]/div/div/form/div[1]/div/div/div/div/div/div[3]/div/div/div/div[3]/div/div[1]/div[1]/input[1]"                    
CALENDAR_NEXT   ="/html/body/div/div/div/div/div[1]/div/div/div/div[1]/div/button[2]"

# CALENDAR_SELECT ="/html/body/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[2]/td[5]"
def set_calendar_xpath(row, col):
    CALENDAR_SELECT ="/html/body/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[" + str(row) + "]/td[" + str(col) + "]"
    logging.info('CALENDAR_SELECT %s', CALENDAR_SELECT)
    return CALENDAR_SELECT

CALENDAR_DECIDE ="/html/body/div/div/div/div/footer/div/div/div/button[2]"
CALENDAR_CONFIRM="/html/body/div/div/div[3]/div/div/div/div[3]/div/button"
CALENDAR_RESERVE="/html/body/div/div/div[1]/div/footer/div/div/div/button[2]"
DIALOG_MESSAGE  ="/html/body/div/div/div[4]/div/div/div/div/div"

class Liff:

    def __init__(self, url, login_name, login_pw, headless):
        self.url          = url
        self.login_name   = login_name
        self.login_pw     = login_pw
        self.calendar_row = 1
        self.calendar_col = 2
        self.options      = Options()
        if(headless):self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)

    # ログイン
    def login(self):
        logging.info('ログイン開始')
        self.driver.get(self.url)
        time.sleep(2)
        id_box = self.driver.find_element_by_name('tid')
        pw_box = self.driver.find_element_by_name('tpasswd')
        id_box.send_keys(self.login_name)
        pw_box.send_keys(self.login_pw)
        pw_box.submit()
        logging.info('ログイン成功')

    def input_data(self):
        logging.info('入力開始')
        logging.info('分類1入力')
        time.sleep(4)
        #1回目 /html/body/div/div/div/div/div[1]/div[1]/div/div/form/div[1]/div/div/div/div/div/div[3]/div/div/div/div[1]/div/div[1]/div[1]/input[1]
        #2回目 (同じ？)
        my_xpath1 = '/html/body/div/div/div/div/div[1]/div[1]/div/div/form/div[1]/div/div/div/div/div/div[3]/div/div/div/div[1]/div/div[1]/div[1]/input[1]'
        cat1_box = self.driver.find_element_by_xpath(my_xpath1)
        cat1_box.send_keys('PNL1')
        cat1_box.send_keys(Keys.ENTER)
        time.sleep(0.5)

        logging.info('分類2入力')
        #1回目 /html/body/div/div/div[1]/div/div[1]/div[1]/div/div/form/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/div[1]/input[1]
        #2回目 /html/body/div/div/div[1]/div/div[1]/div[1]/div/div/form/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/div[1]/input[1]
        my_xpath2 = '/html/body/div/div/div[1]/div/div[1]/div[1]/div/div/form/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/div[1]/input[1]'
        cat2_box = self.driver.find_element_by_xpath(my_xpath2)
        cat2_box.send_keys('PNL2')
        cat2_box.send_keys(Keys.ENTER)
        time.sleep(0.5)

        logging.info('分類3を入力')
        cat3_box = self.driver.find_element_by_xpath(CAT3_XPATH)
        cat3_box.send_keys('PNL3')
        cat3_box.send_keys(Keys.ENTER)
        time.sleep(0.5)

        logging.info('「カレンダー設定に進む」をクリック')
        cat3_box.submit()
        time.sleep(1)
        logging.info('クリック終了')

    def select_calendar(self):

        logging.info('カレンダーで次へを選択')
        btn_calendar_next = self.driver.find_element_by_xpath(CALENDAR_NEXT)
        btn_calendar_next.click()
        time.sleep(0.5)

        logging.info('カレンダーで日付を選択')
        btn_calendar_select = self.driver.find_element_by_xpath(set_calendar_xpath(self.calendar_row, self.calendar_col))
        btn_calendar_select.click()
        time.sleep(0.5)

        logging.info('カレンダーで日付を確定')
        btn_calendar_decide = self.driver.find_element_by_xpath(CALENDAR_DECIDE)
        btn_calendar_decide.click()
        time.sleep(0.5)

        logging.info('カレンダーで日付を確認')
        btn_calendar_confirm = self.driver.find_element_by_xpath(CALENDAR_CONFIRM)
        btn_calendar_confirm.click()
        time.sleep(0.5)

        logging.info('カレンダーで日付を予約確定')
        btn_calendar_reserve = self.driver.find_element_by_xpath(CALENDAR_RESERVE)
        btn_calendar_reserve.click()
        time.sleep(2)
        logging.info('カレンダー選択終了')

    def check_result(self):

        try:
            if(self.driver.find_element_by_xpath('//*[contains(text(), "予約が完了しました")]')):
                return '予約が完了しました'
        except:
            pass

        try:
            if(self.driver.find_element_by_xpath('//*[contains(text(), "予約済みです")]')):
                logging.info('row: %s col: %s は予約状態のため1コマ先を予約します', self.calendar_row, self.calendar_col)
                self.driver.back()
                self.calendar_row += 1
                time.sleep(2)
                return '予約済みです'
        except:
            return '正しく確認できず'


    def quit(self, logging_level):
        logging.info('All done')
        if(logging_level == 'DEBUG'): input('Input Enter Key...')
        self.driver.quit()