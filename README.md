# Kings-of-Glory_CoinCollecter
一个王者荣耀刷金币辅助

## 刷币原理
王者荣耀的冒险模式里有个挑战模式，第一次过关可以获得比较多的金币，后面重新挑战还是会获得少量金币，这不算是bug，也可以手动刷金币。<br>
此关卡使用纯输出英雄20秒左右可以打BOSS，50秒左右可以通关，每次重复通关可以获得奖励19金币。<br>
每周金币上限4200，需要接近4个小时，不建议一次刷满.<br>
## 系统要求
* Windows/MacOS
* Python
* Android SDK

## 脚本默认环境
脚本场景
> 关卡：大师级 - 陨落的废都 - 魔女回忆
> 英雄：刘邦

脚本测试设备
> MI6 , 开发者模式

## 使用步骤
1. 界面打开至挑战关卡：陨落的废都 - 魔女回忆 -点击下一步
2. 进入阵容调整界面，提前安排好阵容
3. cmd输入并执行以下命令
```
python run.py
```

## 准备
- 准备安卓手机一部
- 手机需开启USB调试模式，允许电脑调试
- 电脑需要有[ADB](https://developer.android.com/studio/releases/platform-tools.html)驱动，可以到[这里](https://adb.clockworkmod.com/)下载。
- ADB需要加入环境变量PATH中，方便随时调用。
- 电脑上需要安装Python

### 代码实现
* 场景介绍<br>
> 场景1
![scene_1](https://github.com/Tsingtong/Kings-of-Glory_CoinsCollect/raw/master/Scenes/scene_%20(1).jpg)
> 场景2
![scene_2](https://github.com/Tsingtong/Kings-of-Glory_CoinsCollect/raw/master/Scenes/scene_%20(2).jpg)
> 场景3
![scene_3](https://github.com/Tsingtong/Kings-of-Glory_CoinsCollect/raw/master/Scenes/scene_%20(3).jpg)
> 场景4
![scene_4](https://github.com/Tsingtong/Kings-of-Glory_CoinsCollect/raw/master/Scenes/scene_%20(4).jpg)
> 场景5
![scene_5](https://github.com/Tsingtong/Kings-of-Glory_CoinsCollect/raw/master/Scenes/scene_%20(5).jpg)
> 场景6
![scene_6](https://github.com/Tsingtong/Kings-of-Glory_CoinsCollect/raw/master/Scenes/scene_%20(6).png)
> 场景7
![scene_7](https://github.com/Tsingtong/Kings-of-Glory_CoinsCollect/raw/master/Scenes/scene_%20(7).jpg)
> 场景8
![scene_8](https://github.com/Tsingtong/Kings-of-Glory_CoinsCollect/raw/master/Scenes/scene_%20(8).jpg)

* 通过`adb shell`命令模拟屏幕点击
```
adb shell input tap 500 500
```

* 关卡分为四个部分，8个场景
```python
## part_1   进入游戏状态
#scene_1
    if game_mode == 1:
        logging.debug('#0 开始闯关')
        tap_screen(1600, 970)
        sleep(part_1_wait)
## part_2   游戏中状态
#scene_2
    logging.debug('#1 自动刷怪开启!')
    tap_screen(1780, 40)
    for i in range(part_2_wait):
        tap_screen(1720, 80)
        sleep(1)
## part_3   妲己说废话状态
#scene_3-7
    logging.debug('#2 跳过...\n')
    for i in range(part_3_wait):
        tap_screen(1600, 980)
        sleep(0.2)
## part_4   过关页面展示状态
#scene_8
    logging.debug('#3 确认结果')
    tap_screen(1600, 970)
    sleep(part_4_wait)
```
* 容错<br>
关于容错机制及妲己废话时间不确定的处理方法，我们采用`随缘法`进行容错处理。这是非常佛系的理论思想指导体系，我开创性地将这种思想应用于程序设计中。<br>
经测试，对于场景3采用随缘法进行屏幕模拟点击，脚本容错率达到99.999%

* 参数调整<br>
脚本中明确了可进行参数调整的变量，其他代码无需修改<br>
* 屏幕分辨率
* 通关模式：1=重新挑战 -> 挑战界面，2=重新挑战-> 更换阵容
* 各步骤等待间隔
* 刷金币次数<br>

注意：<br>
1. 本脚本纯属娱乐和探索的心得，暂时不会被封号。
1. 铭文，手机性能，英雄选择都会影响通关速度，自己微调等待时间。
3. 如果你不想被USB数据线束缚，可以考虑[使用无线连接Android真机](https://betacat.online/posts/2017-12-12/connect-adb-via-wifi/)

## 相关链接
- [在 Windows 下搭建 Appium + Android 自动化测试环境](https://betacat.online/posts/2017-05-03/setup-appium-automation-test-environment/)
- [在Mac OSX 上配置Appium+Android自动化测试环境](https://betacat.online/posts/2017-12-10/setup-appium-test-environment-on-mac-osx/)
