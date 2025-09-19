# Food Lottery Program 🍽️

A fun Python program that helps you decide what to eat today using a lottery system! The program reads food preferences from a configuration file and randomly selects what to eat.

## Features

- **Command-line interface**: Simple text-based interaction
- **Graphical interface**: User-friendly GUI using tkinter
- **Configurable preferences**: Easy to modify food preferences via JSON config
- **Multiple selection modes**: Choose from all options or specific person's preferences
- **Launcher script**: Easy way to choose between CLI and GUI versions

## Files Structure

```
what_to_eat_today/
├── config/
│   └── config.json          # Food preferences configuration
├── scripts/
│   ├── food_lottery.py      # Main lottery logic and CLI version
│   ├── food_lottery_gui.py  # GUI version using tkinter
│   └── launcher.py          # Launcher to choose between CLI/GUI
└── README.md               # This file
```

## Configuration

The `config/config.json` file contains the food preferences for different people:

```json
{
  "people": {
    "Alice": {
      "food_preferences": [
        "Pizza", "Sushi", "Burger", "Pasta", "Tacos",
        "Chinese Stir Fry", "Indian Curry", "Thai Pad Thai"
      ]
    },
    "Bob": {
      "food_preferences": [
        "Steak", "Seafood", "BBQ Ribs", "Sandwich", "Salad",
        "Mexican Burrito", "Korean BBQ", "Italian Risotto"
      ]
    }
  }
}
```

You can easily modify this file to add more people or change food preferences.

## How to Run

### Option 1: Using the Launcher (Recommended)
```bash
cd scripts
python launcher.py
```
Then choose:
- `1` for command-line version
- `2` for GUI version

### Option 2: Run Directly

**Command-line version:**
```bash
cd scripts
python food_lottery.py
```

**GUI version:**
```bash
cd scripts
python food_lottery_gui.py
```

## Usage

### Command-line Version
1. The program displays all food preferences
2. Choose between:
   - Option 1: Random selection from all available foods
   - Option 2: Random selection from a specific person's preferences
   - Option 3: Exit
3. View the lottery result!

### GUI Version
1. Select lottery type using radio buttons:
   - "Choose from all food options"
   - "Choose from specific person's preferences" (then select person from dropdown)
2. Click "🎲 Run Lottery!" button
3. View result in the result area and popup message
4. Browse all food preferences in the scrollable text area

## Features

- **Error handling**: Graceful handling of missing config files or invalid JSON
- **Extensible**: Easy to add more people or food options
- **Cross-platform**: Works on Windows, macOS, and Linux
- **No external dependencies**: Uses only Python standard library (tkinter for GUI)

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)

## Customization

To add more people or modify food preferences:

1. Open `config/config.json`
2. Add new people following the same structure:
   ```json
   "NewPerson": {
     "food_preferences": [
       "Food 1", "Food 2", "Food 3"
     ]
   }
   ```
3. Save the file
4. Run the program - changes will be automatically loaded

Enjoy deciding what to eat today! 🎲🍽️