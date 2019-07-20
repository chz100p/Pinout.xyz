<!--
---
name: ADRSZSW
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZSW ゼロワン 照光スイッチ拡張基板
url: http://bit-trade-one.co.jp/product/module/adrszsw/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/2nd/ADRSZSW_Illuminated_Switch
buy: http://btoshop.jp/2018/08/20/4562469771885/
image: 'adrszsw.png'
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
ADRSZSW ゼロワン 照光スイッチ拡張基板
-----------------------
<!--
[

<img alt="WP-製品紹介M50-ADRSZSW-MAIN" class="alignnone wp-image-7882 size-full" height="300" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/5232dc98834c34d98111845a361b4a19.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/5232dc98834c34d98111845a361b4a19.png 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/5232dc98834c34d98111845a361b4a19-300x129.png 300w" width="696"/>

![WP-製品紹介M50-ADRSZSW-MAIN](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20300%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/5232dc98834c34d98111845a361b4a19.png)
-->

**[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**
===========================================================================================

### 製品の特徴

**・コンパクトな”pHAT”サイズ    **

コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

**・外部スイッチ動作とLED動作をまとめて照光スイッチとして利用可能。**

PICマイコンを搭載することでLEDの細かな輝度調整が可能。ラズパイからI2CでLED制御。LEDへの外部電源の引き込みも可能な照光スイッチが製作できます。

**・動作状況が見えるLEDを装備**

ステータスLEDにより駆動状況の確認が容易に、実験時やメンテナンス時に役立ちます。

ご注意！

本製品をお使いになるには電子工作や電子回路についての一般的な知識が必要です。

（＊Raspberry Pi Zero本体及びケース、ケーブル類は付属致しません。） 
<!--
[

<img alt="WP-製品紹介M50-ADRSZSW-SUB" class="alignnone size-full wp-image-7883" height="223" sizes="(max-width: 694px) 100vw, 694px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/b46c83f551d412b3870d87f1a1e7a2d0.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/b46c83f551d412b3870d87f1a1e7a2d0.png 694w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/b46c83f551d412b3870d87f1a1e7a2d0-300x96.png 300w" width="694"/>

![WP-製品紹介M50-ADRSZSW-SUB](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20694%20223%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/b46c83f551d412b3870d87f1a1e7a2d0.png)
-->

外部電源入力について  
DC12V以内でお使いください。

LED-OUTについて  
外部電源を使う場合は、DC12V・2A以内でお使いください。  
内部電源を使う場合は、電圧はDC5Vになります。  
電流はラズパイの電源に依存します。

・LEDと直列に、電流制限抵抗を接続してください  
・電流制限抵抗の代わりに定電流回路を使わないでください  
（照光スイッチ拡張基板の部品に負担がかかり、壊れる恐れがあります）

基本仕様

【対応機種】Raspberry Pi Zero v1.3 / W / WH (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)Raspberry Pi 2/3 (ネジ固定が出来ない場合があります、再起動スイッチは使えません)【LED】ステータスx1

【スイッチ】再起動スイッチ／シャットダウンスイッチ(シャットダウン等の動作についてはWEBページをご確認下さい)

【入出力端子】 スイッチ入力x1(GPIO5に接続)／LEDOUTx1／LED外部電源入力x1（ジャンパピンによる切替が必要です）

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
