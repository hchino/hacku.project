"""
    得られた情報からhtmlファイルを作成するやつ
"""
import sys,os

def make_html_files(title,images,detail,outputfile,number,outputfile2,modoru):
    # ファイルをオープンする
    test_data = open("./HTML_TEMPLATE/template.html", "r")
    data = ""
    #読み込んだテキストファイルを１行ずつ表示
    for line in test_data:
        data += line
    data = data.replace('商品タイトル',title)
    data = data.replace('画像ファイルパス',images)
    if(detail == None):
        detail = "商品情報はありません"
    detail.replace('。 ','<br>')
    data = data.replace('商品説明',detail)
    data = data.replace('UUUUUUUUUUUUUUUUUUUUUUUUU',modoru)
    file_path = os.path.dirname(outputfile)
    #fileが存在しない場合
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(outputfile, mode="w") as f:
        f.write(data)

    #商品まとめのページの作成
    TEST = '<div class="group" id="'+ str(number) +'">\n<div class="alcohol_image">\n<img src="../../../'
    TEST += images + '" height="100%">\n</div>\n<div class="alcohol_explain">\n<h1>'+title+'</h1>\n<br>\n<a href="'
    TEST += './' + str(number+1) + '.html">商品詳細</a>\n</div>\n</div>\n商品情報'
    #初めて作成する場合
    if(int(number) == 0):
        # ファイルをオープンする
        test_data2 = open("./HTML_TEMPLATE/template2.html", "r")
        data2 = ""
        line2 = ""
        #読み込んだテキストファイルを１行ずつ表示
        for line2 in test_data2:
            data2 += line2
        data2 = data2.replace('商品情報',TEST)
        data2 = data2.replace('UUUUUUUUUUUUUUUUUUUUUUUUU',modoru)
        file_path = os.path.dirname(outputfile2)
        #fileが存在しない場合
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        with open(outputfile2, mode="w") as f:
            f.write(data2)
            f.close()
        test_data2.close()
    else:
        # ファイルをオープンする
        test_data2 = open(outputfile2, "r")
        data2 = ""
        line2 = ""
        #読み込んだテキストファイルを１行ずつ表示
        for line2 in test_data2:
            data2 += line2
        test_data2.close()
        data2 = data2.replace('商品情報',TEST)
        with open(outputfile2, mode="w") as f:
            f.write(data2)
            f.close()

def make_html_files2(image_path,i,outputfile,category_id,category_name):
    path = image_path.rsplit("/",1)
    if int(i)==0:
        # ファイルをオープンする
        test_data = open("./HTML_TEMPLATE/template3.html", "r")
    else:
        test_data = open(outputfile,"r")
    data = ""
    #読み込んだテキストファイルを１行ずつ表示
    for line in test_data:
        data += line
    DATA = "*/\n#section"+str(i)+"{\nbackground-image: url(../../../"+image_path+");\npadding: 6% 0 0 0;\nbackground-size:50% 50%;}\n#section"+str(i)+" h1{\ncolor: #000;\nposition: relative;\n}/*CSS_DATAS_MANY1"
    DATA2 = "*/\n$('#section"+str(i)+"').css('background-image','url(' + '../../../" +path[0] +"/' + i + '.png)');\n/*CSS_DATAS_MANY2"
    DATA3 = '--><div class="section " id="section'+str(i)+'"><a href="./'+category_id+'/main.html"><h1 class="btn">'+category_name+'</h1></a><a href="https://developer.yahoo.co.jp/about"><img src="https://s.yimg.jp/images/yjdn/yjdn_attbtn2_105_17.gif" width="105" height="17" title="Webサービス by Yahoo! JAPAN" alt="Webサービス by Yahoo! JAPAN" border="0" style="margin:15px 15px 15px 15px"></a></div><!--CSS_DATAS_MANY3'
    DATA4 = "*/'"+category_name+"',/*CSS_DATAS_MANY4"
    if i == 0:
        DATA5 = "*/'firstPage',/*CSS_DATAS_MANY5"
    elif i==1:
        DATA5 = "*/'secondPage',/*CSS_DATAS_MANY5"
    elif i==2:
        DATA5 = "*/'3rdPage',/*CSS_DATAS_MANY5"
    else:
        DATA5 = "*/'"+str(i+1)+"thPage',/*CSS_DATAS_MANY5"
    DATA6 = "*/'#FFFFFF',/*CSS_DATAS_MANY6"

    data=data.replace("CSS_DATAS_MANY1",DATA)
    data=data.replace("CSS_DATAS_MANY2",DATA2)
    data=data.replace("CSS_DATAS_MANY3",DATA3)
    data=data.replace("CSS_DATAS_MANY4",DATA4)
    data=data.replace("CSS_DATAS_MANY5",DATA5)
    data=data.replace("CSS_DATAS_MANY6",DATA6)
    file_path = os.path.dirname(outputfile)
    #fileが存在しない場合
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(outputfile, mode="w") as f:
        f.write(data)
        f.close()
if __name__ == '__main__':
    print ("test")
