# SoShield (Don't put anything into microwave oven!!!)

## Table of Contents

- [Introduction](#Introduction)
- [Requirements](#Requirements)
- [Instructions](#Instructions)

### Introduction
Soshield aims to literally create a shield for people with social anxiety. If you have social anxiety, you really make a good choice buying our product. From today, you will be no longer harmed by any annoying human beings. The sensor can detect moving humans for you.

### Requirements

#### Option 1: Buy our product directly with a friendly price
Visit our website to purchase.

#### Option 2: Geek, build your own (Not recommanded!!)
Key material list:
- [ESP8266\*1 (CH340G)](https://detail.tmall.com/item.htm?spm=a230r.1.14.16.32d967dfbd0Mvz&id=606082163513&ns=1&abbucket=5)
- [DF robot microwave sensor\*1](https://www.dfrobot.com.cn/goods-1231.html)
- Arduino wires\*20
- [Battery board (Optional)](https://detail.tmall.com/item.htm?spm=a230r.1.14.23.4a26246bT7gXNZ&id=632138891625&ns=1&abbucket=5)
- Arduino Uno\*1


### Instructions
1. Download the whole thing by using command
```
git clone https://github.com/eurethia/SoShield.git
```
2. Open the whole folder of SoShield using visual studio code and install requirements.txt by
 ```
  pip install -r requirements.txt
 ```

3. Configure the line ```WiFiMulti.addAP("hotspot", "1233211234567");``` in <b>BasicHttpClient</b> to your wifi  name and password. Configure the line ```if (http.begin(client, "http://172.20.10.3:5000/stop/"))``` in <b>BasicHttpClient</b> to your IP address (```https://YOUR IP ADRESS/stop/```). Burn the code into the ESP8266 in the SoShield packet by using Arduino software and a normal connecting cable. 

4. Use terminal to run the command
  ```
  python3 app.py
  ```

5. At the actication page, enter the activation code found in the SoShield kit. If this is the first time you use our app, you can enter any username and password combinations. But remember, this combination will be your final one and unchangable. We highly recommand you to use your email as username.

6. You will be directed to the safe page. Click "Start" and try to make motions. If the screen changes to danger, congradulations, it works! You will be redirected back to the safe page in 2 minutes.

7. If you want to calibrate the sensitivity of the sensor, open the SoShield kit and use a screwdriver to adjust the microwave sensor. 
