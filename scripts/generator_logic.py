# scripts/generator_logic.py
import random
from datetime import datetime, timedelta
from .constants import NAMES, SURNAMES, CITIES, CATEGORIES

def get_random_client():
    name = f"{random.choice(NAMES)} {random.choice(SURNAMES)}"
    client_id = f"CL_{hash(name) % 10000:04d}"
    return client_id, name

def generate_normal_transaction():
    client_id, name = get_random_client()
    return {
        'client_id': client_id,
        'client_name': name,
        'category': random.choice(['Zakupy', 'Rachunki', 'ATM']),
        'amount': round(random.uniform(10, 3000), 2),
        'location': random.choice(CITIES[:5]), # Tylko polskie miasta
        'is_anomaly': 0
    }

def generate_suspicious_transaction():
    client_id, name = get_random_client()
    return {
        'client_id': client_id,
        'client_name': name,
        'category': 'Crypto Exchange',
        'amount': round(random.uniform(15000, 50000), 2),
        'location': random.choice(['Dubaj', 'Berlin']),
        'is_anomaly': 1
    }