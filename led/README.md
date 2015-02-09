# LED

## 点灯

![](image/led_a.png)

[Fritzing](http://fritzing.org/home/)を使ってブレッドボード用の回路図を描いてみる。

## 操作（シェル）

![](image/led2_a.png)

GPIO 25を利用可能にし、出力用にする。

```bash
sudo su
echo 25 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio25/direction
```

オン

```bash
echo 1 > /sys/class/gpio/gpio25/value
```

オフ

```bash
echo 0 > /sys/class/gpio/gpio25/value
```

点滅

```bash
while :
do
  echo 1 > /sys/class/gpio/gpio25/value
  sleep 1
  echo 0 > /sys/class/gpio/gpio25/value
  sleep 1
done
```

利用終了

```bash
echo 25 > /sys/class/gpio/unexport
exit
```

## 操作（Python）

<src/led2.py>

## タクトスイッチ

![](image/tact_a.png)

<src/tact.py>

## タクトスイッチ＋プルダウン抵抗

![](image/tact-pulldown_a.png)

<src/tact-pulldown.py>

## タクトスイッチ + LED

1. タクトスイッチの動作確認のために、スイッチを押すとLEDが光る単純な回路を作ってみる。
1. スイッチが押されているかどうかをRaspberry Piで判断するような回路を作る。（この後でトグルスイッチを作る準備である。）

![](image/tact-led_a.png)

<src/tact-led.py>

## トグルスイッチ

<src/toggle.py>

## イベント

<src/event.py>
