import toml
import argparse
import logging
import Logins

parser = argparse.ArgumentParser(description='LIFF tests')  
parser.add_argument('--url'     , help='LIFF URL')
parser.add_argument('--id'      , help='LIFF ID')
parser.add_argument('--pw'      , help='LIFF PW')
parser.add_argument('-f'        , '--file', help='import config file (toml format)')
parser.add_argument('--gha'     , action='store_true', help='for GitHubActions') # --gha がつくとTrue
parser.add_argument('--headless', action='store_true', help='selenium headless mode')
parser.add_argument('--logging' , default='INFO', help='logging level')

args = parser.parse_args() 

# フォーマットを定義
formatter = '%(asctime)s:%(levelname)s: %(message)s'

# ログレベルを 変更
LOGLEVEL='logging.' + args.logging
logging.basicConfig(filename='my.log',
                    level=eval(LOGLEVEL),
                    format=formatter,
                    datefmt='%Y-%m-%d %H:%M:%S')

# -f 指定がある場合
if(args.file):
    my_file  = toml.load(open(args.file))
    LIFF_URL = my_file['LIFF_URL']
    LIFF_ID  = my_file['LIFF_ID']
    LIFF_PW  = my_file['LIFF_PW']

# --gha オプションがある場合
if(args.gha):
    LIFF_URL = args.url
    LIFF_ID  = args.id
    LIFF_PW  = args.pw
    HEADLESS = True

# ヘッドレスモードの設定
HEADLESS = True if args.headless else False

logging.debug('LIFF_URL %s', LIFF_URL)
logging.debug('LIFF_ID %s', LIFF_ID)
logging.debug('LIFF_PW %s', LIFF_PW)
logging.debug('HEADLESS %s', HEADLESS)

my_liff = Logins.Liff(LIFF_URL, LIFF_ID, LIFF_PW, HEADLESS)


# ログイン処理
try: 
    my_liff.login()

except Exception as e:
    logging.error('ログイン失敗', str(e))

# ステップ1処理
try:
    my_liff.input_step1()

except Exception as e:
    logging.error('step1失敗', str(e))

# カレンダー選択
try:
    my_liff.select_calendar()

except Exception as e:
    logging.error('カレンダー選択失敗', str(e))

'''
try:
    # 分類1を入力
    cat1_box = driver.find_element_by_id("input-33")
    cat1_box.send_keys('PNL1')
    cat1_box.send_keys(Keys.ENTER)

    # 分類2を入力
    cat2_box = driver.find_element_by_id("input-39")
    cat2_box.send_keys('PNL2')
    cat2_box.send_keys(Keys.ENTER)

    # 分類3を入力
    cat3_box = driver.find_element_by_xpath(CAT3_XPATH)
    cat3_box.send_keys('PNL3')
    cat3_box.send_keys(Keys.ENTER)

    # 送信
    cat3_box.submit()
    time.sleep(1)

    # カレンダーで次へを選択
    btn_calendar_next = driver.find_element_by_xpath(CALENDAR_NEXT)
    btn_calendar_next.click()
    time.sleep(1)

    # カレンダーで日付を選択
    btn_calendar_select = driver.find_element_by_xpath(CALENDAR_SELECT)
    btn_calendar_select.click()
    time.sleep(1)

    # カレンダーで日付を確定
    btn_calendar_decide = driver.find_element_by_xpath(CALENDAR_DECIDE)
    btn_calendar_decide.click()
    time.sleep(1)

    # カレンダーで日付を確認
    btn_calendar_confirm = driver.find_element_by_xpath(CALENDAR_CONFIRM)
    btn_calendar_confirm.click()
    time.sleep(1)

    # カレンダーで日付を予約確定
    btn_calendar_reserve = driver.find_element_by_xpath(CALENDAR_RESERVE)
    btn_calendar_reserve.click()
    time.sleep(1)

    # カレンダー予約済みダイアログ
    if(driver.find_element_by_xpath(DIALOG_MESSAGE)):
        driver.back()

except Exception as e:
    logging.error('%s', str(e))
'''

my_liff.quit()