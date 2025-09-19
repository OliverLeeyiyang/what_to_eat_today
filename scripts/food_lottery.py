#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Food Lottery Program

This program reads a configuration file containing people's food preferences
and randomly selects what to eat today using a lottery system.
"""

import json
import random
import os
from typing import Dict, List, Tuple


class FoodLottery:
    def __init__(self, config_path: str = None):
        """Initialize the FoodLottery with a config file path."""
        if config_path is None:
            # Default to config folder relative to this script
            current_dir = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(os.path.dirname(current_dir), "config", "config.json")
        
        self.config_path = config_path
        self.config = self.load_config()
    
    def load_config(self) -> Dict:
        """Load the configuration from JSON file."""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as file:
                config = json.load(file)
                return config
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found at: {self.config_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in config file: {self.config_path}")
    
    def get_all_food_options(self) -> List[str]:
        """Get all unique food options from all people's preferences."""
        all_foods = set()
        people = self.config.get("people", {})
        
        for person_data in people.values():
            food_preferences = person_data.get("food_preferences", [])
            all_foods.update(food_preferences)
        
        return list(all_foods)
    
    def get_person_preferences(self, person_name: str) -> List[str]:
        """Get food preferences for a specific person."""
        people = self.config.get("people", {})
        person_data = people.get(person_name, {})
        return person_data.get("food_preferences", [])
    
    def run_lottery(self, person_name: str = None) -> Tuple[str, str]:
        """
        Run the lottery to decide what to eat today.
        
        Args:
            person_name: If specified, choose from this person's preferences only.
                        If None, choose from all available food options.
        
        Returns:
            Tuple of (selected_food, selection_method)
        """
        if person_name:
            food_options = self.get_person_preferences(person_name)
            if not food_options:
                raise ValueError(f"No food preferences found for {person_name}")
            selection_method = f"{person_name}的喜好"
        else:
            food_options = self.get_all_food_options()
            selection_method = "所有选项"
        
        if not food_options:
            raise ValueError("No food options available")
        
        selected_food = random.choice(food_options)
        return selected_food, selection_method
    
    def get_people_list(self) -> List[str]:
        """Get list of all people in the config."""
        return list(self.config.get("people", {}).keys())
    
    def display_all_preferences(self) -> None:
        """Display all people and their food preferences."""
        people = self.config.get("people", {})
        
        print("\n=== Food Preferences ===")
        for person, data in people.items():
            preferences = data.get("food_preferences", [])
            print(f"\n{person}:")
            for i, food in enumerate(preferences, 1):
                print(f"  {i}. {food}")


def main():
    """Main function to run the command-line version of the food lottery."""
    print("🍽️  Welcome to the Food Lottery! 🍽️")
    print("=" * 40)
    
    try:
        lottery = FoodLottery()
        
        # Display all preferences
        lottery.display_all_preferences()
        
        print("\n" + "=" * 40)
        print("Lottery Options:")
        print("1. Choose from all food options")
        print("2. Choose from a specific person's preferences")
        print("3. Exit")
        
        while True:
            choice = input("\nSelect an option (1-3): ").strip()
            
            if choice == "1":
                try:
                    food, method = lottery.run_lottery()
                    print(f"\n🎉 Today's selection: {food}")
                    print(f"Selected {method}")
                    break
                except Exception as e:
                    print(f"Error: {e}")
            
            elif choice == "2":
                people = lottery.get_people_list()
                print(f"\nAvailable people: {', '.join(people)}")
                person = input("Enter person's name: ").strip()
                
                if person in people:
                    try:
                        food, method = lottery.run_lottery(person)
                        print(f"\n🎉 Today's selection: {food}")
                        print(f"Selected {method}")
                        break
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    print(f"Person '{person}' not found in config.")
            
            elif choice == "3":
                print("Goodbye! Enjoy your meal! 🍽️")
                break
            
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
    
    except Exception as e:
        print(f"Error initializing food lottery: {e}")


if __name__ == "__main__":
    main()