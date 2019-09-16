"""
    全てを実行するやつ
    data.txtにパスと商品名を保存
    実行方法
        python main.py
"""

from get_xml import make_xml
from get_images import download_image
from read_xml import Search_Category, Search_Items
from make_html_files import make_html_files, make_html_files2
from tqdm import tqdm

if __name__ == '__main__':
    ID = "2499"
    path = make_xml("0",ID,"feed.xml")  #カテゴリ情報の取得
    list = Search_Category(path)    #カテゴリリストの取得
    DATA = ""
    for i in tqdm(range(len(list))):
        ID2 = ID + "/" + list[i][1] #0でid、1でカテゴリ名
        path = make_xml("0",list[i][0],ID2 + ".xml")
        list2 = Search_Category(path)
        #カテゴリの中にカテゴリがない場合
        if (list2 == []):
            path = make_xml(1,list[i][0],ID2 + ".xml")   #カテゴリにおける商品のxml作成
            List = Search_Items(path)    #商品の検索
            for k in tqdm(range(len(List))):
                DATA += list[i][1] + "\t" + List[k][1] + "\t" + List[k][3] + "\n"
                download_image(List[k][2],List[k][1]) #画像の保存
                make_html_files(List[k][3],List[k][1],List[k][4],'./htmls/' + ID + '/' + list[i][0] + '/' + List[k][0] + '.html', k,'./htmls/' + ID + '/' + list[i][0] + '/main.html','../../../index.html')   #商品情報のhtmlファイルを作成
        else:#カテゴリの中にカテゴリがある場合
            for j in tqdm(range(len(list2))):
                ID3 = ID2 + "/" + list2[j][1] #0でid、1でカテゴリ名
                path = make_xml(1,list2[j][0],ID3 + ".xml")   #カテゴリにおける商品のxml作成
                List = Search_Items(path)    #商品の検索
                for k in tqdm(range(len(List))):
                    DATA += list2[j][1] + "\t" + List[k][1] + "\t" + List[k][3] + "\n"
                    download_image(List[k][2],List[k][1]) #画像の保存
                    make_html_files(List[k][3],'../'+List[k][1],List[k][4],'./htmls/'+ID+'/'+list[i][0]+'/'+list2[j][0]+'/'+List[k][0]+'.html', k,'./htmls/'+ID+'/'+list[i][0]+'/'+list2[j][0]+'/main.html','../../../../index.html')   #商品情報のhtmlファイルを作成
                make_html_files2(List[j][1],j,'./htmls/'+ID+'/'+list[i][0]+'/main.html',list2[j][0],list2[j][1])    #カテゴリ情報のまとめ
    print ("\n\n\n")
    with open("data.csv", mode="w") as f:
        f.write(DATA)
