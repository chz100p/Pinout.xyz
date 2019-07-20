<!--
---
name: ADRSZPY
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZPY ゼロワン 焦電型赤外線センサ拡張基板
url: http://bit-trade-one.co.jp/product/module/adrszpy/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/1st/ADRSZPY_Pyroelectric_Sensor
buy: http://btoshop.jp/2018/07/02/4562469771861/
image: 'adrszpy.png'
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
  '29':
    name: Enable
    mode: input
    active: high
  '31':
    name: ShutDownSW
    mode: input
    active: low
  '37':
    name: StatusLED
    mode: output
    active: high
-->
ADRSZPY ゼロワン 焦電型赤外線センサ拡張基板
--------------------------

<!--
[

<img alt="WP-製品紹介M44-ADRSZPY-MAIN" class="alignnone size-full wp-image-7561" height="300" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/f2af38775904f423457c1ae0aa77f3fb.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/f2af38775904f423457c1ae0aa77f3fb.png 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/f2af38775904f423457c1ae0aa77f3fb-300x129.png 300w" width="696"/>

![WP-製品紹介M44-ADRSZPY-MAIN](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20300%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/f2af38775904f423457c1ae0aa77f3fb.png)
-->

**製品の特長**

・**コンパクトな”pHAT”サイズ  **

コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

**・焦電人感センサを容易に実験 **

ドーム型フレンネルレンズにより120度の広範囲な検知が可能です。簡易な防犯や見守りシステム製作を容易にします。

**・焦電型赤外線センサの駆動状況が見えるLEDを装備**

LEDにより駆動状況の確認が容易に。実験時やメンテナンス時に役立ちます。

<!--
[](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/adrszPY.zip)**[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**
===================================================================================================================================================================

各部の名称

<img alt="" class="wp-image-8099" sizes="(max-width: 693px) 100vw, 693px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/833b8670e08a918223faed9415d816d1-1.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/833b8670e08a918223faed9415d816d1-1.png 693w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/833b8670e08a918223faed9415d816d1-1-300x113.png 300w"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)
-->

 ご注意！          

本製品をお使いになるには電子工作や電子回路についての一般的な知識が必要です。   

（＊Raspberry Pi Zero本体及びケース、ケーブル類は付属致しません。）    

基本仕様          

【対応機種】Raspberry Pi Zero v1.3 / W / WH (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)

Raspberry Pi 2/3（ネジ固定が出来ない場合があります、再起動スイッチは使えません）

【スイッチ】再起動スイッチ／シャットダウンスイッチ([シャットダウン等の動作についてはWEBページをご確認下さい](http://bit-trade-one.co.jp/blog/201807032/ "ラズパイゼロワンシリーズ シャットダウンスイッチ/RUNスイッチ使用手順"))

【LED】ステータスx1／センサ動作状態用x1

【保持時間】5秒～300秒(半固定抵抗で調整)

【レンズ】直径23ｍｍドーム型

【最大検知距離】7ｍ(気温等環境条件により変化します)／半固定抵抗で調整

【検知角度】120度

【本体寸法】W65×D30×H38mm（突起部含めず)

【本体重量】約19g

【電源】Raspberry Pi Zeroより給電

【付属品】ネジセットx1 保証書x1

【生産国】Made in Japan

【保証期間】お買い上げから1年間

その他40pin GPIO対応のRaspberry Pi製品          

―――本製品取扱についてのご注意―――       

・本製品は、ホビー向け商品です。個人利用に限定され、著作権者の許可なく商用利用できません。  

・記載の部品性能は部品単体での性能であり、製品寿命を保証するものではありません。   

・ご利用のPC、Raspberry PiおよびOS環境によってはすべての機能をご利用いただけない場合があります。 

・本キットの製作/使用に関し当社の責に帰すべき事由に基づき、お客様に損害が生じた場合、直接被害に限り、販売代金を上限として損害を賠償し、いかなる場合においても販売代金以上の損害を賠償しないものとします。

・改良のため、予告なく仕様変更をすることがあります。予めご了承下さい。    

＊Raspberry Pi本体及びケース、ケーブル類は付属致しません。     

Raspberry Piは英国Raspberry Pi財団の登録商標です。Raspberry Pi is a trademark of the Raspberry Pi Foundation. そのほか記載されているロゴ、システム名、製品名は各社及び商標権者の登録商標あるいは商標です。
