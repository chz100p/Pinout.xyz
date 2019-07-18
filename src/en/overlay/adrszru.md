<!--
---
name: adrszru
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZRU ゼロワン リレー回路拡張基板
url: http://bit-trade-one.co.jp/product/module/adrszru/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/2nd/ADRSZRU_Relay_Unit
buy: http://btoshop.jp/2018/08/20/4562469771908/
image: 'adrszru.png'
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
ADRSZRU ゼロワン リレー回路拡張基板
----------------------

[

<img alt="WP-製品紹介M49-ADRSZRU-MAIN" class="alignnone size-full wp-image-7886" height="300" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/acb767c7c68fddb9b3f1b609d4c4c213.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/acb767c7c68fddb9b3f1b609d4c4c213.png 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/acb767c7c68fddb9b3f1b609d4c4c213-300x129.png 300w" width="696"/>

![WP-製品紹介M49-ADRSZRU-MAIN](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20300%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/acb767c7c68fddb9b3f1b609d4c4c213.png)

### **[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**

### 製品の特徴

**・コンパクトな”pHAT”サイズ   **

コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

・**ラズパイゼロから信頼のリレーユニットを制御。AC 250V/10A, DC30V/10A に対応。**

リレーユニットには採用実績が多く、AC 250V/10A, DC30V/10A までの電圧/電流に対応する  
SRD-5VDC-SL-C を使用。信頼性の高い部品で安心してご使用いただけます!

**・リレー接続部は簡単に取り付けが可能な端子台を使用。**

ドライバー1本で取り付け可能な端子台を使用、スムーズな製作を可能に!

**・基板上のLEDでリレー端子の状態を確認可能**  
LEDにより視覚的に動作を把握可能。実験時の確認に役立ちます。

ご注意！

本製品をお使いになるには電子工作や電子回路についての一般的な知識が必要です。

（＊Raspberry Pi Zero本体及びケース、ケーブル類は付属致しません。） 

[

<img alt="WP-製品紹介M49-ADRSZRU-SUB" class="alignnone size-full wp-image-7887" height="177" sizes="(max-width: 693px) 100vw, 693px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/f3774acfa0a673bad3beeaa5811a420f.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/f3774acfa0a673bad3beeaa5811a420f.png 693w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/f3774acfa0a673bad3beeaa5811a420f-300x77.png 300w" width="693"/>

![WP-製品紹介M49-ADRSZRU-SUB](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20693%20177%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/08/f3774acfa0a673bad3beeaa5811a420f.png)

基本仕様

【対応機種】Raspberry Pi Zero v1.3 / W / WH (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)Raspberry Pi 2/3 (ネジ固定が出来ない場合があります、再起動スイッチは使えません)

【LED】リレーステータスx1（リレーONで点灯）、ステータス×1

【スイッチ】再起動スイッチ／シャットダウンスイッチ(シャットダウン等の動作については弊社WEBページをご確認下さい)

【入力】レベル入力（GPIO4、HでリレーON）

【出力】接点出力（端子台、リレーONでCOMとNOが導通）

リレー仕様：【出力端子】COM/NO/NC (1C) 【定格電圧/電流】AC 250V/10A, DC30V/10A

【本体寸法】W65×D30×H26mm (突起部含めず)

【本体重量】約20g

【電源】3.3V/5V (Raspberry Pi Zeroより給電)

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
