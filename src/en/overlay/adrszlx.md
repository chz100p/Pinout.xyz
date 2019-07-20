<!--
---
name: ADRSZLX
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZLX ゼロワン 明るさセンサ拡張基板
url: http://bit-trade-one.co.jp/product/module/adrszlx/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/2nd/ADRSZLX_Luminance_Sensor
buy: http://btoshop.jp/2018/08/20/4562469771878/
image: 'adrszlx.png'
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
ADRSZLX ゼロワン 明るさセンサ拡張基板
-----------------------
<!--
<img alt="WP-製品紹介M48-ADRSZLX-MAIN" class="alignnone size-full wp-image-7891" height="300" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/5c214ecdcbccea9e44bde2daeee34f33.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/5c214ecdcbccea9e44bde2daeee34f33.png 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/5c214ecdcbccea9e44bde2daeee34f33-300x129.png 300w" width="696"/>

![WP-製品紹介M48-ADRSZLX-MAIN](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20300%22%3E%3C/svg%3E)
============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
-->

**[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**
===========================================================================================

### 製品の特徴

**・コンパクトな”pHAT”サイズ   **

コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

**・照度と近接センサーを内蔵したVCNL4020を搭載**

赤外線エミッタを有しされ人間の目の感度に近い完全集積型の近接 / 周辺光センサであるデジタル光センサ VCNL4020をI2C接続で搭載。

ラズパイゼロで明るさを高精度で容易に測定可能です。

**・Groveシステム\*(I2C)対応コネクタ搭載    **

Groveシステム\*(I2C)対応のコネクタを搭載、市販のGroveシステムに対応したサーボやセンサ、アクチュエータを利用できるなど拡張性を活かした設計のため、IoTシステムのプロトタイピングにも最適です。 ＊GroveシステムはSeeed Technology Limited社の登録商標です。

ご注意！

本製品をお使いになるには電子工作や電子回路についての一般的な知識が必要です。

（＊Raspberry Pi Zero本体及びケース、ケーブル類は付属致しません。） 
<!--
[

<img alt="WP-製品紹介M48-ADRSZLX-SUB" class="alignnone size-full wp-image-7892" height="186" sizes="(max-width: 693px) 100vw, 693px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/94557135da325cf135b19faf66127a2b.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/94557135da325cf135b19faf66127a2b.png 693w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/94557135da325cf135b19faf66127a2b-300x81.png 300w" width="693"/>

![WP-製品紹介M48-ADRSZLX-SUB](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20693%20186%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/94557135da325cf135b19faf66127a2b.png)
-->

**基本仕様      **

【対応機種】Raspberry Pi Zero v1.3 / W / WH (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)Raspberry Pi 2/3 (ネジ固定が出来ない場合があります、再起動スイッチは使えません)

【LED】ステータス×1

【スイッチ】再起動スイッチ／シャットダウンスイッチ (シャットダウン等の動作については弊社WEBページをご確認下さい)

【環境光分解能】16ビット (0.25~16000ルクス)

【近接分解能】16ビット (1~200mm)

【本体寸法】W65×D30×H19mm (突起部含めず)

【本体重量】約12g

【電源】Raspberry Pi Zeroより給電

【付属品】 ネジセットx1／1X2ピンヘッダx1／保証書 x1

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
