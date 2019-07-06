<!--
---
name: ADRSZSB　ゼロワン サーボモータ拡張基板
class: board
type: other
formfactor: Custom
manufacturer: BitTradeOne
description: An add-on board for the Raspberry Pi
url: http://bit-trade-one.co.jp/product/module/adrszsb/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/1st/ADRSZSB_Servo_Motor
buy: http://btoshop.jp/2018/07/02/4562469771809/
image: 'adrszsb.png'
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
# ADRSZSB　ゼロワン サーボモータ拡張基板

* コンパクトな”pHAT”サイズ         
コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！   
           
* 5Vから最大12Vまで利用可能な外部電源端子を装備       
ジャンパを切り替えることで、GPIO/外部電源端子からの給電を選択可能。     
様々な使用形態に対応します。         
           
* ２つのサーボモータを独立制御可能        
1台のzeroから2つのサーボモータを独立制御可能。
2軸のカメラ台座をコントロールすること等も可能です。
           
* モータの駆動状況が見えるLEDを装備        
LEDにより駆動状況の確認が容易に。        
実験時やメンテナンス時に役立ちます。

* 高分解能16bitPWM        
16bitの高分解能PWM制御を用い、Duty幅をμ秒単位で制御可能！
