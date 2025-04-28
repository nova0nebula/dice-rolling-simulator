#!/usr/bin/env python3

# Python Importing
import random

# Main Loop
while True:
    roll: str = str(input("Roll the dice? (y/n): ")).lower()
    if roll == 'y':
        dice: int = random.randint(1, 6)
      print(f"🎲 You rolled a {dice}!")
    else:
        print("Goodbye! 👋")
        break
