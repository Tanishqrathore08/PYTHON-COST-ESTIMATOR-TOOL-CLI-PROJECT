☁️ Cloud Cost Estimator (Python CLI)
 Overview

This is a simple Python Command Line Interface (CLI) application that helps estimate the monthly cost of cloud infrastructure.

The tool takes user inputs like:

Number of servers (compute)
Storage size (GB)
Database usage (hours)

…and calculates an approximate monthly bill based on standard pricing rates.

💡 Why I Built This

Cloud platforms like AWS follow a pay-as-you-go model, which can sometimes lead to unexpected costs if not managed properly.

I built this project to:

Understand Cloud Financial Management (FinOps) basics
Show how cost estimation can help plan infrastructure better
Demonstrate how simple tools can solve real-world problems
⚙️ How It Works

The application runs in a loop and allows users to calculate costs for different services in one session.

Key Features:
Menu-based CLI interface
Cost estimation for:
Compute (servers)
Storage
Database usage
Continuous execution until the user exits
🧠 Concepts Used

This project focuses on core Python fundamentals:

Control Flow (if-elif-else)
Used to navigate user choices and run the correct cost calculation.
Loops (while)
Keeps the program running so users can perform multiple calculations.
Type Casting (int())
Converts user input into numbers for calculations.
String Formatting (f-strings)
Displays output cleanly, formatted like real currency.
📊 What This Project Shows
Ability to build a working CLI application from scratch
Understanding of basic cloud services (Compute, Storage, Database)
Awareness of cost management in cloud environments
Practical problem-solving using programming
🔮 Future Improvements

This is a basic version, but here’s how I would improve it:

Replace hardcoded pricing with a Python dictionary
Add support for multiple cloud providers (AWS, Azure, GCP)
Connect to a real cloud pricing API for live data
Build a web version (using Flask or React) for better UI
🛠️ Tech Stack
Python (Core)
▶️ How to Run
python main.py
