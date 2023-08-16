import imapclient
from backports import ssl
from OpenSSL import SSL
from email.header import decode_header
import datetime
import re

def loginGmail(gmailAddress, gmailAppPassword):
    # SSL暗号化
    context = ssl.SSLContext(SSL.TLSv1_2_METHOD)

    # IMAP接続用のオブジェクト作成
    imap = imapclient.IMAPClient("imap.gmail.com", ssl=True, ssl_context=context)

    # IMAPサーバーログイン
    imap.login(gmailAddress,gmailAppPassword)

    # 全てのメールフォルダ情報を表示
    print(imap.list_folders())

    return imap

def getGmailClient1(config_ini):
    client1 = loginGmail(   gmailAddress=config_ini['Email']['GMAIL_USER1'],
                            gmailAppPassword=config_ini['Email']['GMAIL_PASSWORD1'])

    return client1

def getGmailClient2(config_ini):
    client2 = loginGmail(   gmailAddress=config_ini['Email']['GMAIL_USER2'],
                            gmailAppPassword=config_ini['Email']['GMAIL_PASSWORD2'])

    return client2

def getGmailClient3(config_ini):
    client3 = loginGmail(   gmailAddress=config_ini['Email']['GMAIL_USER3'],
                            gmailAppPassword=config_ini['Email']['GMAIL_PASSWORD3'])

    return client3




def getEmail():

    print("送ったてい")

#     client = loginGmail(  gmailAddress=config_ini['Email']['GMAIL_USER1'],
#                         gmailAppPassword=config_ini['Email']['GMAIL_PASSWORD1'])

#     # メールフォルダを指定
#     client.select_folder("INBOX", readonly=True)

#     messages = client.search(['FROM', 'example@example.com'])

#     search_word = "【ご依頼】"

#     print("検索開始")

#     for msgid, data in imap.fetch(messages,['ENVELOPE']).items():
#         envelope = data[b'ENVELOPE']

#         subject = decode_header(envelope.subject.decode())

#         if subject[0][1]:
#             subject = subject[0][0].decode(subject[0][1])
#         else:
#             subject = subject[0][0]

#         print(subject)

        # if search_word in subject:
        #     print('Message %d: %s' % (msgid, subject))
        #     return subject


    # #① 検索キーワードを設定 & 検索キーワードに紐づくメールID検索
    # KWD = imap.search(["ここに検索キーワードを記載する"])

    # #② メールID→メール本文取得
    # raw_message = imap.fetch(KWD,["BODY[]"])

    # print(KWD)




def getRedmineEmail(client):

    # メールフォルダを指定
    client.select_folder("INBOX", readonly=True)

    # 直近24時間のメールを指定
    date = (datetime.datetime.now() - datetime.timedelta(hours=24)).strftime("%d-%b-%Y")

    messages = client.search(['FROM', 'hackAP566i@gmail.com', 'SINCE', date])

    return messages

def getRedmineIdsFromEmail(client):
    messages = getRedmineEmail(client)

    ids=[]

    # 日本語対応検索
    for msgid, data in client.fetch(messages,['ENVELOPE']).items():
        envelope = data[b'ENVELOPE']

        subject = decode_header(envelope.subject.decode())

        if subject[0][1]:
            subject = subject[0][0].decode(subject[0][1])
        else:
            subject = subject[0][0]

        print(subject)
        match = re.search(r'\[SOC - Alert #\d+\]', subject)

        if match:
            tmp = re.search(r'#(\d+)', match.group(0))
            number = tmp.group(1)
            print(number)
            ids.append(number)

    return list(set(ids)) # 重複排除したリスト

def sendEmail():
    print("送りました")

#getEmail()