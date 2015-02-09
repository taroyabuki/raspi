# 準備

USBメモリで配布するもの

* NOOBS
* Fritzing

## OSのインストール

1. SDカードをPCにセットする。
1. 必要なら、[SD/SDHC/SDXC用SDフォーマッター4.0](https://www.sdcard.org/jp/downloads/formatter_4/)でSDカードをフォーマットする。
1. <http://www.raspberrypi.org/downloads/>から、NOOBSのZIPファイルをダウンロード（USBメモリで配布）、展開しする。
1. 展開してできたファイルをすべてSDカードにコピーする。
1. Raspberry PiにLANケーブル、HDMIケーブルを接続し、SDカードを挿入する。
1. microUSBケーブルを接続し、電源を入れる。
1. インストーラの指示に従ってインストールする。

## 初期設定

1. `sudo rasp-config`でSSHを有効にする。
1. 再起動時に表示される「My IP address is XXX.XXX.XXX.XXX」でIPアドレスを確認する。

ユーザ名：pi　パスワード：raspberry

## PCからの接続

1. <http://sourceforge.jp/projects/ttssh2/>からインストーラをダウンロードし、実行するインストールする。
1. TeraTermからRaspberry Piに接続する。

## for Raspberry Pi 2

http://blog.adafruit.com/2015/02/05/how-to-fix-error-loading-rpi-gpio-python-library-on-your-brand-new-raspberry-pi-2/

## テキスト編集環境

nanoやviが最初から入っている。`sudo apt-get install emacs`をしてもよいし、Sambaを導入してWindows環境で編集してもよい。
