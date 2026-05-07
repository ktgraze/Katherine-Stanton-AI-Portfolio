# Magic 8-Ball
### Programming Fundamentals (Python) | Houston City College

![Python](https://img.shields.io/badge/Python-3.x-blue)

---

## Problem Statement

This project is a simple command-line Magic 8-Ball game built as an introduction to core Python programming concepts. The program prompts the user to ask a yes/no question, randomly selects one of eight possible responses, and then asks the user if they would like to play again — looping until the user chooses to quit.

---

## Approach and Methodology

The program is structured using four functions to keep the code modular and readable:

- `get_user_question()` — displays a welcome message and collects the user's question
- `generate_random_response()` — uses `random.randint()` to select a random response from a predefined list of eight strings
- `play_game()` — orchestrates a single round by calling the above two functions in sequence
- `main()` — controls the overall game loop, handling replay logic and input validation via nested while loops and if/elif/else statements

Constants are used for the welcome message, farewell message, decorative banner, and response list to keep magic values out of the logic.

---

## Results and Evaluation

The program runs as expected, correctly handling all user input cases including valid yes/no responses and invalid inputs. The `random.randint()` approach produces uniformly distributed responses across the eight possible outcomes. Input validation ensures the game does not crash or behave unexpectedly on unexpected user input.

---

## Data Sources

No external data sources or datasets are used. All responses are hardcoded as constants within the program.

---

## Requirements and Dependencies

Python 3.x is required. No external libraries are needed — only the Python standard library `random` module is used.

To run the program:

```bash
python PROStantonKatherine.py
```

---

## Learning Outcomes

This project introduced me to the fundamentals of Python programming including functions, constants, lists, loops, conditionals, and user input handling. Structuring the program across multiple functions reinforced the importance of modular design even in small projects. Working with the `random` module provided an early example of how Python's standard library can add meaningful functionality with minimal code.

---
