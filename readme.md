# LcdTest - Python版本

这是一个基于Python PyQt5开发的用于测试LCD液晶屏显示和触摸功能的Windows应用程序。

## 版本说明

**当前版本：Python实现**
- 原项目基于Qt C++开发
- 现已重构为Python PyQt5实现，更易于维护和扩展

## 功能概述

LcdTest的主要功能是测试液晶屏的显示和触摸是否正常：

### 1. 设备检测
- 程序启动时自动检查Windows设备管理器中是否存在触摸设备
- 如未检测到触摸设备，会提示用户是否继续测试

### 2. 亮点暗点测试
- 显示不同的纯色背景（白、黑、红、绿、蓝、青、品红、黄）
- 每个颜色会在屏幕中央显示一个随机的4位数字
- 用户需要正确输入该数字才能进入下一个颜色测试
- 此测试用于检测LCD屏幕是否有亮点或暗点缺陷

### 3. 触摸测试
- 完成亮点暗点测试后，进入触摸测试界面
- 界面显示12×20的触摸方块网格
- 用户点击方块时，方块会变为绿色，同时显示红色十字线标识触摸位置
- 用于检测触摸屏的准确性和响应性

## 系统要求

- **操作系统**: Windows 7/8/10/11
- **Python**: 3.6 或更高版本
- **依赖库**: 
  - PyQt5 >= 5.15.0
  - pywin32 >= 300

## 安装和运行

### Windows用户（推荐）

1. **安装依赖** - 双击运行 `install.bat`
2. **启动程序** - 双击运行 `run.bat`

### 手动安装（所有平台）

1. **安装Python依赖**
   ```bash
   pip install -r requirements.txt
   ```

2. **运行程序**
   ```bash
   python main.py
   ```
   
   或使用启动器（会自动检查环境）：
   ```bash
   python launcher.py
   ```

## 项目结构

```
LcdTest/
├── main.py                 # 主程序入口
├── launcher.py            # 启动器（检查环境后运行）
├── device_checker.py       # 设备检测模块
├── lcd_test_widgets.py     # LCD测试界面组件
├── requirements.txt        # Python依赖列表
├── install.bat            # Windows依赖安装脚本
├── run.bat                # Windows快速启动脚本
├── readme.md              # 项目说明（本文件）
├── USAGE.md               # 详细使用指南
└── screenshot/            # 截图目录
```

### 主要模块说明

- **main.py**: 应用程序主入口，负责初始化和流程控制
- **device_checker.py**: 使用WMIC命令查询Windows设备管理器中的触摸设备
- **lcd_test_widgets.py**: 包含以下主要类
  - `BrightDarkSpotTest`: 亮点暗点测试窗口，显示纯色背景和验证数字
  - `TouchTestWidget`: 触摸测试窗口，包含触摸方块网格
  - `TouchLabel`: 触摸方块组件
  - `CrosshairWidget`: 十字线组件

## 技术特点

1. **设备检测**: 使用Windows WMI接口检测触摸设备
2. **用户验证**: 通过数字验证确保用户认真观察每个测试画面
3. **事件处理**: PyQt5的鼠标事件传递和分发机制
4. **界面绘制**: 使用QPainter进行自定义绘图

## 开发历史

- **原版本**: 基于Qt C++ Widget开发
- **当前版本**: 重构为Python PyQt5实现

## 原作者联系方式

**邮箱**: justdoit_mqr@163.com  
**新浪微博**: @为-何-而来