-- sql/init_db.sql
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT NOT NULL,
    amount REAL NOT NULL,
    currency TEXT NOT NULL,
    is_suspicious INTEGER DEFAULT 0 -- Używamy tej nazwy!
);