# jpntdy
Send JAPAN TODAY's articles to Kindle Paper White

# メールアドレスと認証情報の設定
jpntdy/configs/email.py
上記ファイルに

FROM_ADDRESS = 送信元アドレス
MY_PASSWORD = 上のアドレスのパスワード
TO_ADDRESS = Kindleの送信アドレス@kindle.com
CC_ADDRESS = CCのアドレス
SUBJECT = 'JapanToday朝刊'

を定義する

# PDFの保存先ファイルの作成
jpntdy/pdfs を作成する

# 実行
実行するには
python3 JapanTodayList.py　をオプションなしで実行

# それぞれのモジュールの役割
JapanTodayList
->JapanTodayのFeedから各記事へのリンクを取得，保存，メール添付

JapanTodayArticle
->JapanTodayListから各記事のリンクを受け取り，実際に内容を取得して
タイトルや本文を取得

ArticleToPdf
->JapanTodayArticleで取得した内容をKindle用にPDF化する

send_mail
->生成したPDFをKindleに送信する
