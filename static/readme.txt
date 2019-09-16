YahooのショッピングAPIからデータを取得するプログラム
python 3 系で動きます(2系では未実行です)
飲み物のデータをとってきます
実行方法
  python main.py
取得した画像は以下のディレクトリに保存される
  ./images/xml/2499/*
取得した情報(.xml)は以下のディレクトリに保存される
  ./xml/2499/*

get_xml.pyではYahooのAPIからxmlファイルを取得
read_xml.pyで取得したxmlファイルからの情報を取得
  ・カテゴリ情報もしくは商品情報
get_images.pyで商品情報から画像を取得します
