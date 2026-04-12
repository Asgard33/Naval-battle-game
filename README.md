🇫🇷 Une version française est disponible dans README_FR.md


# 🚢 Naval Battle Game

Battleship game implemented in Python featuring a hunt-and-target based strategy AI, multiple game modes (AI vs AI, player vs AI), and a modular architecture 


## Features

- Classic Battleship gameplay
- Random AI opponent (AI)
- Advanced AI using a hunt and target based strategy (AI+)
- Multiples game modes :
    -player vs player
    -player vs AI+
    -AI+ vs AI+
    -AI+ vs AI (to highlight performance differences)
- Modular and readable code structure

---

##  AI Strategy

The AI uses a heuristic approach to make decisions:

- Prioritizes cells based on previous hits
- Targets neighboring cells after a successful hit
- Avoids already played moves
- Uses a combination of rules to simulate strategic gameplay






##  Project Origin

This project is based on an already existing academic group project developped in 2023.
Original version avaiblle here : https://github.com/Ruby44444/Bataille-Navale


In this project, I personally:

- Designed and implemented an advanced heuristic AI (AI+) based on a hunt-and-target strategy:
  - Random search phase without repetition
  - Targeting phase after detecting a ship
- Implemented the ship placement logic (manual and automatic)

I also integrated the AI logic into the main game loop (`naval_battle`).


## Improvements and Refactoring

I refactored the original project by:

- Removing unnecessary game modes to improve clarity and user experience
- Adding few game features to improve the user experiece
- Restructuring the code to better separate gameplay and simulation
- Adding a simulation mode with CSV data export for performance analysis


## 📊 Results

The results PDF is in French as it comes from the original analysis context.  
However, the key insights are:
- AI+ significantly outperforms random AI
- The heuristic strategy improves hit efficiency
