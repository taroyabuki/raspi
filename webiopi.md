# WebIOPI

## インストール

```sh
wget "http://downloads.sourceforge.net/project/webiopi/WebIOPi-0.7.0.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fwebiopi%2Ffiles%2F&ts=1423473182&use_mirror=cznic" -O WebIOPi-0.7.0.tar.gz
tar zxf WebIOPi-0.7.0.tar.gz
cd WebIOPi-0.7.0
sudo ./setup.sh
```

## 起動と停止

```sh
sudo webiopi -d -c /etc/webiopi/config
```

`Ctrl-C`で停止する。

## DEMO

not work on raspi 2?

1. `http://RaspberryPiのIPアドレス:8000/`にアクセスする。
1. LEDの回路で、GPIO 25のオン・オフを試す。

ユーザ名：webiopi　パスワード：raspberry

## Hello, World

### ドキュメントルート

サンプルをコピーする。

```sh
cp -r /usr/share/webiopi ~/
```

`/etc/webiopi/config`を編集し、`/home/pi/webiopi/htdocs`を`doc-root`にする。

```
doc-root = /home/pi/webiopi/htdocs
```

### hello.html

`~/webiopi/htdocs/hello.html`を作成する。

```html:hello.html
<!DOCTYPE html>
<html>
<head>
  <title>Hello</title>
</head>
<body>
  <p>Hello, World.</p>
</body>
</html>
```

`http://RaspberryPiのIPアドレス:8000/hello.html`にアクセスする。

## トグルスイッチ

### Pythonスクリプト

`~/webiopi/switch.py`を作成する。

```python:switch.py
import webiopi

GPIO = webiopi.GPIO
LIGHT = 25

def setup():
  GPIO.setFunction(LIGHT, GPIO.OUT)

def loop():
  webiopi.sleep(1)

def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
```

`switch.py`を`/etc/webiopi/config`に登録する。

```
myscript = /home/pi/webiopi/switch.py
```

### HTMLファイル

`~/webiopi/htdocs/switch.html`を作成する。

```html:switch.html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>Switch</title>
  <script src="/webiopi.js"></script>
  <style>
  * { margin: 0px; padding: 0px;
  }
  #gpio25 {
    position: absolute;
    width:160px; height: 100px;
    top: 50%; left: 50%;
    transform: translateX(-50%) translateY(-50%);
    font-size: large;
  }
  #gpio25.LOW {
    color: black; background-color: white;
  }
  #gpio25.HIGH {
    color: white; background-color: Red;
  }
  </style>
</head>
<body>
  <div id="controls"></div>
  <script>
  webiopi().ready(function() {
    var button = webiopi().createGPIOButton(25, "On / Off");
    $("#controls").append(button);
    webiopi().refreshGPIO(false);
  });
  </script>
</body>
</html>
```
### 動作確認

1. WebIOPiを再起動して、`http://RaspberryPiのIPアドレス:8000/switch.html`にアクセスする。
1. WebIOPiのデモや先に作成した`toggle.py`、`event.py`を使ってLEDを操作して、その結果がswitch.htmlに反映されないことを確認する。
1. `switch.html`の一部を`webiopi().refreshGPIO(true);`のように変更して、ページをリロードする。
1. WebIOPiのデモや先に作成した`toggle.py`、`event.py`を使ってLEDを操作して、その結果がswitch.htmlに反映されることを確認する。
1. ブラウザの開発者ツール等で、通信の様子を観察する。
