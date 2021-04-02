# activemail-scraper
~~けしからん~~素晴らしいWebメール Active!mail から新着メールを Discord に通知する Python スクリプトです．  
スクレイピングしているだけです．cron 等で定時実行させると便利だと思います．


## バグ(仕様)
* 研究室初日の午後の眠い暇な時に雑に作ったのでかなり適当です．  
  特に表示されるまでの待機時間あたりはいい感じになったらプルリクでもしてください．
  調子悪かったら time.sleep() の数値を伸ばしてみてください．

* 2ページ目以降のメールを取得しません．   
  1ページ目に表示されているメールしか監視しません．定時実行する際は取得間隔に気をつけてください．

## 依存
* selenium
* requests
* chrome-driver

## 使い方

### ライブラリをインストール
`$ python3 -m pip install requests selenium`

### chrome-driverをインストール
#### Windows
(ググって)

#### macOS (Big Surで確認)
`# brew tap homebrew/cask`  
`# brew cask install chromedriver`  

#### Linux (CentOS 8で確認)
[参考 (CentOS 7 の通りで動いた)](https://worklog.be/archives/3422)

### 必要事項の入力・実行
watch.py を開き，`user_id`(ユーザーID)，`passwd`(パスワード)，`webhook_url` (Discord の Webhook URL ([なにそれ?(作成項をみて)](https://support.discord.com/hc/ja/articles/228383668-%E3%82%BF%E3%82%A4%E3%83%88%E3%83%AB-Webhooks%E3%81%B8%E3%81%AE%E5%BA%8F%E7%AB%A0))) を入力します．  

main.py を開き，同じく `webhook_url` に Discord Webhook URL を入力します．  
main.py は実行時エラーを監視して通知するものです．いらなければ watch.py を実行だけしても動くと思います．  

`$ python3 main.py`


## 運用している大学へ / Active!mail 開発者様へ
Active!mail に一切の非はありません．   
転送機能を切っている大学がよくないのです．  
そして外部からメールプロトコルによるメール取得を許可しない大学がよくないのです．  
今ではデファクトスタンダードとなっているプッシュ通知が届かない現状は学生にとって苦痛でしかありません．  
もしよろしければ大学のシステムを改善していただく願います．
