<!--
---
name: ADRSZRE
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZRE ゼロワン　ロータリーエンコーダ拡張基板
url: http://bit-trade-one.co.jp/product/module/adrszre/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/1st/ADRSZRE_Rotary_Encoder
buy: http://btoshop.jp/2018/07/02/adrszre/
image: 'adrszre.png'
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
  '8':
    mode: uart
  '10':
    mode: uart
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
ADRSZRE ゼロワン ロータリーエンコーダ拡張基板
---------------------------

<!--
[

<img alt="WP-製品紹介M43-ADRSZRE-MAIN" class="alignnone size-full wp-image-7560" height="300" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/03b4c9e1b2651437f2c457bb7456253a.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/03b4c9e1b2651437f2c457bb7456253a.png 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/03b4c9e1b2651437f2c457bb7456253a-300x129.png 300w" width="696"/>

![WP-製品紹介M43-ADRSZRE-MAIN](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20300%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/03b4c9e1b2651437f2c457bb7456253a.png)
-->

**[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**
===========================================================================================

**製品の特徴  **

**・コンパクトな”pHAT”サイズ     ** 

コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

**・高精度測定       **

端子台/スルーホールにロータリーエンコーダを接続するだけで、簡単に測定が可能。  

あなたのIoTデバイス作成を加速させます。

※ 二つの端子を同時に利用することはできません。

**・リアルタイム性を考慮し、高性能PICマイコンを内蔵  **  

PICマイコンで計測を行うことで、高パルスロータリエンコーダでのパルスの取りこぼしを防ぎます。

**・動作状況が見えるLEDを装備**      

LEDにより駆動状況の確認が容易に。     

実験時やメンテナンス時に役立ちます。     

<!--
各部の名称  

<img alt="" class="elementOfPhoto" src="https://llstock.s3-ap-northeast-1.amazonaws.com/uploads/photo/image/37498/middle\_stockimage.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAI7P6SP7G3K7DHTNA%2F20180629%2Fap-northeast-1%2Fs3%2Faws4\_request&amp;X-Amz-Date=20180629T095701Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=b406ec89d43e973f073617411dc032dbcf64cb6d10fd5dc40a864298c326479d"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)[

<img alt="WP-製品紹介M43-ADRSZRE-SUB" class="alignnone size-full wp-image-7704" height="194" sizes="(max-width: 683px) 100vw, 683px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/3eed0f5e4815fe4bf6908bf61000445d.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/3eed0f5e4815fe4bf6908bf61000445d.png 683w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/3eed0f5e4815fe4bf6908bf61000445d-300x85.png 300w" width="683"/>

![WP-製品紹介M43-ADRSZRE-SUB](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20683%20194%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/3eed0f5e4815fe4bf6908bf61000445d.png)
-->

ご注意！        

本製品をお使いになるには電子工作や電子回路についての一般的な知識とマイナスドライバーが必要です。

（＊Raspberry Pi Zero本体及びロータリーエンコーダ、ケース、ケーブル類は付属致しません。）  

基本仕様        

【対応機種】Raspberry Pi Zero v1.3 / W / WH (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)

Raspberry Pi 2/3 (ネジ固定が出来ない場合があります、再起動スイッチは使えません)

【スイッチ】再起動スイッチ／シャットダウンスイッチ([シャットダウン等の動作についてはWEBページをご確認下さい](http://bit-trade-one.co.jp/blog/201807032/))

【LED】システム状態用×2（ラズパイ、PICマイコン）、ロータリーエンコーダ動作状態用×2

【本体寸法】W65×D30×H18mm（突起部含めず）

【本体重量】約14g

【電源】Raspberry Pi Zero 給電

【ロータリーエンコーダ仕様】A/B相デジタルパルス出力 電源5V

【入出力】I2C 回転量絶対値

【付属品】ネジセットx1／保証書x1

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
