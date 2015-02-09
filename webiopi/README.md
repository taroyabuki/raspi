# WebIOPI

Raspberry Pi 2では動作しない（2015/02/9）。

## インストールと起動・停止

```sh
wget "http://downloads.sourceforge.net/project/webiopi/WebIOPi-0.7.0.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fwebiopi%2Ffiles%2F&ts=1423473182&use_mirror=cznic" -O WebIOPi-0.7.0.tar.gz
tar zxf WebIOPi-0.7.0.tar.gz
cd WebIOPi-0.7.0
sudo ./setup.sh
```

### 起動

```sh
sudo webiopi -d -c /etc/webiopi/config
```

### 停止

`Ctrl-C`で停止する。

## DEMO

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

`http://RaspberryPiのIPアドレス:8000/hello.html`にアクセスする。

## トグルスイッチ

### Pythonスクリプト

1. `~/webiopi/switch.py`を作成する。
1. `switch.py`を`/etc/webiopi/config`に登録する。

```
myscript = /home/pi/webiopi/switch.py
```

### HTMLファイル

`~/webiopi/htdocs/switch.html`を作成する。

### 動作確認

1. WebIOPiを再起動して、`http://RaspberryPiのIPアドレス:8000/switch.html`にアクセスする。
1. WebIOPiのデモや先に作成した`toggle.py`、`event.py`を使ってLEDを操作して、その結果がswitch.htmlに反映されないことを確認する。
1. `switch.html`の一部を`webiopi().refreshGPIO(true);`のように変更して、ページをリロードする。
1. WebIOPiのデモや先に作成した`toggle.py`、`event.py`を使ってLEDを操作して、その結果がswitch.htmlに反映されることを確認する。
1. ブラウザの開発者ツール等で、通信の様子を観察する。
