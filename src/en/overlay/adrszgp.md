<!--
---
name: ADRSZGP
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZGP ゼロワン GPS拡張基板
url: http://bit-trade-one.co.jp/adrszgp/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/4th/ADRSZGP_GPS
buy: 
image: 'adrszgp.png'
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
-->
ADRSZGP ゼロワン GPS拡張基板
--------------------
<!--
<img alt="" class="wp-image-8677" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/12/0dd687137ff34e4900abecc82b13d4b6.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/12/0dd687137ff34e4900abecc82b13d4b6.png 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/12/0dd687137ff34e4900abecc82b13d4b6-300x129.png 300w"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)
-->

**[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**

製品の特徴

・**コンパクトな”pHAT”サイズ **          
コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

・**GPSモジュール（FGPMMOPA6H)を搭載し、「みちびき」に対応**  
NMEA0183に準拠した緯度・経度・高度・時刻などの各種ナビケーション情報をシリアル信号で出力。  
最新のGPSトレンドである日本の「みちびき」3機受信（衛星番号193、194、195）にも対応！

・**GPS外部アンテナ付き！**  
高感度のアンテナを付属。  
受信の難しい環境でも引き出して使用する事が可能。
<!--
<img alt="" class="wp-image-8678" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/12/68202e6d8973941d51560d8385770d50.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/12/68202e6d8973941d51560d8385770d50.png 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/12/68202e6d8973941d51560d8385770d50-300x74.png 300w"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)
-->

ご注意！  
本製品をお使いになるには電子工作や電子回路についての一般的な知識が必要です。  
（＊Raspberry Pi Zero本体及びケース、ケーブル類は付属致しません。）    

基本仕様

【対応機種】推奨機種：Raspberry Pi Zero  WH  
      対応可能機種：Raspberry Pi Zero v1.3 / W  (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)  
             Raspberry Pi 2/3 (ネジ固定が出来ない場合があります)  
【LED】ステータス×1（プログラムで制御）  
【スイッチ】シャットダウンスイッチ (シャットダウン等の動作については弊社WEBページをご確認下さい)

【GPS Chipset】 MT3339  
【シリアル・ボーレート】9,600BPS（設定変更可能）  
【本体寸法】W65×D30×H19mm (突起部含めず)  
【本体重量】約19g  
【電源】Raspberry Pi Zeroより給電  
【付属品】 GPS外部アンテナx1／ネジセットx1／保証書 x1  
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
