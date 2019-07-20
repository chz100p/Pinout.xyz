<!--
---
name: ADRSZOD
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZOD ゼロワン臭気センサ拡張基板
url: http://bit-trade-one.co.jp/adrszod/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/5th/ADRSZOD_Odd_Sensor
buy: http://btoshop.jp/2019/02/14/4562469772103/
image: 'adrszod.png'
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
ADRSZOD ゼロワン 臭気センサ拡張基板
----------------------
<!--
<img alt="" class="alignnone wp-image-9033 size-full" height="300" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/02/ef8f6aa19bacc9191bb706b7e763d680.jpg" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/02/ef8f6aa19bacc9191bb706b7e763d680.jpg 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/02/ef8f6aa19bacc9191bb706b7e763d680-300x129.jpg 300w" width="696"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20300%22%3E%3C/svg%3E)
-->

**[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**

### 製品の特徴

**・コンパクトな”pHAT”サイズ**

コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

**・様々な気体を検知する臭気センサTP-401Aを搭載**

低電力で動作可能な高感度の臭気センサを搭載。

アンモニア、水素、アルコール、一酸化炭素、メタンなど揮発性気体、タバコ、木材燃焼発生した煙など様々な気体に対応。

連続通電を許容する為、ラズパイゼロの小型な形状も相まって様々な所で継続的なチェックが可能です。

換気扇の自動運用や検出表示など、既存ゼロワン製品との組み合わせで、IoTをより身近な物へ。

※動作時にはセンサ部が非常に高温となる為、取り扱いには注意してください。

オプションとしてGroveコネクタ（アナログ）も搭載、更なるセンサの追加が可能。

**・動作状況が見えるLEDを装備       **

ステータスLEDにより駆動状況の確認が容易に、実験時やメンテナンス時に役立ちます。

ご注意！

本製品をお使いになるには電子工作や電子回路についての一般的な知識が必要です。

（＊Raspberry Pi Zero本体及びケース、ケーブル類は付属致しません。）  
<!--
各部の名称
-----

<img alt="" class="alignnone wp-image-9030 size-full" height="211" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/02/0f7bfb3f7ea496197d4c2f45760c9707.jpg" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/02/0f7bfb3f7ea496197d4c2f45760c9707.jpg 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/02/0f7bfb3f7ea496197d4c2f45760c9707-300x91.jpg 300w" width="696"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20211%22%3E%3C/svg%3E)
-->

基本仕様
----

【対応機種】推奨機種：Raspberry Pi Zero  WH

      対応可能機種：Raspberry Pi Zero v1.3 / W  (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)

             Raspberry Pi 2/3 (ネジ固定が出来ない場合があります、再起動スイッチは使えません)

【LED】ステータス×1（プログラムで制御）

【スイッチ】再起動(RUN)スイッチ／シャットダウンスイッチ(シャットダウン等の動作についてはWEBページをご確認下さい)

【においセンサ】TP401A

※動作時には非常に高温となります。取り扱いにはご注意ください。

【本体寸法】W65×D30×H19mm (突起部含めず)

【本体重量】13g

【電源】Raspberry Pi Zeroより給電

【付属品】ネジセットx1／保証書 x1

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
