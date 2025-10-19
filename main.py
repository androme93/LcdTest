"""
LCD Testing Application - Main Entry Point
LCD测试应用程序主入口

作者: 基于原Qt C++项目改写
日期: 2025
功能: LCD显示和触摸测试
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from device_checker import check_touch_device
from lcd_test_widgets import BrightDarkSpotTest, TouchTestWidget


class LcdTestApplication(QWidget):
    """LCD测试主应用程序"""
    
    def __init__(self):
        super().__init__()
        self.bright_dark_test = None
        self.touch_test = None
        self.init_ui()
        
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle('LCD测试程序')
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        # 设置窗口大小 (可根据屏幕分辨率调整)
        self.setGeometry(100, 100, 1024, 600)
        
        # 检查触摸设备
        self.check_and_start()
        
    def check_and_start(self):
        """检查设备并启动测试"""
        print("正在检查系统触摸设备...")
        has_touch = check_touch_device()
        
        if has_touch:
            print("检测到触摸设备，开始测试...")
            self.start_bright_dark_test()
        else:
            # 显示警告对话框
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("设备检查")
            msg.setText("未检测到触摸设备！")
            msg.setInformativeText("系统中未找到可用的触摸设备。\n您仍然可以继续测试，但触摸功能可能无法正常工作。")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.button(QMessageBox.Yes).setText("继续测试")
            msg.button(QMessageBox.No).setText("退出")
            
            result = msg.exec_()
            
            if result == QMessageBox.Yes:
                print("用户选择继续测试...")
                self.start_bright_dark_test()
            else:
                print("用户选择退出...")
                QApplication.quit()
                
    def start_bright_dark_test(self):
        """开始亮点暗点测试"""
        self.hide()
        self.bright_dark_test = BrightDarkSpotTest(self)
        
        # 设置全屏或窗口模式
        screen = QApplication.primaryScreen().geometry()
        self.bright_dark_test.setGeometry(screen)
        # self.bright_dark_test.showFullScreen()  # 全屏模式
        self.bright_dark_test.showMaximized()  # 最大化窗口模式
        
    def show_touch_test(self):
        """显示触摸测试"""
        self.touch_test = TouchTestWidget(self)
        
        # 设置全屏或窗口模式
        screen = QApplication.primaryScreen().geometry()
        self.touch_test.setGeometry(screen)
        # self.touch_test.showFullScreen()  # 全屏模式
        self.touch_test.showMaximized()  # 最大化窗口模式


def main():
    """主函数"""
    app = QApplication(sys.argv)
    
    # 设置应用程序信息
    app.setApplicationName("LCD测试程序")
    app.setOrganizationName("LCD Testing")
    
    # 创建并显示主窗口
    main_window = LcdTestApplication()
    main_window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
