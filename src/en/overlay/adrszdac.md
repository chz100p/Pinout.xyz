<!--
---
name: ADRSZDAC
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZDAC ゼロワン ハイレゾDAC拡張基板
url: http://bit-trade-one.co.jp/adrszdac/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/3rd/ADRSZDAC_Hi-Rez_DAC
buy: 
image: 'adrszdac.png'
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
  '12':
    name: Enable
    mode: output
    active: high
  '35':
    name: Enable
    mode: output
    active: high
  '40':
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
ADRSZDAC ゼロワン ハイレゾDAC拡張基板
-------------------------

<!--
<img alt="" class="wp-image-8152" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/2d07e978bf3a448e9f621b23ca6b71ba.jpg" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/2d07e978bf3a448e9f621b23ca6b71ba.jpg 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/2d07e978bf3a448e9f621b23ca6b71ba-300x129.jpg 300w"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)
-->

**[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**

#### 製品の特徴

**・コンパクトな”pHAT”サイズ**  
コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

**・小さな基板でHi-Resオーディオを実現。ネットワークオーディオ端末としても利用可能。**  
PCM5122を使用し、最大bit長32bit,最大サンプリング周波数384kHzまでのHi-Res音源を制御。  
お好みのソフトウェアを自由にインストールでき、ネットワークオーディオプレイヤー等としての活用も。  
別売りの外部システムクロック入力にも対応、さらなる音質の向上も可能。

**・動作状況が見えるLEDを装備**  
ステータスLEDにより駆動状況の確認が容易に、実験時やメンテナンス時に役立ちます。

ご注意！  
本製品をお使いになるには電子工作や電子回路についての一般的な知識が必要です。  
（＊Raspberry Pi Zero本体及びケース、ケーブル類は付属致しません。）

<!--
<img alt="" class="wp-image-8153" sizes="(max-width: 693px) 100vw, 693px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/658326031b180e9a4e18270f9c0332c2.jpg" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/658326031b180e9a4e18270f9c0332c2.jpg 693w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/09/658326031b180e9a4e18270f9c0332c2-300x78.jpg 300w"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)
-->

###### 基本仕様

【対応機種】Raspberry Pi Zero v1.3 / W / WH (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)Raspberry Pi 2/3 (ネジ固定が出来ない場合があります、再起動スイッチは使えません)  
【LED】ステータスx1、PLAY（再生中に点灯）※使用するソフトによっては点灯しない場合があります  
【スイッチ】再起動スイッチ／シャットダウンスイッチ(シャットダウン等の動作についてはWEBページをご確認下さい)  
【オーディオデータビット長】16/24/32bit ※PCM5122の仕様  
【サンプリング周波数】最小8kHz、最大384kHz ※PCM5122の仕様  
【アナログ出力電圧】標準2.1Vrms  
【負荷インピーダンス】：最小1kΩ  
【入出力】I2S入力×1 I2C×1  
3.5mmLINE出力x1  
【本体寸法】W65×D30×H19mm (突起部含めず)  
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
