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
