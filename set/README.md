## 構成

```
.
├── main.py          // LIFFテストのメイン
├── manipulate.py    // main.pyのオブジェクト・関数
├── README.md        // これ
├── my-example.env   // act確認のサンプルファイル
└── my.env           // act確認の設定ファイル(.gitignore対象)
```

## 環境変数
GitHubActionsのseqretsに入れる値

|  変数名  |             意味             |
| -------- | ---------------------------- |
| LIFF_URL | LIFFのURL                    |
| LIFF_ID  | LINEログインに使うID         |
| LIFF_PW  | LINEログインに使うパスワード |

## 使用方法

* ファイル指定

```
python main.py -f my.env
```

* headlessモード

```
python main.py --headless true
```

* usage

```
python main.py -h

```

## 備忘
### Actions and ACT

* チェックアウトしないと working-directory は有効にならない

```
      - uses: actions/checkout@v2
```

* pull requestをイベントトリガーにして実施

```
$ act pull_request
```

* 何もつけないとpushトリガーになる

```
$ act
```

* dry run
    * -n をつける

```
act pull_request -n
```

* jobのlistを表示
    * -l 

```
$ act -l pull_request
```

To use a different image for the runner, use the -P option.

```
act -P <platform>=<docker-image>
```

* secrets値を使う

```
act --secret-file my.env pull_request
```

### Selenium

* オプションでログレベルを変えることができる
* ただ、secretsの内容とかも出力されるから使わない

```
        self.options.add_argument("--log-level=1")
        self.driver = webdriver.Chrome(
                                options=self.options,
                                service_args=["--log-path=my.log"]
                                )
```

* (ローカル開発などで)残ってしまったchromeを一括削除する

```
killall chromedriver
```

* macだとcommand+tabに残り続けるので、できるだけ `try and except` を適用した方がよい

* 表示されていない箇所はクリックできない
    * headlessmodeであっても


### 参考URL
* 最新のGitHubActions環境
    * https://github.com/actions/virtual-environments/
* act
    * https://github.com/nektos/act#configuration
* actを使うとGithub Actionsのワークフロー定義をローカルで確認しながらやれて便利
    * https://masaru-tech.hateblo.jp/entry/2020/07/17/100621
* [GitHub]Actionsの動作確認時は忘れずにACTIONS_RUNNER_DEBUGとACTIONS_STEP_DEBUGを設定しよう
    * https://dev.classmethod.jp/articles/set-secrets-before-actions-test/
* argpaseの解説
    * https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0
* loggingのタイムスタンプ設定方法
    * https://www.it-swarm.jp.net/ja/python/python%E3%83%AD%E3%82%AE%E3%83%B3%E3%82%B0%E3%81%AE%E6%99%82%E9%96%93%E5%BD%A2%E5%BC%8F%E3%82%92%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%9E%E3%82%A4%E3%82%BA%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95%E3%81%AF%EF%BC%9F/969378224/
* [selenium]「含む」テキスト検索
    * https://stackoverflow.com/questions/12323403/how-do-i-find-an-element-that-contains-specific-text-in-selenium-webdriver-pyth
* クローラ作成に必須！XPATHの記法まとめ
    * https://qiita.com/rllllho/items/cb1187cec0fb17fc650a
* [Python] seleniumで.click()ができない
    * https://hacknote.jp/archives/51261/