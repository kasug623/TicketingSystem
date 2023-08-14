import imapclient
from backports import ssl
from OpenSSL import SSL 

import configparser

def getEmail():

    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')
    
    # SSL暗号化
    context = ssl.SSLContext(SSL.TLSv1_2_METHOD)

    # IMAP接続用のオブジェクト作成
    imap = imapclient.IMAPClient("imap.gmail.com", ssl=True, ssl_context=context)

    # ログイン情報
    my_mail = config_ini['Email']['GMAIL_USER']
    app_password = config_ini['Email']['GMAIL_PASSWORD']

    # IMAPサーバーログイン
    imap.login(my_mail,app_password)

    # 全てのメールフォルダ情報を表示
    print(imap.list_folders())

    # メールフォルダを指定
    imap.select_folder("INBOX", readonly=True)

    #① 検索キーワードを設定 & 検索キーワードに紐づくメールID検索
    KWD = imap.search(["ここに検索キーワードを記載する"])

    #② メールID→メール本文取得
    raw_message = imap.fetch(KWD,["BODY[]"])

    print(KWD)

# if __name__ == '__main__':
#     getEmail()

getEmail()