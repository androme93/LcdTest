@echo off
REM LCD测试程序安装脚本
REM 此脚本用于安装程序所需的Python依赖

echo ================================
echo LCD测试程序 - 依赖安装
echo ================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未检测到Python环境！
    echo 请先安装Python 3.6或更高版本
    echo 下载地址: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo 正在安装依赖包...
echo.

REM 升级pip (忽略错误继续)
echo 正在升级pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo 警告: pip升级失败，将继续安装依赖...
    echo.
)

REM 安装依赖
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo 依赖安装失败！
    echo 请检查网络连接或手动运行: pip install -r requirements.txt
    pause
    exit /b 1
) else (
    echo.
    echo ================================
    echo 安装完成！
    echo ================================
    echo.
    echo 现在可以运行 run.bat 启动程序
    echo.
    pause
)
