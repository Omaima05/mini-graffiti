import sqlite3
from datetime import datetime
from pathlib import Path

# Chemin vers la base de données
DB_PATH = Path(__file__).parent / "conjectures.db"


def get_connection():
    """Retourne une connexion SQLite."""
    return sqlite3.connect(DB_PATH)


def create_table():
    """
    Crée la table des conjectures si elle n'existe pas.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conjectures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            formula TEXT UNIQUE,
            is_true INTEGER,
            tested_on TEXT,
            notes TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_conjecture(formula: str, is_true: bool, notes: str = ""):
    """
    Enregistre ou met à jour une conjecture.

    - formula : conjecture testée (string)
    - is_true : True si validée sur le zoo, False sinon
    - notes : informations supplémentaires (contre-exemple, invariants, etc.)
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO conjectures (formula, is_true, tested_on, notes)
        VALUES (?, ?, ?, ?)
    """, (
        formula,
        int(is_true),
        datetime.now().isoformat(timespec="seconds"),
        notes
    ))
    conn.commit()
    conn.close()


def get_all_conjectures():
    """
    Retourne toutes les conjectures enregistrées.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT formula, is_true, tested_on, notes
        FROM conjectures
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_valid_conjectures():
    """
    Retourne uniquement les conjectures validées.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT formula, tested_on
        FROM conjectures
        WHERE is_true = 1
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_invalid_conjectures():
    """
    Retourne uniquement les conjectures invalidées avec leurs notes.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT formula, notes, tested_on
        FROM conjectures
        WHERE is_true = 0
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


# Création automatique de la table au chargement du module
create_table()
