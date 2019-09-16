"""
    YahooのAPIからカテゴリの検索や商品名のxmlファイルを作成するやつ
    python get_xml.py 0or1 category_id outputfile
    0の場合は、カテゴリ名の検索
    1の場合は、商品名の検索

    例：python get_xml.py 0 2499 feed.xml
"""

import requests
import os,sys

url = "https://shopping.yahooapis.jp/ShoppingWebService/V1/"
SearchData = ["categorySearch","itemSearch"]
AppId = "dj00aiZpPVhyTGtnNEZlUUdUTyZzPWNvbnN1bWVyc2VjcmV0Jng9N2U-"

def make_xml(data_num,category_num,output):
    #アクセスするためのURLの作成
    URL = url + SearchData[int(data_num)]+ "?category_id=" + category_num + "&appid=" + AppId
    #print (URL)
    response = requests.get(URL)    #xmlの取得
    #ディレクトリの作成
    file_path = os.path.dirname('./xml/' + output)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    #xmlの書き込み
    with open('./xml/' + output, 'wb') as file:
        file.write(response.content)
    return './xml/' + output

if __name__ == '__main__':
    args = sys.argv
    if(len(args)==4):
        print (args)
        make_xml(args[1],args[2],args[3])
