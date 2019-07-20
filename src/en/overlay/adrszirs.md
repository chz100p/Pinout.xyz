<!--
---
name: ADRSZIRS
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZIRS ゼロワン 赤外線リモコン拡張基板
url: http://bit-trade-one.co.jp/adrszirs/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/3rd/ADRSZIRS_IR_Sender
buy: 
image: 'adrszirs.png'
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
ADRSZIRS ゼロワン 赤外線送信拡張基板
-----------------------
<!--
<img alt="" class="wp-image-8161" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/2b97c59e0d360c5a60299a59363108a9.jpg" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/2b97c59e0d360c5a60299a59363108a9.jpg 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/2b97c59e0d360c5a60299a59363108a9-300x129.jpg 300w"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)
-->

**[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**

#### 製品の特徴

**・コンパクトな”pHAT”サイズ**  
コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

**・３つの送信用赤外線発光ダイオードで広範囲送出**  
赤外線発光ダイオードを3個搭載することで送出範囲を広範囲にサポートします。

**・受信した赤外線信号をそのまま記録し送信！アップグレードされた送信機能**  
高性能な32bitマイコンを搭載、「受信した赤外線信号をそのまま記録、送信する」事で、赤外線コードに関係なく多彩な信号の送信を実現しました。  
また上位機種”ラズベリー・パイ専用学習リモコン基板”との共通化を図ることで、家電 からエアコンまで、各社 2500 以上のリモコンコードをユーザーが自由 に選んでオリジナルな高機能リモコンを作成できます。

**・動作状況が見えるLEDを装備**  
ステータスLEDにより駆動状況の確認が容易に、実験時やメンテナンス時に役立ちます。

ご注意！  
本製品をお使いになるには電子工作や電子回路についての一般的な知識が必要です。  
（＊Raspberry Pi Zero本体及びケース、ケーブル類は付属致しません。）
<!--
<img alt="" class="wp-image-8162" sizes="(max-width: 694px) 100vw, 694px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/1e4d0df001124654768e3ea4fedc1fd3.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/1e4d0df001124654768e3ea4fedc1fd3.png 694w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/1e4d0df001124654768e3ea4fedc1fd3-300x74.png 300w"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)
-->

基本仕様

【対応機種】Raspberry Pi Zero v1.3 / W / WH (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)Raspberry Pi 2/3 (ネジ固定が出来ない場合があります、再起動スイッチは使えません)  
【LED】LED赤：１個（電源ON時に点滅）LED赤：１個（赤外線送信時に点滅）LED緑：１個（赤外線送受信時に点滅）  
【スイッチ】再起動スイッチ／シャットダウンスイッチ(シャットダウン等の動作についてはWEBページをご確認下さい)  
【入出力】赤外線受光モジュールx1、、出力用赤外線LEDx3  
【本体寸法】W65×D30×H17mm (突起部含めず)  
【本体重量】13g  
【電源】Raspberry Pi Zeroより給電  
【付属品】ネジセットx1／1X2ピンヘッダx1／保証書 x1  
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
