<!--
---
name: ADRSZUP
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZUP ゼロワン 電源保持基板
url: http://bit-trade-one.co.jp/adrszup/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/4th/ADRSZUP_Capacitor
buy: 
image: 'adrszup.png'
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
  '31':
    name: ShutDownSW
    mode: input
    active: low
  '37':
    name: StatusLED
    mode: output
    active: high
-->
ADRSZUP ゼロワン 電源保持基板
-------------------
<!--
<img alt="" class="alignnone size-full wp-image-8684" height="300" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/12/026384f828d666b8a45d324203dca564.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/12/026384f828d666b8a45d324203dca564.png 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/12/026384f828d666b8a45d324203dca564-300x129.png 300w" width="696"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20300%22%3E%3C/svg%3E)
-->

**[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**

### 製品の特徴

**・コンパクトな”pHAT”サイズ**

コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

**・急な停電の際、シャットダウン迄の時間を確保！**

ラズパイの故障原因の一つに、通電時の電源遮断が挙げられます。

 大容量25Fのスーパーキャパシタを2本備える本製品は、通常時はラズパイ本体へ電力を供給しつつ電力を貯蓄。

停電等電力供給が途絶えた際にはラズパイへ即時給電を開始。

シャットダウンシークエンスを終了する迄の間、ラズパイを保護します。

※UPS（無停電電源）のように、電力供給が途絶えた後もラズパイを動かし続けることはできません。

・動作状況が見えるLEDを装備

ステータスLEDにより駆動状況の確認が容易に、実験時やメンテナンス時に役立ちます。

ご注意！

本製品をお使いになるには電子工作や電子回路についての一般的な知識が必要です。

（＊Raspberry Pi Zero本体及びケース、ケーブル類は付属致しません。）
<!--
<img alt="" class="alignnone size-full wp-image-8685" height="176" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/12/654bb861f3262672ec224525263b3126.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/12/654bb861f3262672ec224525263b3126.png 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/12/654bb861f3262672ec224525263b3126-300x76.png 300w" width="696"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20176%22%3E%3C/svg%3E)
-->

**基本仕様 **

【対応機種】推奨機種：Raspberry Pi Zero  WH

      対応可能機種：Raspberry Pi Zero v1.3 / W  (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)

             Raspberry Pi 2/3 (ネジ固定が出来ない場合があります、再起動スイッチは使えません)

【LED】ステータス×1（プログラムで制御）、CHARGE（スーパーキャパシタに電荷が蓄えられているとき点灯）

【スイッチ】再起動(RUN)スイッチ／シャットダウンスイッチ(シャットダウン等の動作についてはWEBページをご確認下さい)

【インターフェース】MicroB USB端子 x1(給電用）

【本体寸法】W65×D30×H36mm (突起部含めず)

【本体重量】27g

【電源】DC5V、各RaspberryPi推奨のA数でご使用下さい

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
