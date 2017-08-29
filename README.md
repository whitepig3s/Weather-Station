# School Weather Station Service
>我們是氣象站團隊! 我們希望開發出小型的氣象觀測站，並將氣象觀測站廣設於校園中，以利同學及老師在上課前可以知道學校的天氣狀況，定期觀測的數據也可作為預報或其他研究用途，此專案開源，所以學校也可將此氣象感測站依需求修改及作為教學用途，如有興趣參與計畫，歡迎與我們聯絡，我們會為你們的學校準備一組氣象站設備。 

### 氣象站服務

[http://weather.nhsh.tp.edu.tw](http://weather.nhsh.tp.edu.tw "氣象站服務")

### 站點架設需求(標準規格)
- 穩定電源(5V/110V/220V)
- 穩定網路(有線/無線)
- 通風良好
- 室外可裝光強度及雨水感測

### 安裝方法1
注意: 安裝前請和我們聯絡，我們會為您建立伺服器中的空間 <br>
下載我們釋出的映像檔(即將推出)並燒入記憶卡，將樹莓派開機後連上網路，執行以下步驟

1. 把感測器單元和樹莓派的 USB 連接
2. 查出感測器單元的 tty* 檔名
3. 執行 `/usr/WeatherServiceClient/install.sh`
4. 依序回答安裝過程中的問題
5. 完成安裝

### 安裝方法2

注意: 安裝前請和我們聯絡，我們會為您建立伺服器中的空間

Clone 我們的專案

```
git clone https://github.com/oxygen-TW/Weather-Station.git
cd Weather-Station
```

1. 使用 Arduino IDE 將 Frimrare 資料夾內的韌體燒錄至感測器單元(已安裝韌體則跳過)
4. 把感測器單元和樹莓派的 USB 連接
5. 查出感測器單元的 tty* 檔名
6. 執行 `install.sh`
7. 依序回答安裝過程中的問題
8. 完成安裝

### 如何移除

執行 `remove.sh`
```
sh remove.sh
```

### 感測器規格
- 簡單規格: 溫度、濕度、光強度
- 標準規格: 溫度、濕度、光強度、紫外線、雨水感測
- 細懸浮微粒型: 溫度、濕度、光強度、紫外線、雨水感測、PM1.0、PM2.5、PM10(開發中)
- 氣壓感測型: 溫度、濕度、光強度、紫外線、雨水感測，大氣壓力
- 土壤濕度監測型: 溫度、濕度、光強度、紫外線、雨水感測、土壤溼度

### 系統架構
- MCU -> Arduino nano(ATmega328)
- 溫溼度感測 -> DHT22
- 紫外線感測 -> UVM30A
- 光強度感測 -> 光敏電阻(測試用)
- 雨水感測 -> KMS030 或其他
- 細懸浮微粒感測 -> pms5003/pms5005
- 氣壓感測 -> BMP180 或其他
- 感測器OS -> Ubuntu IoT core
- Driver -> Python
- Firmware -> C/C++ for Arduino

### 技術需求
如果您對本專案有興趣，歡迎加入我們

- Android/IOS APP 開發
- MCU 開發
- 美工設計

### API

開發中


### 聯絡我們

Group email -> weatherstationtw@gmail.com