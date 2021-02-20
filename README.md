### 構成

```
.
├── LiffTest.py
├── Logins.py
├── README.md
├── my-example.env   // act確認のサンプルファイル
├── my.env           // act確認の設定ファイル(.gitignore対象)
└── test.py
```

### 環境変数
githubactionsのseqretsに入れる値

|  変数名  |             意味             |
| -------- | ---------------------------- |
| LIFF_URL | LIFFのURL                    |
| LIFF_ID  | LINEログインに使うID         |
| LIFF_PW  | LINEログインに使うパスワード |

### 使用方法

* ファイル指定

```
python LiffTest.py -f my.env
```

* headlessモード

```
python LiffTest.py --headless true
```


* 引数なし
    * my.envの値を読み込む

```
python LiffTest.py

```

### Actions and ACT
#### 最新のActions
https://github.com/actions/virtual-environments/

* チェックアウトしないと working-directory は有効にならない

```
      - uses: actions/checkout@v2
```

#### act
https://github.com/nektos/act#configuration

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

### About Selenium

* 残ってしまったchromeを一括削除

```
killall chromedriver
```

### 参考

* actを使うとGithub Actionsのワークフロー定義をローカルで確認しながらやれて便利
    * https://masaru-tech.hateblo.jp/entry/2020/07/17/100621
* [GitHub]Actionsの動作確認時は忘れずにACTIONS_RUNNER_DEBUGとACTIONS_STEP_DEBUGを設定しよう
    * https://dev.classmethod.jp/articles/set-secrets-before-actions-test/
* argpaseの解説
    * https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0