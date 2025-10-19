@echo off
REM LCD测试程序启动脚本
REM 此脚本用于在Windows系统上快速启动LCD测试程序

echo ================================
echo LCD测试程序
echo ================================
echo.

REM 检查Python是否安装
REM 优先使用Python Launcher (py)，如果不存在则使用python命令
py --version >nul 2>&1
if errorlevel 1 (
    python --version >nul 2>&1
    if errorlevel 1 (
        echo 错误: 未检测到Python环境！
        echo 请先安装Python 3.6或更高版本
        echo 下载地址: https://www.python.org/downloads/
        echo.
        pause
        exit /b 1
    )
    set PYTHON_CMD=python
) else (
    set PYTHON_CMD=py
)

echo 正在启动LCD测试程序...
echo.

REM 运行程序
%PYTHON_CMD% main.py

REM 如果程序异常退出，暂停以查看错误信息
if errorlevel 1 (
    echo.
    echo 程序异常退出！
    pause
)
