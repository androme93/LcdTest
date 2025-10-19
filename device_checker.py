"""
Device Manager Touch Device Checker
检查Windows设备管理器中是否存在触摸设备
"""
import sys
import subprocess


def check_touch_device():
    """
    检查系统中是否有触摸设备
    Returns:
        bool: True if touch device exists, False otherwise
    """
    if sys.platform != 'win32':
        print("警告: 此程序仅支持Windows系统")
        return False
    
    try:
        # 使用Windows Management Instrumentation命令行工具查询触摸设备
        # 查询HID兼容触摸屏设备
        result = subprocess.run(
            ['wmic', 'path', 'Win32_PnPEntity', 'where', 
             '"Name like \'%touch%\' or Name like \'%Touch%\' or Name like \'%HID%\'"',
             'get', 'Name'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # 解析输出
        output = result.stdout.strip()
        lines = [line.strip() for line in output.split('\n') if line.strip()]
        
        # 过滤掉标题行
        devices = [line for line in lines if line and line != 'Name']
        
        if devices:
            print("检测到以下可能的触摸设备:")
            for device in devices:
                print(f"  - {device}")
            return True
        else:
            print("未检测到触摸设备")
            return False
            
    except subprocess.TimeoutExpired:
        print("设备查询超时")
        return False
    except FileNotFoundError:
        print("未找到WMIC命令，可能不是Windows系统或命令不可用")
        return False
    except Exception as e:
        print(f"检查触摸设备时发生错误: {e}")
        return False


if __name__ == "__main__":
    has_touch = check_touch_device()
    if has_touch:
        print("\n✓ 系统支持触摸功能")
    else:
        print("\n✗ 系统不支持触摸功能或未检测到触摸设备")
