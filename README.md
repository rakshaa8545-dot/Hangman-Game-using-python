# Hangman-Game-using-python

## 📌 Project Overview

The **Hangman Game** is a Python-based word guessing game where players try to guess a hidden word one letter at a time. The player wins by correctly guessing all the letters in the word before running out of attempts. This project is ideal for beginners to practice Python fundamentals such as loops, conditions, strings, lists, and the `random` module.

---

## 🎯 Features

* Random word selection from a predefined list.
* Interactive letter-by-letter guessing.
* Limited number of attempts.
* Displays correctly guessed letters.
* Prevents duplicate guesses.
* Simple command-line interface.

---

## 🛠️ Technologies Used

* **Python 3**
* **random module**

---

## 📂 Project Structure

```text
Hangman-Game/
│
├── hangman.py
├── README.md

```

---

## 🚀 How It Works

1. The program selects a random word.
2. The player guesses one letter at a time.
3. Correct guesses reveal the letter's position.
4. Incorrect guesses reduce the remaining attempts.
5. The game ends when:

   * The player guesses the complete word, or
   * The player runs out of attempts.

---

## ▶️ Installation & Usage

### Clone the Repository

```bash
git clone https://github.com/your-username/Hangman-Game.git
cd Hangman-Game
```

### Run the Program

```bash
python hangman.py
```

---

## 💻 Sample Output

```text
Welcome to Hangman!

Word: _ _ _ _ _
Guess a letter: a

Correct Guess!

Word: a _ _ _ _
Attempts Left: 5

Guess a letter: z

Wrong Guess!
Attempts Left: 4
```

---

## 📝 Sample Code

```python
import random

words = ["python", "coding", "hangman", "computer", "program"]

word = random.choice(words)
guessed_letters = []
attempts = 6

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess! Attempts left:", attempts)

if attempts == 0:
    print("💀 Game Over! The word was:", word)
```

---

## 📚 Learning Outcomes

By building this project, you will learn:

* Python loops (`for`, `while`)
* Conditional statements (`if`, `else`)
* String manipulation
* Lists and list operations
* User input handling
* Random word selection using the `random` module

---

## 🔮 Future Enhancements

* Add difficulty levels.
* Include categories for words.
* Display Hangman ASCII art.
* Create a graphical interface using Tkinter.
* Store high scores and player statistics.

---

## 👨‍💻 Author

**Raksha A**

