<!--
---
name: ADRSZGR
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZGR ゼロワン ９軸センサ拡張基板
url: http://bit-trade-one.co.jp/adrszgr/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/3rd/ADRSZGR_9-Axis_Gyro
buy: 
image: 'adrszgr.png'
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
  '26':
    name: Enable
    mode: output
    active: high
  '24':
    name: Enable
    mode: output
    active: high
  '21':
    name: Enable
    mode: output
    active: high
  '19':
    name: Enable
    mode: output
    active: high
  '8':
    name: Enable
    mode: output
    active: high
  '10':
    name: Enable
    mode: output
    active: high
  '12':
    name: Enable
    mode: output
    active: high
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
ADRSZGR ゼロワン 9軸センサ拡張基板
----------------------

<!--
<img alt="" class="wp-image-8144" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/f7c31cba9c5a24f034b6f5b10550eaf6.jpg" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/f7c31cba9c5a24f034b6f5b10550eaf6.jpg 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/f7c31cba9c5a24f034b6f5b10550eaf6-300x129.jpg 300w"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)
-->

**[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**

製品の特徴 
------

  
**・コンパクトな”pHAT”サイズ   **        
コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！    
  
**・加速度****3軸＋ジャイロ****3軸＋磁気****3軸の計9つのパラメータを取得可能**センサモジュールとしてMPU9250 を搭載し、加速度3軸、ジャイロ3軸、地磁気(磁界)3軸の計9軸の検出が可能です。  
サンプルスクリプトでは9軸センサの値と1ステップの経過時間を取得し画面に出力、表示します。  
  
**・幅広い計測範囲・変更も可能  
**加速度±16g、角速度2000deg/sまでの広い範囲を計測可能。  
さらにセンサの設定を変更し、範囲を絞り精度を高めた計測も可能です。  
  

**・動作状況が見えるLEDを装備      **    
ステータスLEDにより駆動状況の確認が容易に、実験時やメンテナンス時に役立ちます。

ご注意！本製品をお使いになるには電子工作や電子回路についての一般的な知識が必要です。  
（＊Raspberry Pi Zero本体及びケース、ケーブル類は付属致しません。）    

<!--
<img alt="" class="wp-image-8145" sizes="(max-width: 694px) 100vw, 694px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/a45b5724c0b8bdf3369481b229fc6e0f.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/a45b5724c0b8bdf3369481b229fc6e0f.png 694w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/a45b5724c0b8bdf3369481b229fc6e0f-300x74.png 300w"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)
-->

基本仕様  
【対応機種】Raspberry Pi Zero v1.3 / W / WH (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)Raspberry Pi 2/3 (ネジ固定が出来ない場合があります、再起動スイッチは使えません)  
【LED】ステータスx1 センサ状態確認用2色(赤/緑)LEDx4(GPIOより操作可能)  
【スイッチ】再起動スイッチ／シャットダウンスイッチ(シャットダウン等の動作についてはWEBページをご確認下さい)  
【インターフェース】 I2C×1  
【センサモジュール】MPU-9250  
【３軸加速度】±2 / ±4 / ±8 / ±16g  
【３軸ジャイロ】±250 / ±500 / ±1000 / ±2000dps  
【３軸磁気センサ】±4800μT  
【本体寸法】W65×D30×H17mm (突起部含めず)  
【本体重量】14g  
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
