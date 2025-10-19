"""
LCD Testing Application
LCD测试应用程序 - 亮点暗点测试
"""
import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, 
                              QHBoxLayout, QLineEdit, QPushButton, QMessageBox,
                              QGridLayout, QFrame)
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QPainter, QColor, QPen, QFont


class BrightDarkSpotTest(QWidget):
    """亮点暗点测试窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_color_index = 0
        self.test_colors = [
            ('white', Qt.white),
            ('black', Qt.black),
            ('red', Qt.red),
            ('green', Qt.green),
            ('blue', Qt.blue),
            ('cyan', Qt.cyan),
            ('magenta', Qt.magenta),
            ('yellow', Qt.yellow),
        ]
        self.verification_number = None
        self.input_widget = None
        self.init_ui()
        
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle('LCD亮点暗点测试')
        self.setStyleSheet("background-color: white;")
        
        # 创建验证输入界面（初始隐藏）
        self.create_verification_widget()
        
        # 显示验证数字
        self.show_verification()
        
    def create_verification_widget(self):
        """创建验证输入界面"""
        self.input_widget = QWidget(self)
        self.input_widget.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 180);
            }
            QLabel {
                color: white;
                font-size: 24px;
                background-color: transparent;
            }
            QLineEdit {
                font-size: 24px;
                padding: 10px;
                background-color: white;
                border: 2px solid #4CAF50;
                border-radius: 5px;
            }
            QPushButton {
                font-size: 20px;
                padding: 10px 30px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        # 提示标签
        prompt_label = QLabel("请输入屏幕上显示的数字以继续测试:")
        prompt_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(prompt_label)
        
        # 输入框
        self.number_input = QLineEdit()
        self.number_input.setMaxLength(4)
        self.number_input.setAlignment(Qt.AlignCenter)
        self.number_input.setPlaceholderText("输入数字")
        self.number_input.returnPressed.connect(self.verify_number)
        layout.addWidget(self.number_input)
        
        # 确认按钮
        verify_btn = QPushButton("确认")
        verify_btn.clicked.connect(self.verify_number)
        layout.addWidget(verify_btn)
        
        # 跳过按钮
        skip_btn = QPushButton("跳过此测试")
        skip_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        skip_btn.clicked.connect(self.skip_test)
        layout.addWidget(skip_btn)
        
        self.input_widget.setLayout(layout)
        self.input_widget.hide()
        
    def show_verification(self):
        """显示验证数字"""
        # 生成随机4位数字
        self.verification_number = random.randint(1000, 9999)
        
        # 在5秒后显示输入界面
        QTimer.singleShot(5000, self.show_input_widget)
        
    def show_input_widget(self):
        """显示输入界面"""
        self.input_widget.show()
        self.input_widget.setGeometry(0, 0, self.width(), self.height())
        self.number_input.setFocus()
        
    def verify_number(self):
        """验证输入的数字"""
        input_value = self.number_input.text().strip()
        
        if not input_value:
            QMessageBox.warning(self, "输入错误", "请输入数字！")
            return
            
        try:
            input_num = int(input_value)
            if input_num == self.verification_number:
                QMessageBox.information(self, "验证成功", "数字正确！进入下一测试...")
                self.next_test()
            else:
                QMessageBox.warning(self, "验证失败", 
                                   f"数字错误！\n正确数字是: {self.verification_number}\n请重新输入。")
                self.number_input.clear()
                self.number_input.setFocus()
        except ValueError:
            QMessageBox.warning(self, "输入错误", "请输入有效的数字！")
            self.number_input.clear()
            
    def skip_test(self):
        """跳过测试"""
        reply = QMessageBox.question(self, "确认跳过", 
                                     "确定要跳过此测试吗？",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.next_test()
            
    def next_test(self):
        """进入下一个测试"""
        self.current_color_index += 1
        if self.current_color_index < len(self.test_colors):
            # 切换到下一个颜色
            color_name, color_value = self.test_colors[self.current_color_index]
            self.change_background_color(color_value)
            
            # 隐藏输入界面
            self.input_widget.hide()
            self.number_input.clear()
            
            # 生成新的验证数字并显示
            self.show_verification()
        else:
            # 所有颜色测试完成，进入触摸测试
            QMessageBox.information(self, "测试完成", "亮点暗点测试完成！\n即将进入触摸测试...")
            self.start_touch_test()
            
    def change_background_color(self, color):
        """改变背景颜色"""
        palette = self.palette()
        palette.setColor(self.backgroundRole(), color)
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        
    def start_touch_test(self):
        """开始触摸测试"""
        # 关闭当前窗口，打开触摸测试窗口
        self.parent().show_touch_test()
        self.close()
        
    def paintEvent(self, event):
        """绘制事件 - 显示验证数字"""
        super().paintEvent(event)
        
        if self.verification_number is not None and not self.input_widget.isVisible():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            
            # 根据背景颜色选择文字颜色
            color_name, color_value = self.test_colors[self.current_color_index]
            if color_name in ['white', 'yellow', 'cyan']:
                text_color = Qt.black
            else:
                text_color = Qt.white
                
            painter.setPen(QPen(text_color, 3))
            
            # 设置大字体
            font = QFont('Arial', 120, QFont.Bold)
            painter.setFont(font)
            
            # 在中心绘制数字
            rect = self.rect()
            painter.drawText(rect, Qt.AlignCenter, str(self.verification_number))
            
    def resizeEvent(self, event):
        """窗口大小改变事件"""
        super().resizeEvent(event)
        if self.input_widget:
            self.input_widget.setGeometry(0, 0, self.width(), self.height())


class TouchLabel(QLabel):
    """触摸方块部件"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_touched = False
        self.setMinimumSize(40, 40)
        self.setFrameStyle(QFrame.Box)
        
    def mousePressEvent(self, event):
        """鼠标按下事件"""
        self.is_touched = True
        self.update()
        event.accept()
        
    def paintEvent(self, event):
        """绘图事件"""
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        if self.is_touched:
            painter.setBrush(Qt.green)
            painter.setPen(QPen(Qt.darkGreen, 2))
        else:
            painter.setBrush(Qt.white)
            painter.setPen(QPen(Qt.lightGray, 1))
            
        painter.drawRect(self.rect())


class CrosshairWidget(QWidget):
    """十字线部件"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_pos = None
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        
    def mousePressEvent(self, event):
        """鼠标按下事件"""
        self.current_pos = event.pos()
        self.update()
        super().mousePressEvent(event)
        
    def paintEvent(self, event):
        """绘图事件 - 绘制十字线"""
        super().paintEvent(event)
        if self.current_pos:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(QPen(Qt.red, 2))
            
            # 画横线
            painter.drawLine(0, self.current_pos.y(), self.width(), self.current_pos.y())
            # 画竖线
            painter.drawLine(self.current_pos.x(), 0, self.current_pos.x(), self.height())


class TouchTestWidget(QWidget):
    """触摸测试窗口"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle('LCD触摸测试')
        self.setStyleSheet("background-color: white;")
        
        # 创建触摸块容器
        touch_container = QWidget(self)
        grid_layout = QGridLayout(touch_container)
        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        
        # 创建12x20的触摸块
        self.touch_labels = []
        for i in range(12):
            row = []
            for j in range(20):
                label = TouchLabel(touch_container)
                grid_layout.addWidget(label, i, j)
                row.append(label)
            self.touch_labels.append(row)
            
        # 创建十字线部件
        self.crosshair = CrosshairWidget(self)
        self.crosshair.raise_()
        
        # 完成按钮
        self.finish_btn = QPushButton("完成测试", self)
        self.finish_btn.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.finish_btn.clicked.connect(self.finish_test)
        
    def finish_test(self):
        """完成测试"""
        QMessageBox.information(self, "测试完成", "LCD测试已完成！")
        QApplication.quit()
        
    def mousePressEvent(self, event):
        """鼠标按下事件 - 分发给触摸块"""
        # 临时设置十字线为鼠标透传
        self.crosshair.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        
        # 获取点击位置的部件
        widget = self.childAt(event.pos())
        if widget and isinstance(widget, TouchLabel):
            # 转换坐标并发送事件
            pos = widget.mapFrom(self, event.pos())
            new_event = event.__class__(event.type(), pos, event.button(), 
                                       event.buttons(), event.modifiers())
            QApplication.sendEvent(widget, new_event)
            
        self.crosshair.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        
    def resizeEvent(self, event):
        """窗口大小改变事件"""
        super().resizeEvent(event)
        if hasattr(self, 'crosshair'):
            self.crosshair.setGeometry(0, 0, self.width(), self.height())
        if hasattr(self, 'finish_btn'):
            # 将完成按钮放在右下角
            btn_width = 150
            btn_height = 50
            self.finish_btn.setGeometry(
                self.width() - btn_width - 20,
                self.height() - btn_height - 20,
                btn_width,
                btn_height
            )
            self.finish_btn.raise_()
