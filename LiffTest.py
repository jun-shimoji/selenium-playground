import sys
import toml
import argparse
import Logins

parser = argparse.ArgumentParser(description='LIFF tests')  
parser.add_argument('--url'     , help='LIFF URL')
parser.add_argument('--id'      , help='LIFF ID')
parser.add_argument('--pw'      , help='LIFF PW')
parser.add_argument('-f'        , '--file', help='import config file (toml format)')
parser.add_argument('--gha'     , action='store_true', help='for GitHubActions') # --gha がつくとTrue
parser.add_argument('--headless', action='store_true', help='selenium headless mode')

args = parser.parse_args() 

print("args.file", args.file)
print("args.headless", args.headless)

CAT3_XPATH      ="/html/body/div/div/div[1]/div/div[1]/div[1]/div/div/form/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[3]/div/div[1]/div[1]/input[1]"
CALENDAR_NEXT   ="/html/body/div/div/div/div/div[1]/div/div/div/div[1]/div/button[2]"
CALENDAR_SELECT ="/html/body/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[3]"
CALENDAR_DECIDE ="/html/body/div/div/div/div/footer/div/div/div/button[2]"
CALENDAR_CONFIRM="/html/body/div/div/div[3]/div/div/div/div[3]/div/button"
CALENDAR_RESERVE="/html/body/div/div/div[1]/div/footer/div/div/div/button[2]"
DIALOG_MESSAGE  ="/html/body/div/div/div[4]/div/div/div/div/div"

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

print('LIFF_URL', LIFF_URL)
print('LIFF_ID', LIFF_ID)
print('LIFF_PW', LIFF_PW)
print('HEADLESS', HEADLESS)

my_liff = Logins.Liff(LIFF_URL, LIFF_ID, LIFF_PW, HEADLESS)


# ログイン処理
try: 
    my_liff.login()

except Exception as e:
    print('error:' + str(e))

"""
# カレンダー選択
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
    print('error:' + str(e))
"""

my_liff.quit()