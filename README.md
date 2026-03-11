# 🔐 Password Generator Pro v1.1

A sophisticated desktop security tool built with Python. This version introduces advanced logic for multi-password generation and interactive data management between UI components.

## 🚀 New Engineering Features (v1.1)
* **Nested Loop Logic:** Implemented a "Matrix" generation system (a `while` loop inside a `for` loop) to build 5 unique passwords simultaneously.
* **Smart Selection System:** Interactive "Stage Area" where users can preview 5 options and pick only the preferred one to save.
* **Duplicate Prevention:** Integrated a real-time check to prevent saving the same password twice to the database.
* **State Management:** Professional UI locking (`state="disabled"`) to ensure data integrity and prevent unauthorized manual editing.
* **Persistent JSON Storage:** Robust data flow from RAM to a structured JSON file.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **GUI:** CustomTkinter (Modern UI)
* **Logic:** Random, String, Nested Loops
* **Storage:** JSON Flat-file database
