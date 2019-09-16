"""
    URLから画像を撮ってくるやつ
    python get_images.py url id image_name
    例：python get_images.py https://item-shopping.c.yimg.jp/i/g/meishu-honpo_16308 1348 1
"""

import urllib.error
import urllib.request
import os,sys

def download_image(url, dst_path):
    file_path = os.path.dirname(dst_path)
    #fileが存在しない場合
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    try:
        #URL上から画像を読み込み保存
        data = urllib.request.urlopen(url).read()
        with open(dst_path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)

if __name__ == '__main__':
    args = sys.argv
    url = args[1]
    id = args[2]
    image_name = args[3]
    dst_path = './images/' + id + '/' + image_name + '.png'
    download_image(url, dst_path)
