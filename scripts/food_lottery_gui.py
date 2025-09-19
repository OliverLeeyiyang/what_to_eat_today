#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Food Lottery GUI Application

A graphical user interface for the food lottery program using tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, font
import os
from food_lottery import FoodLottery


class FoodLotteryGUI:
    def __init__(self, root):
        """Initialize the GUI application."""
        self.root = root
        self.root.title("🍽️ 今天吃什么 - 美食抽奖器")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        # Set font configurations for better Chinese character display
        # Try different fonts in order of preference for Chinese support
        self.title_font = ("Microsoft YaHei", 18, "bold")
        self.label_font = ("Microsoft YaHei", 12)
        self.button_font = ("Microsoft YaHei", 11)
        self.text_font = ("Microsoft YaHei", 11)
        self.result_font = ("Microsoft YaHei", 14, "bold")
        
        # Fallback fonts if Microsoft YaHei is not available
        try:
            # Test if we can create a font
            test_font = tk.font.Font(family="Microsoft YaHei", size=10)
        except:
            # Use fallback fonts
            self.title_font = ("SimHei", 18, "bold")
            self.label_font = ("SimHei", 12)
            self.button_font = ("SimHei", 11)
            self.text_font = ("SimHei", 11)
            self.result_font = ("SimHei", 14, "bold")
        
        # Initialize the lottery system
        try:
            self.lottery = FoodLottery()
        except Exception as e:
            messagebox.showerror("错误", f"配置文件加载失败: {e}")
            return
        
        # Configure styles for better Chinese text display
        self.configure_styles()
        self.setup_ui()
        self.load_preferences()
    
    def configure_styles(self):
        """Configure ttk styles for better Chinese text display."""
        style = ttk.Style()
        
        # Configure label styles
        style.configure('TLabel', font=self.label_font)
        style.configure('TLabelframe.Label', font=self.label_font)
        
        # Configure radiobutton and button styles
        style.configure('TRadiobutton', font=self.label_font)
        style.configure('TButton', font=self.button_font)
        style.configure('Accent.TButton', font=self.button_font)
        
        # Configure combobox style
        style.configure('TCombobox', font=self.label_font)
    
    def setup_ui(self):
        """Set up the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="🍽️ 美食抽奖器", font=self.title_font)
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Selection frame
        selection_frame = ttk.LabelFrame(main_frame, text="抽奖选项", padding="15")
        selection_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        selection_frame.columnconfigure(1, weight=1)
        
        # Radio buttons for selection type
        self.selection_type = tk.StringVar(value="all")
        
        radio1 = ttk.Radiobutton(selection_frame, text="从所有美食中抽选", 
                       variable=self.selection_type, value="all")
        radio1.grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 8))
        
        radio2 = ttk.Radiobutton(selection_frame, text="从指定人的喜好中抽选:", 
                       variable=self.selection_type, value="person")
        radio2.grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
        
        # Person selection dropdown
        self.person_var = tk.StringVar()
        self.person_dropdown = ttk.Combobox(selection_frame, textvariable=self.person_var, 
                                          values=self.lottery.get_people_list(), state="readonly",
                                          font=self.label_font)
        self.person_dropdown.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(15, 0), pady=(5, 0))
        
        # Lottery button
        lottery_btn = ttk.Button(selection_frame, text="🎲 开始抽奖!", 
                               command=self.run_lottery, style="Accent.TButton")
        lottery_btn.grid(row=2, column=0, columnspan=2, pady=(20, 0))
        
        # Result frame
        result_frame = ttk.LabelFrame(main_frame, text="抽奖结果", padding="15")
        result_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        result_frame.columnconfigure(0, weight=1)
        result_frame.rowconfigure(0, weight=1)
        
        self.result_text = tk.Text(result_frame, height=4, font=self.result_font, 
                                  wrap=tk.WORD, state=tk.DISABLED, bg="#f0f0f0",
                                  relief="flat", padx=10, pady=10)
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Preferences frame
        pref_frame = ttk.LabelFrame(main_frame, text="美食偏好", padding="15")
        pref_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        pref_frame.columnconfigure(0, weight=1)
        pref_frame.rowconfigure(0, weight=1)
        
        self.pref_text = scrolledtext.ScrolledText(pref_frame, height=12, font=self.text_font, 
                                                  state=tk.DISABLED, wrap=tk.WORD,
                                                  padx=10, pady=5)
        self.pref_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=(15, 0))
        
        refresh_btn = ttk.Button(button_frame, text="刷新偏好", 
                  command=self.load_preferences)
        refresh_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        exit_btn = ttk.Button(button_frame, text="退出", 
                  command=self.root.quit)
        exit_btn.pack(side=tk.LEFT)
    
    def load_preferences(self):
        """Load and display food preferences."""
        try:
            # Reload config in case it changed
            self.lottery = FoodLottery()
            
            # Update person dropdown
            self.person_dropdown['values'] = self.lottery.get_people_list()
            if self.lottery.get_people_list():
                self.person_var.set(self.lottery.get_people_list()[0])
            
            # Display preferences
            self.pref_text.config(state=tk.NORMAL)
            self.pref_text.delete(1.0, tk.END)
            
            people = self.lottery.config.get("people", {})
            
            for person, data in people.items():
                self.pref_text.insert(tk.END, f"{person}:\n")
                preferences = data.get("food_preferences", [])
                for i, food in enumerate(preferences, 1):
                    self.pref_text.insert(tk.END, f"  {i:2d}. {food}\n")
                self.pref_text.insert(tk.END, "\n")
            
            self.pref_text.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("错误", f"加载偏好失败: {e}")
    
    def run_lottery(self):
        """Run the lottery and display the result."""
        try:
            if self.selection_type.get() == "all":
                food, method = self.lottery.run_lottery()
            else:
                person = self.person_var.get()
                if not person:
                    messagebox.showwarning("警告", "请选择一个人。")
                    return
                food, method = self.lottery.run_lottery(person)
            
            # Display result
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"🎉 今日推荐: {food}\n\n")
            self.result_text.insert(tk.END, f"选择来源: {method}")
            self.result_text.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("错误", f"抽奖失败: {e}")


def main():
    """Main function to run the GUI application."""
    # Create the main window
    root = tk.Tk()
    
    # Try to set a nice theme if available
    try:
        style = ttk.Style()
        available_themes = style.theme_names()
        if 'clam' in available_themes:
            style.theme_use('clam')
        elif 'alt' in available_themes:
            style.theme_use('alt')
    except:
        pass  # Use default theme if styling fails
    
    # Create and run the application
    app = FoodLotteryGUI(root)
    
    # Center the window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    
    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()