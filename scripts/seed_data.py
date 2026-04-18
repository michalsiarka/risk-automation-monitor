import sqlite3
import os
import random
from datetime import datetime, timedelta

# Configuration
BASE_DIR = os.getcwd()
DB_PATH = os.path.join(BASE_DIR, 'data', 'risk_monitor.db')
SQL_PATH = os.path.join(BASE_DIR, 'sql', 'init_db.sql')

def run_seeding():
    print("Initiating database seeding process...")
    
    if not os.path.exists('data'):
        os.makedirs('data')

    conn = sqlite3.connect(DB_PATH)
    
    if os.path.exists(SQL_PATH):
        with open(SQL_PATH, 'r') as f:
            conn.executescript(f.read())
    else:
        print(f"Critical error: SQL schema not found at {SQL_PATH}")
        return

    # Data generation logic
    imiona = ['Jan', 'Anna', 'Marek', 'Katarzyna', 'Piotr']
    for _ in range(100):
        klient = f"{random.choice(imiona)} {random.randint(100, 999)}"
        kwota = round(random.uniform(50, 25000), 2)
        podejrzana = 1 if kwota > 15000 else 0
        
        conn.execute('''
            INSERT INTO transactions (client_name, amount, currency, is_suspicious)
            VALUES (?, ?, ?, ?)
        ''', (klient, kwota, 'PLN', podejrzana))

    conn.commit()
    conn.close()
    print(f"Success: Database seeded correctly at {DB_PATH}")

if __name__ == "__main__":
    run_seeding()