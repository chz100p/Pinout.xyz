<!--
---
name: ADRSZSN
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZSN ゼロワン ソレノイド拡張基板
url: http://bit-trade-one.co.jp/product/module/adrszsn/
github: https://github.com/bit-trade-one/RasPi-Zero-One-Series/tree/master/1st/ADRSZSN_Solenoid
buy: http://btoshop.jp/2018/07/02/4562469771854/
image: 'adrszsn.png'
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
  '7':
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
-->
ADRSZSN ゼロワン ソレノイド拡張基板
----------------------
<!--
[

<img alt="WP-製品紹介M41-ADRSZSN-MAIN" class="alignnone size-full wp-image-7558" height="300" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/c040e602f0789b5843f01a25265a00f3.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/c040e602f0789b5843f01a25265a00f3.png 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/c040e602f0789b5843f01a25265a00f3-300x129.png 300w" width="696"/>

![WP-製品紹介M41-ADRSZSN-MAIN](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20300%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/c040e602f0789b5843f01a25265a00f3.png)
-->

**[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**
===========================================================================================

**製品の特長**

**・コンパクトな”pHAT”サイズ**

コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！

**・選べるソレノイド電源**

ラズパイZeroから5V電源供給のほか、外部から12V2Aまでの電源供給に対応（ピンヘッダにより切替）

**・ソレノイドの駆動状況が見えるLEDを装備**

LEDにより駆動状況の確認が容易に。実験時やメンテナンス時に役立ちます。
<!--
各部の名称

<img alt="" class="elementOfPhoto" src="https://llstock.s3-ap-northeast-1.amazonaws.com/uploads/photo/image/37504/middle\_stockimage.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAI7P6SP7G3K7DHTNA%2F20180629%2Fap-northeast-1%2Fs3%2Faws4\_request&amp;X-Amz-Date=20180629T095351Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=34fbde7d6778f1032049f32a1e368d3b38e02e8a91375cc9dc332d15a4e4ddcd"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)[

<img alt="WP-製品紹介M41-ADRSZSN-SUB" class="alignnone size-full wp-image-7702" height="176" sizes="(max-width: 691px) 100vw, 691px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/20b011cd161c6793789c3660fc21cea1.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/20b011cd161c6793789c3660fc21cea1.png 691w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/20b011cd161c6793789c3660fc21cea1-300x76.png 300w" width="691"/>

![WP-製品紹介M41-ADRSZSN-SUB](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20691%20176%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/20b011cd161c6793789c3660fc21cea1.png)
-->

ご注意！

本製品をお使いになるには電子工作や電子回路についての一般的な知識とマイナスドライバーが必要です。

（＊Raspberry Pi Zero本体及びソレノイド、ケース、ケーブル類は付属致しません。）

基本仕様

【対応機種】Raspberry Pi Zero v1.3 / W / WH (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)Raspberry Pi 2/3 (ネジ固定が出来ない場合があります、再起動スイッチは使えません)

【最大制御数】1個【入力】レベル入力（GPIO4、HでソレノイドON)

【基板電源】3.3V/5V (ラズパイZeroから供給)

【出力】電流出力（端子台)

【LED】システム状態用×1、ソレノイド動作状態用×1 (ソレノイドONで点灯)

【スイッチ】再起動スイッチ／シャットダウンスイッチ([シャットダウン等の動作についてはWEBページをご確認下さい](http://bit-trade-one.co.jp/blog/201807032/))

【電源】ソレノイドの電源をGPIO給電 / 外部給電からジャンパで切り替え可能

【本体寸法】W65×D30×H23mm (突起部含めず)

【本体重量】約14g

【付属品】ネジセットx1／保証書x1

【生産国】Made in Japan

【保証期間】お買い上げから1年間

使用可能なソレノイド仕様

・電源：5V (ラズパイZeroから供給)、又はDC3～12V 2A以内(端子台から供給)

・DC3～12V (5V以外は端子台から要供給)

・2A以内(端子台から供給する場合)

・ソレノイドOFFの時、バネ等で復帰すること

※ 自己保持型はサポート対象外となります。

―――本製品取扱についてのご注意―――

・本製品は、ホビー向け商品です。個人利用に限定され、著作権者の許可なく商用利用できません。

・記載の部品性能は部品単体での性能であり、製品寿命を保証するものではありません。

・ご利用のPC、Raspberry PiおよびOS環境によってはすべての機能をご利用いただけない場合があります。

・本キットの製作/使用に関し当社の責に帰すべき事由に基づき、お客様に損害が生じた場合、直接被害に限り、販売代金を上限として損害を賠償し、いかなる場合においても販売代金以上の損害を賠償しないものとします。

・改良のため、予告なく仕様変更をすることがあります。予めご了承下さい。

＊Raspberry Pi本体及びケース、ケーブル類は付属致しません。

Raspberry Piは英国Raspberry Pi財団の登録商標です。Raspberry Pi is a trademark of the Raspberry Pi Foundation. そのほか記載されているロゴ、システム名、製品名は各社及び商標権者の登録商標あるいは商標です。
