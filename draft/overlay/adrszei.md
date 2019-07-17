<!--
---
name: adrszei
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZEI ゼロワン 電子ペーパーモニタ拡張基板
url: http://bit-trade-one.co.jp/adrszel/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/5th/ADRSZEI_Electric_Paper
buy: 
image: 'adrszei.png'
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
  '7':
    name: Enable
    mode: output
    active: high
i2c:
  '0x00':
    name: device display name
    device: chip name
-->
ADRSZEI ゼロワン 電子ペーパー拡張基板
-----------------------

<img alt="" class="alignnone wp-image-9031 size-full" height="300" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/02/da6587a0bdf66f211351691231cad8a4.jpg" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/02/da6587a0bdf66f211351691231cad8a4.jpg 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/02/da6587a0bdf66f211351691231cad8a4-300x129.jpg 300w" width="696"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20300%22%3E%3C/svg%3E)

**[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**

製品の特徴
-----

**・コンパクトな”pHAT”サイズ**

コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

**・様々な表示が可能な電子ペーパー（GDEH0213B1)を自由に書き換え可能。**

電子ペーパーは、紙と同じような表示を可能にする新しい表示媒体です。

従来のディスプレイとは異なり、電子ペーパーはバックライトを必要とせず、電力を使わずにテキストと画像を寿命の限り保持することができます。

画面切替時のみに電力が使われるため非常に低消費電力です。

今回搭載されているGDEH0213B1は2.13インチの電子ペーパーディスプレイです。

特に電力効率が良く、180度に近い視野角を持ち日光下でも視認が可能。

ラズパイから外しても表示は保持されたままなので、

ラベリングやタグ、スマートホーム端末の表示媒体などにぴったりのアイテムです。

 

<img alt="" class="alignnone wp-image-9032 size-full" height="202" sizes="(max-width: 496px) 100vw, 496px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/02/0e85c768beee43c3878456df7b754893.jpg" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/02/0e85c768beee43c3878456df7b754893.jpg 496w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2019/02/0e85c768beee43c3878456df7b754893-300x122.jpg 300w" width="496"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20496%20202%22%3E%3C/svg%3E)

ビット・トレード・ワンではNode-RED上で名前を入力するだけで名札が作れるサンプルプログラム等を用意。ラズパイ内臓の日本語フォントが使用でき様々なサイズで出力可能。

手軽に書き換えることが出来る電子ペーパーの利点をすぐに試して頂けます。

ご注意！

本製品をお使いになるには電子工作や電子回路についての一般的な知識が必要です。

（＊Raspberry Pi Zero本体及びケース、ケーブル類は付属致しません。）  

基本仕様

【対応機種】推奨機種：Raspberry Pi Zero  WH

対応可能機種：Raspberry Pi Zero v1.3 / W  (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)

Raspberry Pi 2/3

【LED】ステータス×1（プログラムで制御）

【表示寸法】2.13インチ

【有効画面】23.8(H) × 48.55(V)mm

【表示色】白/黒

【画面解像度】250×122 画素

【本体寸法】W65×D30×H10mm (突起部含めず)

【本体重量】約14g

【電源】Raspberry Pi Zeroより給電

【付属品】 保証書 x1

【生産国】Made in Japan

【保証期間】お買い上げから1年間

※本製品は特性上、他のゼロワンシリーズ製品とは異なり、RUN/REBOOTスイッチが搭載されておりません。ご了承下さい。

―――本製品取扱についてのご注意―――

・本製品は、ホビー向け商品です。個人利用に限定され、著作権者の許可なく商用利用できません。

・記載の部品性能は部品単体での性能であり、製品寿命を保証するものではありません。

・ご利用のPC、Raspberry PiおよびOS環境によってはすべての機能をご利用いただ

けない場合があります。

・本キットの製作/使用に関し当社の責に帰すべき事由に基づき、お客様に損害が生じた場合、直接被害に限り、販売代金を上限として損害を賠償し、いかなる場合においても販売代金以上の損害を賠償しないものとします。

・改良のため、予告なく仕様変更をすることがあります。予めご了承下さい。

＊Raspberry Pi本体及びケース、ケーブル類は付属致しません。

Raspberry Piは英国Raspberry Pi財団の登録商標です。Raspberry Pi is a trademark of the Raspberry Pi Foundation. そのほか記載されているロゴ、システム名、製品名は各社及び商標権者の登録商標あるいは商標です。
