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
    * 何もつけないとpushトリガーになる

```
$ act pull_request
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


my.env は act をローカルで試す際に使う
git上は、.gitignore対象にしてある


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