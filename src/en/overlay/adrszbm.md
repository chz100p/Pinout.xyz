<!--
---
name: ADRSZBM
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZBM ゼロワン 温湿度・気圧センサ拡張基板
url: http://bit-trade-one.co.jp/product/module/adrszbm/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/1st/ADRSZBM_Enviroment_Sensor
buy: http://btoshop.jp/2018/07/02/4562469771830/
image: 'adrszbm.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '31':
    name: ShutDownSW
    mode: input
    active: low
  '37':
    name: StatusLED
    mode: output
    active: high
i2c:
  '0x00':
    name: device display name
    device: chip name
-->
ADRSZBM ゼロワン 温湿度・気圧センサ拡張基板
--------------------------
<!--
[

<img alt="WP-製品紹介M45-ADRSZBM-MAIN" class="alignnone size-full wp-image-7562" height="300" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/329f8d263d164a16c1875b8408263084.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/329f8d263d164a16c1875b8408263084.png 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/329f8d263d164a16c1875b8408263084-300x129.png 300w" width="696"/>

![WP-製品紹介M45-ADRSZBM-MAIN](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20300%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/329f8d263d164a16c1875b8408263084.png)
-->

 **[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**
============================================================================================

**製品の特長   **

・**コンパクトな”pHAT”サイズ  **

コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

**・BME280搭載    **

ボッシュ社のBME280を搭載したセンサモジュールで、温度、湿度、気圧の３つの環境情報を同時に測定できます 。また付属のジャンパワイヤによってBME280を熱源であるラズパイ本体から離して接続することも可能です。
<!--
<img alt="" class="elementOfPhoto" src="https://llstock.s3-ap-northeast-1.amazonaws.com/uploads/photo/image/33837/middle\_stockimage.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAI7P6SP7G3K7DHTNA%2F20180629%2Fap-northeast-1%2Fs3%2Faws4\_request&amp;X-Amz-Date=20180629T095557Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=34927c63f72e4969a40bafdd65300727f84bb39868406c292e987d80600ab633"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)
-->

**・Groveシステム\*(I2C)対応コネクタ搭載 **

Groveシステム\*(I2C)対応のコネクタを搭載、市販のGroveシステムに対応したサーボやセンサ、アクチュエータを利用できるなど拡張性を活かした設計のため、IoTシステムのプロトタイピングにも最適です。 ＊GroveシステムはSeeed Technology Limited社の登録商標です。
<!--
各部の名称

<img alt="" class="elementOfPhoto" src="https://llstock.s3-ap-northeast-1.amazonaws.com/uploads/photo/image/37500/middle\_stockimage.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAI7P6SP7G3K7DHTNA%2F20180629%2Fap-northeast-1%2Fs3%2Faws4\_request&amp;X-Amz-Date=20180629T095557Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=99c4ee8df8078f05a2c636fe2dc1265680ee86cfe13ab13d28e64f385787bcaa"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)

[

<img alt="WP-製品紹介M45-ADRSZBM-SUB" class="alignnone wp-image-7779 size-full" height="154" sizes="(max-width: 695px) 100vw, 695px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/f786533f0a253d524aa7b68de618ab511.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/f786533f0a253d524aa7b68de618ab511.png 695w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/f786533f0a253d524aa7b68de618ab511-300x66.png 300w" width="695"/>

![WP-製品紹介M45-ADRSZBM-SUB](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20695%20154%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/f786533f0a253d524aa7b68de618ab511.png)
-->

ご注意！

本製品をお使いになるには電子工作や電子回路についての一般的な知識とマイナスドライバーが必要です。

（＊Raspberry Pi Zero本体及びケース、ケーブル類は付属致しません。） 

基本仕様          

【対応機種】Raspberry Pi Zero v1.3 / W / WH (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)Raspberry Pi 2/3 (ネジ固定が出来ない場合があります、再起動スイッチは使えません)

【LED】ステータス×1

【スイッチ】再起動スイッチ／シャットダウンスイッチ([シャットダウン等の動作についてはWEBページをご確認下さい](http://bit-trade-one.co.jp/blog/201807032/))

【測定レンジ及び測定精度】温度：-40～+85℃､ ±1℃／湿度：0～100%、±3%／気圧：300～1100hPa､±1hPa

【分解能】温度：0.01℃／湿度：0.008%／気圧：0.18Pa

【本体寸法】W65×D30×H23mm (突起部含めず)

【本体重量】約14g

【電源】Raspberry Pi Zeroより給電

【付属品】 ブレッドボード・ジャンパーワイヤ(オス－メス) 5本

ネジセットx1保証書 x1

【生産国】Made in Japan

【保証期間】お買い上げから1年間

―――本製品取扱についてのご注意―――       

・本製品は、ホビー向け商品です。個人利用に限定され、著作権者の許可なく商用利用できません。  

・記載の部品性能は部品単体での性能であり、製品寿命を保証するものではありません。   

・ご利用のPC、Raspberry PiおよびOS環境によってはすべての機能をご利用いただけない場合があります。 

・本キットの製作/使用に関し当社の責に帰すべき事由に基づき、お客様に損害が生じた場合、直接被害に限り、販売代金を上限として損害を賠償し、いかなる場合においても販売代金以上の損害を賠償しないものとします。

・改良のため、予告なく仕様変更をすることがあります。予めご了承下さい。    

＊Raspberry Pi本体及びケース、ケーブル類は付属致しません。     

Raspberry Piは英国Raspberry Pi財団の登録商標です。Raspberry Pi is a trademark of the Raspberry Pi Foundation. そのほか記載されているロゴ、システム名、製品名は各社及び商標権者の登録商標あるいは商標です。

＊GroveシステムはSeeed Technology Limited社の登録商標です。
