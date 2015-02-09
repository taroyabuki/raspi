# Mathematica

## ロボットは東大に入れるか

z軸を軸とする半径1の円柱の側面で、xy平面より上（z軸の正の方向）にあり、平面x-√3y+z=1より下（z軸の負の方向）にある部分をDとする。Dの面積を求めよ。（1976年 東大入試 理科第5問 新過程）

```bash
wolfram
```

```mathematica
Area[ImplicitRegion[And[
    x^2 + y^2 == 1,
    z >= 0,
    z <= 1 - x + Sqrt[3] y],
   {x, y, z}]] // Simplify
```

## LED

Raspberry Pi 2では動かない（2015/02/09）。

```mathematica
DeviceConfigure["GPIO", 25 -> "Output"]

Do[
  DeviceWrite["GPIO", 25 -> 1];
  Pause[0.1];
  DeviceWrite["GPIO", 25 -> 0];
  Pause[0.1],
{50}];

Exit[]
```
