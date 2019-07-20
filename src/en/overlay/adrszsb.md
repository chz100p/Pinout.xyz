<!--
---
name: ADRSZSB
class: board
type: other
formfactor: pHAT
manufacturer: BitTradeOne
description: ADRSZSB　ゼロワン サーボモータ拡張基板
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
ADRSZSB ゼロワン サーボモータ拡張基板
-----------------------

<!--
[

<img alt="WP-製品紹介M42-ADRSZSB-MAIN" class="alignnone size-full wp-image-7559" height="300" sizes="(max-width: 696px) 100vw, 696px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/c1c3e4283d9c365f90eb88b318e2f8df.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/c1c3e4283d9c365f90eb88b318e2f8df.png 696w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/c1c3e4283d9c365f90eb88b318e2f8df-300x129.png 300w" width="696"/>

![WP-製品紹介M42-ADRSZSB-MAIN](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20696%20300%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/06/c1c3e4283d9c365f90eb88b318e2f8df.png)
-->

### **[ゼロワン使用法・サンプルプログラムはこちら（GitHub）](https://github.com/bit-trade-one/RasPi-Zero-One-Series)**

**製品の特徴    **
-------------

**・コンパクトな”pHAT”サイズ**         

コンパクトなRaspberry Pi Zero にぴったりの”pHAT”サイズでラズパイZeroと重ねて使用可能！   

**・5Vから最大12Vまで利用可能な外部電源端子を装備  **     

ジャンパを切り替えることで、GPIO/外部電源端子からの給電を選択可能。     

様々な使用形態に対応します。         

**・２つのサーボモータを独立制御可能 **       

1台のzeroから2つのサーボモータを独立制御可能。  
2軸のカメラ台座をコントロールすること等も可能です。

**・モータの駆動状況が見えるLEDを装備  **      

LEDにより駆動状況の確認が容易に。        

実験時やメンテナンス時に役立ちます。

・**高分解能16bitPWM**

16bitの高分解能PWM制御を用い、Duty幅をμ秒単位で制御可能！

<!--
各部の名称   

<img alt="" class="elementOfPhoto" src="https://llstock.s3-ap-northeast-1.amazonaws.com/uploads/photo/image/37494/middle\_stockimage.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAI7P6SP7G3K7DHTNA%2F20180629%2Fap-northeast-1%2Fs3%2Faws4\_request&amp;X-Amz-Date=20180629T095817Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=f2b67cbc81687516607d78c2bf0d217ae6801210e84853802e0a08caff6e3740"/>

![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20%20%22%3E%3C/svg%3E)[

<img alt="WP-製品紹介M42-ADRSZSB-SUB" class="alignnone size-full wp-image-7683" height="167" sizes="(max-width: 691px) 100vw, 691px" src="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/0701ffd8f8159fda2fca853b9d321e05.png" srcset="http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/0701ffd8f8159fda2fca853b9d321e05.png 691w, http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/0701ffd8f8159fda2fca853b9d321e05-300x73.png 300w" width="691"/>

![WP-製品紹介M42-ADRSZSB-SUB](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20691%20167%22%3E%3C/svg%3E)](http://bit-trade-one.co.jp/wp/wp-content/uploads/2018/07/0701ffd8f8159fda2fca853b9d321e05.png)
-->

ご注意！           

本製品をお使いになるには電子工作や電子回路についての一般的な知識が必要です。    

（＊Raspberry Pi Zero本体及びサーボモータ、ケース、ケーブル類は付属致しません。）     

基本仕様           

【対応機種】Raspberry Pi Zero v1.3 / W / WH (v1.3,WにはGPIOピンヘッダのはんだ付けが必要です)   

Raspberry Pi 2/3（ネジ固定が出来ない場合があります、再起動スイッチは使えません）           

【スイッチ】再起動スイッチ／シャットダウンスイッチ([シャットダウン等の動作についてはWEBページをご確認下さい](http://bit-trade-one.co.jp/blog/201807032/))

【スイッチ】シャットダウンスイッチ/再起動スイッチ       

【LED】システム状態用×1、サーボモータ動作状態用×2       

【本体寸法】W65×D30×H22mm（突起部含めず）       

【本体重量】約14g          

【電源】サーボモーターの電源をGPIO給電 / 外部給電からジャンパで切り替え可能      

【PWM分解能】16bit          

【サーボモーター接続コネクタ】3ピン ピンヘッダ × 2ch       

【外部電源入力】DC5V～12V(最大) 端子台より給電

【付属品】 ネジセット1保証書1         

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
