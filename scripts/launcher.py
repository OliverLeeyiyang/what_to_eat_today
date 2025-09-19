#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Food Lottery Launcher

A simple launcher script to choose between command-line and GUI versions.
"""

import sys
import os

def main():
    print("🍽️ 美食抽奖启动器")
    print("=" * 30)
    print("1. 运行命令行版本")
    print("2. 运行图形界面版本")
    print("3. 退出")
    
    while True:
        choice = input("\n请选择一个选项 (1-3): ").strip()
        
        if choice == "1":
            print("\n启动命令行版本...")
            import food_lottery
            food_lottery.main()
            break
            
        elif choice == "2":
            print("\n启动图形界面版本...")
            try:
                import food_lottery_gui
                food_lottery_gui.main()
            except ImportError as e:
                print(f"错误: 无法导入GUI模块: {e}")
                print("请确保已安装tkinter。")
            except Exception as e:
                print(f"GUI运行错误: {e}")
            break
            
        elif choice == "3":
            print("再见!")
            break
            
        else:
            print("无效选择。请选择 1、2 或 3。")

if __name__ == "__main__":
    main()