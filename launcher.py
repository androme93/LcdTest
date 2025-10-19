#!/usr/bin/env python3
"""
LCD Test Launcher Script
LCD测试程序启动器

此脚本用于检查环境并启动LCD测试程序
"""
import sys
import subprocess
import os


def check_python_version():
    """检查Python版本"""
    if sys.version_info < (3, 6):
        print("错误: Python版本过低！")
        print(f"当前版本: {sys.version}")
        print("需要版本: Python 3.6 或更高")
        return False
    return True


def check_dependencies():
    """检查依赖是否已安装"""
    try:
        import PyQt5
        print("✓ PyQt5 已安装")
        return True
    except ImportError:
        print("✗ PyQt5 未安装")
        print("\n请运行以下命令安装依赖:")
        if sys.platform == 'win32':
            print("  Windows用户: 运行 install.bat")
            print("  或手动执行: pip install -r requirements.txt")
        else:
            print("  pip install -r requirements.txt")
        return False


def main():
    """主函数"""
    print("=" * 60)
    print("LCD测试程序启动器")
    print("=" * 60)
    print()
    
    # 检查Python版本
    print("检查Python版本...")
    if not check_python_version():
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print()
    
    # 检查依赖
    print("检查依赖...")
    if not check_dependencies():
        sys.exit(1)
    print()
    
    # 启动主程序
    print("启动LCD测试程序...")
    print("=" * 60)
    print()
    
    try:
        # 导入并运行主程序
        from main import main as run_main
        run_main()
    except KeyboardInterrupt:
        print("\n程序被用户中断")
        sys.exit(0)
    except Exception as e:
        print(f"\n程序运行出错: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
