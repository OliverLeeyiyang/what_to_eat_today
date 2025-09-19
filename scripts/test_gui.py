#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GUI测试脚本 - 快速启动GUI并自动关闭
"""

import tkinter as tk
from food_lottery_gui import FoodLotteryGUI
import threading
import time

def auto_close_gui(root):
    """自动关闭GUI窗口（用于测试）"""
    time.sleep(2)  # 显示2秒后自动关闭
    root.quit()

def test_gui():
    """测试GUI启动"""
    print("🍽️ 启动GUI测试...")
    root = tk.Tk()
    
    # 创建GUI应用
    app = FoodLotteryGUI(root)
    
    # 启动自动关闭线程
    close_thread = threading.Thread(target=auto_close_gui, args=(root,))
    close_thread.daemon = True
    close_thread.start()
    
    print("✅ GUI已启动，窗口大小: 700x600")
    print("✅ 中文字体配置已应用")
    print("✅ 2秒后自动关闭...")
    
    # 启动GUI
    root.mainloop()
    
    print("✅ GUI测试完成！")

if __name__ == "__main__":
    test_gui()