import toml
import argparse
import logging
import Logins

LOGFILE='my_liff.log'
parser = argparse.ArgumentParser(description='LIFF tests')  
parser.add_argument('--url'      , help='LIFF URL')
parser.add_argument('--id'       , help='LIFF ID')
parser.add_argument('--pw'       , help='LIFF PW')
parser.add_argument('-f','--file', help='import config file (toml format)')
parser.add_argument('--gha'      , action='store_true', help='for GitHubActions') # --gha がつくとTrue
parser.add_argument('--headless' , action='store_true', help='selenium headless mode')
parser.add_argument('--logging'  , default='INFO', help='logging level',
                    choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'])

args = parser.parse_args() 

# フォーマットを定義
formatter = '%(asctime)s:%(levelname)s: %(message)s'

# ログレベルを 変更
LOGLEVEL='logging.' + args.logging
logging.basicConfig(filename=LOGFILE,
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

# 予約結果確認
result = '予約済みです'
while result == '予約済みです':
    # ステップ1処理
    try:
        my_liff.input_data()
    except Exception as e:
        logging.error('step1失敗', str(e))

    # カレンダー選択
    try:
        my_liff.select_calendar()   
    except Exception as e:
        logging.error('カレンダー選択失敗', str(e))

    result = my_liff.check_result()
    logging.info('予約結果確認 %s', result)

my_liff.quit(args.logging)
