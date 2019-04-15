HTTP Mail to SendGrid
====

SendGrid経由でメールを送信するスクリプト

## 概要

MTAの無い環境でもSendGridのAPIを利用してメールを送信します。  

## 使い方

SendGritでAPIを発行する。

```
pip install sendgrid
```

`sendgrid.env` がオプション未設定時のデフォルト設定なので必要に応じて記入  

環境変数に設定
```
source ./sendgrid.env
```

オプションを指定して実行(messageは必須)
```
./HTTPMail2SendGrid.py -h
usage: HTTPMail2SendGrid.py [-h] [-f F] [-t TO] [-s SUBJECT] [-k KEY] message

positional arguments:
  message               Mail Message

optional arguments:
  -h, --help            show this help message and exit
  -f F                  Send from Address
  -t TO, --to TO        Send to Address
  -s SUBJECT, --subject SUBJECT
                        Message Subject
  -k KEY, --key KEY     SendGrid API-KEY
```

パイプでテキストデータでも可
```
echo hogehoge | ./HTTPMail2SendGrid.py
```
