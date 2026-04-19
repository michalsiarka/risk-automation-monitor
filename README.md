# Risk Automation Monitor

A modular Python-based framework for simulating financial transactions and implementing automated risk detection rules.

## Project Status: Work In Progress (WIP)
This repository is currently in active development. Core data generation and database schema are implemented, with advanced analytical modules planned for future releases.

## Core Features
- Automated synthetic data generation for testing purposes.
- SQLite-based relational storage for transaction logs.
- Rule-based risk flagging (AML/Fraud simulation).
- Modular architecture for scalability and testing.

## Directory Structure
- `/scripts`: Core Python logic, including database seeders and generators.
- `/sql`: SQL schema definitions (DDL).
- `/data`: Local database storage (Note: .db files are gitignored).
- `test1.ipynb`: Initial data exploration and prototyping.

## Setup and Installation

### Prerequisites
- Python 3.9 or higher

### Environment Setup
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies (if any):
  ```bash
  pip install pandas
  ```

3. Initialize the database and generate test data:
  ```bash
  python3 scripts/seed_data.py
  ```

Development Roadmap
- [ ] Implementation of behavioral analysis patterns (e.g., transaction smurfing).

- [ ] Integration of advanced anomaly detection logic.

- [ ] Enhanced reporting and visualization modules via Pandas/Matplotlib.

License
MIT
