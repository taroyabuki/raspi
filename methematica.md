# Mathematica

## ロボットは東大に入れるか

$z$軸を軸とする半径$1$の円柱の側面で，$xy$平面より上（$z$軸の正の方向）にあり，平面$x-\sqrt{3}y+z=1$より下（$z$軸の負の方向）にある部分を$D$とする．$D$の面積を求めよ．（1976年 東大入試 理科第5問 新過程）

```
wolfram
```

```
Area[ImplicitRegion[And[
    x^2 + y^2 == 1,
    z >= 0,
    z <= 1 - x + Sqrt[3] y],
   {x, y, z}]] // Simplify
```

## LED

not work on RaspPi 2?

```
DeviceConfigure["GPIO", 25 -> "Output"]

Do[
  DeviceWrite["GPIO", 25 -> 1];
  Pause[0.1];
  DeviceWrite["GPIO", 25 -> 0];
  Pause[0.1],
{50}];

Exit[]
```
