#!/usr/bin/env python3
import os
import sys
import argparse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def get_args():
# 引数取得
    parser = argparse.ArgumentParser()

    # 通常の引数指定
    if sys.stdin.isatty():
        parser.add_argument("message", help = "Mail Message", type = str)
    # パイプライン経由
    else:
        parser.add_argument("message", help = "Mail Message", nargs = "?", type = str, default = sys.stdin.read())

    parser.add_argument("-f", help = "Send from Address", default = os.environ.get('FROM_ADDRESS'))
    parser.add_argument("-t", "--to", help = "Send to Address", default = os.environ.get('TO_ADDRESS'))
    parser.add_argument("-s", "--subject", help = "Message Subject", default = os.environ.get('SUBJECT'))
    parser.add_argument("-k", "--key", help = "SendGrid API-KEY", default = os.environ.get('API_KEY'))

    args = parser.parse_args()

    return(args)

def to_sendgrid(args):
# SendGridへAPIにて送信
    message = Mail(
        from_email = args.f,
        to_emails = args.to,
        subject = args.subject,
        plain_text_content = args.message)

    sg = SendGridAPIClient(args.key)
    response = sg.send(message)
    # debug
    #print(response.status_code)
    #print(response.body)
    #print(response.headers)

def main():

    args = get_args()
    to_sendgrid(args)

if __name__ == "__main__":
    main()
