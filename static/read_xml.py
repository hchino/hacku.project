"""
    カテゴリや商品の検索を行う
    python read_xml.py 0or1 filepath
    0の場合は、カテゴリの検索
    1の場合は、商品の検索

    例：python read_xml.py 0 feed.xml
    例：python read_xml.py 1 Yahoo_Api_1348.xml
"""
import xml.etree.ElementTree as ET
import os, sys


#カテゴリの検索
def Search_Category(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    list = []   #idとカテゴリ名のリスト
    #カテゴリまでのパス？的なの
    Children = root.find("{urn:yahoo:jp:categorySearch}Result").find("{urn:yahoo:jp:categorySearch}Categories").find("{urn:yahoo:jp:categorySearch}Children").getchildren()
    for child in Children:
        #お酒のみ取得
        if(len(child)==4 and int(child.attrib['sortOrder'])<130):
            id = child.find("{urn:yahoo:jp:categorySearch}Id").text #カテゴリID取得
            name = child.find("{urn:yahoo:jp:categorySearch}Title").find("{urn:yahoo:jp:categorySearch}Short").text #カテゴリ名の取得
            list.append([id,name])  #[id,カテゴリ名]のリストを作成
    return list

#アイテムの検索
def Search_Items(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    list = []
    for Results in root.find("{urn:yahoo:jp:itemSearch}Result"):
        if (Results.tag == "{urn:yahoo:jp:itemSearch}Hit"):
            item_num = Results.attrib['index']  #カテゴリ内での商品のID
            item_name = Results.find("{urn:yahoo:jp:itemSearch}Name").text  #商品名
            item_description = Results.find("{urn:yahoo:jp:itemSearch}Description").text    #商品の詳細
            name, ext = os.path.splitext(filepath)  #保存するためのファイル名を取得
            url = Results.find("{urn:yahoo:jp:itemSearch}Image").find("{urn:yahoo:jp:itemSearch}Medium").text   #商品の写真のURL
            image_file = "./images/" + name + "/" + item_num + '.png'
            list.append([item_num,image_file,url,item_name,item_description])  #[商品IDと画像のパスと画像のURLと商品名]
    return list

if __name__ == '__main__':
    args = sys.argv
    if(len(args)==3):
        if(int(args[1])==0):        #カテゴリの検索
            print (Search_Category(args[2]))
        elif(int(args[1])==1):        #アイテムの検索
            print (Search_Items(args[2]))
